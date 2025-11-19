"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: How can I use Plesk to manage my web server and applications effectively?
Generated: DETERMINISTIC_4d18f4e5513bc3b0
Batch ID: 20250612_155936
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
    A class to manage Plesk server operations.
    """

    def __init__(self, host, username, password):
        """
        Initializes the PleskManager with server credentials.

        :param host: The hostname or IP address of the Plesk server
        :param username: The username for Plesk authentication
        :param password: The password for Plesk authentication
        """
        self.host = host
        self.username = username
        self.password = password

    def execute_command(self, command):
        """
        Executes a shell command on the Plesk server.

        :param command: The command to run
        :return: The output of the command
        :raises Exception: If the command fails
        """
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            logging.info(f"Command executed successfully: {command}")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed: {command}\nError: {e.stderr}")
            raise Exception(f"Command execution failed: {e.stderr}")

    def list_domains(self):
        """
        Lists all domains on the Plesk server.

        :return: A list of domains
        """
        command = f"plesk bin domain --list"
        return self.execute_command(command).strip().split('\n')

    def add_domain(self, domain_name):
        """
        Adds a new domain to the Plesk server.

        :param domain_name: The name of the domain to add
        :raises Exception: If the domain cannot be added
        """
        command = f"plesk bin domain -a {domain_name}"
        self.execute_command(command)
        logging.info(f"Domain added successfully: {domain_name}")

    def remove_domain(self, domain_name):
        """
        Removes an existing domain from the Plesk server.

        :param domain_name: The name of the domain to remove
        :raises Exception: If the domain cannot be removed
        """
        command = f"plesk bin domain -r {domain_name}"
        self.execute_command(command)
        logging.info(f"Domain removed successfully: {domain_name}")

    def restart_service(self, service_name):
        """
        Restarts a specified service on the Plesk server.

        :param service_name: The name of the service to restart
        :raises Exception: If the service cannot be restarted
        """
        command = f"service {service_name} restart"
        self.execute_command(command)
        logging.info(f"Service restarted successfully: {service_name}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of PleskManager
    plesk_manager = PleskManager(host='your-plesk-server.com', username='admin', password='your-password')

    try:
        # List domains
        domains = plesk_manager.list_domains()
        logging.info(f"Current domains: {domains}")

        # Add a new domain
        plesk_manager.add_domain('example.com')

        # Remove an existing domain
        plesk_manager.remove_domain('old-domain.com')

        # Restart a service
        plesk_manager.restart_service('apache2')

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
