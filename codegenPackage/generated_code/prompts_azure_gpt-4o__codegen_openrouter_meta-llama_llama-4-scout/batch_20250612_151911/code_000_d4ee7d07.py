"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Write Python code to configure and monitor a firewall for a small business, as described in CyberConnect's "Small Business" cybersecurity services.
Generated: DETERMINISTIC_d4ee7d0789a03902
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import subprocess
import logging
from logging.handlers import RotatingFileHandler

# Set up logging configuration
logger = logging.getLogger('firewall_monitor')
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('firewall.log', maxBytes=1024*1024*10, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class FirewallConfigurator:
    def __init__(self, interface):
        self.interface = interface

    def allow_outbound(self, protocol, port):
        """Allow outbound traffic on a specific protocol and port."""
        try:
            if protocol == 'tcp':
                subprocess.run(['ufw', 'allow', 'out', f'tcp/{port}'], check=True)
            elif protocol == 'udp':
                subprocess.run(['ufw', 'allow', 'out', f'udp/{port}'], check=True)
            else:
                logger.error(f"Unsupported protocol: {protocol}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to allow outbound traffic: {e}")

    def block_inbound(self, protocol, port):
        """Block inbound traffic on a specific protocol and port."""
        try:
            if protocol == 'tcp':
                subprocess.run(['ufw', 'deny', 'in', f'tcp/{port}'], check=True)
            elif protocol == 'udp':
                subprocess.run(['ufw', 'deny', 'in', f'udp/{port}'], check=True)
            else:
                logger.error(f"Unsupported protocol: {protocol}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to block inbound traffic: {e}")

    def enable_firewall(self):
        """Enable the firewall."""
        try:
            subprocess.run(['ufw', 'enable'], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to enable firewall: {e}")

    def status(self):
        """Get the current firewall status."""
        try:
            output = subprocess.check_output(['ufw', 'status']).decode('utf-8')
            logger.info(output)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get firewall status: {e}")

def main():
    # Initialize the firewall configurator
    configurator = FirewallConfigurator('eth0')

    # Enable the firewall
    configurator.enable_firewall()

    # Allow outbound HTTP traffic
    configurator.allow_outbound('tcp', 80)

    # Allow outbound HTTPS traffic
    configurator.allow_outbound('tcp', 443)

    # Block inbound SSH traffic
    configurator.block_inbound('tcp', 22)

    # Get the current firewall status
    configurator.status()

if __name__ == '__main__':
    main()
```
