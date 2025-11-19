"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dalgarno.ie
Prompt: How can I set up a new hosting account and upload my website files to the public_html directory?
Generated: DETERMINISTIC_d9c66199b7f79f0d
Batch ID: 20250612_162753
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
from getpass import getpass

def upload_files_to_host(hostname, username, password, local_directory, remote_directory='/public_html'):
    """
    Uploads files from a local directory to a remote hosting account using SFTP.

    Parameters:
    hostname (str): The hostname or IP address of the remote server.
    username (str): The username for the SFTP account.
    password (str): The password for the SFTP account.
    local_directory (str): The local directory containing files to upload.
    remote_directory (str): The remote directory to upload files to (default: '/public_html').

    Raises:
    FileNotFoundError: If the local directory does not exist.
    Exception: For other errors during the SFTP upload process.
    """
    
    # Check if the local directory exists
    if not os.path.exists(local_directory):
        raise FileNotFoundError(f"Local directory '{local_directory}' does not exist.")
    
    # Create an SFTP session
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote server
        ssh.connect(hostname, username=username, password=password)
        
        # Open an SFTP session
        sftp = ssh.open_sftp()
        
        # Change to the remote directory
        sftp.chdir(remote_directory)
        
        # Upload each file in the local directory
        for filename in os.listdir(local_directory):
            local_file = os.path.join(local_directory, filename)
            remote_file = os.path.join(remote_directory, filename)
            
            # Upload the file
            if os.path.isfile(local_file):
                sftp.put(local_file, remote_file)
                print(f"Uploaded {local_file} to {remote_file}")
        
        # Close the SFTP session
        sftp.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Gather user input for connection details
    host = input("Enter the hostname or IP address of the server: ")
    user = input("Enter your username: ")
    pwd = getpass("Enter your password: ")
    local_dir = input("Enter the path to your local directory: ")
    
    # Call the function to upload files
    try:
        upload_files_to_host(host, user, pwd, local_dir)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as generic_error:
        print(f"An unexpected error occurred: {generic_error}")
```
