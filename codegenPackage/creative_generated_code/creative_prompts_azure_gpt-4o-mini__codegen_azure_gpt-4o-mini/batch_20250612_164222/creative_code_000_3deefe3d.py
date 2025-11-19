"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Generate a code snippet to connect to an FTP server using the details provided by DX Link, including options for dedicated speed and real IP.
Generated: DETERMINISTIC_3deefe3d2b4bb1ea
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import socket

class FTPConnection:
    """
    A class to handle FTP connections to a specified server.

    Attributes:
        host (str): The FTP server address.
        port (int): The port for the FTP connection.
        username (str): The username for FTP authentication.
        password (str): The password for FTP authentication.
        speed_limit (int): Optional speed limit for the connection in KB/s.
        real_ip (str): Optional real IP to bind to the connection.
    """

    def __init__(self, host, port, username, password, speed_limit=None, real_ip=None):
        """
        Initializes the FTPConnection instance.

        Args:
            host (str): The FTP server address.
            port (int): The port for the FTP connection.
            username (str): The username for FTP authentication.
            password (str): The password for FTP authentication.
            speed_limit (int, optional): The speed limit for the connection in KB/s.
            real_ip (str, optional): The real IP to bind to the connection.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.speed_limit = speed_limit
        self.real_ip = real_ip
        self.ftp = None

    def connect(self):
        """Establishes the FTP connection with error handling."""
        try:
            # Create an FTP object
            self.ftp = ftplib.FTP()
            # If real_ip is provided, bind to it
            if self.real_ip:
                self._bind_to_ip(self.real_ip)

            # Connect to the FTP server
            self.ftp.connect(self.host, self.port)
            # Login to the FTP server
            self.ftp.login(self.username, self.password)
            print("Connection successful.")
        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _bind_to_ip(self, ip):
        """Binds the FTP connection to a specific IP address."""
        try:
            self.ftp.sock = socket.create_connection((self.host, self.port), source_address=(ip, 0))
            print(f"Bound to IP: {ip}")
        except socket.error as e:
            print(f"Binding failed: {e}")

    def set_speed_limit(self, limit):
        """Sets an optional speed limit for the connection."""
        # This method can be implemented based on specific requirements and libraries.
        self.speed_limit = limit
        print(f"Speed limit set to: {self.speed_limit} KB/s")

    def disconnect(self):
        """Closes the FTP connection gracefully."""
        if self.ftp:
            try:
                self.ftp.quit()
                print("Disconnected successfully.")
            except ftplib.error_perm as e:
                print(f"Failed to disconnect: {e}")

# Example usage
if __name__ == "__main__":
    ftp_details = {
        'host': 'ftp.example.com',
        'port': 21,
        'username': 'username',
        'password': 'password',
        'speed_limit': 50,  # Optional
        'real_ip': '192.168.1.100'  # Optional
    }

    ftp_connection = FTPConnection(**ftp_details)
    ftp_connection.connect()
    # Optionally set a speed limit
    ftp_connection.set_speed_limit(50)
    # Disconnect when done
    ftp_connection.disconnect()
```
