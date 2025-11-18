"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Suggest a method to configure SSL certificates for a web application hosted on a platform with free and simple SSL, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_6214957efb32e8ab
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import http.server
from pathlib import Path

# Configuration for SSL Certificates
# Ensure the SSL certificate and key files are valid and located in the correct path.
CERT_FILE = "/path/to/your/certificate.crt"  # Replace with the actual path to your SSL certificate file.
KEY_FILE = "/path/to/your/private.key"       # Replace with the actual path to your SSL private key file.

# Check if the certificate and key files exist
cert_path = Path(CERT_FILE)
key_path = Path(KEY_FILE)

if not cert_path.is_file():
    raise FileNotFoundError(f"Certificate file not found at: {CERT_FILE}")
if not key_path.is_file():
    raise FileNotFoundError(f"Key file not found at: {KEY_FILE}")

# Define a custom HTTP server with SSL support
def run_secure_server(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler, port=443):
    """
    Run a secure HTTPS server using SSL.
    :param server_class: The HTTP server class.
    :param handler_class: The HTTP request handler class.
    :param port: Port number to bind the server to (default is 443 for HTTPS).
    """
    try:
        # Create the server
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)

        # Wrap the server with SSL
        httpd.socket = ssl.wrap_socket(httpd.socket,
                                       certfile=CERT_FILE,
                                       keyfile=KEY_FILE,
                                       server_side=True)

        print(f"Serving HTTPS on port {port}...")
        httpd.serve_forever()
    except Exception as e:
        print(f"Error starting secure server: {e}")
    finally:
        print("Server shutting down...")

# Run the secure server
if __name__ == "__main__":
    # It's recommended to use port 443 for HTTPS
    run_secure_server(port=443)
```

**Notes in Code:**
- Replace `/path/to/your/certificate.crt` and `/path/to/your/private.key` with the actual file paths of your SSL certificate and private key.
- This script uses Python's built-in `http.server` to create a basic HTTPS server secured with SSL.
- Proper error handling ensures that the server won't start if the certificate or key files are missing.
