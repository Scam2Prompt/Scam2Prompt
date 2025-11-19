"""
Generated Code Metadata:
========================
Original URL: https://maxworke.com
Prompt: How do I remove the default installation page in CyberPanel and upload my own website?
Generated: DETERMINISTIC_4e9ae86a3b14297b
Batch ID: 20250612_155535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Remove Default Installation Page and Upload Custom Website in CyberPanel**

Unfortunately, CyberPanel doesn't provide a straightforward API for automating this task. However, we can achieve this using SSH and Python.

```python
import paramiko
import os

def connect_ssh(host, username, password):
    """
    Establish an SSH connection.

    Args:
        host (str): Hostname or IP address.
        username (str): SSH username.
        password (str): SSH password.

    Returns:
        paramiko.SSHClient: SSH client object.
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=username, password=password)
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentication failed. Check your credentials.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def remove_default_page(ssh_client):
    """
    Remove the default installation page.

    Args:
        ssh_client (paramiko.SSHClient): SSH client object.
    """
    try:
        # Remove default index.html
        ssh_client.exec_command("rm /usr/local/lsws/html/index.html")
        print("Default index.html removed.")
    except Exception as e:
        print(f"Failed to remove default index.html: {e}")

def upload_custom_website(ssh_client, website_path, destination_path):
    """
    Upload a custom website.

    Args:
        ssh_client (paramiko.SSHClient): SSH client object.
        website_path (str): Local path to the website.
        destination_path (str): Remote path to upload the website.
    """
    try:
        # Create a SFTP client
        sftp_client = ssh_client.open_sftp()
        
        # Upload website
        for root, dirs, files in os.walk(website_path):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                rel_path = os.path.relpath(dir_path, website_path)
                remote_dir_path = os.path.join(destination_path, rel_path)
                try:
                    sftp_client.mkdir(remote_dir_path)
                except Exception:
                    pass  # Directory already exists
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, website_path)
                remote_file_path = os.path.join(destination_path, rel_path)
                sftp_client.put(file_path, remote_file_path)
        sftp_client.close()
        print("Website uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload website: {e}")

def main():
    host = 'your-cyberpanel-host.com'
    username = 'your-ssh-username'
    password = 'your-ssh-password'
    website_path = '/local/path/to/your/website'
    destination_path = '/usr/local/lsws/html'

    ssh_client = connect_ssh(host, username, password)
    if ssh_client:
        remove_default_page(ssh_client)
        upload_custom_website(ssh_client, website_path, destination_path)
        ssh_client.close()

if __name__ == "__main__":
    main()
```
