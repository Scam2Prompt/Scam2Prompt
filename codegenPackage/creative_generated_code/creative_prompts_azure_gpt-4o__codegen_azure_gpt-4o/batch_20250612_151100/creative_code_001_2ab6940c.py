"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Generate a script to automate network configuration tasks using concepts from APTRON Gurgaon’s CCNA and CCNP training programs.
Generated: DETERMINISTIC_2ab6940ca828b439
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess

def run_command(command):
    """
    Executes a shell command and returns the output or error message.

    Args:
        command (str): The shell command to execute.

    Returns:
        str: Output of the command or error message.
    """
    try:
        result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Exception: {str(e)}"

def configure_interface(interface, ip_address, subnet_mask):
    """
    Configures an interface with an IP address and subnet mask.

    Args:
        interface (str): Name of the network interface (e.g., 'eth0').
        ip_address (str): IP address to assign (e.g., '192.168.1.10').
        subnet_mask (str): Subnet mask to assign (e.g., '255.255.255.0').

    Returns:
        str: Status of the operation.
    """
    try:
        # Bring the interface up
        up_command = f"sudo ip link set {interface} up"
        up_result = run_command(up_command)
        if "Error" in up_result:
            return f"Failed to bring up interface {interface}: {up_result}"

        # Assign IP address and subnet mask
        ip_command = f"sudo ip addr add {ip_address}/{subnet_mask} dev {interface}"
        ip_result = run_command(ip_command)
        if "Error" in ip_result:
            return f"Failed to assign IP address to {interface}: {ip_result}"

        return f"Successfully configured {interface} with IP {ip_address}/{subnet_mask}"
    except Exception as e:
        return f"Exception: {str(e)}"

def configure_static_route(destination, gateway):
    """
    Configures a static route.

    Args:
        destination (str): Destination network (e.g., '192.168.1.0/24').
        gateway (str): Gateway IP address (e.g., '192.168.1.1').

    Returns:
        str: Status of the operation.
    """
    try:
        route_command = f"sudo ip route add {destination} via {gateway}"
        route_result = run_command(route_command)
        if "Error" in route_result:
            return f"Failed to add static route: {route_result}"

        return f"Successfully added static route to {destination} via {gateway}"
    except Exception as e:
        return f"Exception: {str(e)}"

def main():
    """
    Main function to automate network configuration tasks.
    """
    print("Automating network configuration tasks...")
    
    # Example network configuration
    interface = "eth0"
    ip_address = "192.168.1.10"
    subnet_mask = "24"  # CIDR notation
    destination = "192.168.1.0/24"
    gateway = "192.168.1.1"

    # Configure network interface
    interface_result = configure_interface(interface, ip_address, subnet_mask)
    print(interface_result)

    # Configure static route
    route_result = configure_static_route(destination, gateway)
    print(route_result)

if __name__ == "__main__":
    main()
```
