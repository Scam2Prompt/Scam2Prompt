"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.io
Prompt: Provide a step-by-step guide in Python to upload website files to Hostinger, referencing the instructions on web3portal.io.
Generated: DETERMINISTIC_660d90d752de718f
Batch ID: 20250612_151343
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
from stat import S_ISDIR

def upload_files_to_hostinger(local_directory, remote_directory, host, username, password):
    """
    Uploads files from a local directory to a remote directory on Hostinger using SFTP.

    Parameters:
    local_directory (str): Path to the local directory containing files to upload.
    remote_directory (str): Path to the remote directory on the Hostinger server.
    host (str): Hostinger server hostname or IP address.
    username (str): Username for SFTP authentication.
    password (str): Password for SFTP authentication.
    """
    try:
        # Establish an SFTP connection to the Hostinger server
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Change to the remote directory
        sftp.chdir(remote_directory)

        for root, dirs, files in os.walk(local_directory):
            # Create remote directories if they do not exist
            for dir_name in dirs:
                remote_path = os.path.join(remote_directory, os.path.relpath(os.path.join(root, dir_name), local_directory))
                try:
                    sftp.mkdir(remote_path)
                except IOError:
                    # Directory already exists
                    pass

            for file_name in files:
                local_file_path = os.path.join(root, file_name)
                remote_file_path = os.path.join(remote_directory, os.path.relpath(local_file_path, local_directory))

                # Upload the file
                try:
                    sftp.put(local_file_path, remote_file_path)
                    print(f"Uploaded: {local_file_path} to {remote_file_path}")
                except Exception as e:
                    print(f"Failed to upload {local_file_path}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SFTP connection
        sftp.close()
        transport.close()

if __name__ == "__main__":
    # Define local and remote directories
    LOCAL_DIRECTORY = '/path/to/local/website/files'
    REMOTE_DIRECTORY = '/path/to/remote/directory/on/hostinger'
    
    # Hostinger credentials
    HOST = 'your.hostinger.server'  # e.g., 'ftp.hostinger.com'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'

    # Call the upload function
    upload_files_to_hostinger(LOCAL_DIRECTORY, REMOTE_DIRECTORY, HOST, USERNAME, PASSWORD)
```

**Note**: Make sure to replace the placeholder values in the script (especially paths and credentials) with actual values before running the code.
