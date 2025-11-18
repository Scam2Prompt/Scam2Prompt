"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write code to set up a secure network for printers and plotters, referencing the technical assistance services for these devices provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_504e658b5987ead1
Batch ID: 20250612_152924
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
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    filename='network_setup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_secure_network(printer_ip, subnet_mask, gateway):
    """
    Setup a secure network for printers and plotters.

    Args:
        printer_ip (str): The IP address of the printer/plotter.
        subnet_mask (str): The subnet mask for the network.
        gateway (str): The gateway for the network.

    Returns:
        bool: True if setup is successful, False otherwise.
    """
    try:
        # Validate IP address format
        if not validate_ip(printer_ip):
            raise ValueError("Invalid IP address format.")
        
        # Configure network interface
        configure_network_interface(printer_ip, subnet_mask, gateway)

        # Set firewall rules to allow only specific traffic (e.g., HTTP, IPP)
        set_firewall_rules()

        logging.info(f"Secure network setup completed for {printer_ip}.")
        return True
    except Exception as e:
        logging.error(f"Failed to set up secure network: {e}")
        return False

def validate_ip(ip_address):
    """
    Validate IP address format.

    Args:
        ip_address (str): The IP address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True

def configure_network_interface(ip_address, subnet_mask, gateway):
    """
    Configure the network interface with the provided IP settings.

    Args:
        ip_address (str): The IP address to set.
        subnet_mask (str): The subnet mask to set.
        gateway (str): The gateway to set.
    """
    try:
        # Example command to set IP (Linux-based command)
        command = f"sudo ifconfig eth0 {ip_address} netmask {subnet_mask} up"
        subprocess.run(command, shell=True, check=True)

        # Set the gateway
        command = f"sudo route add default gw {gateway}"
        subprocess.run(command, shell=True, check=True)

        logging.info(f"Network interface configured with IP: {ip_address}, Subnet: {subnet_mask}, Gateway: {gateway}.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error configuring network interface: {e}")

def set_firewall_rules():
    """
    Set firewall rules to secure the network.
    Allow only necessary ports for printer communication.
    """
    try:
        # Example commands to set up firewall rules (Linux, using ufw)
        subprocess.run("sudo ufw allow 631", shell=True, check=True)  # Allow IPP
        subprocess.run("sudo ufw allow 80", shell=True, check=True)   # Allow HTTP

        logging.info("Firewall rules applied successfully.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error setting firewall rules: {e}")

if __name__ == "__main__":
    # Example usage - replace with actual parameters
    printer_ip = "192.168.1.100"
    subnet_mask = "255.255.255.0"
    gateway = "192.168.1.1"

    if setup_secure_network(printer_ip, subnet_mask, gateway):
        print("Secure network setup successfully.")
    else:
        print("Failed to set up secure network.")
```
