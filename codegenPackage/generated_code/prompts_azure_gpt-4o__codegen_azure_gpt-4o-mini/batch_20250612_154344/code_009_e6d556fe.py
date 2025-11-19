"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Write code to configure and monitor firewalls and VPNs for a secure business network, based on IMTS's network management services.
Generated: DETERMINISTIC_e6d556fedf9a9a80
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import subprocess
import json
from typing import Dict, Any

# Configure logging for monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkManager:
    def __init__(self, config_file: str):
        """
        Initialize the NetworkManager with a configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """
        Load the network configuration from a JSON file.

        :return: Configuration dictionary.
        """
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                logging.info("Configuration loaded successfully.")
                return config
        except FileNotFoundError:
            logging.error("Configuration file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def configure_firewall(self):
        """
        Configure the firewall based on the loaded configuration.
        """
        firewall_rules = self.config.get('firewall_rules', [])
        for rule in firewall_rules:
            try:
                command = f"iptables {rule}"
                subprocess.run(command, shell=True, check=True)
                logging.info(f"Firewall rule applied: {rule}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply firewall rule '{rule}': {e}")

    def configure_vpn(self):
        """
        Configure the VPN based on the loaded configuration.
        """
        vpn_config = self.config.get('vpn', {})
        try:
            command = f"openvpn --config {vpn_config.get('config_file')}"
            subprocess.run(command, shell=True, check=True)
            logging.info("VPN configured successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure VPN: {e}")

    def monitor_network(self):
        """
        Monitor the network status and log relevant information.
        """
        try:
            command = "netstat -tuln"
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            logging.info("Network status:\n" + result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to monitor network: {e}")

if __name__ == "__main__":
    try:
        # Initialize the NetworkManager with the path to the configuration file
        network_manager = NetworkManager('network_config.json')
        
        # Configure firewall and VPN
        network_manager.configure_firewall()
        network_manager.configure_vpn()
        
        # Monitor network status
        network_manager.monitor_network()
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```

**Note**: Ensure that the `network_config.json` file exists and is properly formatted according to the expected structure for firewall rules and VPN configuration.
