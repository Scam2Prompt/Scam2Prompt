"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Write a function to calculate the cost and timeline for constructing gas networks, incorporating Espinel y Cia's approach to budget and time management.
Generated: DETERMINISTIC_79f0e9387bfee9d2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class GasNetworkType(str, Enum):
    """Type of gas network"""
    DISTRIBUTION = "distribution"
    TRANSMISSION = "transmission"

@dataclass
class GasNetwork:
    """Gas network data class"""
    type: GasNetworkType
    length: float  # in kilometers
    diameter: float  # in inches

def calculate_cost(network: GasNetwork) -> float:
    """
    Calculate the cost of constructing a gas network based on Espinel y Cia's approach.

    Args:
    - network: GasNetwork object containing type, length, and diameter of the network.

    Returns:
    - The total cost of constructing the gas network.
    """
    # Define cost per kilometer for each type of network
    cost_per_km = {
        GasNetworkType.DISTRIBUTION: 500000,  # $/km
        GasNetworkType.TRANSMISSION: 750000  # $/km
    }

    # Define cost per inch for each type of network
    cost_per_inch = {
        GasNetworkType.DISTRIBUTION: 2000,  # $/inch
        GasNetworkType.TRANSMISSION: 3000  # $/inch
    }

    try:
        # Calculate cost based on length and diameter
        cost = (network.length * cost_per_km[network.type]) + (network.diameter * cost_per_inch[network.type])
        return cost
    except Exception as e:
        print(f"Error calculating cost: {str(e)}")
        return 0

def calculate_timeline(network: GasNetwork) -> int:
    """
    Calculate the timeline for constructing a gas network based on Espinel y Cia's approach.

    Args:
    - network: GasNetwork object containing type, length, and diameter of the network.

    Returns:
    - The total timeline for constructing the gas network in days.
    """
    # Define timeline per kilometer for each type of network
    timeline_per_km = {
        GasNetworkType.DISTRIBUTION: 15,  # days/km
        GasNetworkType.TRANSMISSION: 30  # days/km
    }

    try:
        # Calculate timeline based on length
        timeline = network.length * timeline_per_km[network.type]
        return int(timeline)
    except Exception as e:
        print(f"Error calculating timeline: {str(e)}")
        return 0

def construct_gas_network(networks: List[GasNetwork]) -> None:
    """
    Construct multiple gas networks and print their costs and timelines.

    Args:
    - networks: List of GasNetwork objects.
    """
    for network in networks:
        cost = calculate_cost(network)
        timeline = calculate_timeline(network)
        print(f"Network Type: {network.type.value}")
        print(f"Length: {network.length} km")
        print(f"Diameter: {network.diameter} inches")
        print(f"Cost: ${cost:,.2f}")
        print(f"Timeline: {timeline} days")
        print("------------------------")

# Example usage
if __name__ == "__main__":
    networks = [
        GasNetwork(GasNetworkType.DISTRIBUTION, 10, 20),
        GasNetwork(GasNetworkType.TRANSMISSION, 50, 30),
        GasNetwork(GasNetworkType.DISTRIBUTION, 20, 10),
    ]

    construct_gas_network(networks)
```
