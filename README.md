# KodeKloud_ecommerce_website
KodeKloud exercise to deploy website using Ansible playbook.

## Install Ansible in RedHat based distros
`sudo yum install -y ansible`

## 1. Create an inventory file
- Refer to the inventory file under `inventory` directory.

## 2. Run Ansible playbook against the inventory file
`ansible-playbook deploy_ecommerce_website.yml -i inventory.txt --extra-vars "{'host':'db_web_server'}"`
