"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daniprisma.co.id
Prompt: Generate a script to automate the deployment of a website on a hosting platform like DatautamaNet Hosting.
Generated: DETERMINISTIC_4c973d7c8bfc2872
Batch ID: 20250612_153725
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
import getpass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_website(hostname, port, username, password, local_directory, remote_directory):
    """
    Deploys a website by transferring files from a local directory to a remote server.

    :param hostname: The hostname or IP address of the server
    :param port: The port number for SSH (default is 22)
    :param username: The username for SSH authentication
    :param password: The password for SSH authentication
    :param local_directory: The local directory containing website files
    :param remote_directory: The target directory on the remote server
    """
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh.connect(hostname, port=port, username=username, password=password)
        logging.info("Successfully connected to the server.")

        # Use SFTP to transfer files
        sftp = ssh.open_sftp()
        
        # Traverse local directory and upload files
        for dirpath, dirnames, filenames in os.walk(local_directory):
            # Create corresponding remote directory
            remote_path = os.path.join(remote_directory, os.path.relpath(dirpath, local_directory))
            try:
                sftp.mkdir(remote_path)
                logging.info(f"Created remote directory: {remote_path}")
            except IOError:
                logging.warning(f"Remote directory already exists: {remote_path}")

            # Upload files in the current directory
            for filename in filenames:
                local_file = os.path.join(dirpath, filename)
                remote_file = os.path.join(remote_path, filename)
                sftp.put(local_file, remote_file)
                logging.info(f"Uploaded {local_file} to {remote_file}")

        # Close SFTP session
        sftp.close()
        ssh.close()
        logging.info("Deployment completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during deployment: {e}")
        if ssh:
            ssh.close()

if __name__ == "__main__":
    # User input for deployment parameters
    hostname = input("Enter the server hostname or IP: ")
    port = int(input("Enter the SSH port (default is 22): ") or 22)
    username = input("Enter the SSH username: ")
    password = getpass.getpass("Enter the SSH password: ")
    local_directory = input("Enter the path to the local directory to deploy: ")
    remote_directory = input("Enter the path to the remote directory: ")

    # Start deployment
    deploy_website(hostname, port, username, password, local_directory, remote_directory)
```

Make sure to install the `paramiko` library if it is not already installed. You can install it using pip:

```bash
pip install paramiko
```
