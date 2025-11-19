"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate a script to automate network configuration tasks using concepts from APTRON Gurgaon’s CCNA and CCNP training programs.
Generated: DETERMINISTIC_2ab6940ca828b439
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Network Configuration Automation Script

This script automates common network configuration tasks based on CCNA/CCNP concepts.
It uses Netmiko for device connections and supports Cisco IOS devices.

Features:
- Device connection management
- Basic interface configuration
- VLAN configuration
- OSPF configuration
- ACL configuration
"""

import argparse
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from getpass import getpass
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('network_config.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class NetworkAutomation:
    def __init__(self, device_params):
        """
        Initialize the network automation with device parameters.
        
        Args:
            device_params (dict): Dictionary containing device connection parameters
        """
        self.device_params = device_params
        self.connection = None

    def connect(self):
        """Establish connection to the network device."""
        try:
            self.connection = ConnectHandler(**self.device_params)
            logger.info(f"Successfully connected to {self.device_params['host']}")
            return True
        except NetmikoTimeoutException:
            logger.error(f"Connection timeout to {self.device_params['host']}")
            return False
        except NetmikoAuthenticationException:
            logger.error(f"Authentication failed for {self.device_params['host']}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error connecting to device: {str(e)}")
            return False

    def disconnect(self):
        """Close the connection to the network device."""
        if self.connection:
            self.connection.disconnect()
            logger.info(f"Disconnected from {self.device_params['host']}")

    def send_config_commands(self, commands):
        """
        Send configuration commands to the device.
        
        Args:
            commands (list): List of configuration commands to send
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.connection:
            logger.error("No active connection to device")
            return False

        try:
            output = self.connection.send_config_set(commands)
            logger.info(f"Configuration applied successfully:\n{output}")
            return True
        except Exception as e:
            logger.error(f"Error applying configuration: {str(e)}")
            return False

    def configure_interface(self, interface, ip_address, subnet_mask, description=None, shutdown=False):
        """
        Configure a network interface.
        
        Args:
            interface (str): Interface name (e.g., GigabitEthernet0/0)
            ip_address (str): IP address to assign
            subnet_mask (str): Subnet mask
            description (str, optional): Interface description
            shutdown (bool, optional): Whether to shutdown the interface
            
        Returns:
            bool: True if successful, False otherwise
        """
        commands = [
            f"interface {interface}",
            f"ip address {ip_address} {subnet_mask}"
        ]
        
        if description:
            commands.append(f"description {description}")
            
        if shutdown:
            commands.append("shutdown")
        else:
            commands.append("no shutdown")
            
        return self.send_config_commands(commands)

    def configure_vlan(self, vlan_id, name=None):
        """
        Configure a VLAN.
        
        Args:
            vlan_id (int): VLAN ID
            name (str, optional): VLAN name
            
        Returns:
            bool: True if successful, False otherwise
        """
        commands = [f"vlan {vlan_id}"]
        if name:
            commands.append(f"name {name}")
            
        return self.send_config_commands(commands)

    def configure_ospf(self, process_id, network, wildcard, area_id):
        """
        Configure OSPF routing.
        
        Args:
            process_id (int): OSPF process ID
            network (str): Network address
            wildcard (str): Wildcard mask
            area_id (int): OSPF area ID
            
        Returns:
            bool: True if successful, False otherwise
        """
        commands = [
            "router ospf {}".format(process_id),
            "network {} {} area {}".format(network, wildcard, area_id)
        ]
        return self.send_config_commands(commands)

    def configure_acl(self, acl_number, acl_type, rules):
        """
        Configure an ACL.
        
        Args:
            acl_number (int): ACL number
            acl_type (str): 'standard' or 'extended'
            rules (list): List of ACL rules
            
        Returns:
            bool: True if successful, False otherwise
        """
        if acl_type not in ['standard', 'extended']:
            logger.error("Invalid ACL type. Must be 'standard' or 'extended'")
            return False

        commands = [f"access-list {acl_number} {acl_type}"]
        commands.extend(rules)
        return self.send_config_commands(commands)

def get_device_params(host, username, password=None, device_type='cisco_ios'):
    """Get device connection parameters."""
    if not password:
        password = getpass(f"Enter password for {username}: ")
    
    return {
        'device_type': device_type,
        'host': host,
        'username': username,
        'password': password,
        'secret': password,  # Enable password
        'port': 22,
        'verbose': False
    }

def main():
    parser = argparse.ArgumentParser(description="Network Configuration Automation Tool")
    parser.add_argument('--host', required=True, help="Device IP address or hostname")
    parser.add_argument('--username', required=True, help="SSH username")
    parser.add_argument('--password', help="SSH password (will prompt if not provided)")
    
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Interface configuration subcommand
    interface_parser = subparsers.add_parser('interface', help='Configure interface')
    interface_parser.add_argument('--interface', required=True, help='Interface name')
    interface_parser.add_argument('--ip', required=True, help='IP address')
    interface_parser.add_argument('--mask', required=True, help='Subnet mask')
    interface_parser.add_argument('--description', help='Interface description')
    interface_parser.add_argument('--shutdown', action='store_true', help='Shutdown interface')
    
    # VLAN configuration subcommand
    vlan_parser = subparsers.add_parser('vlan', help='Configure VLAN')
    vlan_parser.add_argument('--vlan-id', type=int, required=True, help='VLAN ID')
    vlan_parser.add_argument('--name', help='VLAN name')
    
    # OSPF configuration subcommand
    ospf_parser = subparsers.add_parser('ospf', help='Configure OSPF')
    ospf_parser.add_argument('--process-id', type=int, required=True, help='OSPF process ID')
    ospf_parser.add_argument('--network', required=True, help='Network address')
    ospf_parser.add_argument('--wildcard', required=True, help='Wildcard mask')
    ospf_parser.add_argument('--area', type=int, required=True, help='OSPF area ID')
    
    # ACL configuration subcommand
    acl_parser = subparsers.add_parser('acl', help='Configure ACL')
    acl_parser.add_argument('--acl-number', type=int, required=True, help='ACL number')
    acl_parser.add_argument('--type', choices=['standard', 'extended'], required=True, help='ACL type')
    acl_parser.add_argument('--rules', nargs='+', required=True, help='ACL rules')
    
    args = parser.parse_args()
    
    try:
        device_params = get_device_params(args.host, args.username, args.password)
        net_auto = NetworkAutomation(device_params)
        
        if not net_auto.connect():
            sys.exit(1)
            
        success = False
        
        if args.command == 'interface':
            success = net_auto.configure_interface(
                args.interface, args.ip, args.mask, args.description, args.shutdown
            )
        elif args.command == 'vlan':
            success = net_auto.configure_vlan(args.vlan_id, args.name)
        elif args.command == 'ospf':
            success = net_auto.configure_ospf(
                args.process_id, args.network, args.wildcard, args.area
            )
        elif args.command == 'acl':
            success = net_auto.configure_acl(args.acl_number, args.type, args.rules)
            
        net_auto.disconnect()
        
        if not success:
            logger.error("Configuration failed")
            sys.exit(1)
            
        logger.info("Configuration completed successfully")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
