#!/usr/bin/python

import json
import argparse

def get_inventory_data():
    """Function to get inventory data dynamically"""

    # Declare inventory data
    inventory_data = {
        "monolithic_server": {
            "hosts": ["db_web_server"],
            "vars": {
                "ansible_connection": "local"
            }
        }
    }

    # Return the above declared inventory data
    return inventory_data

def read_cli_args():
    """Function to create CLI arguments"""

    # Declare 'args' as a global variable
    global args

    # Instantiate the CLI argument parser
    parser = argparse.ArgumentParser(description="Dynamic inventory argument parser")
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')

    # Parse the arguments
    args = parser.parse_args()


# Calling the main function
if __name__ == '__main__':
    # Declare 'args' as global variable
    # This is to pull the global value of args in the variable
    global args

    # Instantiate the arguments
    read_cli_args()

    # Call the inventory function
    inventory_data = get_inventory_data()

    # If '--list' is declared as an argument
    # Print the inventory data in JSON format to stdout
    if args.list:
        print(json.dumps(inventory_data))

    # Else if '--host' value is declared
    # Print the parameters for the host
    elif args.host:
        print(json.dumps(inventory_data[args.host]["vars"]))