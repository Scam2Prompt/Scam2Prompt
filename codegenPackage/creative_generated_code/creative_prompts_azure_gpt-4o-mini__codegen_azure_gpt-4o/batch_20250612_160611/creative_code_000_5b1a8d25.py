"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth.info
Prompt: How can I upload my website files to the public_html directory on steth.info?
Generated: DETERMINISTIC_5b1a8d25c9841267
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script using `paramiko` (a library for SSH and SFTP connections) to upload website files to the `public_html` directory on `steth.info`. Ensure you have the required package installed (`pip install paramiko`) and proper credentials to connect to the server.

```python
import paramiko
import os

def upload_files_to_public_html(server, port, username, password, local_directory, remote_directory):
    """
    Uploads all files from a local directory to the public_html directory on a remote server.
    
    Args:
        server (str): The server's hostname or IP address (e.g., "steth.info").
        port (int): The port for SSH connection (default SSH port is 22).
        username (str): Username for authentication.
        password (str): Password for authentication.
        local_directory (str): Local directory containing the website files.
        remote_directory (str): Remote directory on the server (e.g., "public_html").
    """
    try:
        # Initialize the SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown host keys

        # Connect to the server
        ssh.connect(server, port=port, username=username, password=password)
        print("Connected to the server successfully.")

        # Initialize the SFTP client
        sftp = ssh.open_sftp()

        # Ensure the local directory exists
        if not os.path.isdir(local_directory):
            raise FileNotFoundError(f"Local directory '{local_directory}' does not exist.")

        # Upload files from local_directory to remote_directory
        for file_name in os.listdir(local_directory):
            local_file_path = os.path.join(local_directory, file_name)
            remote_file_path = os.path.join(remote_directory, file_name)

            if os.path.isfile(local_file_path):  # Only upload files, skip subdirectories
                print(f"Uploading {file_name} to {remote_directory}...")
                sftp.put(local_file_path, remote_file_path)  # Upload file
                print(f"Uploaded {file_name} successfully.")

        print("All files uploaded successfully.")

        # Close the SFTP client and SSH connection
        sftp.close()
        ssh.close()
        print("Connection closed.")

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection error: {ssh_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual server details and credentials
    SERVER = "steth.info"
    PORT = 22
    USERNAME = "your_username"
    PASSWORD = "your_password"
    LOCAL_DIRECTORY = "/path/to/your/local/website/files"
    REMOTE_DIRECTORY = "/home/your_username/public_html"

    upload_files_to_public_html(SERVER, PORT, USERNAME, PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
```

### Requirements:
1. Replace the placeholders like `your_username`, `your_password`, `/path/to/your/local/website/files`, and `/home/your_username/public_html` with the actual values relevant to your server and local environment.
   
2. Ensure you have installed Paramiko (`pip install paramiko`) before running the script.
