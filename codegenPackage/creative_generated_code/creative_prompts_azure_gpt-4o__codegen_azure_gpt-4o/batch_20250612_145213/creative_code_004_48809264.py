"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-nftclaim.free.nf
Prompt: Create a guide for transferring an existing website to a hosting service that offers free website transfers and unlimited disk space, such as iFastNet hosting.
Generated: DETERMINISTIC_48809264bd9d50ab
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to automate the transfer of an existing website to a hosting service like iFastNet.
This script assumes the user has access to their current website files and database,
and the new hosting service offers free website transfers and unlimited disk space.

Prerequisites:
- Python 3 installed on your machine.
- FTP or SFTP credentials for both the current and new hosting service.
- Database credentials for both the current and new hosting service.

IMPORTANT: Test the script in a safe environment before using it in production.
"""

import os
import ftplib
import pymysql
import shutil

# Configuration for current hosting
CURRENT_HOST = {
    "ftp_server": "current-ftp-server.com",
    "ftp_user": "current-ftp-username",
    "ftp_password": "current-ftp-password",
    "db_host": "current-db-server.com",
    "db_user": "current-db-username",
    "db_password": "current-db-password",
    "db_name": "current-db-name",
}

# Configuration for new hosting (e.g., iFastNet)
NEW_HOST = {
    "ftp_server": "new-ftp-server.com",
    "ftp_user": "new-ftp-username",
    "ftp_password": "new-ftp-password",
    "db_host": "new-db-server.com",
    "db_user": "new-db-username",
    "db_password": "new-db-password",
    "db_name": "new-db-name",
}

# Local directory for temporary storage
LOCAL_BACKUP_DIR = "website_backup"


def download_files_via_ftp(ftp_server, ftp_user, ftp_password, local_dir):
    """Download website files from the current hosting to a local directory."""
    print("Connecting to current FTP server...")
    try:
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        print("Connected to FTP server.")

        os.makedirs(local_dir, exist_ok=True)
        print(f"Downloading files to {local_dir}...")

        def download_file(file_path, local_path):
            with open(local_path, "wb") as f:
                ftp.retrbinary(f"RETR {file_path}", f.write)

        for item in ftp.nlst():  # List files and directories
            local_path = os.path.join(local_dir, item)
            download_file(item, local_path)

        ftp.quit()
        print("File download completed.")
    except Exception as e:
        print(f"Error during FTP operation: {e}")
        raise


def upload_files_via_ftp(ftp_server, ftp_user, ftp_password, local_dir):
    """Upload website files from the local directory to the new hosting."""
    print("Connecting to new FTP server...")
    try:
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        print("Connected to FTP server.")

        print(f"Uploading files from {local_dir}...")
        for root, dirs, files in os.walk(local_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, "rb") as f:
                    ftp.storbinary(f"STOR {file_name}", f)

        ftp.quit()
        print("File upload completed.")
    except Exception as e:
        print(f"Error during FTP operation: {e}")
        raise


def backup_database(db_host, db_user, db_password, db_name, backup_file_path):
    """Backup the current database to a SQL file."""
    print(f"Backing up database {db_name}...")
    try:
        connection = pymysql.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]

        with open(backup_file_path, "w") as f:
            for table in tables:
                cursor.execute(f"SHOW CREATE TABLE {table}")
                create_statement = cursor.fetchone()[1]
                f.write(f"{create_statement};\n")

                cursor.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()
                for row in rows:
                    values = ", ".join(str(v) for v in row)
                    f.write(f"INSERT INTO {table} VALUES ({values});\n")

        print(f"Database backup completed: {backup_file_path}")
    except Exception as e:
        print(f"Error during database backup: {e}")
        raise


def restore_database(db_host, db_user, db_password, db_name, backup_file_path):
    """Restore the database from a SQL file to the new hosting."""
    print(f"Restoring database {db_name}...")
    try:
        connection = pymysql.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        cursor = connection.cursor()

        with open(backup_file_path, "r") as f:
            sql_commands = f.read().split(";")
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

        connection.commit()
        print(f"Database restore completed.")
    except Exception as e:
        print(f"Error during database restore: {e}")
        raise


def main():
    """Main function to transfer the website to the new hosting."""
    try:
        # Step 1: Backup and transfer website files
        download_files_via_ftp(
            CURRENT_HOST["ftp_server"],
            CURRENT_HOST["ftp_user"],
            CURRENT_HOST["ftp_password"],
            LOCAL_BACKUP_DIR,
        )
        upload_files_via_ftp(
            NEW_HOST["ftp_server"],
            NEW_HOST["ftp_user"],
            NEW_HOST["ftp_password"],
            LOCAL_BACKUP_DIR,
        )

        # Step 2: Backup and transfer the database
        db_backup_path = os.path.join(LOCAL_BACKUP_DIR, "database_backup.sql")
        backup_database(
            CURRENT_HOST["db_host"],
            CURRENT_HOST["db_user"],
            CURRENT_HOST["db_password"],
            CURRENT_HOST["db_name"],
            db_backup_path,
        )
        restore_database(
            NEW_HOST["db_host"],
            NEW_HOST["db_user"],
            NEW_HOST["db_password"],
            NEW_HOST["db_name"],
            db_backup_path,
        )

        print("Website transfer completed successfully.")

        # Cleanup local backup directory
        shutil.rmtree(LOCAL_BACKUP_DIR)
        print("Local backup files cleaned up.")
    except Exception as e:
        print(f"An error occurred during the transfer process: {e}")


if __name__ == "__main__":
    main()
```
