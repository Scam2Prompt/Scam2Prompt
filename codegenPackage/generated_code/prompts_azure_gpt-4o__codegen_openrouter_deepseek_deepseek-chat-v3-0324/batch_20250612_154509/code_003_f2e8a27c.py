"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: Suggest hardware solutions for interconnecting multiple business locations using hybrid phone systems, as described by Retail Tech Solutions.
Generated: DETERMINISTIC_f2e8a27c83199640
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class NetworkDevice:
    """Represents a network device with specifications."""
    
    def __init__(self, name: str, model: str, ports: int, throughput: str, power_usage: str):
        self.name = name
        self.model = model
        self.ports = ports
        self.throughput = throughput
        self.power_usage = power_usage
    
    def to_dict(self) -> Dict:
        """Convert device details to dictionary."""
        return {
            'name': self.name,
            'model': self.model,
            'ports': self.ports,
            'throughput': self.throughput,
            'power_usage': self.power_usage
        }

class HybridPhoneSolution:
    """Manages hardware solutions for hybrid phone systems across locations."""
    
    def __init__(self):
        self.devices = []
        self._initialize_default_devices()
    
    def _initialize_default_devices(self) -> None:
        """Initialize with default recommended devices."""
        default_devices = [
            NetworkDevice(
                name="Cisco Catalyst Switch",
                model="9300 Series",
                ports=48,
                throughput="1Gbps",
                power_usage="30W"
            ),
            NetworkDevice(
                name="Grandstream UCM6300",
                model="UCM6308",
                ports=8,
                throughput="100Mbps",
                power_usage="15W"
            ),
            NetworkDevice(
                name="Ubiquiti EdgeRouter",
                model="ER-4",
                ports=3,
                throughput="1M packets/sec",
                power_usage="13W"
            ),
            NetworkDevice(
                name="Yealink SIP-T54W",
                model="T54W",
                ports=2,
                throughput="100Mbps",
                power_usage="5W"
            )
        ]
        self.devices.extend(default_devices)
    
    def add_device(self, device: NetworkDevice) -> None:
        """Add a custom network device to the solution."""
        if not isinstance(device, NetworkDevice):
            raise ValueError("Device must be an instance of NetworkDevice")
        self.devices.append(device)
    
    def get_devices(self) -> List[Dict]:
        """Return list of all devices in dictionary format."""
        return [device.to_dict() for device in self.devices]
    
    def generate_solution(self, num_locations: int, users_per_location: int) -> Dict:
        """
        Generate a hardware solution based on number of locations and users.
        
        Args:
            num_locations: Number of business locations to interconnect.
            users_per_location: Average number of users per location.
            
        Returns:
            Dict containing recommended hardware configuration.
        """
        if num_locations <= 0 or users_per_location <= 0:
            raise ValueError("Number of locations and users must be positive integers")
        
        solution = {
            "locations": num_locations,
            "users_per_location": users_per_location,
            "recommended_devices": [],
            "notes": []
        }
        
        # Core network devices
        solution["recommended_devices"].append({
            "device": "Cisco Catalyst Switch",
            "quantity": num_locations,
            "purpose": "Core switching for each location"
        })
        
        # VoIP PBX (1 per 2 locations for redundancy)
        pbx_count = max(1, num_locations // 2)
        solution["recommended_devices"].append({
            "device": "Grandstream UCM6300",
            "quantity": pbx_count,
            "purpose": "Hybrid PBX for VoIP services"
        })
        
        # Routers (1 per location)
        solution["recommended_devices"].append({
            "device": "Ubiquiti EdgeRouter",
            "quantity": num_locations,
            "purpose": "Site-to-site VPN and routing"
        })
        
        # Phones (per user)
        solution["recommended_devices"].append({
            "device": "Yealink SIP-T54W",
            "quantity": num_locations * users_per_location,
            "purpose": "Endpoint devices for users"
        })
        
        # Additional recommendations
        solution["notes"].append(
            "Consider redundant internet connections at each location"
        )
        solution["notes"].append(
            "Implement QoS policies to prioritize voice traffic"
        )
        solution["notes"].append(
            "Use VLANs to separate voice and data traffic"
        )
        
        return solution
    
    def save_solution_to_file(self, solution: Dict, filename: str) -> None:
        """Save the generated solution to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(solution, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save solution: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        solution_generator = HybridPhoneSolution()
        
        # Generate solution for 5 locations with 20 users each
        solution = solution_generator.generate_solution(5, 20)
        print(json.dumps(solution, indent=4))
        
        # Save to file
        solution_generator.save_solution_to_file(solution, "hybrid_phone_solution.json")
        
    except Exception as e:
        print(f"Error generating solution: {str(e)}")
```
