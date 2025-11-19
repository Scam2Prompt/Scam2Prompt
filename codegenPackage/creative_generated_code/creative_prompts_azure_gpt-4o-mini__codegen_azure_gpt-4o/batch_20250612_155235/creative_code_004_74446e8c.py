"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inovarerep.com.br
Prompt: How do I set up a new website by uploading files to the public_html directory?
Generated: DETERMINISTIC_74446e8c4fa496ee
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Python script using `paramiko` to upload files to the `public_html` directory via SFTP. Make sure to install the `paramiko` library (`pip install paramiko`) before running the script.

```python
import os
import paramiko

# Function to upload files to the 'public_html' directory
def upload_to_public_html(server, port, username, password, local_dir, remote_dir='public_html'):
    """
    Uploads files from a local directory to the public_html directory on a remote server.

    Parameters:
    server (str): The remote server's hostname or IP address.
    port (int): The port for SFTP connection (default is 22 for SSH/SFTP).
    username (str): The username for the remote server.
    password (str): The password for the remote server.
    local_dir (str): The path to the local directory containing files to upload.
    remote_dir (str): The path to the remote directory (default is 'public_html').

    Returns:
    None
    """
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown hosts
        ssh.connect(server, port=port, username=username, password=password)

        # Open SFTP session
        sftp = ssh.open_sftp()

        # Ensure the remote directory exists; create if necessary
        try:
            sftp.listdir(remote_dir)  # Check if the directory exists
        except FileNotFoundError:
            sftp.mkdir(remote_dir)  # Create the directory if it does not exist

        # Upload files to the remote directory
        for root, _, files in os.walk(local_dir):
            for file in files:
                local_path = os.path.join(root, file)
                remote_path = os.path.join(remote_dir, file)
                sftp.put(local_path, remote_path)  # Upload the file
                print(f"Uploaded: {local_path} -> {remote_path}")

        print("All files uploaded successfully.")

        # Close the SFTP session
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        if 'sftp' in locals():  # Ensure SFTP is closed in case of an error
            sftp.close()
        if 'ssh' in locals():  # Ensure SSH is closed in case of an error
            ssh.close()

# Example usage:
if __name__ == "__main__":
    # Replace these with your actual server details and local directory path
    SERVER = 'example.com'
    PORT = 22
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    LOCAL_DIR = '/path/to/your/local/files'

    upload_to_public_html(SERVER, PORT, USERNAME, PASSWORD, LOCAL_DIR)
```

Key points of the code:
1. The script uses `paramiko` for secure file transfer (SFTP).
2. It checks if the `public_html` directory exists, and creates it if not.
3. It traverses the local directory and uploads all files to the remote `public_html` folder.
4. Error handling ensures issues (e.g., authentication failures, missing directories) are gracefully reported.
