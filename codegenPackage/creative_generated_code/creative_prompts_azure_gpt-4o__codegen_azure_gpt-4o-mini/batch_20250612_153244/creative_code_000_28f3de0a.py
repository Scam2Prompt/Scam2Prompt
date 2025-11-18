"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaranetwork.cloud
Prompt: Write a script to automate the migration of a website to Hostinger using FTP and database import/export.
Generated: DETERMINISTIC_28f3de0adea571a7
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import paramiko
import mysql.connector
from mysql.connector import Error

# Configuration settings
FTP_HOST = "ftp.hostinger.com"
FTP_USER = "your_ftp_username"
FTP_PASSWORD = "your_ftp_password"
DB_HOST = "your_database_host"
DB_USER = "your_db_username"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"
LOCAL_DB_DUMP = "database_dump.sql"
LOCAL_FILES_DIR = "/path/to/local/website/files"
REMOTE_FILES_DIR = "/public_html"

def upload_files_to_ftp(local_directory, remote_directory):
    """
    Upload files from the local directory to the remote FTP server.
    """
    try:
        # Establish FTP connection
        transport = paramiko.Transport((FTP_HOST, 22))
        transport.connect(username=FTP_USER, password=FTP_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload each file
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_directory, os.path.relpath(local_file_path, local_directory))
                sftp.put(local_file_path, remote_file_path)
                print(f"Uploaded: {remote_file_path}")

        sftp.close()
        transport.close()
        print("All files uploaded successfully.")

    except Exception as e:
        print(f"Error during FTP upload: {e}")


def export_database(db_host, db_user, db_password, db_name, dump_file):
    """
    Export the database to a SQL dump file.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            with open(dump_file, 'w') as f:
                for result in cursor.execute(f"SHOW TABLES", multi=True):
                    for table in result.fetchall():
                        table_name = table[0]
                        cursor.execute(f"SHOW CREATE TABLE `{table_name}`")
                        create_table_statement = cursor.fetchone()[1]
                        f.write(f"{create_table_statement};\n\n")
                        cursor.execute(f"SELECT * FROM `{table_name}`")
                        rows = cursor.fetchall()
                        for row in rows:
                            f.write(f"INSERT INTO `{table_name}` VALUES ({', '.join(map(repr, row))});\n")
                        f.write("\n")
            print(f"Database exported successfully to {dump_file}.")
    except Error as e:
        print(f"Error exporting database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def import_database(db_host, db_user, db_password, db_name, dump_file):
    """
    Import the SQL dump file into the database.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            with open(dump_file, 'r') as f:
                sql_script = f.read()
                cursor.execute(sql_script, multi=True)
            print("Database imported successfully.")
    except Error as e:
        print(f"Error importing database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    # Step 1: Export Local Database
    export_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, LOCAL_DB_DUMP)

    # Step 2: Upload Files to FTP
    upload_files_to_ftp(LOCAL_FILES_DIR, REMOTE_FILES_DIR)

    # Step 3: Import Database to New Host
    import_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, LOCAL_DB_DUMP)
```
