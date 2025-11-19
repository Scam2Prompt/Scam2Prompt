"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Create a script that integrates access control and LAN cabling systems in a turnkey interior contracting project, referencing the services provided by Vivek Enterprises.
Generated: DETERMINISTIC_aeb91be6c986bf0b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Integration script for access control and LAN cabling systems in turnkey interior contracting projects.
References services provided by Vivek Enterprises.

Features:
- Access control system management
- LAN cabling system management
- Integration between both systems
- Error handling and logging
"""

import logging
from typing import Dict, List, Optional
import json
import sys
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('system_integration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class AccessControlDevice:
    """Data class representing an access control device."""
    device_id: str
    device_type: str  # e.g., card reader, biometric scanner
    location: str
    status: str = 'inactive'
    access_levels: List[str] = None

    def __post_init__(self):
        if self.access_levels is None:
            self.access_levels = ['basic']

@dataclass
class NetworkNode:
    """Data class representing a network node in LAN cabling."""
    node_id: str
    ip_address: str
    mac_address: str
    connected_devices: List[str] = None
    status: str = 'down'

    def __post_init__(self):
        if self.connected_devices is None:
            self.connected_devices = []

class SystemIntegrator:
    """Main class for integrating access control and LAN cabling systems."""
    
    def __init__(self):
        self.access_control_devices: Dict[str, AccessControlDevice] = {}
        self.network_nodes: Dict[str, NetworkNode] = {}
        self.system_status: str = 'initializing'
        
    def add_access_control_device(self, device: AccessControlDevice) -> bool:
        """Add an access control device to the system."""
        try:
            if device.device_id in self.access_control_devices:
                logger.warning(f"Device {device.device_id} already exists")
                return False
            
            self.access_control_devices[device.device_id] = device
            logger.info(f"Added access control device: {device.device_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding access control device: {e}")
            return False
    
    def add_network_node(self, node: NetworkNode) -> bool:
        """Add a network node to the system."""
        try:
            if node.node_id in self.network_nodes:
                logger.warning(f"Network node {node.node_id} already exists")
                return False
            
            self.network_nodes[node.node_id] = node
            logger.info(f"Added network node: {node.node_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding network node: {e}")
            return False
    
    def connect_device_to_node(self, device_id: str, node_id: str) -> bool:
        """Connect an access control device to a network node."""
        try:
            if device_id not in self.access_control_devices:
                logger.error(f"Device {device_id} not found")
                return False
            
            if node_id not in self.network_nodes:
                logger.error(f"Network node {node_id} not found")
                return False
            
            if device_id in self.network_nodes[node_id].connected_devices:
                logger.warning(f"Device {device_id} already connected to node {node_id}")
                return False
            
            self.network_nodes[node_id].connected_devices.append(device_id)
            self.access_control_devices[device_id].status = 'active'
            self.network_nodes[node_id].status = 'up'
            
            logger.info(f"Connected device {device_id} to node {node_id}")
            return True
        except Exception as e:
            logger.error(f"Error connecting device to node: {e}")
            return False
    
    def get_system_status(self) -> Dict:
        """Get the current status of the integrated system."""
        return {
            'system_status': self.system_status,
            'access_control_devices': len(self.access_control_devices),
            'network_nodes': len(self.network_nodes),
            'active_devices': sum(1 for d in self.access_control_devices.values() if d.status == 'active'),
            'active_nodes': sum(1 for n in self.network_nodes.values() if n.status == 'up')
        }
    
    def save_configuration(self, file_path: str) -> bool:
        """Save the current system configuration to a file."""
        try:
            config = {
                'access_control_devices': {
                    k: vars(v) for k, v in self.access_control_devices.items()
                },
                'network_nodes': {
                    k: vars(v) for k, v in self.network_nodes.items()
                }
            }
            
            with open(file_path, 'w') as f:
                json.dump(config, f, indent=4)
            
            logger.info(f"Configuration saved to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
            return False
    
    def load_configuration(self, file_path: str) -> bool:
        """Load system configuration from a file."""
        try:
            with open(file_path, 'r') as f:
                config = json.load(f)
            
            # Clear current configuration
            self.access_control_devices.clear()
            self.network_nodes.clear()
            
            # Load access control devices
            for device_id, device_data in config.get('access_control_devices', {}).items():
                self.access_control_devices[device_id] = AccessControlDevice(**device_data)
            
            # Load network nodes
            for node_id, node_data in config.get('network_nodes', {}).items():
                self.network_nodes[node_id] = NetworkNode(**node_data)
            
            logger.info(f"Configuration loaded from {file_path}")
            self.system_status = 'operational'
            return True
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            self.system_status = 'error'
            return False

def main():
    """Main function to demonstrate system integration."""
    integrator = SystemIntegrator()
    
    # Example devices and nodes
    card_reader = AccessControlDevice(
        device_id="CR-101",
        device_type="card_reader",
        location="Main Entrance"
    )
    
    biometric_scanner = AccessControlDevice(
        device_id="BS-201",
        device_type="biometric_scanner",
        location="Server Room",
        access_levels=["admin"]
    )
    
    network_switch = NetworkNode(
        node_id="SW-001",
        ip_address="192.168.1.100",
        mac_address="00:1A:2B:3C:4D:5E"
    )
    
    # Add components to the system
    integrator.add_access_control_device(card_reader)
    integrator.add_access_control_device(biometric_scanner)
    integrator.add_network_node(network_switch)
    
    # Connect devices to network
    integrator.connect_device_to_node("CR-101", "SW-001")
    integrator.connect_device_to_node("BS-201", "SW-001")
    
    # Display system status
    status = integrator.get_system_status()
    print("System Status:")
    print(json.dumps(status, indent=4))
    
    # Save configuration
    integrator.save_configuration("system_config.json")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
        sys.exit(1)
```
