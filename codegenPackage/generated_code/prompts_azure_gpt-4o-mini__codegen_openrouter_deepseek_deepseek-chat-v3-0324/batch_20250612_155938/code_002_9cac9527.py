"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Create a configuration example for setting up a secure network infrastructure, including routers and firewalls, based on IMTS's network management services.
Generated: DETERMINISTIC_9cac9527c49e6c8b
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Secure Network Infrastructure Configuration Example for IMTS Network Management Services

This script provides a configuration template for setting up a secure network infrastructure
with routers and firewalls. It follows industry best practices for security and network management.
"""

import json
from typing import Dict, List, Optional

class NetworkDevice:
    """Base class for network devices (routers, firewalls)."""
    
    def __init__(self, hostname: str, ip_address: str, model: str):
        """
        Initialize a network device.
        
        Args:
            hostname: Device hostname
            ip_address: Management IP address
            model: Device model/type
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.model = model
        self.config = {}
    
    def generate_config(self) -> Dict:
        """Generate base configuration for the device."""
        self.config = {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "model": self.model,
            "interfaces": [],
            "security": {}
        }
        return self.config
    
    def validate_config(self) -> bool:
        """Validate the device configuration."""
        required_fields = ["hostname", "ip_address", "model"]
        return all(field in self.config for field in required_fields)

class Router(NetworkDevice):
    """Router device configuration."""
    
    def __init__(self, hostname: str, ip_address: str, model: str, routing_protocol: str = "OSPF"):
        super().__init__(hostname, ip_address, model)
        self.routing_protocol = routing_protocol
    
    def generate_config(self) -> Dict:
        """Generate router-specific configuration."""
        config = super().generate_config()
        config.update({
            "device_type": "router",
            "routing": {
                "protocol": self.routing_protocol,
                "areas": [],
                "networks": []
            },
            "access_control": {
                "acl": []
            }
        })
        return config
    
    def add_interface(self, name: str, ip: str, subnet: str, description: str = "") -> None:
        """Add an interface to the router configuration."""
        interface = {
            "name": name,
            "ip_address": ip,
            "subnet_mask": subnet,
            "description": description,
            "status": "up"
        }
        self.config["interfaces"].append(interface)
    
    def add_acl_rule(self, rule_name: str, action: str, src: str, dst: str, protocol: str, port: Optional[int] = None) -> None:
        """Add an Access Control List rule."""
        rule = {
            "name": rule_name,
            "action": action,
            "source": src,
            "destination": dst,
            "protocol": protocol
        }
        if port:
            rule["port"] = port
        self.config["access_control"]["acl"].append(rule)

class Firewall(NetworkDevice):
    """Firewall device configuration."""
    
    def __init__(self, hostname: str, ip_address: str, model: str, default_policy: str = "deny"):
        super().__init__(hostname, ip_address, model)
        self.default_policy = default_policy
    
    def generate_config(self) -> Dict:
        """Generate firewall-specific configuration."""
        config = super().generate_config()
        config.update({
            "device_type": "firewall",
            "security_policies": {
                "default": self.default_policy,
                "rules": []
            },
            "zones": {
                "internal": [],
                "external": [],
                "dmz": []
            }
        })
        return config
    
    def add_security_rule(self, name: str, src_zone: str, dst_zone: str, service: str, action: str) -> None:
        """Add a security rule to the firewall."""
        rule = {
            "name": name,
            "source_zone": src_zone,
            "destination_zone": dst_zone,
            "service": service,
            "action": action
        }
        self.config["security_policies"]["rules"].append(rule)
    
    def add_zone_interface(self, zone: str, interface: str) -> None:
        """Add an interface to a security zone."""
        if zone in self.config["zones"]:
            self.config["zones"][zone].append(interface)

def generate_network_config() -> Dict:
    """Generate a complete network configuration example for IMTS."""
    
    # Core router configuration
    core_router = Router("core-router1", "192.168.1.1", "Cisco ISR4431", "OSPF")
    core_router.generate_config()
    core_router.add_interface("GigabitEthernet0/0/0", "192.168.1.1", "255.255.255.0", "LAN Connection")
    core_router.add_interface("GigabitEthernet0/0/1", "203.0.113.1", "255.255.255.252", "WAN Uplink")
    core_router.add_acl_rule("ALLOW_HTTP", "permit", "any", "192.168.1.10", "tcp", 80)
    core_router.add_acl_rule("DENY_INVALID", "deny", "any", "any", "ip")
    
    # Firewall configuration
    edge_firewall = Firewall("edge-fw1", "192.168.1.2", "FortiGate 100F", "deny")
    edge_firewall.generate_config()
    edge_firewall.add_zone_interface("internal", "port1")
    edge_firewall.add_zone_interface("external", "port2")
    edge_firewall.add_security_rule("ALLOW_WEB", "external", "internal", "http", "accept")
    edge_firewall.add_security_rule("ALLOW_SSH", "internal", "external", "ssh", "accept")
    
    # Network configuration
    network_config = {
        "network_name": "IMTS_Corporate_Network",
        "devices": [
            core_router.config,
            edge_firewall.config
        ],
        "security_policies": {
            "password_policy": {
                "min_length": 12,
                "complexity": True,
                "expiry_days": 90
            },
            "logging": {
                "syslog_server": "192.168.1.100",
                "log_level": "debug"
            }
        }
    }
    
    return network_config

def save_config_to_file(config: Dict, filename: str) -> bool:
    """Save configuration to JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving configuration: {str(e)}")
        return False

if __name__ == "__main__":
    # Generate and save the configuration
    config = generate_network_config()
    if save_config_to_file(config, "imts_network_config.json"):
        print("Configuration successfully generated and saved.")
    else:
        print("Failed to save configuration.")
```
