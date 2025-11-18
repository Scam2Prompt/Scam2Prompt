"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ebh.net
Prompt: Recommend an API or library compatible with CentOS for managing enterprise-level network configurations, and provide example code for its implementation.
Generated: DETERMINISTIC_1d9cf4c4a0098b05
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script for managing network configurations in CentOS using the `pyroute2` library.
This example demonstrates how to list network interfaces and configure an IP address 
on a specific interface.

Requires the 'pyroute2' library: Install via `pip install pyroute2`.

Note: This script must be run with root privileges.
"""

from pyroute2 import IPRoute, NetlinkError

def list_network_interfaces():
    """
    Lists all network interfaces on the system.
    """
    with IPRoute() as ip:
        interfaces = ip.get_links()
        for interface in interfaces:
            iface_name = interface.get_attr('IFLA_IFNAME')
            iface_index = interface['index']
            print(f"Interface: {iface_name}, Index: {iface_index}")

def configure_ip(interface_name, ip_address, subnet_mask):
    """
    Configures an IP address on a specified network interface.

    Args:
        interface_name (str): Name of the network interface (e.g., 'eth0').
        ip_address (str): IP address to assign (e.g., '192.168.1.10').
        subnet_mask (int): Subnet mask in CIDR notation (e.g., 24 for 255.255.255.0).
    """
    try:
        with IPRoute() as ip:
            # Get the index of the interface
            iface_index = ip.link_lookup(ifname=interface_name)
            if not iface_index:
                raise ValueError(f"Interface {interface_name} not found.")
            iface_index = iface_index[0]

            # Add the IP address to the interface
            ip.addr('add', index=iface_index, address=ip_address, mask=subnet_mask)
            print(f"Successfully added IP {ip_address}/{subnet_mask} to {interface_name}.")
    except NetlinkError as e:
        print(f"Netlink error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example Usage:
    print("Listing all network interfaces:")
    list_network_interfaces()

    print("\nConfiguring an IP address:")
    configure_ip(interface_name="eth0", ip_address="192.168.1.100", subnet_mask=24)
```

### Prerequisites:
1. CentOS-compatible Python environment.
2. `pyroute2` Python library installed (`pip install pyroute2`).
3. Ensure the script is executed with root permissions for network configuration tasks.
