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
import socket
import json

class MinecraftServerDiagnoser:
    """
    A tool to diagnose common Minecraft server issues such as connection errors,
    missing plugins, or configuration conflicts. Designed to handle errors gracefully
    and provide actionable feedback to users.
    """

    def __init__(self, server_address, port, server_directory):
        """
        Initializes the server diagnoser with the server's address, port, and directory.
        
        :param server_address: IP or hostname of the Minecraft server
        :param port: Port number of the Minecraft server
        :param server_directory: Path to the server files directory
        """
        self.server_address = server_address
        self.port = port
        self.server_directory = server_directory

    def check_connection(self):
        """
        Checks if the Minecraft server is reachable via the given IP and port.
        
        :return: Tuple (status: bool, message: str)
        """
        try:
            # Attempt to create a socket connection
            with socket.create_connection((self.server_address, self.port), timeout=5):
                return True, "Server is reachable."
        except socket.timeout:
            return False, "Connection timed out. Check your firewall or server status."
        except socket.error as e:
            return False, f"Connection failed: {str(e)}"

    def check_plugins(self):
        """
        Checks for missing plugins in the server directory.
        Assumes a `plugins.json` file exists in the server directory to define required plugins.
        
        :return: Tuple (status: bool, message: str)
        """
        try:
            plugins_path = os.path.join(self.server_directory, "plugins.json")
            if not os.path.exists(plugins_path):
                return False, "plugins.json file not found in server directory."
            
            # Load required plugins from plugins.json
            with open(plugins_path, "r") as f:
                required_plugins = json.load(f).get("required_plugins", [])
            
            # Check for missing plugins in the 'plugins' folder
            installed_plugins_dir = os.path.join(self.server_directory, "plugins")
            installed_plugins = os.listdir(installed_plugins_dir) if os.path.exists(installed_plugins_dir) else []

            missing_plugins = [plugin for plugin in required_plugins if plugin not in installed_plugins]
            if missing_plugins:
                return False, f"Missing plugins detected: {', '.join(missing_plugins)}"
            
            return True, "All required plugins are installed."
        except (json.JSONDecodeError, FileNotFoundError) as e:
            return False, f"Error reading or parsing plugins.json: {str(e)}"
        except Exception as e:
            return False, f"An error occurred while checking plugins: {str(e)}"

    def check_configuration(self):
        """
        Checks for configuration conflicts in the server files.
        Assumes a `server.properties` file exists and checks basic entries.
        
        :return: Tuple (status: bool, message: str)
        """
        try:
            config_path = os.path.join(self.server_directory, "server.properties")
            if not os.path.exists(config_path):
                return False, "server.properties file not found in server directory."
            
            # Read configuration file
            with open(config_path, "r") as f:
                lines = f.readlines()
            
            # Check for common configuration errors
            config_dict = {}
            for line in lines:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    config_dict[key] = value
            
            if config_dict.get("online-mode", "true").lower() not in ["true", "false"]:
                return False, "Invalid value for 'online-mode' in server.properties."

            if not config_dict.get("server-port", "").isdigit():
                return False, "'server-port' must be a valid number in server.properties."
            
            return True, "Configuration looks good."
        except Exception as e:
            return False, f"An error occurred while checking configuration: {str(e)}"

    def diagnose(self):
        """
        Runs all diagnostic checks and prints a summary report.
        """
        print("Starting diagnosis...\n")
        
        # Check connection
        connection_status, connection_message = self.check_connection()
        print(f"Connection Test: {'PASS' if connection_status else 'FAIL'} - {connection_message}\n")
        
        # Check plugins
        plugins_status, plugins_message = self.check_plugins()
        print(f"Plugins Test: {'PASS' if plugins_status else 'FAIL'} - {plugins_message}\n")
        
        # Check configuration
        config_status, config_message = self.check_configuration()
        print(f"Configuration Test: {'PASS' if config_status else 'FAIL'} - {config_message}\n")
        
        print("Diagnosis completed.")


# Example usage:
if __name__ == "__main__":
    # Replace with your server's IP, port, and directory path
    server_ip = "127.0.0.1"
    server_port = 25565
    server_directory = "/path/to/minecraft/server"

    diagnoser = MinecraftServerDiagnoser(server_ip, server_port, server_directory)
    diagnoser.diagnose()
```
