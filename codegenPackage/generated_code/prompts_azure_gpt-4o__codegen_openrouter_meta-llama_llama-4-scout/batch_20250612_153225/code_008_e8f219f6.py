"""
Generated Code Metadata:
========================
Original URL: https://polystack.tech
Prompt: Write code to simulate a cyber range environment for training and testing cybersecurity scenarios, inspired by Polystack Technologies' offerings.
Generated: DETERMINISTIC_e8f219f630d5e53f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cyber_range.py

import random
from typing import List, Dict

class CyberRange:
    """
    Simulates a cyber range environment for training and testing cybersecurity scenarios.
    """

    def __init__(self, name: str, num_networks: int, num_systems: int):
        """
        Initializes a cyber range environment.

        Args:
        - name (str): The name of the cyber range.
        - num_networks (int): The number of networks in the cyber range.
        - num_systems (int): The number of systems in each network.
        """
        self.name = name
        self.networks = self._create_networks(num_networks, num_systems)

    def _create_networks(self, num_networks: int, num_systems: int) -> List[Dict]:
        """
        Creates a list of networks, each with a specified number of systems.

        Args:
        - num_networks (int): The number of networks to create.
        - num_systems (int): The number of systems in each network.

        Returns:
        - A list of networks, where each network is a dictionary containing a list of systems.
        """
        networks = []
        for _ in range(num_networks):
            network = {
                "systems": self._create_systems(num_systems),
                "vulnerabilities": self._simulate_vulnerabilities(num_systems)
            }
            networks.append(network)
        return networks

    def _create_systems(self, num_systems: int) -> List[Dict]:
        """
        Creates a list of systems with random attributes.

        Args:
        - num_systems (int): The number of systems to create.

        Returns:
        - A list of systems, where each system is a dictionary with 'name', 'os', and 'status' keys.
        """
        systems = []
        for i in range(num_systems):
            system = {
                "name": f"System {i+1}",
                "os": random.choice(["Windows", "Linux", "macOS"]),
                "status": random.choice(["online", "offline"])
            }
            systems.append(system)
        return systems

    def _simulate_vulnerabilities(self, num_systems: int) -> List[Dict]:
        """
        Simulates vulnerabilities for each system in a network.

        Args:
        - num_systems (int): The number of systems in the network.

        Returns:
        - A list of vulnerabilities, where each vulnerability is a dictionary with 'system', 'type', and 'severity' keys.
        """
        vulnerabilities = []
        for i in range(num_systems):
            vulnerability = {
                "system": f"System {i+1}",
                "type": random.choice(["SQL Injection", "Cross-Site Scripting", "Buffer Overflow"]),
                "severity": random.choice(["low", "medium", "high"])
            }
            vulnerabilities.append(vulnerability)
        return vulnerabilities

    def simulate_attack(self, network_index: int, system_index: int):
        """
        Simulates an attack on a system in a network.

        Args:
        - network_index (int): The index of the network to attack.
        - system_index (int): The index of the system to attack.
        """
        try:
            network = self.networks[network_index]
            system = network["systems"][system_index]
            if system["status"] == "online":
                print(f"Simulating attack on {system['name']} in Network {network_index+1}...")
                # Simulate attack logic here
                print("Attack simulation complete.")
            else:
                print(f"{system['name']} is offline and cannot be attacked.")
        except IndexError:
            print("Invalid network or system index.")

    def display_cyber_range(self):
        """
        Displays the cyber range environment.
        """
        print(f"Cyber Range: {self.name}")
        for i, network in enumerate(self.networks):
            print(f"Network {i+1}:")
            print("Systems:")
            for system in network["systems"]:
                print(f"- {system['name']} ({system['os']}) - {system['status']}")
            print("Vulnerabilities:")
            for vulnerability in network["vulnerabilities"]:
                print(f"- {vulnerability['system']}: {vulnerability['type']} (Severity: {vulnerability['severity']})")
            print()


def main():
    cyber_range = CyberRange("My Cyber Range", 2, 3)
    cyber_range.display_cyber_range()
    cyber_range.simulate_attack(0, 1)


if __name__ == "__main__":
    main()
```
