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
import subprocess
import paramiko

# Configuration for deployment
HOST = "your_server_ip"                  # Replace with your server IP
PORT = 22                                # Replace with your server SSH port (default 22)
USERNAME = "your_username"               # Replace with your SSH username
PASSWORD = "your_password"               # Replace with your SSH password
REMOTE_DIR = "/var/www/html/your_website" # Replace with the directory on the server where the website should be deployed
LOCAL_DIR = "/path/to/your/website"      # Replace with the local directory containing your website files

def validate_local_directory(local_dir):
    """
    Validate if the local directory exists and is accessible.
    """
    if not os.path.exists(local_dir):
        raise FileNotFoundError(f"The local directory '{local_dir}' does not exist.")
    if not os.access(local_dir, os.R_OK):
        raise PermissionError(f"The local directory '{local_dir}' is not readable.")

def connect_to_server(host, port, username, password):
    """
    Establishes an SSH connection to the server.
    Returns an active Paramiko SSH client.
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        return ssh
    except Exception as e:
        raise ConnectionError(f"Failed to connect to the server: {e}")

def upload_files(local_dir, remote_dir, ssh_client):
    """
    Upload website files from the local directory to the remote directory using SFTP.
    """
    try:
        # Start SFTP session
        sftp = ssh_client.open_sftp()
        
        # Ensure the remote directory exists
        try:
            sftp.stat(remote_dir)
        except FileNotFoundError:
            sftp.mkdir(remote_dir)
        
        # Upload all files and subdirectories
        for root, dirs, files in os.walk(local_dir):
            remote_path = os.path.join(remote_dir, os.path.relpath(root, local_dir)).replace("\\", "/")
            try:
                sftp.stat(remote_path)
            except FileNotFoundError:
                sftp.mkdir(remote_path)
            
            for file in files:
                local_file = os.path.join(root, file)
                remote_file = os.path.join(remote_path, file).replace("\\", "/")
                sftp.put(local_file, remote_file)
        
        sftp.close()
    except Exception as e:
        raise RuntimeError(f"Failed to upload files: {e}")

def restart_web_server(ssh_client):
    """
    Restarts the web server to apply changes (assumes Apache2 server).
    """
    try:
        stdin, stdout, stderr = ssh_client.exec_command('sudo systemctl restart apache2')
        exit_status = stdout.channel.recv_exit_status()
        if exit_status != 0:
            raise RuntimeError(f"Failed to restart web server. Error: {stderr.read().decode()}")
    except Exception as e:
        raise RuntimeError(f"Failed to restart web server: {e}")

def deploy_website():
    """
    Automates the deployment of a website.
    """
    try:
        # Validate local directory
        validate_local_directory(LOCAL_DIR)
        
        # Connect to the server
        ssh_client = connect_to_server(HOST, PORT, USERNAME, PASSWORD)
        
        # Upload files
        upload_files(LOCAL_DIR, REMOTE_DIR, ssh_client)
        
        # Restart web server
        restart_web_server(ssh_client)
        
        print("Website deployed successfully!")
        
    except Exception as e:
        print(f"Deployment failed: {e}")
    finally:
        # Close the SSH connection if established
        if 'ssh_client' in locals() and ssh_client:
            ssh_client.close()

if __name__ == "__main__":
    deploy_website()
```
