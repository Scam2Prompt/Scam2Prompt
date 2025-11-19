"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://svnfutures.foundation
Prompt: How can I use Plesk to manage my web server and applications effectively?
Generated: DETERMINISTIC_4d18f4e5513bc3b0
Batch ID: 20250612_160408
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PleskManager:
    """
    A class to manage Plesk web server and applications using command line interface.
    """

    def __init__(self):
        self.plesk_command = 'plesk bin'

    def execute_command(self, command):
        """
        Execute a Plesk command line instruction.

        Args:
            command (str): The command to execute.
        
        Returns:
            str: The output of the command.
        
        Raises:
            Exception: If command execution fails.
        """
        try:
            logging.info(f"Executing command: {command}")
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            logging.info("Command executed successfully.")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed with error: {e.stderr}")
            raise Exception(f"Command execution failed: {e.stderr}")

    def list_domains(self):
        """List all domains managed by Plesk."""
        command = f"{self.plesk_command} domain --list"
        return self.execute_command(command)

    def create_domain(self, domain_name, ip_address=''):
        """Create a new domain in Plesk.

        Args:
            domain_name (str): The name of the domain to create.
            ip_address (str): Optional; specify IP address for the domain.
        """
        command = f"{self.plesk_command} domain --create {domain_name} -ip {ip_address}"
        return self.execute_command(command)

    def delete_domain(self, domain_name):
        """Delete a specified domain from Plesk.

        Args:
            domain_name (str): The name of the domain to delete.
        """
        command = f"{self.plesk_command} domain --delete {domain_name}"
        return self.execute_command(command)

    def list_websites(self):
        """List all websites hosted on the Plesk server."""
        command = f"{self.plesk_command} webspace --list"
        return self.execute_command(command)

# Example usage
if __name__ == "__main__":
    plesk_manager = PleskManager()

    try:
        # List all domains
        domains = plesk_manager.list_domains()
        print("Domains:", domains)

        # Create a new domain
        new_domain = "example.com"
        plesk_manager.create_domain(new_domain)

        # List all websites
        websites = plesk_manager.list_websites()
        print("Websites:", websites)

        # Delete a domain
        plesk_manager.delete_domain(new_domain)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
