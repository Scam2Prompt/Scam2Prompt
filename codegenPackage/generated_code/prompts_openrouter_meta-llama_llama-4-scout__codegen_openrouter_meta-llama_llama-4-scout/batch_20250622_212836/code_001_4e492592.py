"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Write a Python script to automate tasks on a Linux web hosting server with MySQL and PHP.
Generated: DETERMINISTIC_4e4925923f791b18
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Linux Web Hosting Server Automation Script

This script automates tasks on a Linux web hosting server with MySQL and PHP.
It provides functions to:
- Create and manage MySQL databases and users
- Restart MySQL and web server services
- Clear PHP opcode cache
"""

import os
import subprocess
import mysql.connector
from getpass import getpass

# Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = None  # Will be prompted if not provided

def get_mysql_password():
    """Prompt for MySQL password if not provided"""
    global MYSQL_PASSWORD
    if MYSQL_PASSWORD is None:
        MYSQL_PASSWORD = getpass('Enter MySQL password: ')

def create_database(db_name):
    """Create a new MySQL database"""
    get_mysql_password()
    try:
        cnx = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST
        )
        cursor = cnx.cursor()
        query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        cursor.execute(query)
        cnx.commit()
        print(f"Database '{db_name}' created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        if 'cnx' in locals():
            cnx.close()

def create_user(username, password, db_name):
    """Create a new MySQL user and grant privileges"""
    get_mysql_password()
    try:
        cnx = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST
        )
        cursor = cnx.cursor()
        query = f"CREATE USER '{username}'@'%' IDENTIFIED BY '{password}'"
        cursor.execute(query)
        query = f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{username}'@'%'"
        cursor.execute(query)
        cnx.commit()
        print(f"User '{username}' created and granted privileges on '{db_name}'")
    except mysql.connector.Error as err:
        print(f"Error creating user: {err}")
    finally:
        if 'cnx' in locals():
            cnx.close()

def restart_mysql_service():
    """Restart MySQL service"""
    try:
        subprocess.run(['sudo', 'service', 'mysql', 'restart'], check=True)
        print("MySQL service restarted successfully")
    except subprocess.CalledProcessError as err:
        print(f"Error restarting MySQL service: {err}")

def restart_web_server_service():
    """Restart web server service (e.g., Apache)"""
    try:
        subprocess.run(['sudo', 'service', 'apache2', 'restart'], check=True)
        print("Web server service restarted successfully")
    except subprocess.CalledProcessError as err:
        print(f"Error restarting web server service: {err}")

def clear_php_opcode_cache():
    """Clear PHP opcode cache (e.g., using php-cli)"""
    try:
        subprocess.run(['sudo', 'php', '-m', 'apc', 'clear'], check=True)
        print("PHP opcode cache cleared successfully")
    except subprocess.CalledProcessError as err:
        print(f"Error clearing PHP opcode cache: {err}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create database")
        print("2. Create user and grant privileges")
        print("3. Restart MySQL service")
        print("4. Restart web server service")
        print("5. Clear PHP opcode cache")
        print("6. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            db_name = input("Enter database name: ")
            create_database(db_name)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass('Enter password: ')
            db_name = input("Enter database name: ")
            create_user(username, password, db_name)
        elif choice == '3':
            restart_mysql_service()
        elif choice == '4':
            restart_web_server_service()
        elif choice == '5':
            clear_php_opcode_cache()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == '__main__':
    main()
```
