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
import subprocess
import logging
import os
from getpass import getpass

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """
    Executes a shell command and returns the output, error, and exit status.
    
    Parameters:
        command (str): The command to execute.

    Returns:
        tuple: (output, error, exit_status)
    """
    try:
        logging.info(f'Executing command: {command}')
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        logging.info(f'Command output: {result.stdout.strip()}')
        if result.stderr:
            logging.error(f'Command error: {result.stderr.strip()}')
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        logging.error(f'Failed to execute command "{command}": {str(e)}')
        return None, str(e), -1

def configure_interface(interface, ip_address, subnet_mask):
    """
    Configures a network interface with the specified IP address and subnet mask.

    Parameters:
        interface (str): The interface name (e.g., 'eth0', 'g0/1').
        ip_address (str): The IP address to assign.
        subnet_mask (str): The subnet mask.
    """
    command = f"ifconfig {interface} {ip_address} netmask {subnet_mask}"
    _, error, status = run_command(command)
    if status != 0:
        logging.error(f'Failed to configure interface {interface}: {error}')
    else:
        logging.info(f'Successfully configured {interface} with IP {ip_address}')

def configure_static_route(destination, subnet_mask, next_hop):
    """
    Configures a static route.

    Parameters:
        destination (str): The destination network.
        subnet_mask (str): The subnet mask for the destination.
        next_hop (str): The next hop IP address.
    """
    command = f"route add -net {destination} netmask {subnet_mask} gw {next_hop}"
    _, error, status = run_command(command)
    if status != 0:
        logging.error(f'Failed to configure static route to {destination}: {error}')
    else:
        logging.info(f'Successfully added static route to {destination} via {next_hop}')

def main():
    """
    Main function to execute the network configuration tasks.
    """
    # Gather necessary information for configuration
    try:
        interface = input("Enter the interface name (e.g., eth0, g0/1): ")
        ip_address = input("Enter the IP address to assign: ")
        subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")
        configure_interface(interface, ip_address, subnet_mask)

        destination = input("Enter the destination network for the static route (e.g., 192.168.2.0): ")
        dest_subnet_mask = input("Enter the subnet mask for the destination (e.g., 255.255.255.0): ")
        next_hop = input("Enter the next hop IP address: ")
        configure_static_route(destination, dest_subnet_mask, next_hop)

    except KeyboardInterrupt:
        logging.info("Configuration task cancelled by user.")
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()
```
