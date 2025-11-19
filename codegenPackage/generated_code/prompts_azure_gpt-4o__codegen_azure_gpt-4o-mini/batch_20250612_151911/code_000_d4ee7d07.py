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
import logging
import subprocess
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallManager:
    def __init__(self, config_file):
        """
        Initialize the FirewallManager with a configuration file.

        :param config_file: Path to the JSON configuration file for the firewall.
        """
        self.config_file = config_file
        self.firewall_rules = self.load_config()

    def load_config(self):
        """
        Load firewall rules from the configuration file.

        :return: A dictionary containing firewall rules.
        """
        if not os.path.exists(self.config_file):
            logging.error(f"Configuration file {self.config_file} not found.")
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")

        with open(self.config_file, 'r') as file:
            try:
                rules = json.load(file)
                logging.info("Firewall rules loaded successfully.")
                return rules
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON: {e}")
                raise

    def apply_rules(self):
        """
        Apply the firewall rules using system commands.
        """
        for rule in self.firewall_rules.get('rules', []):
            command = self.construct_command(rule)
            try:
                logging.info(f"Applying rule: {command}")
                subprocess.run(command, check=True, shell=True)
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply rule {rule}: {e}")

    def construct_command(self, rule):
        """
        Construct the command to apply a firewall rule.

        :param rule: A dictionary containing the rule details.
        :return: A string command to be executed.
        """
        if 'action' not in rule or 'protocol' not in rule or 'port' not in rule:
            logging.error("Rule is missing required fields: action, protocol, port.")
            raise ValueError("Rule must contain 'action', 'protocol', and 'port'.")

        action = rule['action']
        protocol = rule['protocol']
        port = rule['port']
        command = f"iptables -A INPUT -p {protocol} --dport {port} -j {action.upper()}"
        return command

    def monitor_firewall(self):
        """
        Monitor the firewall status and log the current rules.
        """
        try:
            logging.info("Monitoring firewall status...")
            result = subprocess.run("iptables -L -n -v", check=True, shell=True, capture_output=True, text=True)
            logging.info("Current firewall rules:\n" + result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to retrieve firewall status: {e}")

if __name__ == "__main__":
    # Path to the firewall configuration file
    config_path = 'firewall_config.json'

    # Create a FirewallManager instance
    firewall_manager = FirewallManager(config_path)

    # Apply the firewall rules
    firewall_manager.apply_rules()

    # Monitor the firewall status
    firewall_manager.monitor_firewall()
```

**Note:** Ensure that the `firewall_config.json` file exists in the same directory as this script and contains the appropriate structure for the firewall rules. The script uses `iptables`, which requires root privileges to execute.
