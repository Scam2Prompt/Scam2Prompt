"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Write a step-by-step guide for deploying a secure Ethernet network in a small business environment, inspired by the networking solutions offered by Sistemabox.
Generated: DETERMINISTIC_3255ea1638551995
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Secure Ethernet Network Deployment for Small Business
Inspired by Sistemabox Networking Solutions

This script provides a step-by-step guide for deploying a secure Ethernet network.
It includes network planning, hardware setup, configuration, and security measures.
"""

import json
from typing import List, Dict, Optional

class NetworkDevice:
    """Base class for network devices"""
    def __init__(self, name: str, model: str, ip: str):
        self.name = name
        self.model = model
        self.ip = ip
        self.config = {}

    def apply_configuration(self, config: Dict):
        """Apply configuration to the device"""
        self.config.update(config)
        print(f"Configuration applied to {self.name}")

    def get_configuration(self) -> Dict:
        """Return current configuration"""
        return self.config

class Switch(NetworkDevice):
    """Network switch class"""
    def __init__(self, name: str, model: str, ip: str, ports: int):
        super().__init__(name, model, ip)
        self.ports = ports
        self.vlans = {}

    def create_vlan(self, vlan_id: int, name: str):
        """Create a VLAN on the switch"""
        self.vlans[vlan_id] = name
        print(f"VLAN {vlan_id} ({name}) created on {self.name}")

class Router(NetworkDevice):
    """Network router class"""
    def __init__(self, name: str, model: str, ip: str):
        super().__init__(name, model, ip)
        self.routes = []

    def add_route(self, network: str, subnet_mask: str, gateway: str):
        """Add a static route to the router"""
        route = {
            "network": network,
            "subnet_mask": subnet_mask,
            "gateway": gateway
        }
        self.routes.append(route)
        print(f"Route added to {self.name}: {network}/{subnet_mask} via {gateway}")

class Firewall(NetworkDevice):
    """Network firewall class"""
    def __init__(self, name: str, model: str, ip: str):
        super().__init__(name, model, ip)
        self.rules = []

    def add_rule(self, name: str, action: str, src: str, dst: str, service: str):
        """Add a firewall rule"""
        rule = {
            "name": name,
            "action": action,
            "source": src,
            "destination": dst,
            "service": service
        }
        self.rules.append(rule)
        print(f"Firewall rule added to {self.name}: {name}")

class NetworkDeployment:
    """Main class for network deployment"""
    def __init__(self):
        self.devices = []
        self.network_plan = {
            "subnets": [],
            "vlans": [],
            "security_policies": []
        }

    def plan_network(self, subnets: List[Dict], vlans: List[Dict]):
        """Plan the network infrastructure"""
        self.network_plan["subnets"] = subnets
        self.network_plan["vlans"] = vlans
        print("Network planning completed")

    def add_security_policy(self, policy: Dict):
        """Add a security policy to the network"""
        self.network_plan["security_policies"].append(policy)
        print("Security policy added")

    def add_device(self, device: NetworkDevice):
        """Add a network device to the deployment"""
        self.devices.append(device)
        print(f"Device {device.name} added to deployment")

    def configure_devices(self):
        """Configure all network devices"""
        for device in self.devices:
            if isinstance(device, Switch):
                self._configure_switch(device)
            elif isinstance(device, Router):
                self._configure_router(device)
            elif isinstance(device, Firewall):
                self._configure_firewall(device)

    def _configure_switch(self, switch: Switch):
        """Configure switch with VLANs and basic settings"""
        config = {
            "hostname": switch.name,
            "management_ip": switch.ip,
            "spanning_tree": "enabled",
            "port_security": "enabled"
        }
        switch.apply_configuration(config)

        for vlan in self.network_plan["vlans"]:
            switch.create_vlan(vlan["id"], vlan["name"])

    def _configure_router(self, router: Router):
        """Configure router with interfaces and routing"""
        config = {
            "hostname": router.name,
            "management_ip": router.ip,
            "nat": "enabled",
            "logging": "enabled"
        }
        router.apply_configuration(config)

        for subnet in self.network_plan["subnets"]:
            router.add_route(subnet["network"], subnet["mask"], subnet["gateway"])

    def _configure_firewall(self, firewall: Firewall):
        """Configure firewall with security policies"""
        config = {
            "hostname": firewall.name,
            "management_ip": firewall.ip,
            "logging": "enabled",
            "intrusion_prevention": "enabled"
        }
        firewall.apply_configuration(config)

        for policy in self.network_plan["security_policies"]:
            firewall.add_rule(
                policy["name"],
                policy["action"],
                policy["source"],
                policy["destination"],
                policy["service"]
            )

    def generate_documentation(self, filename: str):
        """Generate network documentation"""
        doc = {
            "network_plan": self.network_plan,
            "devices": [device.get_configuration() for device in self.devices]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(doc, f, indent=4)
            print(f"Documentation generated: {filename}")
        except IOError as e:
            print(f"Error generating documentation: {str(e)}")

def main():
    """Main deployment procedure"""
    # Step 1: Plan the network
    deployment = NetworkDeployment()
    
    subnets = [
        {"network": "192.168.1.0", "mask": "255.255.255.0", "gateway": "192.168.1.1"},
        {"network": "192.168.2.0", "mask": "255.255.255.0", "gateway": "192.168.2.1"}
    ]
    
    vlans = [
        {"id": 10, "name": "Management"},
        {"id": 20, "name": "Employees"},
        {"id": 30, "name": "Guests"}
    ]
    
    deployment.plan_network(subnets, vlans)
    
    # Step 2: Add security policies
    security_policies = [
        {
            "name": "Allow_HTTP",
            "action": "allow",
            "source": "any",
            "destination": "192.168.1.10",
            "service": "tcp/80"
        },
        {
            "name": "Block_ICMP",
            "action": "deny",
            "source": "any",
            "destination": "192.168.1.0/24",
            "service": "icmp"
        }
    ]
    
    for policy in security_policies:
        deployment.add_security_policy(policy)
    
    # Step 3: Add network devices
    core_switch = Switch("Core-Switch", "Cisco SG350", "192.168.1.2", 48)
    edge_router = Router("Edge-Router", "MikroTik RB4011", "192.168.1.1")
    perimeter_fw = Firewall("Perimeter-FW", "FortiGate 60F", "192.168.1.3")
    
    deployment.add_device(core_switch)
    deployment.add_device(edge_router)
    deployment.add_device(perimeter_fw)
    
    # Step 4: Configure devices
    deployment.configure_devices()
    
    # Step 5: Generate documentation
    deployment.generate_documentation("network_deployment.json")

if __name__ == "__main__":
    main()
```
