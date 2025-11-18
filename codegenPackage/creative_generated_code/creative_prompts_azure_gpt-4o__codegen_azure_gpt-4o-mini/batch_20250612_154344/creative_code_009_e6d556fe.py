"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write code to configure and monitor firewalls and VPNs for a secure business network, based on IMTS's network management services.
Generated: DETERMINISTIC_e6d556fedf9a9a80
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import logging
import json
from typing import List, Dict

# Configure logging for monitoring purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkDevice:
    def __init__(self, ip_address: str, device_type: str):
        self.ip_address = ip_address
        self.device_type = device_type

    def configure_firewall(self, rules: List[Dict[str, str]]) -> bool:
        """
        Configures the firewall with the specified rules.

        :param rules: List of dictionaries containing firewall rules.
        :return: True if configuration is successful, False otherwise.
        """
        try:
            logging.info(f"Configuring firewall on {self.device_type} [{self.ip_address}] with rules: {rules}")
            # Simulating firewall configuration via a command
            command = f"ssh admin@{self.ip_address} 'apply-firewall-rules {json.dumps(rules)}'"
            subprocess.run(command, shell=True, check=True)
            logging.info("Firewall configured successfully.")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure firewall: {e}")
            return False

    def configure_vpn(self, config: Dict[str, str]) -> bool:
        """
        Configures the VPN with the provided configuration.

        :param config: Dictionary containing VPN configuration settings.
        :return: True if configuration is successful, False otherwise.
        """
        try:
            logging.info(f"Configuring VPN on {self.device_type} [{self.ip_address}] with config: {config}")
            # Simulating VPN configuration via a command
            command = f"ssh admin@{self.ip_address} 'setup-vpn {json.dumps(config)}'"
            subprocess.run(command, shell=True, check=True)
            logging.info("VPN configured successfully.")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure VPN: {e}")
            return False

    def monitor_device(self) -> Dict[str, str]:
        """
        Monitors the device and returns its status.

        :return: Dictionary containing device status information.
        """
        try:
            logging.info(f"Monitoring device [{self.device_type}] at {self.ip_address}")
            # Simulating device monitoring via a command
            command = f"ssh admin@{self.ip_address} 'get-device-status'"
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            status_info = json.loads(result.stdout)
            logging.info(f"Device status: {status_info}")
            return status_info
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            logging.error(f"Failed to monitor device: {e}")
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    firewall_device = NetworkDevice(ip_address='192.168.1.1', device_type='Firewall')
    
    # Configure firewall rules
    firewall_rules = [
        {"action": "allow", "source": "192.168.1.100", "destination": "any", "port": "80"},
        {"action": "deny", "source": "any", "destination": "192.168.1.200", "port": "22"}
    ]
    firewall_device.configure_firewall(rules=firewall_rules)

    # Configure VPN
    vpn_config = {
        "server": "vpn.example.com",
        "username": "user",
        "password": "securepassword"
    }
    firewall_device.configure_vpn(config=vpn_config)

    # Monitor device status
    status = firewall_device.monitor_device()
    logging.info(f"Final Status: {status}")
```

**Note:** This code assumes that SSH access to the network devices is configured and that the respective commands `apply-firewall-rules` and `setup-vpn` are available on those devices. Ensure to replace the placeholders with actual commands as per your network's architecture and requirements.
