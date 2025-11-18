"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drutnet.in
Prompt: Generate a step-by-step Python script for transferring website files to Hostinger, ensuring compatibility with the migration process mentioned.
Generated: DETERMINISTIC_06591273e6b01d81
Batch ID: 20250612_152000
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
from scp import SCPClient, SCPException

def create_ssh_client(server_ip, server_port, username, password):
    """
    Create an SSH client and connect to the server.

    :param server_ip: IP address of the server
    :param server_port: Port number for SSH (default is 22)
    :param username: Username for SSH authentication
    :param password: Password for SSH authentication
    :return: SSH client object
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server_ip, port=server_port, username=username, password=password)
        return client
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
        raise

def transfer_files_to_hostinger(local_path, remote_path, ssh_client):
    """
    Transfer files from local directory to a remote server using SCP.

    :param local_path: Local directory path containing files to be transferred
    :param remote_path: Remote directory path on the server
    :param ssh_client: Established SSH client for communication
    """
    try:
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(local_path, recursive=True)  # Transfer files recursively
            print(f"Files successfully transferred to {remote_path}")
    except SCPException as e:
        print(f"File transfer failed: {e}")
        raise

def main():
    # Configuration parameters for the transfer
    SERVER_IP = 'your_hostinger_ip'  # Hostinger IP address
    SERVER_PORT = 22                   # SSH port (default 22)
    USERNAME = 'your_username'         # SSH username
    PASSWORD = 'your_password'         # SSH password
    LOCAL_PATH = '/path/to/local/files'  # Local directory to transfer
    REMOTE_PATH = '/path/to/remote/directory'  # Remote directory on Hostinger

    # Create SSH client
    ssh_client = create_ssh_client(SERVER_IP, SERVER_PORT, USERNAME, PASSWORD)

    try:
        # Transfer files
        transfer_files_to_hostinger(LOCAL_PATH, REMOTE_PATH, ssh_client)
    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == '__main__':
    main()
```

Make sure to replace `'your_hostinger_ip'`, `'your_username'`, `'your_password'`, and the directory paths with your actual Hostinger details before running the script.
