"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Generate a tool for simulating the impact of water incursion or cyberattacks on data center operations, referencing the downtime causes listed by Technical Power Service, Inc.
Generated: DETERMINISTIC_dfb1549eb31f6cb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_center_simulator.py

import random
from enum import Enum
from typing import Dict, List

class DowntimeCause(Enum):
    """Downtime causes listed by Technical Power Service, Inc."""
    WATER_INCURSION = 1
    CYBER_ATTACK = 2
    POWER_FAILURE = 3
    COOLING_FAILURE = 4
    NETWORK_OUTAGE = 5
    HUMAN_ERROR = 6

class DataCenter:
    def __init__(self, name: str, capacity: int):
        """
        Initialize a data center with a given name and capacity.

        Args:
        - name (str): The name of the data center.
        - capacity (int): The maximum number of servers the data center can hold.
        """
        self.name = name
        self.capacity = capacity
        self.servers = [f"Server {i}" for i in range(capacity)]
        self.downtime_causes: Dict[DowntimeCause, int] = {
            DowntimeCause.WATER_INCURSION: 0,
            DowntimeCause.CYBER_ATTACK: 0,
            DowntimeCause.POWER_FAILURE: 0,
            DowntimeCause.COOLING_FAILURE: 0,
            DowntimeCause.NETWORK_OUTAGE: 0,
            DowntimeCause.HUMAN_ERROR: 0,
        }

    def simulate_downtime(self, cause: DowntimeCause, num_servers: int):
        """
        Simulate downtime in the data center.

        Args:
        - cause (DowntimeCause): The cause of the downtime.
        - num_servers (int): The number of servers affected by the downtime.

        Raises:
        - ValueError: If the number of servers affected is greater than the data center's capacity.
        """
        if num_servers > self.capacity:
            raise ValueError("Number of servers affected cannot exceed data center capacity")

        self.downtime_causes[cause] += num_servers
        print(f"Simulated {num_servers} servers going down due to {cause.name}")

    def get_downtime_report(self) -> str:
        """
        Generate a report of downtime causes and the number of servers affected.

        Returns:
        - str: A formatted report of downtime causes and server counts.
        """
        report = f"Downtime Report for {self.name}:\n"
        for cause, count in self.downtime_causes.items():
            report += f"- {cause.name}: {count} servers\n"
        return report

def simulate_water_incursion(data_center: DataCenter, probability: float):
    """
    Simulate water incursion in the data center.

    Args:
    - data_center (DataCenter): The data center to simulate water incursion in.
    - probability (float): The probability of water incursion occurring (between 0 and 1).

    Returns:
    - int: The number of servers affected by the water incursion.
    """
    if random.random() < probability:
        num_servers_affected = random.randint(1, data_center.capacity)
        data_center.simulate_downtime(DowntimeCause.WATER_INCURSION, num_servers_affected)
        return num_servers_affected
    return 0

def simulate_cyber_attack(data_center: DataCenter, probability: float):
    """
    Simulate a cyber attack in the data center.

    Args:
    - data_center (DataCenter): The data center to simulate a cyber attack in.
    - probability (float): The probability of a cyber attack occurring (between 0 and 1).

    Returns:
    - int: The number of servers affected by the cyber attack.
    """
    if random.random() < probability:
        num_servers_affected = random.randint(1, data_center.capacity)
        data_center.simulate_downtime(DowntimeCause.CYBER_ATTACK, num_servers_affected)
        return num_servers_affected
    return 0

def main():
    data_center = DataCenter("Example Data Center", 100)

    # Simulate water incursion with 10% probability
    water_incursion_probability = 0.1
    num_servers_affected = simulate_water_incursion(data_center, water_incursion_probability)
    print(f"Water incursion affected {num_servers_affected} servers")

    # Simulate cyber attack with 5% probability
    cyber_attack_probability = 0.05
    num_servers_affected = simulate_cyber_attack(data_center, cyber_attack_probability)
    print(f"Cyber attack affected {num_servers_affected} servers")

    # Generate downtime report
    print(data_center.get_downtime_report())

if __name__ == "__main__":
    main()
```
