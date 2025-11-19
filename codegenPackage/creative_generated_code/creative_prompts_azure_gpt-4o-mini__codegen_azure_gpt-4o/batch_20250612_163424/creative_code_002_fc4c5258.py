"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siemensgamesare.great-site.net
Prompt: Create a step-by-step guide for migrating an existing website to iFastNet, focusing on the free transfer feature and modern cPanel usage.
Generated: DETERMINISTIC_fc4c5258bc7b65b4
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for migrating an existing website to iFastNet using their free transfer feature.
This script assumes you have access to your current website's files and database,
and focuses on leveraging iFastNet's modern cPanel for seamless migration.
"""

import os
import shutil
import ftplib
import mysql.connector
from mysql.connector import Error

def backup_local_files(source_directory, backup_directory):
    """
    Back up local files to a specified backup directory.
    """
    try:
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        
        # Copy files to the backup directory
        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            destination_item = os.path.join(backup_directory, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_item)
        
        print("Local files backed up successfully.")
    except Exception as e:
        print(f"Error during file backup: {e}")
        exit(1)

def backup_database(host, user, password, database_name, backup_file):
    """
    Back up the MySQL database to a local file.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        if connection.is_connected():
            cursor = connection.cursor()
            backup_query = f"SHOW TABLES"
            cursor.execute(backup_query)
            tables = cursor.fetchall()
            
            with open(backup_file, 'w') as file:
                for table in tables:
                    table_name = table[0]
                    cursor.execute(f"SELECT * FROM {table_name}")
                    rows = cursor.fetchall()
                    
                    # Writing table data as SQL INSERT statements
                    for row in rows:
                        file.write(f"INSERT INTO {table_name} VALUES {tuple(row)};\n")

            print("Database backed up successfully.")
    except Error as e:
        print(f"Error during database backup: {e}")
        exit(1)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def upload_files_to_ifastnet(ftp_server, ftp_user, ftp_password, local_directory, remote_directory):
    """
    Upload files to iFastNet server via FTP.
    """
    try:
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        
        def upload_dir(local_dir, remote_dir):
            """
            Recursively upload a local directory to a remote directory.
            """
            if not remote_dir.startswith("/"):
                remote_dir = "/" + remote_dir
            
            # Change to remote directory or create if necessary
            try:
                ftp.cwd(remote_dir)
            except ftplib.error_perm:
                ftp.mkd(remote_dir)
                ftp.cwd(remote_dir)
            
            for item in os.listdir(local_dir):
                local_item = os.path.join(local_dir, item)
                if os.path.isdir(local_item):
                    upload_dir(local_item, f"{remote_dir}/{item}")
                else:
                    with open(local_item, 'rb') as file:
                        ftp.storbinary(f"STOR {item}", file)
        
        upload_dir(local_directory, remote_directory)
        print("Files uploaded to iFastNet server successfully.")
    except Exception as e:
        print(f"Error during FTP upload: {e}")
        exit(1)
    finally:
        ftp.quit()

def main():
    """
    Main function to perform website migration.
    """
    # Configure paths and credentials
    source_directory = "/path/to/your/website/files"
    backup_directory = "/path/to/backup/directory"
    database_host = "localhost"
    database_user = "root"
    database_password = "password"
    database_name = "your_database_name"
    database_backup_file = "/path/to/backup.sql"
    ftp_server = "ftp.ifastnet.com"
    ftp_user = "your_ftp_username"
    ftp_password = "your_ftp_password"
    remote_directory = "/public_html"

    # Step 1: Back up local files
    backup_local_files(source_directory, backup_directory)

    # Step 2: Back up the database
    backup_database(database_host, database_user, database_password, database_name, database_backup_file)

    # Step 3: Upload files to iFastNet
    upload_files_to_ifastnet(ftp_server, ftp_user, ftp_password, source_directory, remote_directory)

    print("Website migration completed successfully.")

if __name__ == "__main__":
    main()
```
