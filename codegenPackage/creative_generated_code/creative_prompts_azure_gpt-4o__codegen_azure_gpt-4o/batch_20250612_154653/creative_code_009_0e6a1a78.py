"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Write code to integrate SSL certificates provided by Smart Validation into a website to enable secure HTTPS connections and improve search engine rankings.
Generated: DETERMINISTIC_0e6a1a781c26fd28
Batch ID: 20250612_154653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.host}:{self.port": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

class SecureHTTPServer:
    """
    A class to set up a secure HTTPS server using SSL certificates.
    """

    def __init__(self, host='localhost', port=443, cert_file='cert.pem', key_file='key.pem'):
        """
        Initialize the HTTPS server with SSL certificates.
        
        :param host: The hostname for the server (default: 'localhost').
        :param port: The port number for the server (default: 443).
        :param cert_file: Path to the SSL certificate file.
        :param key_file: Path to the SSL key file.
        """
        self.host = host
        self.port = port
        self.cert_file = cert_file
        self.key_file = key_file

        # Check if the certificate and key files exist
        self._validate_ssl_files()

    def _validate_ssl_files(self):
        """
        Validates the presence of SSL certificate and key files.
        Raises an exception if any file is missing.
        """
        if not os.path.isfile(self.cert_file):
            raise FileNotFoundError(f"Certificate file '{self.cert_file}' not found.")
        if not os.path.isfile(self.key_file):
            raise FileNotFoundError(f"Key file '{self.key_file}' not found.")

    def start(self):
        """
        Starts the HTTPS server and binds it to the specified host and port.
        """
        # Create HTTP server
        server = HTTPServer((self.host, self.port), SimpleHTTPRequestHandler)

        # Configure SSL
        server.socket = ssl.wrap_socket(
            server.socket,
            certfile=self.cert_file,
            keyfile=self.key_file,
            server_side=True
        )

        print(f"Secure HTTPS server running at https://{self.host}:{self.port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server...")
        except Exception as e:
            print(f"An error occurred while running the server: {e}")
        finally:
            server.server_close()
            print("Server stopped.")

if __name__ == '__main__':
    # Configure SSL certificate and key file paths provided by Smart Validation
    CERT_FILE = 'path/to/cert.pem'  # Replace with your SSL certificate file path
    KEY_FILE = 'path/to/key.pem'    # Replace with your SSL key file path

    # Instantiate and start the server
    try:
        secure_server = SecureHTTPServer(host='0.0.0.0', port=443, cert_file=CERT_FILE, key_file=KEY_FILE)
        secure_server.start()
    except Exception as e:
        print(f"Failed to start the server: {e}")
```
