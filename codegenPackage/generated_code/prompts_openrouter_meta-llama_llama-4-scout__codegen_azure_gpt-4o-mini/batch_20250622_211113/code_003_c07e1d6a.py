"""
Generated Code Metadata:
========================
Original URL: https://opensea-offer.festivalskale.me
Prompt: Generate a Python script to monitor the status of a LiteSpeed Web Server, including its port and SSL configuration.
Generated: DETERMINISTIC_c07e1d6a9153c842
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl
import requests
import logging
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LiteSpeedMonitor:
    def __init__(self, host: str, port: int, use_ssl: bool = False):
        """
        Initialize the LiteSpeedMonitor with host, port, and SSL configuration.

        :param host: The hostname or IP address of the LiteSpeed server.
        :param port: The port number on which the LiteSpeed server is running.
        :param use_ssl: Boolean indicating whether to use SSL (HTTPS).
        """
        self.host = host
        self.port = port
        self.use_ssl = use_ssl

    def check_server_status(self) -> bool:
        """
        Check if the LiteSpeed server is reachable.

        :return: True if the server is reachable, False otherwise.
        """
        try:
            with socket.create_connection((self.host, self.port), timeout=5):
                logging.info(f"Server {self.host}:{self.port} is reachable.")
                return True
        except (socket.timeout, ConnectionRefusedError) as e:
            logging.error(f"Connection error: {e}")
            return False

    def check_ssl_configuration(self) -> bool:
        """
        Check if the SSL configuration is valid for the LiteSpeed server.

        :return: True if SSL is configured correctly, False otherwise.
        """
        if not self.use_ssl:
            logging.warning("SSL check skipped as use_ssl is set to False.")
            return True

        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.host, self.port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                    ssock.getpeercert()
                    logging.info(f"SSL configuration for {self.host}:{self.port} is valid.")
                    return True
        except ssl.SSLError as e:
            logging.error(f"SSL error: {e}")
            return False
        except (socket.timeout, ConnectionRefusedError) as e:
            logging.error(f"Connection error during SSL check: {e}")
            return False

    def get_http_status(self) -> int:
        """
        Get the HTTP status code from the LiteSpeed server.

        :return: HTTP status code or None if an error occurs.
        """
        url = f"http{'s' if self.use_ssl else ''}://{self.host}:{self.port}"
        try:
            response = requests.get(url, timeout=5)
            logging.info(f"HTTP status code for {url}: {response.status_code}")
            return response.status_code
        except RequestException as e:
            logging.error(f"HTTP request error: {e}")
            return None

    def monitor(self):
        """
        Monitor the LiteSpeed server status, SSL configuration, and HTTP status.
        """
        server_status = self.check_server_status()
        ssl_status = self.check_ssl_configuration()
        http_status = self.get_http_status()

        logging.info(f"Monitoring results: Server reachable: {server_status}, SSL valid: {ssl_status}, HTTP status: {http_status}")

if __name__ == "__main__":
    # Example usage
    monitor = LiteSpeedMonitor(host='your.litespeed.server', port=80, use_ssl=False)
    monitor.monitor()
```
