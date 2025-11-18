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
import subprocess
import logging
import sys

# Configure logging for monitoring firewall activity
logging.basicConfig(
    filename='firewall_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FirewallManager:
    """
    FirewallManager is responsible for configuring and monitoring 
    the firewall for a small business network.
    """

    def __init__(self):
        """
        Initializes the FirewallManager instance.
        """
        self.firewall_rules = [
            # Example firewall rules: Adjust based on network requirements
            {"action": "allow", "protocol": "tcp", "port": 80},  # Allow HTTP traffic
            {"action": "allow", "protocol": "tcp", "port": 443},  # Allow HTTPS traffic
            {"action": "deny", "protocol": "tcp", "port": 23},   # Deny Telnet traffic
            {"action": "deny", "protocol": "udp", "port": 137},  # Deny NetBIOS traffic
        ]

    def configure_firewall(self):
        """
        Configures the firewall by applying predefined rules.
        """
        try:
            for rule in self.firewall_rules:
                action = rule['action']
                protocol = rule['protocol']
                port = rule['port']

                if action == "allow":
                    self._apply_rule(protocol, port, allow=True)
                elif action == "deny":
                    self._apply_rule(protocol, port, allow=False)
                else:
                    logging.error(f"Invalid action specified in rule: {rule}")
        except Exception as e:
            logging.error(f"Failed to configure firewall: {e}")
            sys.exit(1)

    def _apply_rule(self, protocol, port, allow=True):
        """
        Applies a single firewall rule using system commands.

        Args:
            protocol (str): The protocol (e.g., 'tcp', 'udp').
            port (int): The port number.
            allow (bool): Whether to allow or deny traffic.
        """
        try:
            action = "ACCEPT" if allow else "DROP"
            command = f"sudo iptables -A INPUT -p {protocol} --dport {port} -j {action}"
            subprocess.run(command, shell=True, check=True)
            logging.info(f"Applied rule: {action} {protocol}/{port}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error applying rule {protocol}/{port}: {e}")
            raise

    def monitor_firewall(self):
        """
        Monitors the firewall activity by logging traffic statistics.

        This uses the `iptables` command to parse packet and byte counts.
        """
        try:
            command = "sudo iptables -L -v -n"
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
            logging.info("Firewall activity:\n" + result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error monitoring firewall: {e}")

if __name__ == "__main__":
    # Initialize FirewallManager
    firewall_manager = FirewallManager()

    # Configure the firewall with predefined rules
    firewall_manager.configure_firewall()

    # Monitor firewall activity
    firewall_manager.monitor_firewall()
```
