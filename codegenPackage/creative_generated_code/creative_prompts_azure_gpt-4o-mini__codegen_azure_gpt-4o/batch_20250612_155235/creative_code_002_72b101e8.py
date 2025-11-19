"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inovarerep.com.br
Prompt: Can you provide a code snippet for uploading files to a web server's public_html directory using FTP?
Generated: DETERMINISTIC_72b101e8a501590f
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import os

def upload_file_to_server(ftp_host, ftp_port, username, password, local_file_path, remote_directory):
    """
    Uploads a file to the specified remote directory on an FTP server.

    Args:
        ftp_host (str): The hostname or IP address of the FTP server.
        ftp_port (int): The port number of the FTP server (default FTP port is 21).
        username (str): The username for FTP authentication.
        password (str): The password for FTP authentication.
        local_file_path (str): The path to the file to be uploaded on the local machine.
        remote_directory (str): The remote directory (e.g., public_html) where the file should be uploaded.

    Returns:
        bool: True if the upload is successful, False otherwise.
    """
    try:
        # Validate the local file exists.
        if not os.path.isfile(local_file_path):
            print(f"Error: File '{local_file_path}' does not exist.")
            return False

        # Connect to the FTP server.
        with ftplib.FTP() as ftp:
            ftp.connect(host=ftp_host, port=ftp_port)
            print("Connected to FTP server.")

            # Login using provided credentials.
            ftp.login(user=username, passwd=password)
            print("Logged in successfully.")

            # Change directory to the target location.
            ftp.cwd(remote_directory)
            print(f"Changed directory to '{remote_directory}'.")

            # Open the local file for reading in binary mode.
            with open(local_file_path, 'rb') as file:
                # Upload the file using STOR command.
                remote_filename = os.path.basename(local_file_path)
                ftp.storbinary(f"STOR {remote_filename}", file)
                print(f"File '{local_file_path}' uploaded successfully as '{remote_filename}'.")

        # Return True if the function executes without exceptions.
        return True
    except ftplib.all_errors as e:
        # Capture and print any FTP-related errors.
        print(f"FTP error: {e}")
        return False
    except Exception as e:
        # Capture general exceptions.
        print(f"An error occurred: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    # Replace these with actual values.
    FTP_HOST = "ftp.example.com"
    FTP_PORT = 21
    USERNAME = "your_username"
    PASSWORD = "your_password"
    LOCAL_FILE_PATH = "path/to/your/file.txt"
    REMOTE_DIRECTORY = "/public_html"

    # Attempt to upload the file.
    success = upload_file_to_server(FTP_HOST, FTP_PORT, USERNAME, PASSWORD, LOCAL_FILE_PATH, REMOTE_DIRECTORY)
    if success:
        print("File uploaded successfully.")
    else:
        print("File upload failed.")
```
