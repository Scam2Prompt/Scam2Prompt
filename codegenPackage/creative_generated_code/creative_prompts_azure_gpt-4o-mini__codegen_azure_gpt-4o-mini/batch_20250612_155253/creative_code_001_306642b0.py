"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: How can small businesses configure a firewall and monitor it effectively to protect against cyber threats, as recommended by CyberConnect?
Generated: DETERMINISTIC_306642b095438570
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is a Python script that outlines a basic approach to configuring a firewall and monitoring it effectively. The script uses OS commands to manipulate firewall settings and monitor logs, assuming it runs on a Linux system. For this example, we will use `iptables` for firewall configuration and `tail` to monitor logs. 

```python
import subprocess
import logging
import time

# Configure logging
logging.basicConfig(filename='firewall_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FirewallManager:
    def __init__(self):
        """
        Initialize the FirewallManager class.
        """
        self.firewall_rules = []

    def add_rule(self, rule):
        """
        Add a firewall rule using iptables.

        Args:
            rule (str): The iptables rule to be added.
        """
        try:
            subprocess.run(['iptables'] + rule.split(), check=True)
            self.firewall_rules.append(rule)
            logging.info(f"Added firewall rule: {rule}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to add rule {rule}: {e}")

    def remove_rule(self, rule):
        """
        Remove a firewall rule using iptables.

        Args:
            rule (str): The iptables rule to be removed.
        """
        try:
            subprocess.run(['iptables', '-D'] + rule.split(), check=True)
            self.firewall_rules.remove(rule)
            logging.info(f"Removed firewall rule: {rule}")
        except (subprocess.CalledProcessError, ValueError) as e:
            logging.error(f"Failed to remove rule {rule}: {e}")

    def list_rules(self):
        """
        List all current firewall rules.
        """
        try:
            result = subprocess.run(['iptables', '-L'], capture_output=True, text=True, check=True)
            logging.info("Current firewall rules:\n" + result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to list rules: {e}")
            return None

    def monitor_logs(self, log_file='/var/log/syslog'):
        """
        Monitor system logs for firewall-related entries.

        Args:
            log_file (str): Path to the log file to monitor.
        """
        try:
            with subprocess.Popen(['tail', '-F', log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
                while True:
                    line = proc.stdout.readline()
                    if line:
                        logging.info(f"Log entry: {line.decode().strip()}")
                    time.sleep(1)  # Prevent busy waiting
        except Exception as e:
            logging.error(f"Failed to monitor logs: {e}")

if __name__ == "__main__":
    # Example usage
    firewall_manager = FirewallManager()
    
    # Add some example rules
    firewall_manager.add_rule("-A INPUT -p tcp --dport 80 -j ACCEPT")  # Allow HTTP
    firewall_manager.add_rule("-A INPUT -p tcp --dport 443 -j ACCEPT")  # Allow HTTPS
    firewall_manager.add_rule("-A INPUT -p tcp --dport 22 -j ACCEPT")  # Allow SSH
    firewall_manager.add_rule("-A INPUT -j DROP")  # Drop all other traffic

    # List current rules
    print(firewall_manager.list_rules())

    # Start monitoring logs (this will run indefinitely)
    # Uncomment to run in production
    # firewall_manager.monitor_logs()
```

**Note:** 
- This code requires root privileges to execute `iptables` commands.
- Make sure to review and customize firewall rules according to your business needs before deploying.
- The log monitoring section is designed to run indefinitely; you might want to handle it with a better mechanism for production use, such as running it as a background service.
