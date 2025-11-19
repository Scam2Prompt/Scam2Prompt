"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Develop a network architecture for a small enterprise in Douala, Cameroon, including firewall configuration and secure data storage solutions."
Generated: DETERMINISTIC_cb4e20525d1d98aa
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
import ipaddress
from typing import Dict, List, Optional

# Define network architecture constants
ENTERPRISE_NETWORK_CIDR = "192.168.0.0/16"
DMZ_CIDR = "192.168.1.0/24"
INTERNAL_NETWORK_CIDR = "192.168.2.0/24"
STORAGE_NETWORK_CIDR = "192.168.3.0/24"
PUBLIC_IP = "41.202.160.0/20"  # Example public IP range for Douala

class NetworkDevice:
    """Base class for network devices"""
    def __init__(self, name: str, ip_address: str):
        self.name = name
        self.ip_address = ip_address
        self.configuration = {}

    def configure(self, config: Dict):
        """Apply configuration to device"""
        self.configuration.update(config)

    def validate_ip(self, ip: str) -> bool:
        """Validate IP address format"""
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

class Firewall(NetworkDevice):
    """Firewall device with security rules"""
    def __init__(self, name: str, ip_address: str):
        super().__init__(name, ip_address)
        self.rules = []
        self.zones = {
            "WAN": [],
            "DMZ": [],
            "LAN": [],
            "STORAGE": []
        }

    def add_rule(self, rule: Dict):
        """Add a firewall rule"""
        required_fields = ["name", "source", "destination", "action", "service"]
        if all(field in rule for field in required_fields):
            self.rules.append(rule)
        else:
            raise ValueError("Firewall rule missing required fields")

    def configure_zones(self):
        """Configure firewall security zones"""
        self.zones["WAN"] = [str(ip) for ip in ipaddress.IPv4Network(PUBLIC_IP)]
        self.zones["DMZ"] = [str(ip) for ip in ipaddress.IPv4Network(DMZ_CIDR)]
        self.zones["LAN"] = [str(ip) for ip in ipaddress.IPv4Network(INTERNAL_NETWORK_CIDR)]
        self.zones["STORAGE"] = [str(ip) for ip in ipaddress.IPv4Network(STORAGE_NETWORK_CIDR)]

    def generate_config(self) -> Dict:
        """Generate firewall configuration"""
        self.configure_zones()
        return {
            "device": self.name,
            "ip_address": self.ip_address,
            "zones": self.zones,
            "rules": self.rules
        }

class StorageServer(NetworkDevice):
    """Secure storage server implementation"""
    def __init__(self, name: str, ip_address: str):
        super().__init__(name, ip_address)
        self.storage_pools = []
        self.encryption_enabled = False
        self.access_controls = []

    def create_storage_pool(self, name: str, size_gb: int, raid_level: int):
        """Create a new storage pool"""
        if raid_level not in [0, 1, 5, 6, 10]:
            raise ValueError("Invalid RAID level")
        self.storage_pools.append({
            "name": name,
            "size_gb": size_gb,
            "raid_level": raid_level,
            "status": "active"
        })

    def enable_encryption(self, algorithm: str = "AES-256"):
        """Enable storage encryption"""
        if algorithm not in ["AES-128", "AES-192", "AES-256"]:
            raise ValueError("Unsupported encryption algorithm")
        self.encryption_enabled = True
        self.configuration["encryption"] = {
            "algorithm": algorithm,
            "status": "enabled"
        }

    def add_access_control(self, network: str, access_level: str):
        """Add access control rule"""
        valid_levels = ["read-only", "read-write", "admin"]
        if access_level not in valid_levels:
            raise ValueError("Invalid access level")
        
        try:
            ipaddress.ip_network(network)
            self.access_controls.append({
                "network": network,
                "access_level": access_level
            })
        except ValueError:
            raise ValueError("Invalid network CIDR")

class EnterpriseNetwork:
    """Enterprise network architecture implementation"""
    def __init__(self, name: str):
        self.name = name
        self.devices = []
        self.subnets = {
            "DMZ": DMZ_CIDR,
            "Internal": INTERNAL_NETWORK_CIDR,
            "Storage": STORAGE_NETWORK_CIDR
        }
        self.security_policies = []

    def add_device(self, device: NetworkDevice):
        """Add a network device to the architecture"""
        if not isinstance(device, NetworkDevice):
            raise TypeError("Device must be a NetworkDevice instance")
        self.devices.append(device)

    def add_security_policy(self, policy: Dict):
        """Add a security policy to the network"""
        required_fields = ["name", "description", "rules"]
        if all(field in policy for field in required_fields):
            self.security_policies.append(policy)
        else:
            raise ValueError("Security policy missing required fields")

    def generate_network_diagram(self) -> Dict:
        """Generate network architecture diagram"""
        return {
            "enterprise_name": self.name,
            "subnets": self.subnets,
            "devices": [device.name for device in self.devices],
            "security_policies": [policy["name"] for policy in self.security_policies]
        }

    def save_configuration(self, filename: str):
        """Save network configuration to file"""
        config = {
            "network": self.generate_network_diagram(),
            "devices": [device.generate_config() if hasattr(device, 'generate_config') else device.configuration 
                       for device in self.devices]
        }
        with open(filename, 'w') as f:
            json.dump(config, f, indent=2)

# Example implementation
if __name__ == "__main__":
    # Create enterprise network
    enterprise = EnterpriseNetwork("Douala Enterprise Network")
    
    # Configure firewall
    firewall = Firewall("Main Firewall", "192.168.0.1")
    firewall.add_rule({
        "name": "Allow HTTP to DMZ",
        "source": "any",
        "destination": "DMZ",
        "action": "allow",
        "service": "HTTP"
    })
    firewall.add_rule({
        "name": "Block External Storage Access",
        "source": "WAN",
        "destination": "STORAGE",
        "action": "deny",
        "service": "any"
    })
    
    # Configure storage server
    storage = StorageServer("Primary Storage", "192.168.3.10")
    storage.create_storage_pool("Primary", 1000, 5)
    storage.enable_encryption()
    storage.add_access_control(INTERNAL_NETWORK_CIDR, "read-write")
    storage.add_access_control(DMZ_CIDR, "read-only")
    
    # Add devices to network
    enterprise.add_device(firewall)
    enterprise.add_device(storage)
    
    # Add security policy
    enterprise.add_security_policy({
        "name": "Data Protection Policy",
        "description": "Ensures all stored data is encrypted and access controlled",
        "rules": [
            "All storage must use AES-256 encryption",
            "External access to storage network is prohibited"
        ]
    })
    
    # Save configuration
    enterprise.save_configuration("douala_enterprise_config.json")
```
