"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a script that automates system administration tasks, utilizing the knowledge shared by Susan Lunn in the FOSS@RIT community.
Generated: DETERMINISTIC_e5c8316f373108e8
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# system_administration_script.py

"""
Automates system administration tasks.

This script utilizes the knowledge shared by Susan Lunn in the FOSS@RIT community.
It provides functionality for managing users, groups, and system updates.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import pwd
import grp
import subprocess
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_user(username):
    """
    Creates a new user with the given username.

    Args:
        username (str): The username of the new user.

    Returns:
        bool: True if the user was created successfully, False otherwise.
    """
    try:
        # Check if the user already exists
        pwd.getpwnam(username)
        logging.warning(f"User '{username}' already exists.")
        return False
    except KeyError:
        # Create the new user
        subprocess.run(["sudo", "useradd", username], check=True)
        logging.info(f"User '{username}' created successfully.")
        return True

def delete_user(username):
    """
    Deletes the user with the given username.

    Args:
        username (str): The username of the user to delete.

    Returns:
        bool: True if the user was deleted successfully, False otherwise.
    """
    try:
        # Check if the user exists
        pwd.getpwnam(username)
        # Delete the user
        subprocess.run(["sudo", "userdel", username], check=True)
        logging.info(f"User '{username}' deleted successfully.")
        return True
    except KeyError:
        logging.warning(f"User '{username}' does not exist.")
        return False
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to delete user '{username}': {e}")
        return False

def create_group(groupname):
    """
    Creates a new group with the given groupname.

    Args:
        groupname (str): The groupname of the new group.

    Returns:
        bool: True if the group was created successfully, False otherwise.
    """
    try:
        # Check if the group already exists
        grp.getgrnam(groupname)
        logging.warning(f"Group '{groupname}' already exists.")
        return False
    except KeyError:
        # Create the new group
        subprocess.run(["sudo", "groupadd", groupname], check=True)
        logging.info(f"Group '{groupname}' created successfully.")
        return True

def delete_group(groupname):
    """
    Deletes the group with the given groupname.

    Args:
        groupname (str): The groupname of the group to delete.

    Returns:
        bool: True if the group was deleted successfully, False otherwise.
    """
    try:
        # Check if the group exists
        grp.getgrnam(groupname)
        # Delete the group
        subprocess.run(["sudo", "groupdel", groupname], check=True)
        logging.info(f"Group '{groupname}' deleted successfully.")
        return True
    except KeyError:
        logging.warning(f"Group '{groupname}' does not exist.")
        return False
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to delete group '{groupname}': {e}")
        return False

def update_system():
    """
    Updates the system using the package manager.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        # Update the package index
        subprocess.run(["sudo", "apt", "update"], check=True)
        # Upgrade the packages
        subprocess.run(["sudo", "apt", "full-upgrade", "-y"], check=True)
        logging.info("System updated successfully.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to update system: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="System Administration Script")
    subparsers = parser.add_subparsers(dest="command")

    # Create user parser
    create_user_parser = subparsers.add_parser("create_user", help="Create a new user")
    create_user_parser.add_argument("username", help="The username of the new user")

    # Delete user parser
    delete_user_parser = subparsers.add_parser("delete_user", help="Delete a user")
    delete_user_parser.add_argument("username", help="The username of the user to delete")

    # Create group parser
    create_group_parser = subparsers.add_parser("create_group", help="Create a new group")
    create_group_parser.add_argument("groupname", help="The groupname of the new group")

    # Delete group parser
    delete_group_parser = subparsers.add_parser("delete_group", help="Delete a group")
    delete_group_parser.add_argument("groupname", help="The groupname of the group to delete")

    # Update system parser
    update_system_parser = subparsers.add_parser("update_system", help="Update the system")

    args = parser.parse_args()

    if args.command == "create_user":
        create_user(args.username)
    elif args.command == "delete_user":
        delete_user(args.username)
    elif args.command == "create_group":
        create_group(args.groupname)
    elif args.command == "delete_group":
        delete_group(args.groupname)
    elif args.command == "update_system":
        update_system()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```
