"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Describe the steps to transfer an existing website to iFastNet hosting and provide a sample code for the migration process.
Generated: DETERMINISTIC_ab6c2e4d093ac710
Batch ID: 20250612_155544
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
import ftplib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transfer_website_to_ifastnet(local_dir, remote_host, remote_user, remote_password, remote_dir):
    """
    Transfers a website's files from the local machine to iFastNet hosting via SFTP.

    Parameters:
    - local_dir (str): Local directory containing website files.
    - remote_host (str): iFastNet hosting server address.
    - remote_user (str): FTP username for iFastNet.
    - remote_password (str): FTP password for iFastNet.
    - remote_dir (str): Remote directory on iFastNet to upload files.

    Returns:
    - None
    """
    try:
        # Validate inputs
        if not os.path.exists(local_dir):
            raise ValueError(f"Local directory '{local_dir}' does not exist.")

        # Initialize SSH client for SFTP connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        logging.info("Connecting to the remote server...")
        ssh_client.connect(remote_host, username=remote_user, password=remote_password)

        # Open SFTP session
        sftp = ssh_client.open_sftp()

        # Ensure remote directory exists
        try:
            sftp.stat(remote_dir)
        except FileNotFoundError:
            logging.info(f"Remote directory '{remote_dir}' does not exist. Creating it...")
            sftp.mkdir(remote_dir)

        # Upload files recursively
        def upload_directory(local_path, remote_path):
            """
            Helper function to upload files recursively.
            """
            for item in os.listdir(local_path):
                local_item_path = os.path.join(local_path, item)
                remote_item_path = os.path.join(remote_path, item)

                if os.path.isdir(local_item_path):
                    logging.info(f"Creating directory '{remote_item_path}' on remote server...")
                    try:
                        sftp.mkdir(remote_item_path)
                    except OSError:
                        pass  # Directory may already exist
                    upload_directory(local_item_path, remote_item_path)
                else:
                    logging.info(f"Uploading file '{local_item_path}' to '{remote_item_path}'...")
                    sftp.put(local_item_path, remote_item_path)

        # Start the upload process
        upload_directory(local_dir, remote_dir)

        # Close SFTP and SSH connections
        sftp.close()
        ssh_client.close()
        logging.info("Website files transferred successfully!")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        if 'sftp' in locals():
            sftp.close()
        if 'ssh_client' in locals():
            ssh_client.close()
        raise

if __name__ == "__main__":
    # Example usage: replace these values with actual details
    LOCAL_DIR = "/path/to/your/local/website"
    REMOTE_HOST = "ftp.ifastnet.com"
    REMOTE_USER = "your_ifastnet_username"
    REMOTE_PASSWORD = "your_ifastnet_password"
    REMOTE_DIR = "/path/to/your/remote/website"

    transfer_website_to_ifastnet(LOCAL_DIR, REMOTE_HOST, REMOTE_USER, REMOTE_PASSWORD, REMOTE_DIR)
```
