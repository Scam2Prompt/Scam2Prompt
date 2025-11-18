"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv2.epizy.com
Prompt: Provide a step-by-step guide for migrating an existing website to a hosting service that offers free transfer, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_0fb2763ca186d0a6
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Step-by-Step Script for Migrating an Existing Website to iFastNet's Hosting Service

This script automates the process of migrating a website's files and database to iFastNet's hosting service.
Before running the script:
1. Ensure you have access to your old hosting server (FTP credentials and database details).
2. Ensure you have your iFastNet hosting account credentials.
3. Install the required Python packages using `pip install ftplib mysql-connector-python`.

This script uses FTP for file transfer and MySQL for database migration.
"""

import ftplib
import mysql.connector
import os
import zipfile
from datetime import datetime

# Function to connect to FTP and download website files
def download_website_files(ftp_host, ftp_user, ftp_password, remote_dir, local_backup_dir):
    """
    Download website files from the old hosting server via FTP.
    """
    try:
        print("Connecting to FTP server...")
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd(remote_dir)
        
        # Ensure local backup directory exists
        os.makedirs(local_backup_dir, exist_ok=True)
        
        print("Starting download of website files...")
        for filename in ftp.nlst():
            local_filepath = os.path.join(local_backup_dir, filename)
            with open(local_filepath, 'wb') as f:
                ftp.retrbinary('RETR ' + filename, f.write)
            print(f"Downloaded: {filename}")
        
        ftp.quit()
        print("FTP download completed successfully.")
    except Exception as e:
        print(f"Error during FTP file transfer: {e}")
        raise

# Function to export the MySQL database from old hosting
def export_database(db_host, db_user, db_password, db_name, backup_file):
    """
    Export the MySQL database to an SQL file.
    """
    try:
        print("Connecting to the old database server...")
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        
        print("Exporting database...")
        with open(backup_file, 'w') as f:
            for result in cursor.execute(f"SHOW TABLES", multi=False):
                table_name = result[0]
                cursor.execute(f"SHOW CREATE TABLE `{table_name}`")
                create_table_sql = cursor.fetchone()[1]
                f.write(f"{create_table_sql};\n")
                
                cursor.execute(f"SELECT * FROM `{table_name}`")
                rows = cursor.fetchall()
                for row in rows:
                    values = ', '.join(f"'{str(value)}'" for value in row)
                    f.write(f"INSERT INTO `{table_name}` VALUES ({values});\n")
        
        cursor.close()
        conn.close()
        print("Database export completed successfully.")
    except Exception as e:
        print(f"Error during database export: {e}")
        raise

# Function to upload files to the new hosting server via FTP
def upload_website_files(ftp_host, ftp_user, ftp_password, local_backup_dir, remote_dir):
    """
    Upload website files to the new hosting server via FTP.
    """
    try:
        print("Connecting to the new FTP server...")
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd(remote_dir)
        
        print("Starting upload of website files...")
        for filename in os.listdir(local_backup_dir):
            local_filepath = os.path.join(local_backup_dir, filename)
            with open(local_filepath, 'rb') as f:
                ftp.storbinary('STOR ' + filename, f)
            print(f"Uploaded: {filename}")
        
        ftp.quit()
        print("FTP upload completed successfully.")
    except Exception as e:
        print(f"Error during FTP file upload: {e}")
        raise

# Function to import the database into the new hosting server
def import_database(db_host, db_user, db_password, db_name, backup_file):
    """
    Import the MySQL database from an SQL file to the new hosting server.
    """
    try:
        print("Connecting to the new database server...")
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        
        print("Importing database...")
        with open(backup_file, 'r') as f:
            sql_commands = f.read().split(';')
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("Database import completed successfully.")
    except Exception as e:
        print(f"Error during database import: {e}")
        raise

# Main migration function
def migrate_website(old_ftp_details, old_db_details, new_ftp_details, new_db_details, backup_dir):
    """
    Perform the complete migration of files and database from old hosting to new hosting.
    """
    try:
        # Create timestamped backup directory
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_dir = os.path.join(backup_dir, f"backup_{timestamp}")
        
        # Step 1: Download website files from old hosting
        download_website_files(
            ftp_host=old_ftp_details['host'],
            ftp_user=old_ftp_details['user'],
            ftp_password=old_ftp_details['password'],
            remote_dir=old_ftp_details['remote_dir'],
            local_backup_dir=backup_dir
        )
        
        # Step 2: Export the database from old hosting
        backup_file = os.path.join(backup_dir, "database_backup.sql")
        export_database(
            db_host=old_db_details['host'],
            db_user=old_db_details['user'],
            db_password=old_db_details['password'],
            db_name=old_db_details['name'],
            backup_file=backup_file
        )
        
        # Step 3: Upload website files to new hosting
        upload_website_files(
            ftp_host=new_ftp_details['host'],
            ftp_user=new_ftp_details['user'],
            ftp_password=new_ftp_details['password'],
            local_backup_dir=backup_dir,
            remote_dir=new_ftp_details['remote_dir']
        )
        
        # Step 4: Import the database into new hosting
        import_database(
            db_host=new_db_details['host'],
            db_user=new_db_details['user'],
            db_password=new_db_details['password'],
            db_name=new_db_details['name'],
            backup_file=backup_file
        )
        
        print("Website migration completed successfully.")
    except Exception as e:
        print(f"Error during website migration: {e}")
        raise

# Example input details (replace with your actual credentials)
old_ftp_details = {
    'host': 'ftp.oldhost.com',
    'user': 'old_ftp_user',
    'password': 'old_ftp_password',
    'remote_dir': '/public_html'
}

old_db_details = {
    'host': 'oldhost.com',
    'user': 'old_db_user',
    'password': 'old_db_password',
    'name': 'old_database_name'
}

new_ftp_details = {
    'host': 'ftp.ifastnet.com',
    'user': 'new_ftp_user',
    'password': 'new_ftp_password',
    'remote_dir': '/public_html'
}

new_db_details = {
    'host': 'ifastnet.com',
    'user': 'new_db_user',
    'password': 'new_db_password',
    'name': 'new_database_name'
}

backup_dir = './website_backup'

# Execute migration process
migrate_website(old_ftp_details, old_db_details, new_ftp_details, new_db_details, backup_dir)
```
