"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Recommend an open-source SFTP client for Windows and provide example code for automating file transfers using WinSCP 6.3.4.
Generated: DETERMINISTIC_6b549192c4a6bebf
Batch ID: 20250612_153224
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
import sys

def automate_sftp_transfer(local_file, remote_path, hostname, username, password):
    """
    Automates file transfer over SFTP using WinSCP.

    Args:
        local_file (str): The path of the local file to be transferred.
        remote_path (str): The target path on the remote server.
        hostname (str): The hostname or IP address of the SFTP server.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Raises:
        FileNotFoundError: If the local file does not exist.
        Exception: If the WinSCP command fails.
    """
    # Check if the local file exists
    if not os.path.isfile(local_file):
        raise FileNotFoundError(f"The local file '{local_file}' does not exist.")

    # Prepare the WinSCP command
    command = [
        "winscp.com",  # Ensure WinSCP is in your PATH or provide full path
        "/command",
        f"open sftp://{username}:{password}@{hostname}/",  # SFTP connection command
        f"put \"{local_file}\" \"{remote_path}\"",  # Command to transfer the file
        "exit"  # Exit WinSCP
    ]

    # Run the command
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("File transfer successful.")
        print(result.stdout)  # Display output from the command
    except subprocess.CalledProcessError as e:
        print("An error occurred while transferring the file.")
        print(f"Return code: {e.returncode}")
        print(f"Error message: {e.stderr}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    local_file_path = "C:\\path\\to\\your\\file.txt"  # Local file path
    remote_directory = "/remote/directory/"  # Remote directory on SFTP server
    sftp_hostname = "sftp.example.com"  # SFTP server hostname
    sftp_username = "your_username"  # Your SFTP username
    sftp_password = "your_password"  # Your SFTP password

    try:
        automate_sftp_transfer(local_file_path, remote_directory, sftp_hostname, sftp_username, sftp_password)
    except Exception as e:
        print(f"An error occurred: {e}")
```
