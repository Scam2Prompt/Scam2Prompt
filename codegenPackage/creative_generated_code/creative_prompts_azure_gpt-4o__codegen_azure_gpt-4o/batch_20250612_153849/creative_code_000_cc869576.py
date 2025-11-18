"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-nodeprotocol.host
Prompt: Write code to automate the migration of a website to Hostinger using FTP or other hosting protocols.
Generated: DETERMINISTIC_cc869576faba2f75
Batch ID: 20250612_153849
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

class WebsiteMigration:
    """
    Automates the migration of a website to Hostinger using FTP.
    """

    def __init__(self, ftp_host, ftp_username, ftp_password, local_directory, remote_directory):
        """
        Initializes the WebsiteMigration class with FTP credentials and directories.

        :param ftp_host: The hostname or IP address of the FTP server.
        :param ftp_username: The username for FTP authentication.
        :param ftp_password: The password for FTP authentication.
        :param local_directory: The local directory containing website files.
        :param remote_directory: The remote directory where files will be uploaded on the server.
        """
        self.ftp_host = ftp_host
        self.ftp_username = ftp_username
        self.ftp_password = ftp_password
        self.local_directory = local_directory
        self.remote_directory = remote_directory
        self.ftp_connection = None

    def connect_to_ftp(self):
        """
        Establishes a connection to the FTP server.
        """
        try:
            self.ftp_connection = ftplib.FTP(self.ftp_host)
            self.ftp_connection.login(self.ftp_username, self.ftp_password)
            print(f"Connected to FTP server: {self.ftp_host}")
        except ftplib.all_errors as e:
            print(f"Error connecting to FTP server: {e}")
            raise

    def upload_file(self, local_file_path, remote_file_path):
        """
        Uploads a single file to the remote FTP server.

        :param local_file_path: Path of the file in the local system.
        :param remote_file_path: Target path on the remote system.
        """
        try:
            with open(local_file_path, 'rb') as file:
                self.ftp_connection.storbinary(f"STOR {remote_file_path}", file)
                print(f"Uploaded: {local_file_path} -> {remote_file_path}")
        except ftplib.all_errors as e:
            print(f"Error uploading file {local_file_path}: {e}")
            raise

    def upload_directory(self, local_dir, remote_dir):
        """
        Recursively uploads a directory and its contents to the FTP server.

        :param local_dir: Local directory to upload.
        :param remote_dir: Target remote directory on the server.
        """
        try:
            # Ensure the remote directory exists
            try:
                self.ftp_connection.mkd(remote_dir)
                print(f"Created remote directory: {remote_dir}")
            except ftplib.error_perm:
                print(f"Remote directory already exists: {remote_dir}")

            # Iterate through files and subdirectories
            for item in os.listdir(local_dir):
                local_path = os.path.join(local_dir, item)
                remote_path = f"{remote_dir}/{item}"

                if os.path.isfile(local_path):
                    self.upload_file(local_path, remote_path)
                elif os.path.isdir(local_path):
                    self.upload_directory(local_path, remote_path)
        except ftplib.all_errors as e:
            print(f"Error uploading directory {local_dir}: {e}")
            raise

    def migrate(self):
        """
        Performs the migration by uploading all files from the local directory to the remote directory.
        """
        try:
            self.connect_to_ftp()
            self.upload_directory(self.local_directory, self.remote_directory)
            print("Website migration completed successfully.")
        except Exception as e:
            print(f"Migration failed: {e}")
        finally:
            # Close FTP connection
            if self.ftp_connection:
                self.ftp_connection.quit()
                print("FTP connection closed.")

# Example usage
if __name__ == "__main__":
    # FTP credentials and directories (replace with actual values)
    FTP_HOST = "ftp.hostinger.com"
    FTP_USERNAME = "your-ftp-username"
    FTP_PASSWORD = "your-ftp-password"
    LOCAL_DIRECTORY = "/path/to/your/local/website"
    REMOTE_DIRECTORY = "/public_html"

    # Initialize and run the migration
    migration = WebsiteMigration(FTP_HOST, FTP_USERNAME, FTP_PASSWORD, LOCAL_DIRECTORY, REMOTE_DIRECTORY)
    migration.migrate()
```
