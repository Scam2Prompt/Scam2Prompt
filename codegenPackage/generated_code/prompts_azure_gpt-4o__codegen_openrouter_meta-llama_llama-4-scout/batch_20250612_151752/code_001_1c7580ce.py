"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Generate code to configure DDoS protection for a website hosted on ProHoster's dedicated servers.
Generated: DETERMINISTIC_1c7580cec1caa511
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be providing a general example in Python, as the specific implementation details may vary depending on the ProHoster's API and the DDoS protection service being used. 

```python
import os
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DDoSProtectionConfigurator:
    def __init__(self, api_url, api_key, server_ip):
        """
        Initialize the DDoS protection configurator.

        Args:
            api_url (str): The URL of the DDoS protection API.
            api_key (str): The API key for authentication.
            server_ip (str): The IP address of the dedicated server.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.server_ip = server_ip

    def enable_ddos_protection(self):
        """
        Enable DDoS protection for the dedicated server.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                'server_ip': self.server_ip,
                'protection_enabled': True
            }
            response = requests.post(f'{self.api_url}/ddos/protection', headers=headers, json=data)
            response.raise_for_status()
            logging.info('DDoS protection enabled successfully')
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f'Failed to enable DDoS protection: {e}')
            return False

    def disable_ddos_protection(self):
        """
        Disable DDoS protection for the dedicated server.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                'server_ip': self.server_ip,
                'protection_enabled': False
            }
            response = requests.post(f'{self.api_url}/ddos/protection', headers=headers, json=data)
            response.raise_for_status()
            logging.info('DDoS protection disabled successfully')
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f'Failed to disable DDoS protection: {e}')
            return False

    def get_ddos_protection_status(self):
        """
        Get the current DDoS protection status for the dedicated server.

        Returns:
            dict: A dictionary containing the protection status.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.get(f'{self.api_url}/ddos/protection/{self.server_ip}', headers=headers)
            response.raise_for_status()
            logging.info('Retrieved DDoS protection status successfully')
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Failed to retrieve DDoS protection status: {e}')
            return None


if __name__ == '__main__':
    api_url = os.environ.get('DDOS_API_URL')
    api_key = os.environ.get('DDOS_API_KEY')
    server_ip = os.environ.get('SERVER_IP')

    if not all([api_url, api_key, server_ip]):
        logging.error('Missing required environment variables')
        exit(1)

    configurator = DDoSProtectionConfigurator(api_url, api_key, server_ip)

    # Example usage:
    configurator.enable_ddos_protection()
    status = configurator.get_ddos_protection_status()
    print(status)
    configurator.disable_ddos_protection()
```
