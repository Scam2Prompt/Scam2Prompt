"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth.fanclub.rocks
Prompt: Write a guide for transferring an existing website to a hosting service that offers free transfer, unlimited disk space, and modern cPanel, as described on iFastNet.
Generated: DETERMINISTIC_1460e78553d54950
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates the process of transferring a website to a hosting service such as iFastNet, leveraging their free transfer capabilities. This script uses the FTP protocol for file transfer and assumes SSH access for database migration. Replace placeholder values as needed.

```python
import os
import ftplib
import paramiko
import shutil

# Configuration for old and new hosting servers
OLD_SERVER = {
    "ftp_host": "old-server-ftp.com",
    "ftp_user": "old_ftp_user",
    "ftp_pass": "old_ftp_password",
    "website_root": "/public_html",  # Directory path to the website files
    "ssh_host": "old-server-ssh.com",
    "ssh_port": 22,
    "ssh_user": "old_ssh_user",
    "ssh_pass": "old_ssh_password",
    "db_name": "old_db_name",
    "db_user": "old_db_user",
    "db_pass": "old_db_password",
}
NEW_SERVER = {
    "ftp_host": "new-server-ftp.com",
    "ftp_user": "new_ftp_user",
    "ftp_pass": "new_ftp_password",
    "website_root": "/public_html",  # Directory path to upload the website files
    "ssh_host": "new-server-ssh.com",
    "ssh_port": 22,
    "ssh_user": "new_ssh_user",
    "ssh_pass": "new_ssh_password",
    "db_name": "new_db_name",
    "db_user": "new_db_user",
    "db_pass": "new_db_password",
}

# Backup directory
BACKUP_DIR = "./website_backup"


def download_website_files():
    """Download all website files from the old hosting server."""
    print("Downloading website files from the old server...")
    try:
        # Connect to old server via FTP
        ftp = ftplib.FTP(OLD_SERVER["ftp_host"], OLD_SERVER["ftp_user"], OLD_SERVER["ftp_pass"])
        ftp.cwd(OLD_SERVER["website_root"])
        
        # Ensure backup directory exists
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        # Helper function for recursive download
        def download_files(directory):
            os.chdir(BACKUP_DIR)
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)
            ftp.cwd(directory)

            items = ftp.nlst()
            for item in items:
                if "." in item:  # Assuming it's a file
                    with open(item, "wb") as f:
                        ftp.retrbinary(f"RETR {item}", f.write)
                else:  # Assuming it's a directory
                    download_files(item)
                    ftp.cwd("..")
                    os.chdir("..")

        download_files(OLD_SERVER["website_root"])
        print("Website files downloaded successfully!")
        ftp.quit()

    except ftplib.all_errors as e:
        print(f"Error downloading website files: {e}")
        raise


def backup_database():
    """Backup database from the old hosting server."""
    print("Backing up database from the old server...")
    try:
        # Connect to old server via SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            OLD_SERVER["ssh_host"],
            port=OLD_SERVER["ssh_port"],
            username=OLD_SERVER["ssh_user"],
            password=OLD_SERVER["ssh_pass"],
        )

        # Dump the database
        dump_file_path = os.path.join(BACKUP_DIR, f"{OLD_SERVER['db_name']}_backup.sql")
        dump_command = f"mysqldump -u {OLD_SERVER['db_user']} -p{OLD_SERVER['db_pass']} {OLD_SERVER['db_name']} > {dump_file_path}"
        stdin, stdout, stderr = ssh.exec_command(dump_command)
        stdout.channel.recv_exit_status()  # Wait for command to finish

        if os.path.exists(dump_file_path):
            print("Database backup completed successfully!")
        else:
            raise Exception("Failed to dump the database.")

        ssh.close()

    except paramiko.SSHException as e:
        print(f"Error backing up the database: {e}")
        raise


def upload_website_files():
    """Upload all website files to the new hosting server."""
    print("Uploading website files to the new server...")
    try:
        # Connect to new server via FTP
        ftp = ftplib.FTP(NEW_SERVER["ftp_host"], NEW_SERVER["ftp_user"], NEW_SERVER["ftp_pass"])
        ftp.cwd(NEW_SERVER["website_root"])

        # Helper function for recursive upload
        def upload_files(directory):
            os.chdir(BACKUP_DIR)
            os.chdir(directory)
            ftp.cwd(directory)

            items = os.listdir()
            for item in items:
                if os.path.isfile(item):  # Assuming it's a file
                    with open(item, "rb") as f:
                        ftp.storbinary(f"STOR {item}", f)
                else:  # Assuming it's a directory
                    ftp.mkd(item)
                    upload_files(item)
                    ftp.cwd("..")
                    os.chdir("..")

        upload_files(OLD_SERVER["website_root"])
        print("Website files uploaded successfully!")
        ftp.quit()

    except ftplib.all_errors as e:
        print(f"Error uploading website files: {e}")
        raise


def restore_database():
    """Restore database on the new hosting server."""
    print("Restoring database to the new server...")
    try:
        # Connect to new server via SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            NEW_SERVER["ssh_host"],
            port=NEW_SERVER["ssh_port"],
            username=NEW_SERVER["ssh_user"],
            password=NEW_SERVER["ssh_pass"],
        )

        # Restore the database
        dump_file_path = os.path.join(BACKUP_DIR, f"{OLD_SERVER['db_name']}_backup.sql")
        restore_command = f"mysql -u {NEW_SERVER['db_user']} -p{NEW_SERVER['db_pass']} {NEW_SERVER['db_name']} < {dump_file_path}"
        stdin, stdout, stderr = ssh.exec_command(restore_command)
        stdout.channel.recv_exit_status()  # Wait for command to finish

        print("Database restored successfully!")
        ssh.close()

    except paramiko.SSHException as e:
        print(f"Error restoring the database: {e}")
        raise


def transfer_website():
    """Main function to transfer the website."""
    try:
        print("Starting website transfer process...")
        download_website_files()
        backup_database()
        upload_website_files()
        restore_database()
        print("Website transfer completed successfully!")
    except Exception as e:
        print(f"Error during website transfer: {e}")


if __name__ == "__main__":
    transfer_website()
```

This script handles website file transfer via FTP and database backup/restoration via SSH. It uses Python libraries `ftplib` for FTP operations and `paramiko` for SSH commands. Make sure to install the required libraries and have proper permissions/access for both servers before running the script.
