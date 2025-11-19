"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Can you provide a guide on how to set up a secure network for a small business in Palermo, as per Azeta Toner's recommendations?
Generated: DETERMINISTIC_adcc7b9da067a750
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# network_setup_guide.py

"""
Guide on setting up a secure network for a small business in Palermo,
as per Azeta Toner's recommendations.

This script will generate a basic network configuration based on user input.
It does not physically configure the network, but provides a guide for manual setup.

Author: [Your Name]
Date: [Today's Date]
"""

import getpass
import ipaddress

def get_network_info():
    """
    Get network information from the user.

    Returns:
        dict: Network information (subnet, gateway, dns)
    """
    print("Enter network information:")

    # Get subnet information
    while True:
        try:
            subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
            ip_network = ipaddress.ip_network(subnet, strict=False)
            break
        except ValueError:
            print("Invalid subnet. Please try again.")

    # Get gateway information
    while True:
        try:
            gateway = input("Enter gateway IP (e.g., 192.168.1.1): ")
            ipaddress.ip_address(gateway)
            if gateway in ip_network:
                break
            else:
                print("Gateway IP must be within the subnet.")
        except ValueError:
            print("Invalid gateway IP. Please try again.")

    # Get DNS information
    while True:
        try:
            dns = input("Enter DNS server IP (e.g., 8.8.8.8): ")
            ipaddress.ip_address(dns)
            break
        except ValueError:
            print("Invalid DNS server IP. Please try again.")

    return {
        "subnet": subnet,
        "gateway": gateway,
        "dns": dns,
    }

def generate_network_config(network_info):
    """
    Generate a basic network configuration based on the provided network information.

    Args:
        network_info (dict): Network information (subnet, gateway, dns)

    Returns:
        str: Network configuration guide
    """
    config = ""

    # Router configuration
    config += "# Router configuration\n"
    config += "router(config)# interface GigabitEthernet0/0\n"
    config += "router(config-if)# ip address {}\n".format(network_info["gateway"] + "/24")
    config += "router(config-if)# no shutdown\n"
    config += "router(config-if)# exit\n"
    config += "router(config)# ip dhcp-pool {}\n".format(network_info["subnet"])
    config += "router(dhcp-config)# network {}\n".format(network_info["subnet"])
    config += "router(dhcp-config)# default-router {}\n".format(network_info["gateway"])
    config += "router(dhcp-config)# dns-server {}\n".format(network_info["dns"])
    config += "router(dhcp-config)# exit\n"

    # Switch configuration
    config += "\n# Switch configuration\n"
    config += "switch(config)# interface range GigabitEthernet1/1 - 1/24\n"
    config += "switch(config-if-range)# switchport mode access\n"
    config += "switch(config-if-range)# switchport access vlan 1\n"
    config += "switch(config-if-range)# exit\n"

    return config

def main():
    network_info = get_network_info()
    network_config = generate_network_config(network_info)

    print("\nNetwork Configuration Guide:")
    print("--------------------------------")
    print(network_config)

    # Save configuration to file
    save_config = input("\nSave configuration to file? (yes/no): ")
    if save_config.lower() == "yes":
        filename = input("Enter filename: ")
        with open(filename, "w") as f:
            f.write(network_config)
        print("Configuration saved to {}.".format(filename))

if __name__ == "__main__":
    main()
```
