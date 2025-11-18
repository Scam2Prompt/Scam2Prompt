"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Write code to integrate DX Link's FTP server options into a file transfer application, ensuring compatibility with their network specifications.
Generated: DETERMINISTIC_196a3f577ceb6c73
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import logging
import os

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FTPClient:
    def __init__(self, host, username, password, port=21):
        """
        Initializes the FTP client with the given credentials and server details.

        :param host: The FTP server's hostname or IP address.
        :param username: The username for FTP authentication.
        :param password: The password for FTP authentication.
        :param port: The port for the FTP server (default is 21).
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the FTP server.
        """
        try:
            logging.info(f"Connecting to FTP server at {self.host}:{self.port}...")
            self.connection = ftplib.FTP()
            self.connection.connect(self.host, self.port)
            self.connection.login(self.username, self.password)
            logging.info("Successfully connected and logged in to the FTP server.")
        except Exception as e:
            logging.error(f"Failed to connect to FTP server: {e}")
            raise

    def upload_file(self, local_file_path, remote_file_path):
        """
        Uploads a file to the FTP server.

        :param local_file_path: The path to the file on the local system.
        :param remote_file_path: The path to save the file on the FTP server.
        """
        if not os.path.exists(local_file_path):
            logging.error("Local file does not exist: " + local_file_path)
            raise FileNotFoundError("Local file does not exist.")

        try:
            with open(local_file_path, 'rb') as file:
                logging.info(f"Uploading {local_file_path} to {remote_file_path}...")
                self.connection.storbinary(f"STOR {remote_file_path}", file)
                logging.info("File uploaded successfully.")
        except Exception as e:
            logging.error(f"Failed to upload file: {e}")
            raise

    def download_file(self, remote_file_path, local_file_path):
        """
        Downloads a file from the FTP server.

        :param remote_file_path: The path to the file on the FTP server.
        :param local_file_path: The path to save the file locally.
        """
        try:
            with open(local_file_path, 'wb') as file:
                logging.info(f"Downloading {remote_file_path} to {local_file_path}...")
                self.connection.retrbinary(f"RETR {remote_file_path}", file.write)
                logging.info("File downloaded successfully.")
        except Exception as e:
            logging.error(f"Failed to download file: {e}")
            raise

    def list_files(self, directory='.'):
        """
        Lists files in the specified directory on the FTP server.

        :param directory: The directory to list files from (default is current directory).
        :return: A list of filenames in the directory.
        """
        try:
            logging.info(f"Listing files in directory: {directory}")
            file_list = self.connection.nlst(directory)
            logging.info(f"Files in directory '{directory}': {file_list}")
            return file_list
        except Exception as e:
            logging.error(f"Failed to list files: {e}")
            raise

    def disconnect(self):
        """
        Disconnects from the FTP server.
        """
        try:
            if self.connection is not None:
                logging.info("Closing connection to FTP server...")
                self.connection.quit()
                logging.info("Disconnected from FTP server.")
        except Exception as e:
            logging.error(f"Failed to disconnect: {e}")
            raise


# Example usage of the FTPClient class (Replace with actual host, username, and password)
if __name__ == "__main__":
    ftp_host = "ftp.dxlink.com"  # Replace with DX Link FTP server address
    ftp_user = "your_username"  # Replace with your username
    ftp_password = "your_password"  # Replace with your password

    try:
        # Initialize FTP client
        ftp_client = FTPClient(host=ftp_host, username=ftp_user, password=ftp_password)

        # Connect to FTP server
        ftp_client.connect()

        # Perform file operations (e.g., upload, download, list files)
        # Example: Upload a file
        ftp_client.upload_file("path/to/local/file.txt", "path/on/server/file.txt")

        # Example: Download a file
        ftp_client.download_file("path/on/server/file.txt", "path/to/local/file.txt")

        # Example: List files
        ftp_client.list_files("/")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Disconnect from FTP server
        ftp_client.disconnect()
```
