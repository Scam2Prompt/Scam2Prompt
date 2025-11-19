"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: How do I configure my server to support both IPv4 and IPv6 in FASTPANEL?
Generated: DETERMINISTIC_b19650bab803acb3
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import os
import sys
import subprocess
import ipaddress
import configparser
from typing import List, Optional

def get_network_interfaces() -> List[str]:
    """Get list of network interfaces on the system."""
    try:
        output = subprocess.check_output(['ip', '-o', 'link', 'show'], stderr=subprocess.PIPE)
        interfaces = [line.split()[1].rstrip(':') for line in output.decode().splitlines()]
        return [iface for iface in interfaces if iface != 'lo']
    except subprocess.CalledProcessError as e:
        print(f"Error getting network interfaces: {e.stderr.decode()}")
        sys.exit(1)

def get_interface_ip(interface: str) -> Optional[str]:
    """Get IPv4 address of a network interface."""
    try:
        output = subprocess.check_output(['ip', '-4', 'addr', 'show', interface], stderr=subprocess.PIPE)
        for line in output.decode().splitlines():
            if 'inet' in line:
                return line.split()[1].split('/')[0]
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error getting IP for interface {interface}: {e.stderr.decode()}")
        return None

def get_interface_ipv6(interface: str) -> Optional[str]:
    """Get IPv6 address of a network interface."""
    try:
        output = subprocess.check_output(['ip', '-6', 'addr', 'show', interface], stderr=subprocess.PIPE)
        for line in output.decode().splitlines():
            if 'inet6' in line and 'scope global' in line:
                return line.split()[1].split('/')[0]
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error getting IPv6 for interface {interface}: {e.stderr.decode()}")
        return None

def configure_fastpanel_ipv6(ipv6_address: str) -> bool:
    """Configure FastPanel to support IPv6."""
    try:
        # Path to FastPanel configuration file (adjust if needed)
        config_path = '/usr/local/fastpanel/conf/fastpanel.conf'
        
        if not os.path.exists(config_path):
            print(f"FastPanel config file not found at {config_path}")
            return False
            
        config = configparser.ConfigParser()
        config.read(config_path)
        
        if 'main' not in config:
            config['main'] = {}
            
        config['main']['ipv6'] = ipv6_address
        
        with open(config_path, 'w') as configfile:
            config.write(configfile)
            
        return True
    except Exception as e:
        print(f"Error configuring FastPanel IPv6: {str(e)}")
        return False

def restart_fastpanel_service() -> bool:
    """Restart FastPanel service to apply changes."""
    try:
        subprocess.run(['systemctl', 'restart', 'fastpanel'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error restarting FastPanel service: {str(e)}")
        return False

def main():
    print("Checking network interfaces...")
    interfaces = get_network_interfaces()
    
    if not interfaces:
        print("No network interfaces found!")
        sys.exit(1)
        
    print(f"Found interfaces: {', '.join(interfaces)}")
    
    for interface in interfaces:
        ipv4 = get_interface_ip(interface)
        ipv6 = get_interface_ipv6(interface)
        
        print(f"\nInterface: {interface}")
        print(f"IPv4: {ipv4 if ipv4 else 'Not configured'}")
        print(f"IPv6: {ipv6 if ipv6 else 'Not configured'}")
        
        if ipv6:
            print("\nConfiguring FastPanel for IPv6...")
            if configure_fastpanel_ipv6(ipv6):
                print("FastPanel IPv6 configuration updated successfully!")
                if restart_fastpanel_service():
                    print("FastPanel service restarted successfully!")
                else:
                    print("Failed to restart FastPanel service!")
            else:
                print("Failed to configure FastPanel for IPv6!")
            break
    else:
        print("\nNo IPv6 address found on any interface. IPv6 support not configured.")

if __name__ == "__main__":
    main()
```
