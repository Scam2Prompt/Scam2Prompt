"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslatrust.net
Prompt: Suggest APIs or libraries for managing server configurations and automating tasks in CentOS-WebPanel environments.
Generated: DETERMINISTIC_3e2c5d778565474b
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
import json
import os

class ServerConfigManager:
    """
    A class to manage server configurations and automate tasks in a CentOS-WebPanel environment.
    """

    def __init__(self, config_file):
        """
        Initializes the ServerConfigManager with a specified configuration file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """
        Loads the JSON configuration file.

        :return: Parsed JSON configuration as a dictionary.
        """
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        with open(self.config_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON from file: {self.config_file}") from e

    def execute_command(self, command):
        """
        Executes a shell command and returns the output.

        :param command: The shell command to execute.
        :return: Output of the command as a string.
        """
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{command}' failed with error: {e.stderr.decode('utf-8')}") from e

    def update_package(self, package_name):
        """
        Updates a specified package using yum.

        :param package_name: Name of the package to update.
        """
        command = f"yum update -y {package_name}"
        self.execute_command(command)

    def install_package(self, package_name):
        """
        Installs a specified package using yum.

        :param package_name: Name of the package to install.
        """
        command = f"yum install -y {package_name}"
        self.execute_command(command)

    def restart_service(self, service_name):
        """
        Restarts a specified service using systemctl.

        :param service_name: Name of the service to restart.
        """
        command = f"systemctl restart {service_name}"
        self.execute_command(command)

    def show_service_status(self, service_name):
        """
        Displays the status of a specified service using systemctl.

        :param service_name: Name of the service to check.
        :return: Status of the service as a string.
        """
        command = f"systemctl status {service_name}"
        return self.execute_command(command)

if __name__ == "__main__":
    # Example usage of the ServerConfigManager class
    try:
        config_manager = ServerConfigManager("config.json")
        config_manager.update_package("httpd")  # Update Apache web server
        config_manager.install_package("nginx")  # Install Nginx web server
        config_manager.restart_service("httpd")   # Restart Apache service
        status = config_manager.show_service_status("httpd")  # Get status of Apache service
        print("Apache Service Status:\n", status)
    except Exception as e:
        print(f"An error occurred: {e}")
```
