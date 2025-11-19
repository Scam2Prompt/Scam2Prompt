"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: "Design a network infrastructure for a multi-location retail business, including a PBX phone system and security camera system, using Retail Tech Solutions' expertise."
Generated: DETERMINISTIC_feef02bab61e58b3
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# network_infrastructure.py

import ipaddress

class NetworkInfrastructure:
    def __init__(self, locations):
        """
        Initialize the network infrastructure for multiple locations.

        Args:
            locations (list): List of dictionaries containing location information.
        """
        self.locations = locations
        self.network_config = {}

    def design_network(self):
        """
        Design the network infrastructure for each location.

        Returns:
            dict: Network configuration for all locations.
        """
        for location in self.locations:
            location_name = location['name']
            ip_subnet = ipaddress.ip_network(location['ip_subnet'], strict=False)

            # Initialize location network config
            self.network_config[location_name] = {
                'ip_subnet': str(ip_subnet),
                'gateways': [],
                'devices': []
            }

            # Configure PBX phone system
            pbx_config = self.configure_pbx(location_name, ip_subnet)
            self.network_config[location_name]['devices'].append(pbx_config)

            # Configure security camera system
            camera_config = self.configure_security_cameras(location_name, ip_subnet)
            self.network_config[location_name]['devices'].append(camera_config)

            # Configure gateways
            gateway_config = self.configure_gateways(location_name, ip_subnet)
            self.network_config[location_name]['gateways'].append(gateway_config)

        return self.network_config

    def configure_pbx(self, location_name, ip_subnet):
        """
        Configure the PBX phone system for a location.

        Args:
            location_name (str): Name of the location.
            ip_subnet (ipaddress.IPv4Network): IP subnet for the location.

        Returns:
            dict: PBX configuration.
        """
        # Assign IP address to PBX system
        pbx_ip = str(ip_subnet[10])  # Using .10 as the PBX IP

        return {
            'type': 'PBX',
            'location': location_name,
            'ip_address': pbx_ip,
            'phone_numbers': ['+1-123-456-7890']  # Example phone number
        }

    def configure_security_cameras(self, location_name, ip_subnet):
        """
        Configure the security camera system for a location.

        Args:
            location_name (str): Name of the location.
            ip_subnet (ipaddress.IPv4Network): IP subnet for the location.

        Returns:
            dict: Security camera configuration.
        """
        # Assign IP addresses to security cameras
        camera_ips = [str(ip_subnet[i]) for i in range(20, 25)]  # Using .20-.24 for cameras

        return {
            'type': 'Security Camera',
            'location': location_name,
            'ip_addresses': camera_ips,
            'resolution': '1080p'
        }

    def configure_gateways(self, location_name, ip_subnet):
        """
        Configure the gateways for a location.

        Args:
            location_name (str): Name of the location.
            ip_subnet (ipaddress.IPv4Network): IP subnet for the location.

        Returns:
            dict: Gateway configuration.
        """
        # Assign IP address to gateway
        gateway_ip = str(ip_subnet[1])  # Using .1 as the gateway IP

        return {
            'type': 'Gateway',
            'location': location_name,
            'ip_address': gateway_ip,
            'subnet_mask': str(ip_subnet.netmask)
        }

def main():
    locations = [
        {
            'name': 'New York',
            'ip_subnet': '10.10.1.0/24'
        },
        {
            'name': 'Los Angeles',
            'ip_subnet': '10.10.2.0/24'
        }
    ]

    network_infrastructure = NetworkInfrastructure(locations)
    network_config = network_infrastructure.design_network()

    print(network_config)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
