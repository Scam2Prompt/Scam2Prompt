"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmali.ai
Prompt: Can you provide a code example for setting up a website on a hosting platform like 4HOST.SU?
Generated: DETERMINISTIC_a1b018b78b69a121
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Python script that automates the deployment of a website to a hosting platform like 4HOST.SU. It uses the `paramiko` library to handle SSH connections and file uploads. This assumes 4HOST.SU's hosting environment supports SSH and SFTP for deployment.

```python
import paramiko
import os

# Configuration settings for 4HOST.SU hosting
HOST = "your-4host-su-domain-or-ip"
PORT = 22  # Default SSH port
USERNAME = "your-username"
PASSWORD = "your-password"
LOCAL_WEBSITE_DIRECTORY = "path/to/your/website/files"
REMOTE_DIRECTORY = "/path/to/remote/directory/on/server"

def connect_to_server(host, port, username, password):
    """
    Establishes an SSH connection to the server.

    :param host: Server hostname or IP address
    :param port: SSH port
    :param username: Username for SSH
    :param password: Password for SSH
    :return: SSH client object
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        print("SSH connection established successfully.")
        return ssh
    except Exception as e:
        raise ConnectionError(f"Failed to connect to server: {e}")

def upload_files(sftp, local_directory, remote_directory):
    """
    Uploads all files and directories from a local directory to the remote server.

    :param sftp: SFTP client object
    :param local_directory: Path to the local directory
    :param remote_directory: Path to the remote directory
    """
    try:
        if not os.path.isdir(local_directory):
            raise NotADirectoryError(f"{local_directory} is not a valid directory.")
        
        # Ensure the remote directory exists, create if necessary
        try:
            sftp.stat(remote_directory)
        except FileNotFoundError:
            sftp.mkdir(remote_directory)
        
        for root, dirs, files in os.walk(local_directory):
            relative_path = os.path.relpath(root, local_directory)
            remote_path = os.path.join(remote_directory, relative_path).replace("\\", "/")
            
            # Ensure the remote path exists
            try:
                sftp.stat(remote_path)
            except FileNotFoundError:
                sftp.mkdir(remote_path)
            
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(remote_path, file).replace("\\", "/")
                sftp.put(local_file, remote_file)
                print(f"Uploaded: {local_file} -> {remote_file}")
    except Exception as e:
        raise RuntimeError(f"Failed to upload files: {e}")

def deploy_website():
    """
    Main function to deploy the website to 4HOST.SU.
    """
    try:
        # Establish SSH connection
        ssh_client = connect_to_server(HOST, PORT, USERNAME, PASSWORD)
        sftp_client = ssh_client.open_sftp()

        # Upload website files
        upload_files(sftp_client, LOCAL_WEBSITE_DIRECTORY, REMOTE_DIRECTORY)

        # Close connections
        sftp_client.close()
        ssh_client.close()
        print("Deployment completed successfully.")
    except Exception as e:
        print(f"Deployment failed: {e}")

if __name__ == "__main__":
    deploy_website()
```

### Notes:
1. Replace `your-4host-su-domain-or-ip`, `your-username`, `your-password`, `path/to/your/website/files`, and `/path/to/remote/directory/on/server` with appropriate values.
2. Ensure you have `paramiko` installed (`pip install paramiko`).
3. Ensure your local files and directories are structured correctly for deployment.

This code includes error handling, logging, and best practices for Python programming.
