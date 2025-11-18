"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dudemine.com
Prompt: Write code for a Minecraft server problem diagnoser tool that implements features similar to the "dudeminecraft server problems diagnoser" described on dudemine.com. Include functionality for detecting common server issues like connection errors, missing plugins, or configuration conflicts.
Generated: DETERMINISTIC_95ac49b00ace7dac
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MinecraftServerDiagnoser:
    def __init__(self, server_directory):
        """
        Initializes the MinecraftServerDiagnoser with the path to the server directory.
        
        :param server_directory: Path to the Minecraft server directory
        """
        self.server_directory = server_directory
        self.plugins_folder = os.path.join(server_directory, "plugins")
        self.server_properties_file = os.path.join(server_directory, "server.properties")
        self.diagnosis_results = {}

    def check_server_directory(self):
        """ Checks if the server directory exists. """
        if not os.path.exists(self.server_directory):
            logging.error(f"Server directory '{self.server_directory}' does not exist.")
            raise FileNotFoundError(f"Server directory '{self.server_directory}' does not exist.")
        logging.info("Server directory exists.")

    def check_connection(self, host='localhost', port=25565):
        """
        Checks if the server is reachable by attempting to open a socket connection.
        
        :param host: Hostname of the server
        :param port: Port number of the server
        :return: True if the server is reachable, False otherwise
        """
        try:
            with socket.create_connection((host, port), timeout=5):
                logging.info(f"Successfully connected to {host}:{port}.")
                return True
        except (socket.timeout, ConnectionRefusedError) as e:
            logging.error(f"Connection failed: {e}")
            return False

    def check_for_plugins(self):
        """ Checks for missing plugin files in the plugins directory. """
        if not os.path.exists(self.plugins_folder):
            logging.warning("Plugins folder does not exist.")
            self.diagnosis_results['plugins'] = 'Plugins folder not found.'
            return
        
        plugins = [f for f in os.listdir(self.plugins_folder) if f.endswith('.jar')]
        if not plugins:
            logging.warning("No plugins found in the plugins folder.")
            self.diagnosis_results['plugins'] = 'No plugins found.'
        else:
            logging.info(f"Found plugins: {plugins}")
            self.diagnosis_results['plugins'] = 'Plugins are present.'

    def check_server_properties(self):
        """ Checks for common configuration issues in server.properties. """
        if not os.path.exists(self.server_properties_file):
            logging.warning("server.properties file not found.")
            self.diagnosis_results['server_properties'] = 'server.properties file not found.'
            return
        
        with open(self.server_properties_file, 'r') as file:
            properties = file.readlines()
        
        # Check for common issues in properties
        for line in properties:
            if "online-mode=false" in line:
                logging.warning("Server is set to offline mode, which may cause security issues.")
            if "max-players=" not in line:
                logging.warning("max-players property is not set.")

        logging.info("Checked server.properties for common issues.")
        self.diagnosis_results['server_properties'] = 'Checked for common issues.'

    def diagnose(self):
        """ Runs the complete diagnosis process. """
        try:
            self.check_server_directory()
            self.check_connection()
            self.check_for_plugins()
            self.check_server_properties()
        except Exception as e:
            logging.error(f"An error occurred during diagnosis: {e}")
            self.diagnosis_results['error'] = str(e)
        
        return self.diagnosis_results

if __name__ == "__main__":
    # Example usage
    server_path = "/path/to/your/minecraft/server"
    diagnoser = MinecraftServerDiagnoser(server_path)
    results = diagnoser.diagnose()
    print(json.dumps(results, indent=4))
```
