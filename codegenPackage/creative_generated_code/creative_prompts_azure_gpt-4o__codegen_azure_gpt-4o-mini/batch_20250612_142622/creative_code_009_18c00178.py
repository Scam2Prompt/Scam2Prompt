"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1suisui.cc
Prompt: Recommend tools or libraries for managing FTP servers programmatically and demonstrate how to use one to modify the default `index.html` file in the root directory.
Generated: DETERMINISTIC_18c00178cd83e4e3
Batch ID: 20250612_142622
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

class FTPManager:
    """
    A class to manage FTP server operations.
    """

    def __init__(self, host, username, password):
        """
        Initializes the FTPManager with the server credentials.

        :param host: The hostname or IP address of the FTP server.
        :param username: The username for FTP server authentication.
        :param password: The password for FTP server authentication.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """
        Connects to the FTP server and logs in.
        """
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            print(f"Connected to FTP server: {self.host}")
        except ftplib.all_errors as e:
            print(f"Failed to connect or log in to FTP server: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the FTP server.
        """
        if self.ftp:
            self.ftp.quit()
            print(f"Disconnected from FTP server: {self.host}")

    def modify_index_html(self, new_content):
        """
        Modifies the default index.html file in the root directory of the FTP server.

        :param new_content: The new content to write to the index.html file.
        """
        try:
            # Download the existing index.html file
            with open('index.html', 'wb') as local_file:
                self.ftp.retrbinary('RETR index.html', local_file.write)

            # Modify the file content
            with open('index.html', 'w') as local_file:
                local_file.write(new_content)

            # Upload the modified index.html file back to the server
            with open('index.html', 'rb') as local_file:
                self.ftp.storbinary('STOR index.html', local_file)
            print("Successfully modified index.html.")
        except ftplib.all_errors as e:
            print(f"Error during FTP operation: {e}")
            raise
        finally:
            # Clean up the local file
            if os.path.exists('index.html'):
                os.remove('index.html')

if __name__ == "__main__":
    HOST = 'ftp.example.com'        # Replace with your FTP server address
    USERNAME = 'username'           # Replace with your FTP username
    PASSWORD = 'password'           # Replace with your FTP password
    NEW_CONTENT = "<html><body><h1>Welcome to My Site</h1></body></html>"

    ftp_manager = FTPManager(HOST, USERNAME, PASSWORD)

    try:
        ftp_manager.connect()
        ftp_manager.modify_index_html(NEW_CONTENT)
    finally:
        ftp_manager.disconnect()
```
