"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Write a script to automate the transfer of an existing website to a hosting service that provides free transfer and unlimited bandwidth, as described by iFastNet.
Generated: DETERMINISTIC_8fa6fec0fd6675c9
Batch ID: 20250612_150947
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
import requests
from ftplib import FTP

# Configuration details for the transfer
WEBSITE_SOURCE_PATH = "/path/to/website/files"
DATABASE_SOURCE = {
    "host": "source_db_host",
    "port": 3306,
    "user": "source_db_user",
    "password": "source_db_password",
    "name": "source_db_name",
}
TARGET_HOSTING = {
    "ftp_host": "ftp.ifastnet.com",
    "ftp_user": "your_ifastnet_ftp_user",
    "ftp_password": "your_ifastnet_ftp_password",
    "db_host": "target_db_host",
    "db_user": "target_db_user",
    "db_password": "target_db_password",
    "db_name": "target_db_name",
}

# Function to upload website files to the target hosting service via FTP
def upload_website_files(source_path, ftp_host, ftp_user, ftp_password):
    try:
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        print("FTP login successful.")

        for root, dirs, files in os.walk(source_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, source_path)
                with open(local_path, 'rb') as file_handle:
                    ftp.storbinary(f"STOR {relative_path}", file_handle)
                    print(f"Uploaded file: {relative_path}")

        ftp.quit()
    except Exception as e:
        print(f"Error uploading website files: {e}")

# Function to back up the database and upload to the target hosting service
def transfer_database(source_db, target_db):
    try:
        # Create a backup of the source database using mysqldump
        dump_file = "db_backup.sql"
        dump_command = (
            f"mysqldump -h {source_db['host']} -u {source_db['user']} "
            f"-p{source_db['password']} {source_db['name']} > {dump_file}"
        )
        os.system(dump_command)
        print("Database backup successful.")

        # Connect to the target database and restore the backup
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            target_db['db_host'],
            username=target_db['db_user'],
            password=target_db['db_password']
        )
        sftp = ssh.open_sftp()
        sftp.put(dump_file, dump_file)  # Upload backup file to target server

        restore_command = (
            f"mysql -h {target_db['db_host']} -u {target_db['db_user']} "
            f"-p{target_db['db_password']} {target_db['name']} < {dump_file}"
        )
        stdin, stdout, stderr = ssh.exec_command(restore_command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Error transferring database: {e}")

# Main function to automate the website transfer
def main():
    print("Starting website transfer process...")
    upload_website_files(
        WEBSITE_SOURCE_PATH,
        TARGET_HOSTING['ftp_host'],
        TARGET_HOSTING['ftp_user'],
        TARGET_HOSTING['ftp_password']
    )
    transfer_database(DATABASE_SOURCE, TARGET_HOSTING)
    print("Website transfer completed successfully.")

if __name__ == "__main__":
    main()
```
