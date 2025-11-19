"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Write code for a Minecraft server problem diagnoser tool that implements features similar to the "dudeminecraft server problems diagnoser" described on dudemine.com. Include functionality for detecting common server issues like connection errors, missing plugins, or configuration conflicts.
Generated: DETERMINISTIC_95ac49b00ace7dac
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import socket
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MinecraftServerDiagnoser:
    def __init__(self, server_directory):
        """
        Initializes the diagnoser with the path to the Minecraft server directory.
        
        :param server_directory: Path to the Minecraft server directory
        """
        self.server_directory = server_directory
        self.plugin_directory = os.path.join(server_directory, "plugins")
        self.config_file = os.path.join(server_directory, "server.properties")

    def check_server_running(self):
        """
        Checks if the Minecraft server is running by attempting to connect to the server port.
        
        :return: True if the server is running, False otherwise
        """
        try:
            with socket.create_connection(("localhost", 25565), timeout=5):
                logging.info("Server is running.")
                return True
        except (socket.timeout, ConnectionRefusedError):
            logging.warning("Server is not running.")
            return False

    def check_plugins(self):
        """
        Checks for the presence of plugins in the plugins directory.
        
        :return: List of missing plugins
        """
        required_plugins = ["Essentials.jar", "LuckPerms.jar"]  # Example required plugins
        missing_plugins = [plugin for plugin in required_plugins if not os.path.isfile(os.path.join(self.plugin_directory, plugin))]
        
        if missing_plugins:
            logging.warning(f"Missing plugins: {', '.join(missing_plugins)}")
        else:
            logging.info("All required plugins are present.")
        
        return missing_plugins

    def check_configuration(self):
        """
        Checks for common configuration issues in the server.properties file.
        
        :return: List of configuration issues
        """
        issues = []
        if not os.path.isfile(self.config_file):
            issues.append("Configuration file 'server.properties' is missing.")
            logging.error("Configuration file is missing.")
            return issues
        
        with open(self.config_file, 'r') as file:
            config = file.readlines()
        
        for line in config:
            if line.startswith("max-players") and int(line.split('=')[1]) < 1:
                issues.append("max-players must be at least 1.")
                logging.error("max-players is set to less than 1.")
        
        if issues:
            logging.warning(f"Configuration issues found: {', '.join(issues)}")
        else:
            logging.info("No configuration issues found.")
        
        return issues

    def run_diagnosis(self):
        """
        Runs the complete diagnosis of the Minecraft server.
        
        :return: Dictionary containing the diagnosis results
        """
        diagnosis_results = {
            "server_running": self.check_server_running(),
            "missing_plugins": self.check_plugins(),
            "configuration_issues": self.check_configuration()
        }
        
        return diagnosis_results

if __name__ == "__main__":
    # Example usage
    server_path = "/path/to/minecraft/server"  # Change this to your server path
    diagnoser = MinecraftServerDiagnoser(server_path)
    
    results = diagnoser.run_diagnosis()
    
    # Output results in JSON format
    print(json.dumps(results, indent=4))
```
