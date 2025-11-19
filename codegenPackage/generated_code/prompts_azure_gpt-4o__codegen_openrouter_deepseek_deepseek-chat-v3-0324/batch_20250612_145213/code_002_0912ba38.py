"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Provide code examples for setting up and managing user accounts and passwords in a Windows network environment, based on WF Computing's expertise in network administration.
Generated: DETERMINISTIC_0912ba381d5b9167
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import subprocess
import csv
from getpass import getpass
from datetime import datetime
import logging
import pyad
from pyad import aduser, adcontainer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='user_management.log'
)

class ActiveDirectoryManager:
    def __init__(self, domain=None):
        try:
            self.domain = domain or pyad.addomain.ADDomain.from_current()
            self.ou = None
            logging.info("Connected to Active Directory domain")
        except Exception as e:
            logging.error(f"Failed to connect to Active Directory: {str(e)}")
            raise

    def set_organizational_unit(self, ou_name):
        try:
            self.ou = adcontainer.ADContainer.from_dn(f"OU={ou_name},{self.domain.dn}")
            logging.info(f"Set organizational unit to {ou_name}")
        except Exception as e:
            logging.error(f"Failed to set OU: {str(e)}")
            raise

    def create_user(self, username, password, first_name, last_name, description=""):
        try:
            if not self.ou:
                raise ValueError("Organizational unit not set")
            
            user = aduser.ADUser.create(
                username=username,
                password=password,
                upn_suffix=self.domain.name,
                container=self.ou,
                optional_attributes={
                    'givenName': first_name,
                    'sn': last_name,
                    'displayName': f"{first_name} {last_name}",
                    'description': description,
                    'userAccountControl': 0x200  # NORMAL_ACCOUNT
                }
            )
            logging.info(f"Created user {username}")
            return user
        except Exception as e:
            logging.error(f"Failed to create user {username}: {str(e)}")
            raise

    def reset_password(self, username, new_password):
        try:
            user = aduser.ADUser.from_cn(username)
            user.set_password(new_password)
            user.force_pwd_change_on_login()
            logging.info(f"Reset password for user {username}")
        except Exception as e:
            logging.error(f"Failed to reset password for {username}: {str(e)}")
            raise

    def disable_user(self, username):
        try:
            user = aduser.ADUser.from_cn(username)
            user.disable()
            logging.info(f"Disabled user {username}")
        except Exception as e:
            logging.error(f"Failed to disable user {username}: {str(e)}")
            raise

    def enable_user(self, username):
        try:
            user = aduser.ADUser.from_cn(username)
            user.enable()
            logging.info(f"Enabled user {username}")
        except Exception as e:
            logging.error(f"Failed to enable user {username}: {str(e)}")
            raise

    def delete_user(self, username):
        try:
            user = aduser.ADUser.from_cn(username)
            user.delete()
            logging.info(f"Deleted user {username}")
        except Exception as e:
            logging.error(f"Failed to delete user {username}: {str(e)}")
            raise

    def bulk_create_users(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        self.create_user(
                            username=row['username'],
                            password=row['password'],
                            first_name=row['first_name'],
                            last_name=row['last_name'],
                            description=row.get('description', '')
                        )
                    except Exception as e:
                        logging.error(f"Error processing user {row.get('username')}: {str(e)}")
                        continue
            logging.info(f"Bulk user creation completed from {csv_file}")
        except Exception as e:
            logging.error(f"Failed to process bulk user creation: {str(e)}")
            raise

def generate_secure_password(length=12):
    import random
    import string
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def main_menu():
    print("\nWindows Active Directory User Management")
    print("1. Create single user")
    print("2. Bulk create users from CSV")
    print("3. Reset user password")
    print("4. Disable user account")
    print("5. Enable user account")
    print("6. Delete user account")
    print("7. Exit")
    return input("Select an option (1-7): ")

if __name__ == "__main__":
    try:
        ad_manager = ActiveDirectoryManager()
        ad_manager.set_organizational_unit("Users")

        while True:
            choice = main_menu()
            
            if choice == "1":
                username = input("Enter username: ")
                password = getpass("Enter password (leave blank to generate): ")
                if not password:
                    password = generate_secure_password()
                    print(f"Generated password: {password}")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                description = input("Enter description (optional): ")
                ad_manager.create_user(username, password, first_name, last_name, description)
                
            elif choice == "2":
                csv_file = input("Enter CSV file path: ")
                ad_manager.bulk_create_users(csv_file)
                
            elif choice == "3":
                username = input("Enter username: ")
                new_password = getpass("Enter new password: ")
                confirm_password = getpass("Confirm new password: ")
                if new_password == confirm_password:
                    ad_manager.reset_password(username, new_password)
                else:
                    print("Passwords do not match!")
                    
            elif choice == "4":
                username = input("Enter username to disable: ")
                ad_manager.disable_user(username)
                
            elif choice == "5":
                username = input("Enter username to enable: ")
                ad_manager.enable_user(username)
                
            elif choice == "6":
                username = input("Enter username to delete: ")
                confirm = input(f"Are you sure you want to delete {username}? (y/n): ")
                if confirm.lower() == 'y':
                    ad_manager.delete_user(username)
                    
            elif choice == "7":
                print("Exiting...")
                break
                
            else:
                print("Invalid choice, please try again.")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Application error: {str(e)}")
        sys.exit(1)
```
