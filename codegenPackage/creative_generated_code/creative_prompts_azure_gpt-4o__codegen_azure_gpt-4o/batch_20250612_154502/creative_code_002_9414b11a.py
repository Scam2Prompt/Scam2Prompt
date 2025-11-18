"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: Generate a step-by-step guide to transfer an existing website to a hosting provider that offers free transfers and modern cPanel, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_9414b11a28858f78
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates the process of transferring an existing website to a hosting provider using cPanel and FTP. It assumes you have access to the iFastNet hosting service API or user credentials for the transfer:

```python
import os
import ftplib
import paramiko
from dotenv import load_dotenv

# Load environment variables from a .env file for security
load_dotenv()

# Constants for website transfer
SOURCE_WEBSITE_FILES = os.getenv("SOURCE_WEBSITE_FILES")  # Path to the local website files
SOURCE_DB_FILE = os.getenv("SOURCE_DB_FILE")  # Path to the local database dump (.sql file)
DESTINATION_FTP_HOST = os.getenv("DESTINATION_FTP_HOST")  # FTP host for iFastNet
DESTINATION_FTP_USERNAME = os.getenv("DESTINATION_FTP_USERNAME")  # FTP username for iFastNet
DESTINATION_FTP_PASSWORD = os.getenv("DESTINATION_FTP_PASSWORD")  # FTP password for iFastNet
DESTINATION_PUBLIC_HTML = "/public_html"  # Remote folder for website files
DESTINATION_SSH_HOST = os.getenv("DESTINATION_SSH_HOST")  # SSH host for iFastNet
DESTINATION_SSH_USERNAME = os.getenv("DESTINATION_SSH_USERNAME")  # SSH username for iFastNet
DESTINATION_SSH_PASSWORD = os.getenv("DESTINATION_SSH_PASSWORD")  # SSH password for iFastNet

def upload_files_via_ftp(local_path, remote_path):
    """
    Uploads files to the remote server via FTP.

    Args:
        local_path (str): Path to the local files.
        remote_path (str): Path on the remote FTP server.
    """
    try:
        print("Connecting to FTP server...")
        with ftplib.FTP(DESTINATION_FTP_HOST, DESTINATION_FTP_USERNAME, DESTINATION_FTP_PASSWORD) as ftp:
            ftp.cwd(remote_path)  # Change directory on the server
            for root, _, files in os.walk(local_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    with open(local_file_path, 'rb') as file_handle:
                        print(f"Uploading {file}...")
                        ftp.storbinary(f"STOR {file}", file_handle)
        print("Files uploaded successfully!")
    except Exception as e:
        print(f"Error during FTP upload: {e}")

def upload_database_via_ssh(local_db_path, remote_db_path="/home/tmp/db.sql"):
    """
    Uploads a database dump file to the remote server via SSH.

    Args:
        local_db_path (str): Path to the local database dump.
        remote_db_path (str): Remote path to upload the database dump.
    """
    try:
        print("Connecting to SSH server...")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(DESTINATION_SSH_HOST, username=DESTINATION_SSH_USERNAME, password=DESTINATION_SSH_PASSWORD)
        
        sftp = ssh_client.open_sftp()
        print(f"Uploading database dump file to {remote_db_path}...")
        sftp.put(local_db_path, remote_db_path)
        sftp.close()
        
        print("Restoring database on the remote server...")
        restore_command = f"mysql -u username -p'password' database_name < {remote_db_path}"
        stdin, stdout, stderr = ssh_client.exec_command(restore_command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        
        ssh_client.close()
        print("Database uploaded and restored successfully!")
    except Exception as e:
        print(f"Error during SSH transfer: {e}")

def main():
    """
    Main function to execute the website transfer process.
    """
    print("Starting website transfer process...")
    print("Step 1: Upload website files via FTP...")
    upload_files_via_ftp(SOURCE_WEBSITE_FILES, DESTINATION_PUBLIC_HTML)
    
    print("Step 2: Upload database dump via SSH...")
    upload_database_via_ssh(SOURCE_DB_FILE)

    print("Website transfer completed successfully!")

if __name__ == "__main__":
    main()
```

### Notes:
1. **Environment Variables:** Create a `.env` file to securely store sensitive data such as usernames, passwords, and server details.
2. **Dependencies:** Install required libraries using `pip install python-dotenv paramiko`.
3. **Error Handling:** The script includes basic error handling for FTP and SSH operations.
4. **Production-Ready:** Ensure you replace placeholder credentials with actual values and test the script in a staging environment before using it in production.
