"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inovarerep.com.br
Prompt: How can I upload my website files to the public_html directory on a server?
Generated: DETERMINISTIC_0598a5c61591c44e
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code using the `paramiko` library to upload website files to the `public_html` directory on a server via SFTP.

```python
import paramiko
import os

def upload_files_to_server(server_host, server_port, username, password, local_dir, remote_dir):
    """
    Uploads files from a local directory to a remote server's directory (e.g., public_html).

    Parameters:
    - server_host (str): The server's hostname or IP address.
    - server_port (int): The server's port number (default for SFTP is usually 22).
    - username (str): The username for authentication.
    - password (str): The password for authentication.
    - local_dir (str): Path to the local directory containing the website files.
    - remote_dir (str): Path to the remote directory (e.g., public_html).

    Returns:
    None
    """
    try:
        # Establish an SSH connection to the server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept unknown host keys
        ssh.connect(server_host, port=server_port, username=username, password=password)

        # Open an SFTP session
        sftp = ssh.open_sftp()

        # Ensure the remote directory exists
        try:
            sftp.stat(remote_dir)  # Check if the directory exists
        except FileNotFoundError:
            sftp.mkdir(remote_dir)  # Create the directory if it doesn't exist
        
        # Upload files from the local directory to the remote directory
        for root, _, files in os.walk(local_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_dir)  # Get relative path
                remote_file_path = os.path.join(remote_dir, relative_path).replace("\\", "/")  # Handle cross-platform paths

                # Ensure remote subdirectories exist
                remote_subdir = os.path.dirname(remote_file_path)
                try:
                    sftp.stat(remote_subdir)
                except FileNotFoundError:
                    sftp.mkdir(remote_subdir)

                # Upload the file
                sftp.put(local_file_path, remote_file_path)
                print(f"Uploaded: {local_file_path} -> {remote_file_path}")

        print("All files uploaded successfully.")
        
        # Close the SFTP session
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace these values with your server and directory info
    SERVER_HOST = "your-server.com"
    SERVER_PORT = 22
    USERNAME = "your-username"
    PASSWORD = "your-password"
    LOCAL_DIRECTORY = "/path/to/your/local/files"
    REMOTE_DIRECTORY = "/path/to/public_html"

    upload_files_to_server(SERVER_HOST, SERVER_PORT, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
```

**Notes:**
- Install the required library `paramiko` using `pip install paramiko` before running this script.
- Ensure the server credentials are valid and the user has the necessary permissions to write to `public_html`.
