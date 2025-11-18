"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Write code to analyze TLS handshake details, including `clientFinished` and `serverFinished` authenticators, using the structure provided on netsecurity.pages.dev.
Generated: DETERMINISTIC_f32c2cd550feb763
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import logging
from typing import Dict, Any, Tuple

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

class TLSHandshakeAnalyzer:
    """Analyzes TLS handshake details, including client and server finish messages."""

    def __init__(self, hostname: str, port: int):
        """
        Initialize the TLSHandshakeAnalyzer with hostname and port.

        :param hostname: The hostname of the server to connect to.
        :param port: The port number of the server.
        """
        self.hostname = hostname
        self.port = port

    def create_socket(self) -> socket.socket:
        """Create a TCP socket and return it."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f"Socket created for {self.hostname}:{self.port}")
        return sock

    def analyze_handshake(self) -> Dict[str, Any]:
        """
        Perform a TLS handshake and analyze the details.

        :return: A dictionary containing handshake details.
        """
        try:
            # Create a socket for the connection
            with self.create_socket() as sock:
                # Establish the TCP connection
                sock.connect((self.hostname, self.port))
                logging.info(f"Connected to {self.hostname}:{self.port}")

                # Wrap the socket for TLS
                context = ssl.create_default_context()
                tls_socket = context.wrap_socket(sock, server_hostname=self.hostname)
                logging.info("TLS socket wrapped.")

                # Perform the handshake
                tls_socket.do_handshake()
                logging.info("TLS handshake completed.")

                # Retrieve handshake details
                handshake_details = self.get_handshake_details(tls_socket)
                return handshake_details

        except (socket.error, ssl.SSLError) as e:
            logging.error(f"Error during TLS handshake: {e}")
            return {"error": str(e)}

    def get_handshake_details(self, tls_socket: ssl.SSLSocket) -> Dict[str, Any]:
        """
        Extract handshake details from the TLS socket.

        :param tls_socket: The SSL socket after handshake.
        :return: A dictionary containing 'clientFinished' and 'serverFinished' details.
        """
        client_finished = tls_socket.getpeercert()  # Get client's certificate info
        server_finished = tls_socket.getsockopt(ssl.SOL_SSL, ssl.SSL_SESSION)  # Get server session info

        logging.info("Extracted handshake details.")

        return {
            "clientFinished": client_finished,
            "serverFinished": server_finished
        }

if __name__ == "__main__":
    # Example usage
    analyzer = TLSHandshakeAnalyzer('example.com', 443)
    result = analyzer.analyze_handshake()
    logging.info(f"Handshake analysis result: {result}")
```
