"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlock.io
Prompt: How can I migrate a website to Hostinger using the steps described on Hyperlock.io?
Generated: DETERMINISTIC_9dce376d8665dc7a
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for migrating a website to Hostinger based on steps described on Hyperlock.io.
This script assumes you have access to the source website's files and database,
as well as Hostinger's FTP and database credentials.

Requirements:
- Python 3.x
- Necessary libraries: ftplib, mysql-connector-python, shutil, os

Make sure to install dependencies before running:
pip install mysql-connector-python
"""

import os
import shutil
import ftplib
import mysql.connector
from mysql.connector import Error

# Configuration for the source website
SOURCE_WEBSITE_PATH = "/path/to/source/website/files"  # Local path to the source website's files
SOURCE_DB_HOST = "source-db-host"
SOURCE_DB_USER = "source-db-user"
SOURCE_DB_PASSWORD = "source-db-password"
SOURCE_DB_NAME = "source-db-name"

# Configuration for the Hostinger server
HOSTINGER_FTP_HOST = "ftp.hostinger.com"
HOSTINGER_FTP_USER = "your-hostinger-ftp-username"
HOSTINGER_FTP_PASSWORD = "your-hostinger-ftp-password"
HOSTINGER_DB_HOST = "your-hostinger-db-host"
HOSTINGER_DB_USER = "your-hostinger-db-username"
HOSTINGER_DB_PASSWORD = "your-hostinger-db-password"
HOSTINGER_DB_NAME = "your-hostinger-db-name"

# Local temporary paths
TEMP_DB_BACKUP_FILE = "./backup.sql"
TEMP_WEBSITE_ARCHIVE = "./website.zip"


def backup_database(host, user, password, db_name, output_file):
    """
    Creates a backup of the database by exporting it to a SQL file.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        if connection.is_connected():
            cursor = connection.cursor()
            with open(output_file, "w") as f:
                for result in cursor.execute(f"SHOW TABLES;", multi=True):
                    for row in result.fetchall():
                        table = row[0]
                        f.write(f"-- Dumping table {table}\n")
                        cursor.execute(f"SELECT * FROM {table};")
                        for record in cursor.fetchall():
                            f.write(f"INSERT INTO {table} VALUES {record};\n")
            print(f"Database backup completed: {output_file}")
    except Error as e:
        print(f"Error occurred during database backup: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def archive_website_files(source_path, archive_path):
    """
    Archives the website files into a zip file for easier transfer.
    """
    try:
        shutil.make_archive(archive_path.replace(".zip", ""), "zip", source_path)
        print(f"Website files archived at: {archive_path}")
    except Exception as e:
        print(f"Error occurred during file archiving: {e}")


def upload_to_hostinger_ftp(host, user, password, local_file, remote_file):
    """
    Uploads a file to the Hostinger server via FTP.
    """
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=password)

        with open(local_file, "rb") as f:
            ftp.storbinary(f"STOR {remote_file}", f)
        print(f"File uploaded to Hostinger: {remote_file}")

        ftp.quit()
    except ftplib.all_errors as e:
        print(f"Error occurred during FTP upload: {e}")


def restore_database_to_hostinger(host, user, password, db_name, sql_file):
    """
    Restores the database on Hostinger by importing the SQL file.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        if connection.is_connected():
            cursor = connection.cursor()
            with open(sql_file, "r") as f:
                sql_commands = f.read()
                for command in sql_commands.split(";"):
                    if command.strip():
                        cursor.execute(command)
            print(f"Database restored successfully to Hostinger.")
    except Error as e:
        print(f"Error occurred during database restoration: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Main migration script
if __name__ == "__main__":
    try:
        print("Starting website migration...")

        # Step 1: Backup source database
        backup_database(SOURCE_DB_HOST, SOURCE_DB_USER, SOURCE_DB_PASSWORD, SOURCE_DB_NAME, TEMP_DB_BACKUP_FILE)

        # Step 2: Archive source website files
        archive_website_files(SOURCE_WEBSITE_PATH, TEMP_WEBSITE_ARCHIVE)

        # Step 3: Upload files to Hostinger via FTP
        upload_to_hostinger_ftp(HOSTINGER_FTP_HOST, HOSTINGER_FTP_USER, HOSTINGER_FTP_PASSWORD, TEMP_WEBSITE_ARCHIVE, "website.zip")

        # Step 4: Restore database backup to Hostinger
        restore_database_to_hostinger(HOSTINGER_DB_HOST, HOSTINGER_DB_USER, HOSTINGER_DB_PASSWORD, HOSTINGER_DB_NAME, TEMP_DB_BACKUP_FILE)

        print("Website migration completed successfully!")
    except Exception as e:
        print(f"An error occurred during migration: {e}")
    finally:
        # Clean up temporary files
        if os.path.exists(TEMP_DB_BACKUP_FILE):
            os.remove(TEMP_DB_BACKUP_FILE)
        if os.path.exists(TEMP_WEBSITE_ARCHIVE):
            os.remove(TEMP_WEBSITE_ARCHIVE)
```
