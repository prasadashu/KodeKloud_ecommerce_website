# KodeKloud_ecommerce_website
KodeKloud exercise to deploy website using Ansible playbook.

## How to run the playbook?
- Install Ansible in RedHat based distros.

`sudo yum install -y ansible`

- Clone this repo.

`git clone -b ansible_tasks https://github.com/prasadashu/KodeKloud_ecommerce_website.git`

- Run the playbook.

`ansible-playbook deploy_ecommerce_website.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"`

## Repository details
### 1. Create an inventory file
- Refer to the inventory file under `inventory` directory.

### 2. Create a host_vars directory
- The `host_vars` directory should contain a YAML file with the **same name as that declared in inventory file**.
- The YAML file should contain all the required variables linked to the host.

### 3. Create a tasks directory
- The `tasks` directory should be in the **same location as the master playbook**.
- Within the `tasks` directory we can have several specific tasks playbooks.
- Each task playbook is a YAML file.
- Each YAML file will have a set of tasks pertaining to the concerned task.

### 4. Adding the tasks to the master playbook
- Instead of adding a module for each task, we will use the `include` tag to include the respective tasks.
- The roles will be listed sequentially in run order under `roles` tag.

### 5. Run Ansible playbook against the inventory file
`ansible-playbook deploy_ecommerce_website.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"`
