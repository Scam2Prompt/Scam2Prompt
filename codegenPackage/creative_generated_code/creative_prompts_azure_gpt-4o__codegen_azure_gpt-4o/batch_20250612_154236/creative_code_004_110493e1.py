"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.rf.gd
Prompt: Provide a step-by-step guide for transferring a website from existing hosting to a service offering free transfer and multiple PHP versions, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_110493e10cdeb6f9
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to automate the process of transferring a website from existing hosting to iFastNet hosting.
This script assumes:
1. The website files are accessible via FTP.
2. The database can be exported as a `.sql` file.
3. The iFastNet account is already set up and credentials are available.
4. The new hosting supports multiple PHP versions as per iFastNet’s offering.

Prerequisites:
- Install the `ftplib` and `mysql-connector-python` libraries:
  `pip install mysql-connector-python`
"""

import ftplib
import os
import mysql.connector
from mysql.connector import Error


def download_website_files(ftp_host, ftp_user, ftp_pass, remote_dir, local_dir):
    """
    Connects to the old host's FTP server and downloads website files.
    
    Args:
        ftp_host (str): FTP server address.
        ftp_user (str): FTP username.
        ftp_pass (str): FTP password.
        remote_dir (str): Directory on the FTP server containing website files.
        local_dir (str): Local directory to store downloaded files.

    Returns:
        None
    """
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        ftp.cwd(remote_dir)

        # Ensure local directory exists
        os.makedirs(local_dir, exist_ok=True)

        # List files in remote directory
        files = ftp.nlst()

        for file in files:
            local_file_path = os.path.join(local_dir, file)
            with open(local_file_path, "wb") as local_file:
                ftp.retrbinary(f"RETR {file}", local_file.write)
            print(f"Downloaded: {file}")

        ftp.quit()
    except Exception as e:
        print(f"Error during FTP file transfer: {e}")
        raise


def export_database(db_host, db_user, db_pass, db_name, export_path):
    """
    Connects to the old host's MySQL database and exports it as a `.sql` file.
    
    Args:
        db_host (str): Database host address.
        db_user (str): Database username.
        db_pass (str): Database password.
        db_name (str): Name of the database to export.
        export_path (str): Path to save the exported `.sql` file.

    Returns:
        None
    """
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        with open(export_path, "w") as sql_file:
            for table in tables:
                table_name = table[0]
                cursor.execute(f"SHOW CREATE TABLE `{table_name}`")
                create_statement = cursor.fetchone()[1]
                sql_file.write(f"{create_statement};\n")
                
                cursor.execute(f"SELECT * FROM `{table_name}`")
                rows = cursor.fetchall()
                
                for row in rows:
                    values = ", ".join([f"'{str(value)}'" for value in row])
                    sql_file.write(f"INSERT INTO `{table_name}` VALUES ({values});\n")
        
        print(f"Database exported successfully to {export_path}")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error during database export: {e}")
        raise


def upload_to_ifastnet(ftp_host, ftp_user, ftp_pass, local_dir, remote_dir):
    """
    Uploads the website files to the new iFastNet hosting account.

    Args:
        ftp_host (str): FTP server of the iFastNet account.
        ftp_user (str): FTP username for iFastNet.
        ftp_pass (str): FTP password for iFastNet.
        local_dir (str): Local directory containing website files.
        remote_dir (str): Remote directory on the iFastNet FTP server.

    Returns:
        None
    """
    try:
        ftp = ftplib.FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        ftp.cwd(remote_dir)

        files = os.listdir(local_dir)

        for file in files:
            local_file_path = os.path.join(local_dir, file)
            with open(local_file_path, "rb") as local_file:
                ftp.storbinary(f"STOR {file}", local_file)
            print(f"Uploaded: {file}")

        ftp.quit()
    except Exception as e:
        print(f"Error during FTP upload: {e}")
        raise


def import_database_to_ifastnet(db_host, db_user, db_pass, db_name, sql_file_path):
    """
    Imports the exported `.sql` file into the new iFastNet MySQL database.

    Args:
        db_host (str): Database host for iFastNet.
        db_user (str): Database username for iFastNet.
        db_pass (str): Database password for iFastNet.
        db_name (str): Name of the database to import into.
        sql_file_path (str): Path to the `.sql` file.

    Returns:
        None
    """
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )

        cursor = connection.cursor()

        with open(sql_file_path, "r") as sql_file:
            sql_commands = sql_file.read().split(";")  # Split commands by semicolon
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

        connection.commit()
        print(f"Database imported successfully from {sql_file_path}")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error during database import: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    # Old hosting FTP details
    old_ftp_host = "old-host.com"
    old_ftp_user = "username"
    old_ftp_pass = "password"
    old_remote_dir = "/public_html"
    local_dir = "website_backup"

    # Old hosting MySQL details
    old_db_host = "old-db.com"
    old_db_user = "db_user"
    old_db_pass = "db_password"
    old_db_name = "db_name"
    db_export_path = "database_backup.sql"

    # iFastNet FTP details
    new_ftp_host = "ifastnet-ftp.com"
    new_ftp_user = "new_username"
    new_ftp_pass = "new_password"
    new_remote_dir = "/public_html"

    # iFastNet MySQL details
    new_db_host = "ifastnet-db.com"
    new_db_user = "new_db_user"
    new_db_pass = "new_db_password"
    new_db_name = "new_db_name"

    # Step 1: Download website files from old host
    download_website_files(old_ftp_host, old_ftp_user, old_ftp_pass, old_remote_dir, local_dir)

    # Step 2: Export database from old host
    export_database(old_db_host, old_db_user, old_db_pass, old_db_name, db_export_path)

    # Step 3: Upload website files to iFastNet
    upload_to_ifastnet(new_ftp_host, new_ftp_user, new_ftp_pass, local_dir, new_remote_dir)

    # Step 4: Import database to iFastNet
    import_database_to_ifastnet(new_db_host, new_db_user, new_db_pass, new_db_name, db_export_path)
```
