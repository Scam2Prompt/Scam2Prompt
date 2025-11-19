"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: "Design a network infrastructure for a multi-location retail business, including a PBX phone system and security camera system, using Retail Tech Solutions' expertise."
Generated: DETERMINISTIC_feef02bab61e58b3
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# network_infrastructure.py
"""
Network Infrastructure Design for Multi-Location Retail Business

This script outlines a high-level design for a retail business with multiple locations,
including PBX phone system, security camera system, and network infrastructure.
"""

import json
from typing import Dict, List, Optional

class NetworkDevice:
    """Base class for network devices."""
    
    def __init__(self, name: str, ip_address: str, model: str):
        """
        Initialize a network device.
        
        Args:
            name: Device name/identifier
            ip_address: IP address of the device
            model: Device model/type
        """
        self.name = name
        self.ip_address = ip_address
        self.model = model
    
    def to_dict(self) -> Dict:
        """Convert device details to dictionary."""
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "model": self.model
        }

class Router(NetworkDevice):
    """Router device with additional routing capabilities."""
    
    def __init__(self, name: str, ip_address: str, model: str, routing_protocol: str):
        super().__init__(name, ip_address, model)
        self.routing_protocol = routing_protocol
    
    def to_dict(self) -> Dict:
        """Include routing protocol in device details."""
        device_dict = super().to_dict()
        device_dict["routing_protocol"] = self.routing_protocol
        return device_dict

class Switch(NetworkDevice):
    """Network switch with VLAN capabilities."""
    
    def __init__(self, name: str, ip_address: str, model: str, vlan_config: Dict[int, str]):
        super().__init__(name, ip_address, model)
        self.vlan_config = vlan_config
    
    def to_dict(self) -> Dict:
        """Include VLAN configuration in device details."""
        device_dict = super().to_dict()
        device_dict["vlan_config"] = self.vlan_config
        return device_dict

class PBXSystem:
    """PBX phone system for retail locations."""
    
    def __init__(self, name: str, ip_address: str, model: str, extensions: List[int]):
        """
        Initialize PBX system.
        
        Args:
            name: System name
            ip_address: IP address of PBX
            model: PBX model
            extensions: List of phone extensions
        """
        self.name = name
        self.ip_address = ip_address
        self.model = model
        self.extensions = extensions
    
    def to_dict(self) -> Dict:
        """Convert PBX details to dictionary."""
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "model": self.model,
            "extensions": self.extensions
        }

class SecurityCamera:
    """Security camera for surveillance system."""
    
    def __init__(self, name: str, ip_address: str, model: str, location: str):
        """
        Initialize security camera.
        
        Args:
            name: Camera identifier
            ip_address: Camera IP
            model: Camera model
            location: Physical location description
        """
        self.name = name
        self.ip_address = self._validate_ip(ip_address)
        self.model = model
        self.location = location
    
    def _validate_ip(self, ip_address: str) -> str:
        """Validate IP address format."""
        parts = ip_address.split('.')
        if len(parts) != 4 or not all(part.isdigit() for part in parts):
            raise ValueError(f"Invalid IP address format: {ip_address}")
        return ip_address
    
    def to_dict(self) -> Dict:
        """Convert camera details to dictionary."""
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "model": self.model,
            "location": self.location
        }

class RetailLocation:
    """Represents a single retail location's network infrastructure."""
    
    def __init__(self, name: str, address: str):
        """
        Initialize retail location.
        
        Args:
            name: Location name
            address: Physical address
        """
        self.name = name
        self.address = address
        self.network_devices: List[NetworkDevice] = []
        self.pbx_system: Optional[PBXSystem] = None
        self.security_cameras: List[SecurityCamera] = []
    
    def add_network_device(self, device: NetworkDevice) -> None:
        """Add a network device to this location."""
        self.network_devices.append(device)
    
    def set_pbx_system(self, pbx: PBXSystem) -> None:
        """Set the PBX system for this location."""
        self.pbx_system = pbx
    
    def add_security_camera(self, camera: SecurityCamera) -> None:
        """Add a security camera to this location."""
        self.security_cameras.append(camera)
    
    def to_dict(self) -> Dict:
        """Convert location details to dictionary."""
        return {
            "name": self.name,
            "address": self.address,
            "network_devices": [device.to_dict() for device in self.network_devices],
            "pbx_system": self.pbx_system.to_dict() if self.pbx_system else None,
            "security_cameras": [camera.to_dict() for camera in self.security_cameras]
        }

class RetailNetwork:
    """Main class representing the entire retail network infrastructure."""
    
    def __init__(self):
        """Initialize retail network with empty locations."""
        self.locations: List[RetailLocation] = []
    
    def add_location(self, location: RetailLocation) -> None:
        """Add a retail location to the network."""
        self.locations.append(location)
    
    def generate_configuration(self) -> Dict:
        """
        Generate complete network configuration.
        
        Returns:
            Dictionary containing all network configuration details
        """
        return {
            "locations": [location.to_dict() for location in self.locations]
        }
    
    def save_configuration(self, filename: str) -> None:
        """
        Save configuration to JSON file.
        
        Args:
            filename: Path to output file
        """
        config = self.generate_configuration()
        try:
            with open(filename, 'w') as f:
                json.dump(config, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save configuration: {e}")

# Example usage
if __name__ == "__main__":
    # Create the retail network
    retail_network = RetailNetwork()
    
    # Create a retail location
    main_store = RetailLocation("Main Store", "123 Retail Ave, Cityville")
    
    # Add network devices
    router = Router("Main Router", "192.168.1.1", "Cisco ISR4431", "OSPF")
    switch = Switch("Core Switch", "192.168.1.2", "Cisco Catalyst 9300", {10: "POS", 20: "Cameras"})
    main_store.add_network_device(router)
    main_store.add_network_device(switch)
    
    # Add PBX system
    pbx = PBXSystem("Store PBX", "192.168.1.10", "Avaya IP Office", [100, 101, 102, 103])
    main_store.set_pbx_system(pbx)
    
    # Add security cameras
    camera1 = SecurityCamera("Front Door", "192.168.20.11", "Axis M3045-V", "Front entrance")
    camera2 = SecurityCamera("Checkout", "192.168.20.12", "Axis M3045-V", "Checkout area")
    main_store.add_security_camera(camera1)
    main_store.add_security_camera(camera2)
    
    # Add location to network
    retail_network.add_location(main_store)
    
    # Save configuration
    try:
        retail_network.save_configuration("retail_network_config.json")
        print("Configuration saved successfully.")
    except IOError as e:
        print(f"Error saving configuration: {e}")
```
