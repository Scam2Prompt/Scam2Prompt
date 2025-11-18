"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drutnet.in
Prompt: Write code to automate the migration of a website to Hostinger, referencing steps outlined in the "How can I migrate a website to Hostinger?" guide.
Generated: DETERMINISTIC_126001f4b530e2e6
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import requests
from getpass import getpass

def download_website_files(source_directory, destination_directory):
    """
    Download website files from the source directory to the destination directory.

    Parameters:
    source_directory (str): The local path to the website files.
    destination_directory (str): The path to the directory where files will be stored.

    Returns:
    bool: True if files are copied successfully, False otherwise.
    """
    try:
        shutil.copytree(source_directory, destination_directory)
        print(f"Website files copied from '{source_directory}' to '{destination_directory}'.")
        return True
    except Exception as e:
        print(f"Error copying files: {e}")
        return False

def backup_database(db_host, db_user, db_password, db_name, backup_file):
    """
    Backup the database using mysqldump command.

    Parameters:
    db_host (str): Database host.
    db_user (str): Database username.
    db_password (str): Database password.
    db_name (str): Database name.
    backup_file (str): Path to save the database backup.

    Returns:
    bool: True if backup is successful, False otherwise.
    """
    try:
        command = f"mysqldump -h {db_host} -u {db_user} -p{db_password} {db_name} > {backup_file}"
        os.system(command)
        print(f"Database backup created at '{backup_file}'.")
        return True
    except Exception as e:
        print(f"Error backing up database: {e}")
        return False

def upload_files_to_hostinger(destination_directory):
    """
    Upload website files to Hostinger using FTP.

    Parameters:
    destination_directory (str): The local path to the website files on the user's machine.

    Returns:
    bool: True if files are uploaded successfully, False otherwise.
    """
    # Placeholder for FTP upload logic.
    # Use an FTP library such as ftplib to connect to Hostinger and upload files.
    print(f"Uploading files from '{destination_directory}' to Hostinger...")
    # Implement FTP upload logic here.
    return True

def main():
    # User inputs for migration
    source_directory = input("Enter the path to your website files: ")
    destination_directory = input("Enter the path where you want to save the website files: ")

    # Step 1: Download website files
    if not download_website_files(source_directory, destination_directory):
        return

    # Step 2: Backup the database
    db_host = input("Enter your database host: ")
    db_user = input("Enter your database username: ")
    db_password = getpass("Enter your database password: ")
    db_name = input("Enter your database name: ")
    backup_file = os.path.join(destination_directory, f"{db_name}_backup.sql")

    if not backup_database(db_host, db_user, db_password, db_name, backup_file):
        return

    # Step 3: Upload files to Hostinger
    if not upload_files_to_hostinger(destination_directory):
        return

    print("Website migration to Hostinger completed successfully.")

if __name__ == "__main__":
    main()
```

Make sure to implement the FTP upload logic in the `upload_files_to_hostinger` function using appropriate libraries (like `ftplib`) to handle file transfers to your Hostinger account. Remember to test the script thoroughly in a safe environment before using it for actual migration.
