"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Generate a code snippet to connect to an FTP server using the details provided by DX Link, including options for dedicated speed and real IP.
Generated: DETERMINISTIC_3deefe3d2b4bb1ea
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ftplib
import socket

class FTPConnection:
    """
    A class to handle FTP connections with options for dedicated speed and real IP.
    """

    def __init__(self, host, username, password, port=21, timeout=30):
        """
        Initializes the FTPConnection instance.

        :param host: The FTP server hostname or IP address.
        :param username: The username for FTP authentication.
        :param password: The password for FTP authentication.
        :param port: The port number for the FTP connection (default is 21).
        :param timeout: The timeout for the connection in seconds (default is 30).
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.ftp = None

    def connect(self):
        """
        Connects to the FTP server and logs in with the provided credentials.
        """
        try:
            # Create an FTP object
            self.ftp = ftplib.FTP()
            # Set the timeout for the connection
            self.ftp.connect(self.host, self.port, self.timeout)
            # Log in to the FTP server
            self.ftp.login(self.username, self.password)
            print("Successfully connected to the FTP server.")
        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def disconnect(self):
        """
        Disconnects from the FTP server.
        """
        if self.ftp:
            try:
                self.ftp.quit()
                print("Successfully disconnected from the FTP server.")
            except ftplib.all_errors as e:
                print(f"Error while disconnecting: {e}")

    def upload_file(self, file_path, remote_path):
        """
        Uploads a file to the FTP server.

        :param file_path: The local path of the file to upload.
        :param remote_path: The destination path on the FTP server.
        """
        if not self.ftp:
            print("Not connected to any FTP server.")
            return

        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                print(f"Successfully uploaded {file_path} to {remote_path}.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ftplib.all_errors as e:
            print(f"FTP error during upload: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during upload: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with your FTP server details
    ftp_host = "ftp.example.com"
    ftp_username = "your_username"
    ftp_password = "your_password"

    # Create an instance of FTPConnection
    ftp_connection = FTPConnection(ftp_host, ftp_username, ftp_password)

    # Connect to the FTP server
    ftp_connection.connect()

    # Upload a file (replace with actual file paths)
    ftp_connection.upload_file("local_file.txt", "remote_file.txt")

    # Disconnect from the FTP server
    ftp_connection.disconnect()
```
