"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write Python code to configure and monitor a firewall for a small business, as described in CyberConnect's "Small Business" cybersecurity services.
Generated: DETERMINISTIC_d4ee7d0789a03902
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import subprocess
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Firewall configuration class
class Firewall:
    def __init__(self, config_file):
        """
        Initializes the Firewall class.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.rules = self.load_configuration()

    def load_configuration(self):
        """
        Load firewall rules from the configuration file.

        :return: List of firewall rules.
        """
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                logging.info("Loaded firewall configuration successfully.")
                return config.get('rules', [])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load configuration: {e}")
            return []

    def apply_rules(self):
        """
        Apply the firewall rules to the system.
        """
        for rule in self.rules:
            try:
                command = self.build_command(rule)
                subprocess.run(command, check=True)
                logging.info(f"Applied rule: {rule}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to apply rule {rule}: {e}")

    def build_command(self, rule):
        """
        Build the command to apply a single firewall rule.

        :param rule: A dictionary representing a firewall rule.
        :return: Command as a list.
        """
        # Example rule structure: {'action': 'allow', 'protocol': 'tcp', 'port': 80}
        action = 'iptables'
        if rule['action'] == 'allow':
            action += ' -A INPUT -p {protocol} --dport {port} -j ACCEPT'.format(**rule)
        elif rule['action'] == 'deny':
            action += ' -A INPUT -p {protocol} --dport {port} -j DROP'.format(**rule)
        else:
            logging.warning(f"Unknown action {rule['action']} for rule: {rule}")
            return []
        return action.split()

    def monitor(self):
        """
        Monitor the firewall rules and log their status.
        """
        try:
            output = subprocess.check_output(['iptables', '-L'], text=True)
            logging.info("Current Firewall Rules:\n" + output)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to retrieve firewall rules: {e}")

def main():
    """
    Main function to configure and monitor the firewall.
    """
    # Path to the firewall configuration JSON file
    config_file = 'firewall_config.json'
    
    # Check if the configuration file exists
    if not os.path.exists(config_file):
        logging.error(f"Configuration file {config_file} does not exist.")
        return

    # Initialize and apply firewall rules
    firewall = Firewall(config_file)
    firewall.apply_rules()
    
    # Monitor firewall status
    firewall.monitor()

if __name__ == '__main__':
    main()
```

**Note:** Ensure that the `firewall_config.json` file is structured properly before running the script. Example structure:

```json
{
    "rules": [
        {"action": "allow", "protocol": "tcp", "port": 80},
        {"action": "deny", "protocol": "tcp", "port": 23}
    ]
}
```
