"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisvvap.run
Prompt: Write a script to automate the deployment of a website on a server managed by Ispmanager.
Generated: DETERMINISTIC_a311544e32d2a1b8
Batch ID: 20250612_161059
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
import sys
from scp import SCPClient

class DeploymentError(Exception):
    """Custom exception for deployment errors."""
    pass

def create_ssh_client(server_ip, server_port, username, password):
    """Establishes an SSH connection to the server."""
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server_ip, port=server_port, username=username, password=password)
        return client
    except Exception as e:
        raise DeploymentError(f"Failed to create SSH client: {str(e)}")

def deploy_files(ssh_client, local_path, remote_path):
    """Deploys files from local path to remote path on the server."""
    try:
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(local_path, recursive=True, remote_path=remote_path)
    except Exception as e:
        raise DeploymentError(f"Failed to deploy files: {str(e)}")

def restart_web_server(ssh_client):
    """Restarts the web server on the remote server."""
    try:
        stdin, stdout, stderr = ssh_client.exec_command('sudo systemctl restart nginx')  # Adjust based on your web server
        if stderr.read():
            raise DeploymentError(f"Failed to restart web server: {stderr.read().decode()}")
    except Exception as e:
        raise DeploymentError(f"Error executing command: {str(e)}")

def main():
    """Main function to run the deployment script."""
    SERVER_IP = os.getenv('SERVER_IP')
    SERVER_PORT = int(os.getenv('SERVER_PORT', 22))
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    LOCAL_PATH = os.getenv('LOCAL_PATH')
    REMOTE_PATH = os.getenv('REMOTE_PATH')

    try:
        # Establish SSH connection
        ssh_client = create_ssh_client(SERVER_IP, SERVER_PORT, USERNAME, PASSWORD)
        
        # Deploy files
        deploy_files(ssh_client, LOCAL_PATH, REMOTE_PATH)
        
        # Restart the web server
        restart_web_server(ssh_client)
        
        print("Deployment completed successfully.")
        
    except DeploymentError as e:
        print(f"Deployment failed: {str(e)}")
        sys.exit(1)
    finally:
        ssh_client.close()

if __name__ == '__main__':
    main()
```

**Note:** 
- Ensure you have `paramiko` and `scp` libraries installed. You can install them using `pip install paramiko scp`.
- Set environment variables for `SERVER_IP`, `SERVER_PORT`, `USERNAME`, `PASSWORD`, `LOCAL_PATH`, and `REMOTE_PATH` before running the script. Adjust the web server restart command based on your server configuration.
