"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daniprisma.co.id
Prompt: Write a script to automate the deployment of a website on DatautamaNet Hosting.
Generated: DETERMINISTIC_2226c2b4ccef92a7
Batch ID: 20250612_155638
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_website(host, port, username, password, local_file_path, remote_directory):
    """
    Automates the deployment of a website to DatautamaNet Hosting via SFTP.

    Parameters:
        host (str): The hostname or IP of the server.
        port (int): The port for SFTP (typically 22).
        username (str): The username for authentication.
        password (str): The password for authentication.
        local_file_path (str): The path to the local file to deploy.
        remote_directory (str): The remote directory where the file will be uploaded.
    """
    try:
        # Initialize the SSH client
        logging.info("Initializing SSH client...")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the hosting server
        logging.info(f"Connecting to {host}:{port}...")
        ssh_client.connect(hostname=host, port=port, username=username, password=password)

        # Open an SFTP session
        logging.info("Opening SFTP session...")
        sftp = ssh_client.open_sftp()

        # Ensure the remote directory exists, creating it if necessary
        try:
            logging.info(f"Ensuring remote directory '{remote_directory}' exists...")
            sftp.stat(remote_directory)
        except FileNotFoundError:
            logging.info(f"Remote directory '{remote_directory}' not found. Creating it...")
            sftp.mkdir(remote_directory)

        # Upload the local file to the remote directory
        remote_file_path = os.path.join(remote_directory, os.path.basename(local_file_path))
        logging.info(f"Uploading file '{local_file_path}' to '{remote_file_path}'...")
        sftp.put(local_file_path, remote_file_path)

        logging.info("File successfully uploaded!")

        # Close the SFTP session and SSH connection
        logging.info("Closing SFTP session and SSH connection...")
        sftp.close()
        ssh_client.close()

    except Exception as e:
        logging.error("An error occurred during deployment:", exc_info=True)
        raise RuntimeError("Deployment failed.") from e


if __name__ == "__main__":
    # User-defined parameters for deployment
    HOST = "your-datautamanet-hosting.com"  # Replace with your actual host
    PORT = 22  # SFTP default port
    USERNAME = "your-username"  # Replace with your actual username
    PASSWORD = "your-password"  # Replace with your actual password
    LOCAL_FILE_PATH = "path/to/your/website.zip"  # Replace with your local file path
    REMOTE_DIRECTORY = "/public_html/"  # Replace with your target remote directory

    try:
        deploy_website(HOST, PORT, USERNAME, PASSWORD, LOCAL_FILE_PATH, REMOTE_DIRECTORY)
        logging.info("Website deployment completed successfully.")
    except RuntimeError:
        logging.error("Website deployment failed.")
```
