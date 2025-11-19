"""
Generated Code Metadata:
========================
Original URL: https://geosatelites.com
Prompt: Write Python code to connect to the GEOSAT NTRIP service using the provided IP (190.212.223.230), port (2102), mountpoint (GEOSAT), username (geosatnic), and password (geosat2025).
Generated: DETERMINISTIC_1c809c901a83fc29
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import base64

class NTRIPClient:
    """
    A client to connect to an NTRIP (Networked Transport of RTCM via Internet Protocol) server.
    """
    
    def __init__(self, host, port, mountpoint, username, password):
        """
        Initialize the NTRIP client with connection details.
        
        Args:
            host (str): NTRIP server IP address or hostname.
            port (int): NTRIP server port.
            mountpoint (str): NTRIP mountpoint.
            username (str): NTRIP username.
            password (str): NTRIP password.
        """
        self.host = host
        self.port = port
        self.mountpoint = mountpoint
        self.username = username
        self.password = password
        self.socket = None
        
    def connect(self):
        """
        Connect to the NTRIP server and authenticate.
        
        Raises:
            socket.error: If connection or authentication fails.
            Exception: For other unexpected errors.
        """
        try:
            # Create a socket connection
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            
            # Prepare authentication header
            credentials = f"{self.username}:{self.password}"
            encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
            
            # Send HTTP GET request with authentication
            request = (
                f"GET /{self.mountpoint} HTTP/1.1\r\n"
                f"Host: {self.host}:{self.port}\r\n"
                f"Authorization: Basic {encoded_credentials}\r\n"
                "User-Agent: NTRIP PythonClient\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            self.socket.sendall(request.encode('utf-8'))
            
            # Check response
            response = self.socket.recv(4096).decode('utf-8')
            if "HTTP/1.1 200 OK" not in response:
                raise socket.error(f"Server returned an error: {response.splitlines()[0]}")
            
            print("Successfully connected to NTRIP server.")
            
        except socket.error as e:
            raise socket.error(f"Socket error: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")
            
    def disconnect(self):
        """Disconnect from the NTRIP server."""
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Disconnected from NTRIP server.")
            
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()


if __name__ == "__main__":
    # Connection details
    HOST = "190.212.223.230"
    PORT = 2102
    MOUNTPOINT = "GEOSAT"
    USERNAME = "geosatnic"
    PASSWORD = "geosat2025"
    
    try:
        # Connect using context manager
        with NTRIPClient(HOST, PORT, MOUNTPOINT, USERNAME, PASSWORD) as client:
            # Here you can add code to read data from the NTRIP stream
            pass
            
    except socket.error as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Error: {e}")
```
