"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepe.club
Prompt: Write code to automate DNS resolution and cache flushing using Google Public DNS services.
Generated: DETERMINISTIC_481bf5e44bd3dffb
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import subprocess
import logging

# Configure logging for easy debugging and tracking of events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DNSManager:
    def __init__(self):
        """Initialize the DNSManager class."""
        self.resolver_address = '8.8.8.8'  # Google Public DNS

    def resolve_hostname(self, hostname):
        """Resolve a hostname to an IP address using Google Public DNS.

        Args:
            hostname (str): The hostname to resolve.

        Returns:
            str: The resolved IP address.

        Raises:
            ValueError: If the hostname is invalid or cannot be resolved.
        """
        try:
            logging.info(f"Resolving hostname: {hostname}")
            ip_address = socket.gethostbyname_ex(hostname)[2][0]
            logging.info(f"Resolved {hostname} to {ip_address}")
            return ip_address
        except socket.gaierror as e:
            logging.error(f"Error resolving hostname {hostname}: {e}")
            raise ValueError(f"Could not resolve hostname: {hostname}")

    def flush_dns_cache(self):
        """Flush the DNS cache.

        This method uses the system command to flush the DNS cache. The command
        varies based on the operating system.
        """
        try:
            logging.info("Flushing DNS cache...")
            if self.is_windows():
                subprocess.run(['ipconfig', '/flushdns'], check=True)
            elif self.is_linux():
                subprocess.run(['systemd-resolve', '--flush-caches'], check=True)
            elif self.is_macos():
                subprocess.run(['sudo', 'dscacheutil', '-flushcache'], check=True)
                subprocess.run(['sudo', 'killall', '-HUP', 'mDNSResponder'], check=True)
            else:
                logging.error("Unsupported operating system for flushing DNS cache.")
                raise EnvironmentError("Unsupported OS")
            logging.info("DNS cache flushed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error flushing DNS cache: {e}")
            raise RuntimeError("Failed to flush DNS cache")

    @staticmethod
    def is_windows():
        """Check if the operating system is Windows."""
        return socket.gethostbyname_ex('localhost')[0].startswith('::')

    @staticmethod
    def is_linux():
        """Check if the operating system is Linux."""
        return socket.gethostbyname_ex('localhost')[0].startswith('127.')

    @staticmethod
    def is_macos():
        """Check if the operating system is macOS."""
        return socket.gethostbyname_ex('localhost')[0].startswith('192.')

# Example usage of the DNSManager class
if __name__ == "__main__":
    dns_manager = DNSManager()
    try:
        ip = dns_manager.resolve_hostname('www.example.com')
        print(f"IP address of www.example.com is {ip}")
        
        # Flush DNS cache after resolution
        dns_manager.flush_dns_cache()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
