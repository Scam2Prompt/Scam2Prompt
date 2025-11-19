"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Write a script to set up a multi-location VPN using ProHoster's 50+ server locations for enhanced privacy.
Generated: DETERMINISTIC_6981365d68ae2521
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys
import json

class VPNSetupError(Exception):
    """Custom exception for VPN setup errors."""
    pass

class MultiLocationVPN:
    def __init__(self, config_file):
        """
        Initialize the MultiLocationVPN class.

        :param config_file: Path to the configuration file containing server locations.
        """
        self.config_file = config_file
        self.servers = self.load_servers()

    def load_servers(self):
        """
        Load server locations from the configuration file.

        :return: List of server locations.
        :raises VPNSetupError: If the configuration file cannot be read or is invalid.
        """
        try:
            with open(self.config_file, 'r') as file:
                servers = json.load(file)
                if not isinstance(servers, list):
                    raise VPNSetupError("Invalid configuration format. Expected a list of servers.")
                return servers
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise VPNSetupError(f"Error loading configuration: {e}")

    def connect_to_server(self, server):
        """
        Connect to a specified VPN server.

        :param server: The server address to connect to.
        :raises VPNSetupError: If the connection command fails.
        """
        try:
            # Example command to connect to a VPN server using OpenVPN
            command = f"openvpn --config {server}.ovpn"
            subprocess.run(command, shell=True, check=True)
            print(f"Successfully connected to {server}.")
        except subprocess.CalledProcessError as e:
            raise VPNSetupError(f"Failed to connect to {server}: {e}")

    def setup_vpn(self):
        """
        Set up the VPN by connecting to all specified servers.
        """
        for server in self.servers:
            try:
                self.connect_to_server(server)
            except VPNSetupError as e:
                print(e)

if __name__ == "__main__":
    # Path to the configuration file containing server locations
    config_path = "servers.json"

    # Check if the configuration file exists
    if not os.path.exists(config_path):
        print(f"Configuration file '{config_path}' not found.")
        sys.exit(1)

    # Initialize and run the VPN setup
    vpn_setup = MultiLocationVPN(config_path)
    vpn_setup.setup_vpn()
```

**Note:** Ensure that the `servers.json` file exists in the same directory as this script and contains a valid JSON array of server names (without the `.ovpn` extension). For example:
```json
["server1", "server2", "server3"]
```
