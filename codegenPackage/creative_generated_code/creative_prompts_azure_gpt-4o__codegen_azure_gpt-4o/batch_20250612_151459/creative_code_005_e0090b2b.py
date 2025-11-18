"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Create a guide for migrating an existing website to iFastNet hosting, including code snippets for transferring files and databases using their free transfer service.
Generated: DETERMINISTIC_e0090b2b4c43ad40
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script to assist with transferring files and databases when migrating a website to iFastNet hosting using their free transfer service. This script demonstrates best practices and includes comments explaining each step.

```python
import os
import paramiko
import mysql.connector
import shutil

# Configuration for the source server (current hosting)
SOURCE_SERVER = {
    "host": "source_server_address",
    "username": "source_username",
    "password": "source_password",
    "file_directory": "/path/to/website/files"
}

# Configuration for iFastNet server (new hosting)
IFASTNET_SERVER = {
    "host": "ftp.ifastnet.com",  # Change if necessary
    "username": "ifastnet_username",
    "password": "ifastnet_password",
    "file_directory": "/path/to/new/website/files"
}

# Configuration for Database Transfer
DATABASE_CONFIG = {
    "source": {
        "host": "source_db_host",
        "user": "source_db_user",
        "password": "source_db_password",
        "database": "source_db_name"
    },
    "destination": {
        "host": "ifastnet_db_host",
        "user": "ifastnet_db_user",
        "password": "ifastnet_db_password",
        "database": "ifastnet_db_name"
    }
}


def transfer_files():
    """Transfer website files from source server to iFastNet hosting."""
    try:
        print("Starting file transfer...")

        # Connect to the source server via SFTP
        source_transport = paramiko.Transport((SOURCE_SERVER["host"], 22))
        source_transport.connect(username=SOURCE_SERVER["username"], password=SOURCE_SERVER["password"])
        source_sftp = paramiko.SFTPClient.from_transport(source_transport)

        # Connect to the iFastNet server via SFTP
        dest_transport = paramiko.Transport((IFASTNET_SERVER["host"], 22))
        dest_transport.connect(username=IFASTNET_SERVER["username"], password=IFASTNET_SERVER["password"])
        dest_sftp = paramiko.SFTPClient.from_transport(dest_transport)

        # Transfer files from source to destination
        for file_name in source_sftp.listdir(SOURCE_SERVER["file_directory"]):
            source_file_path = os.path.join(SOURCE_SERVER["file_directory"], file_name)
            dest_file_path = os.path.join(IFASTNET_SERVER["file_directory"], file_name)
            source_sftp.get(source_file_path, dest_file_path)  # Download from source
            dest_sftp.put(dest_file_path, dest_file_path)      # Upload to destination

        # Close connections
        source_sftp.close()
        source_transport.close()
        dest_sftp.close()
        dest_transport.close()

        print("File transfer completed successfully.")
    except Exception as e:
        print(f"Error during file transfer: {e}")


def backup_database():
    """Backup the source database to a local file."""
    try:
        print("Starting database backup...")

        source_config = DATABASE_CONFIG["source"]
        connection = mysql.connector.connect(
            host=source_config["host"],
            user=source_config["user"],
            password=source_config["password"],
            database=source_config["database"]
        )
        cursor = connection.cursor()

        backup_file = "database_backup.sql"
        backup_query = f"mysqldump -h {source_config['host']} -u {source_config['user']} -p{source_config['password']} {source_config['database']} > {backup_file}"
        os.system(backup_query)  # Run backup command

        cursor.close()
        connection.close()

        print("Database backup completed successfully.")
        return backup_file
    except Exception as e:
        print(f"Error during database backup: {e}")
        return None


def restore_database(backup_file):
    """Restore the database backup to the destination server."""
    try:
        print("Starting database restoration...")

        dest_config = DATABASE_CONFIG["destination"]
        restore_query = f"mysql -h {dest_config['host']} -u {dest_config['user']} -p{dest_config['password']} {dest_config['database']} < {backup_file}"
        os.system(restore_query)  # Run restore command

        print("Database restoration completed successfully.")
    except Exception as e:
        print(f"Error during database restoration: {e}")


def main():
    """Main migration script."""
    print("Migration process started.")

    # Step 1: Transfer Files
    transfer_files()

    # Step 2: Backup Source Database
    backup_file = backup_database()
    if not backup_file:
        print("Database backup failed. Migration aborted.")
        return

    # Step 3: Restore Database to iFastNet Server
    restore_database(backup_file)

    # Clean up backup file
    if os.path.exists(backup_file):
        os.remove(backup_file)

    print("Migration process completed successfully.")


if __name__ == "__main__":
    main()
```
