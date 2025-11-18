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

# Configure logging
logging.basicConfig(
    filename="network_security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NetworkSecurityManager:
    """
    A class to configure and monitor firewalls and VPNs for a secure business network.
    """

    def __init__(self, firewall_config_file, vpn_config_file):
        """
        Initializes the NetworkSecurityManager with configuration files.

        :param firewall_config_file: Path to the firewall configuration JSON file.
        :param vpn_config_file: Path to the VPN configuration JSON file.
        """
        self.firewall_config_file = firewall_config_file
        self.vpn_config_file = vpn_config_file

    def load_configuration(self, config_file):
        """
        Loads configuration from a JSON file.

        :param config_file: Path to the configuration JSON file.
        :return: Parsed configuration as a dictionary.
        """
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {config_file}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Failed to decode JSON from file: {config_file}")
            raise

    def configure_firewall(self):
        """
        Configures the firewall based on the provided configuration file.
        """
        firewall_config = self.load_configuration(self.firewall_config_file)
        logging.info("Starting firewall configuration...")

        for rule in firewall_config.get("rules", []):
            try:
                # Example of applying a firewall rule using a hypothetical command
                command = f"sudo iptables {rule.get('action')} {rule.get('protocol')} -p {rule.get('port')}"
                subprocess.run(command, shell=True, check=True)
                logging.info(f"Applied firewall rule: {rule}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply firewall rule: {rule} - Error: {str(e)}")

    def configure_vpn(self):
        """
        Configures the VPN based on the provided configuration file.
        """
        vpn_config = self.load_configuration(self.vpn_config_file)
        logging.info("Starting VPN configuration...")

        try:
            # Example of configuring a VPN using a hypothetical command
            command = f"sudo openvpn --config {vpn_config.get('config_path')}"
            subprocess.run(command, shell=True, check=True)
            logging.info("VPN configuration applied successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure VPN - Error: {str(e)}")

    def monitor_firewall(self):
        """
        Monitors the firewall status.
        """
        logging.info("Monitoring firewall status...")
        try:
            # Example of checking firewall status using a hypothetical command
            result = subprocess.run("sudo iptables -L", shell=True, check=True, capture_output=True)
            logging.info("Firewall status:\n" + result.stdout.decode())
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to monitor firewall status - Error: {str(e)}")

    def monitor_vpn(self):
        """
        Monitors the VPN status.
        """
        logging.info("Monitoring VPN status...")
        try:
            # Example of checking VPN status using a hypothetical command
            result = subprocess.run("sudo systemctl status openvpn", shell=True, check=True, capture_output=True)
            logging.info("VPN status:\n" + result.stdout.decode())
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to monitor VPN status - Error: {str(e)}")


if __name__ == "__main__":
    # File paths for configuration
    FIREWALL_CONFIG_FILE = "firewall_config.json"
    VPN_CONFIG_FILE = "vpn_config.json"

    # Initialize the NetworkSecurityManager
    manager = NetworkSecurityManager(FIREWALL_CONFIG_FILE, VPN_CONFIG_FILE)

    # Configure and monitor firewall and VPN
    try:
        manager.configure_firewall()
        manager.configure_vpn()
        manager.monitor_firewall()
        manager.monitor_vpn()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {str(e)}")
```

### Notes for Production:
- Ensure `firewall_config.json` and `vpn_config.json` are correctly formatted and accessible.
- This code assumes `iptables` and `openvpn` are installed on the system.
- The logging setup sends logs to `network_security.log` for debugging and monitoring purposes.
