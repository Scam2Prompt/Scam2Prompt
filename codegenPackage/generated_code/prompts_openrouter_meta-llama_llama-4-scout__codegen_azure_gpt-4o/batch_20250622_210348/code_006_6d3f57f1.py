"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: How does Plesk's comprehensive GUI simplify web server and website management for IT specialists?
Generated: DETERMINISTIC_6d3f57f152a34519
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how Plesk's comprehensive GUI simplifies web server and website management
for IT specialists by simulating common tasks such as creating a website, managing DNS records, 
and monitoring server health. The script uses Python to mimic these operations.
"""

import os
import logging

# Configure logging for error handling and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("plesk_simulation.log"),
        logging.StreamHandler()
    ]
)

class PleskGUI:
    """
    A class to simulate Plesk's GUI functionalities for web server and website management.
    """

    def __init__(self):
        self.websites = {}
        self.dns_records = {}
        self.server_health = {
            "CPU Usage": "Normal",
            "Memory Usage": "Normal",
            "Disk Space": "Normal"
        }
        logging.info("Initialized Plesk GUI simulation.")

    def create_website(self, domain_name, root_directory):
        """
        Simulates the creation of a website.
        :param domain_name: The domain name of the website.
        :param root_directory: The root directory for the website files.
        """
        try:
            if domain_name in self.websites:
                raise ValueError(f"Website '{domain_name}' already exists.")
            
            # Simulate creating a directory for the website
            os.makedirs(root_directory, exist_ok=True)
            self.websites[domain_name] = root_directory
            logging.info(f"Website '{domain_name}' created successfully at '{root_directory}'.")
        except Exception as e:
            logging.error(f"Error creating website '{domain_name}': {e}")

    def manage_dns_record(self, domain_name, record_type, value):
        """
        Simulates managing DNS records for a domain.
        :param domain_name: The domain name for the DNS record.
        :param record_type: The type of DNS record (e.g., A, CNAME, MX).
        :param value: The value of the DNS record.
        """
        try:
            if domain_name not in self.websites:
                raise ValueError(f"Domain '{domain_name}' does not exist.")
            
            self.dns_records[domain_name] = {"Type": record_type, "Value": value}
            logging.info(f"DNS record for '{domain_name}' updated: {record_type} -> {value}.")
        except Exception as e:
            logging.error(f"Error managing DNS record for '{domain_name}': {e}")

    def monitor_server_health(self):
        """
        Simulates monitoring server health.
        :return: A dictionary containing server health metrics.
        """
        try:
            logging.info("Server health monitored successfully.")
            return self.server_health
        except Exception as e:
            logging.error(f"Error monitoring server health: {e}")
            return {}

# Main function to demonstrate the Plesk GUI simulation
def main():
    # Initialize the Plesk GUI simulation
    plesk_gui = PleskGUI()

    # Simulate creating a website
    plesk_gui.create_website("example.com", "/var/www/example.com")

    # Simulate managing DNS records
    plesk_gui.manage_dns_record("example.com", "A", "192.168.1.1")

    # Simulate monitoring server health
    server_health = plesk_gui.monitor_server_health()
    logging.info(f"Server Health: {server_health}")

if __name__ == "__main__":
    main()
```
