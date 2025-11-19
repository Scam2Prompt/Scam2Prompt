"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: How can I transfer my existing website to iFastNet Web Hosting while ensuring minimal downtime?
Generated: DETERMINISTIC_9493dea07b55c135
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import paramiko
from getpass import getpass

def transfer_files_to_ifastnet(local_directory: str, remote_directory: str, host: str, username: str, password: str):
    """
    Transfer files from a local directory to an iFastNet web hosting server using SFTP.

    :param local_directory: Path to the local directory containing website files.
    :param remote_directory: Path to the directory on the iFastNet server.
    :param host: Hostname or IP address of the iFastNet server.
    :param username: Username for iFastNet server login.
    :param password: Password for iFastNet server login.
    :raises FileNotFoundError: If the local directory does not exist.
    :raises Exception: For any other errors during file transfer.
    """
    # Check if the local directory exists
    if not os.path.isdir(local_directory):
        raise FileNotFoundError(f"Local directory '{local_directory}' does not exist.")

    # Initialize SFTP connection
    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Create remote directory if it doesn't exist
        try:
            sftp.mkdir(remote_directory)
        except FileExistsError:
            pass  # Ignore if the directory already exists

        # Transfer files
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_directory)
                remote_file_path = os.path.join(remote_directory, relative_path)

                # Create remote directories if necessary
                remote_file_dir = os.path.dirname(remote_file_path)
                try:
                    sftp.mkdir(remote_file_dir)
                except FileExistsError:
                    pass  # Ignore if the directory already exists

                # Transfer the file
                sftp.put(local_file_path, remote_file_path)

        print("File transfer completed successfully.")

    except Exception as e:
        print(f"An error occurred during file transfer: {e}")
    finally:
        sftp.close()
        transport.close()

if __name__ == "__main__":
    # User input for file transfer
    local_dir = input("Enter the path to the local directory: ")
    remote_dir = input("Enter the path to the remote directory on iFastNet: ")
    server_host = input("Enter the iFastNet server hostname or IP address: ")
    user = input("Enter your iFastNet username: ")
    passwd = getpass("Enter your iFastNet password: ")

    # Start file transfer
    transfer_files_to_ifastnet(local_dir, remote_dir, server_host, user, passwd)
```

This code transfers website files to an iFastNet web hosting server using SFTP and includes error handling and proper comments for clarity.
