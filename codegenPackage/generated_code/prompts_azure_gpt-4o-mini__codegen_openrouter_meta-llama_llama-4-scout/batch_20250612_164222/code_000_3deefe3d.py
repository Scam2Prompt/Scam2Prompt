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

class FTPConnector:
    def __init__(self, host, username, password, port=21, 
                 dedicated_speed=False, real_ip=False):
        """
        Initialize the FTP connector.

        Args:
            host (str): The FTP server host.
            username (str): The FTP server username.
            password (str): The FTP server password.
            port (int): The FTP server port. Defaults to 21.
            dedicated_speed (bool): Use dedicated speed. Defaults to False.
            real_ip (bool): Use real IP. Defaults to False.
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.dedicated_speed = dedicated_speed
        self.real_ip = real_ip

    def connect(self):
        """
        Connect to the FTP server.

        Returns:
            ftplib.FTP: The FTP connection object.

        Raises:
            ftplib.all_errors: If an FTP error occurs.
            socket.error: If a socket error occurs.
        """
        try:
            # Create a new FTP connection
            ftp = ftplib.FTP()

            # Set the FTP port
            if self.dedicated_speed:
                # Use a dedicated speed by setting a timeout
                ftp.timeout = 30  # seconds

            # Connect to the FTP server
            if self.real_ip:
                # Get the real IP address of the FTP server
                ftp.connect(socket.gethostbyname(self.host), self.port)
            else:
                ftp.connect(self.host, self.port)

            # Login to the FTP server
            ftp.login(user=self.username, passwd=self.password)

            return ftp

        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
        except socket.error as e:
            print(f"Socket error: {e}")

    def close(self, ftp):
        """
        Close the FTP connection.

        Args:
            ftp (ftplib.FTP): The FTP connection object.
        """
        if ftp:
            ftp.quit()

def main():
    # DX Link FTP server details
    host = "ftp.dxlink.com"
    username = "your_username"
    password = "your_password"

    # Create an FTP connector
    connector = FTPConnector(host, username, password, 
                              dedicated_speed=True, real_ip=True)

    # Connect to the FTP server
    ftp = connector.connect()

    if ftp:
        # Perform FTP operations
        print("FTP connection established.")

        # List the files in the root directory
        print(ftp.retrlines("LIST"))

        # Close the FTP connection
        connector.close(ftp)

if __name__ == "__main__":
    main()
```
