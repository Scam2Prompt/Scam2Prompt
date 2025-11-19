"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a tutorial on configuring Cisco networking protocols, referencing the CompTIA Networking and Security Technologies section on edukacija.net.
Generated: DETERMINISTIC_a503687d64f45aac
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cisco Networking Protocols Configuration Tutorial
Reference: CompTIA Networking and Security Technologies - edukacija.net

This script provides a tutorial on configuring common Cisco networking protocols.
It includes examples for VLAN, OSPF, EIGRP, and ACL configurations.
"""

import re

class CiscoConfigTutorial:
    """
    A class to demonstrate Cisco networking protocol configurations.
    """
    
    def __init__(self):
        """Initialize with common configuration templates."""
        self.config_templates = {
            'vlan': self._vlan_config,
            'ospf': self._ospf_config,
            'eigrp': self._eigrp_config,
            'acl': self._acl_config
        }
    
    def _validate_ip(self, ip_address):
        """Validate an IPv4 address."""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(pattern, ip_address):
            raise ValueError(f"Invalid IP address: {ip_address}")
        return True
    
    def _vlan_config(self, vlan_id, name, interface=None):
        """
        Generate VLAN configuration.
        
        Args:
            vlan_id (int): VLAN ID (1-4094)
            name (str): VLAN name
            interface (str, optional): Interface to assign VLAN to
            
        Returns:
            str: VLAN configuration commands
        """
        if not 1 <= vlan_id <= 4094:
            raise ValueError("VLAN ID must be between 1 and 4094")
            
        config = [
            f"vlan {vlan_id}",
            f" name {name}",
            "exit"
        ]
        
        if interface:
            config.extend([
                f"interface {interface}",
                " switchport mode access",
                f" switchport access vlan {vlan_id}",
                "exit"
            ])
            
        return "\n".join(config)
    
    def _ospf_config(self, process_id, router_id, networks):
        """
        Generate OSPF configuration.
        
        Args:
            process_id (int): OSPF process ID
            router_id (str): Router ID in IPv4 format
            networks (list): List of tuples (network, wildcard, area)
            
        Returns:
            str: OSPF configuration commands
        """
        self._validate_ip(router_id)
        
        config = [
            f"router ospf {process_id}",
            f" router-id {router_id}"
        ]
        
        for network, wildcard, area in networks:
            self._validate_ip(network)
            config.append(f" network {network} {wildcard} area {area}")
            
        config.append("exit")
        return "\n".join(config)
    
    def _eigrp_config(self, as_number, router_id, networks):
        """
        Generate EIGRP configuration.
        
        Args:
            as_number (int): Autonomous System number
            router_id (str): Router ID in IPv4 format
            networks (list): List of network addresses
            
        Returns:
            str: EIGRP configuration commands
        """
        self._validate_ip(router_id)
        
        config = [
            f"router eigrp {as_number}",
            f" eigrp router-id {router_id}",
            " no auto-summary"
        ]
        
        for network in networks:
            self._validate_ip(network)
            config.append(f" network {network}")
            
        config.append("exit")
        return "\n".join(config)
    
    def _acl_config(self, acl_number, entries):
        """
        Generate standard ACL configuration.
        
        Args:
            acl_number (int): ACL number (1-99 for standard)
            entries (list): List of tuples (action, source, wildcard)
            
        Returns:
            str: ACL configuration commands
        """
        if not 1 <= acl_number <= 99:
            raise ValueError("Standard ACL number must be between 1 and 99")
            
        config = [f"access-list {acl_number}"]
        
        for action, source, wildcard in entries:
            self._validate_ip(source)
            config.append(f" {action} {source} {wildcard}")
            
        config.append("exit")
        return "\n".join(config)
    
    def generate_config(self, protocol, **kwargs):
        """
        Generate configuration for specified protocol.
        
        Args:
            protocol (str): Protocol to configure (vlan, ospf, eigrp, acl)
            **kwargs: Protocol-specific parameters
            
        Returns:
            str: Generated configuration
        """
        if protocol not in self.config_templates:
            raise ValueError(f"Unsupported protocol: {protocol}")
            
        return self.config_templates[protocol](**kwargs)

# Example usage
if __name__ == "__main__":
    tutorial = CiscoConfigTutorial()
    
    try:
        # VLAN Configuration Example
        print("=== VLAN Configuration ===")
        print(tutorial.generate_config(
            'vlan',
            vlan_id=10,
            name='MANAGEMENT',
            interface='GigabitEthernet0/1'
        ))
        
        # OSPF Configuration Example
        print("\n=== OSPF Configuration ===")
        print(tutorial.generate_config(
            'ospf',
            process_id=1,
            router_id='192.168.1.1',
            networks=[
                ('192.168.1.0', '0.0.0.255', '0'),
                ('10.0.0.0', '0.255.255.255', '0')
            ]
        ))
        
        # EIGRP Configuration Example
        print("\n=== EIGRP Configuration ===")
        print(tutorial.generate_config(
            'eigrp',
            as_number=100,
            router_id='192.168.1.1',
            networks=['192.168.1.0', '10.0.0.0']
        ))
        
        # ACL Configuration Example
        print("\n=== ACL Configuration ===")
        print(tutorial.generate_config(
            'acl',
            acl_number=10,
            entries=[
                ('permit', '192.168.1.0', '0.0.0.255'),
                ('deny', 'any', 'any')
            ]
        ))
        
    except ValueError as e:
        print(f"Configuration error: {e}")
```
