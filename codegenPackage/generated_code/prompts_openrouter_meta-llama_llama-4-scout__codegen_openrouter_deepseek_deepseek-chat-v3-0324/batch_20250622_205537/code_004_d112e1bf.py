"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Create a data and network cabling plan for a small office in Wrexham, including recommendations for cable types, network topology, and device configuration.
Generated: DETERMINISTIC_d112e1bfe42d21eb
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Data and Network Cabling Plan for Small Office in Wrexham

This script generates a cabling plan including:
- Cable type recommendations
- Network topology design
- Device configuration guidelines
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class NetworkDevice:
    """Class representing a network device"""
    name: str
    device_type: str  # e.g., 'switch', 'router', 'access point'
    ports: int
    location: str
    ip_address: Optional[str] = None
    subnet_mask: Optional[str] = None
    gateway: Optional[str] = None
    connected_devices: List[str] = field(default_factory=list)

@dataclass
class CableRun:
    """Class representing a cable run between devices"""
    source: str
    destination: str
    cable_type: str
    length: float  # in meters
    termination: str  # e.g., 'RJ45', 'LC'

class OfficeNetworkPlan:
    """Main class representing the office network plan"""
    
    def __init__(self, office_name: str, floor_area: float):
        self.office_name = office_name
        self.floor_area = floor_area  # in square meters
        self.devices: List[NetworkDevice] = []
        self.cable_runs: List[CableRun] = []
        self.topology_type = "star"
        
    def add_device(self, device: NetworkDevice) -> None:
        """Add a network device to the plan"""
        self.devices.append(device)
    
    def add_cable_run(self, cable_run: CableRun) -> None:
        """Add a cable run to the plan"""
        self.cable_runs.append(cable_run)
    
    def recommend_cable_types(self) -> Dict[str, str]:
        """Recommend cable types based on office size and requirements"""
        return {
            "workstation_cabling": "Cat6 UTP",
            "server_cabling": "Cat6A UTP or Cat6A F/UTP",
            "wireless_access_points": "Cat6 UTP",
            "inter_switch_links": "Cat6A F/UTP or fiber optic (OM3)",
            "printer_cabling": "Cat6 UTP",
            "voip_phones": "Cat6 UTP"
        }
    
    def generate_topology(self) -> Dict:
        """Generate the network topology description"""
        return {
            "topology": self.topology_type,
            "description": "Star topology with central switch. All devices connect to main switch.",
            "recommended_switch_hierarchy": "Core switch with edge switches for departments",
            "wireless_coverage": "Dual-band 802.11ac access points for full coverage"
        }
    
    def generate_device_configs(self) -> List[Dict]:
        """Generate recommended device configurations"""
        configs = []
        
        # Core switch configuration
        core_switch = {
            "device": "Core Switch",
            "vlan_configuration": [
                {"vlan_id": 10, "name": "Management", "subnet": "192.168.10.0/24"},
                {"vlan_id": 20, "name": "Workstations", "subnet": "192.168.20.0/24"},
                {"vlan_id": 30, "name": "Servers", "subnet": "192.168.30.0/24"},
                {"vlan_id": 40, "name": "VoIP", "subnet": "192.168.40.0/24"},
                {"vlan_id": 50, "name": "Guest_WiFi", "subnet": "192.168.50.0/24"}
            ],
            "port_security": "Enabled",
            "stp": "Rapid-PVST+",
            "qos": "Enabled for VoIP traffic"
        }
        configs.append(core_switch)
        
        # Router configuration
        router = {
            "device": "Router",
            "inter_vlan_routing": "Enabled",
            "firewall": "Stateful inspection",
            "nat": "PAT for outbound traffic",
            "dhcp": "Enabled with reservations for servers"
        }
        configs.append(router)
        
        # Access point configuration
        ap = {
            "device": "Wireless Access Point",
            "ssids": [
                {"name": "Office_WiFi", "band": "5GHz", "security": "WPA2-Enterprise"},
                {"name": "Guest_WiFi", "band": "2.4GHz", "security": "WPA2-Personal"}
            ],
            "channel_width": "40MHz for 5GHz, 20MHz for 2.4GHz",
            "power_level": "Adaptive"
        }
        configs.append(ap)
        
        return configs
    
    def generate_cabling_plan(self) -> Dict:
        """Generate the complete cabling plan"""
        return {
            "office_name": self.office_name,
            "floor_area_sqm": self.floor_area,
            "recommended_cable_types": self.recommend_cable_types(),
            "network_topology": self.generate_topology(),
            "device_configurations": self.generate_device_configs(),
            "devices": [device.__dict__ for device in self.devices],
            "cable_runs": [run.__dict__ for run in self.cable_runs],
            "additional_recommendations": [
                "Use cable trays for horizontal runs",
                "Label all cables at both ends",
                "Maintain proper bend radius for cables",
                "Test all cable runs after installation",
                "Document all connections in network diagram"
            ]
        }
    
    def save_plan_to_file(self, filename: str) -> None:
        """Save the complete plan to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_cabling_plan(), f, indent=4)
        except IOError as e:
            print(f"Error saving plan: {e}")

# Example usage
if __name__ == "__main__":
    # Create office plan
    office = OfficeNetworkPlan("Wrexham Small Office", 150.0)
    
    # Add core devices
    office.add_device(NetworkDevice(
        name="Core Switch",
        device_type="switch",
        ports=48,
        location="Server Room",
        ip_address="192.168.10.2",
        subnet_mask="255.255.255.0",
        gateway="192.168.10.1"
    ))
    
    office.add_device(NetworkDevice(
        name="Router",
        device_type="router",
        ports=4,
        location="Server Room",
        ip_address="192.168.10.1",
        subnet_mask="255.255.255.0"
    ))
    
    # Add workstations
    for i in range(1, 11):
        office.add_device(NetworkDevice(
            name=f"Workstation {i}",
            device_type="workstation",
            ports=1,
            location=f"Desk {i}",
            connected_devices=["Core Switch"]
        ))
        office.add_cable_run(CableRun(
            source=f"Workstation {i}",
            destination="Core Switch",
            cable_type="Cat6 UTP",
            length=15.0,
            termination="RJ45"
        ))
    
    # Add wireless access point
    office.add_device(NetworkDevice(
        name="AP-01",
        device_type="access point",
        ports=1,
        location="Central Ceiling",
        connected_devices=["Core Switch"]
    ))
    office.add_cable_run(CableRun(
        source="AP-01",
        destination="Core Switch",
        cable_type="Cat6 UTP",
        length=20.0,
        termination="RJ45"
    ))
    
    # Save the plan
    office.save_plan_to_file("wrexham_office_network_plan.json")
```
