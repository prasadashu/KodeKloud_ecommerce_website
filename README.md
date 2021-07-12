# KodeKloud_ecommerce_website
KodeKloud exercise to deploy website using Ansible playbook.

## How to run the playbook?
- Install Ansible in RedHat based distros.

`sudo yum install -y ansible`

- Clone this repo.

`git clone -b ansible_dynamic_inventory https://github.com/prasadashu/KodeKloud_ecommerce_website.git`

- Run the playbook.

`ansible-playbook deploy_ecommerce_website.yml -i inventory/inventory.py --extra-vars "{'host':'db_web_server'}"`

## Repository details
### 1. Create a dynamic inventory script
- Refer to the python inventory file under `inventory` directory.

### 2. Modify inventory python file permission
- The python inventory file should have **execute privileges**.
- If execute permissions are missing, **Permission denier** error will occur while running the playbook.

### 3. Create a roles directory
- The `roles` directory should be in the **same location as the master playbook**.
- Within the `roles` directory we can have several specific role directories.
- Each role directory will have a `tasks` directory.
- Under the `tasks` directory we have a YAML file by the name `main.yml`.
- The `main.yml` file will have a set of tasks pertaining to the role.

### 4. Adding the roles to the master playbook
- Instead of the `tasks` tag in the master playbook, we will have the `roles` tag.
- The roles will be listed sequentially in run order under `roles` tag.

### 5. Run Ansible playbook against the inventory file
`ansible-playbook deploy_ecommerce_website.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"`

## Extra Information
- Information about the hosts can be listed from the python dynamic inventory script by using the `--list` argument.

`./inventory.py --list`

- Information related to a specific host can be viewed using the `--host` argument followed by the particular host.

`./inventory.py --host monolithic_server`

- **NOTE:** Make sure the interpreter path *#!/usr/bin/python* exists in the machine running the playbook.