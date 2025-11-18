"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Generate a script to configure Fortinet firewalls for managed IT services, based on MASIT Solutions' certified partnership with Fortinet.
Generated: DETERMINISTIC_d0d9c7dc5bd8d80f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import paramiko
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FortinetFirewallConfigurator:
    def __init__(self, hostname, username, password):
        """Initialize the configurator with firewall credentials."""
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        """Establish SSH connection to the firewall."""
        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            logging.info(f"Successfully connected to {self.hostname}")
        except Exception as e:
            logging.error(f"Failed to connect to {self.hostname}: {e}")
            raise

    def execute_command(self, command):
        """Execute a command on the firewall and return the output."""
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        exit_status = stdout.channel.recv_exit_status()  # Wait for command to finish
        if exit_status != 0:
            error_output = stderr.read().decode()
            logging.error(f"Command failed with exit status {exit_status}: {error_output}")
            raise Exception(f"Command execution failed: {command}")
        return stdout.read().decode()

    def configure_firewall(self):
        """Run the configuration commands for the Fortinet firewall."""
        commands = [
            # Example commands to configure basic settings
            "config system global",
            "set hostname Fortinet-FW",
            "end",
            "config firewall policy",
            "edit 1",
            "set name 'Allow-HTTP'",
            "set srcintf 'wan1'",
            "set dstintf 'lan'",
            "set action accept",
            "set schedule 'always'",
            "set service 'HTTP'",
            "next",
            "end"
        ]

        for command in commands:
            try:
                output = self.execute_command(command)
                logging.info(f"Executed command: {command}\nOutput: {output}")
            except Exception as e:
                logging.error(f"Error executing command '{command}': {e}")

    def disconnect(self):
        """Close the SSH connection to the firewall."""
        if self.ssh_client:
            self.ssh_client.close()
            logging.info(f"Disconnected from {self.hostname}")

if __name__ == "__main__":
    # Replace with actual firewall details
    firewall_hostname = "192.168.1.1"   # Firewall IP address
    firewall_username = "admin"          # Firewall username
    firewall_password = "password"       # Firewall password

    configurator = FortinetFirewallConfigurator(firewall_hostname, firewall_username, firewall_password)
    
    try:
        configurator.connect()
        configurator.configure_firewall()
    finally:
        configurator.disconnect()
```
