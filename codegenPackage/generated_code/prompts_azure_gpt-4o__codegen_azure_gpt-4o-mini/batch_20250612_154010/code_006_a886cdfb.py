"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Provide a Python function to compare the specifications of various lithium portable power packs, such as the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI, based on Battery Australia's product details.
Generated: DETERMINISTIC_a886cdfbd7905c47
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class PowerPack:
    """
    A class to represent a lithium portable power pack.
    """

    def __init__(self, name: str, capacity: int, output_ports: int, weight: float, price: float):
        """
        Initializes a PowerPack instance.

        :param name: Name of the power pack
        :param capacity: Battery capacity in Wh
        :param output_ports: Number of output ports
        :param weight: Weight of the power pack in kg
        :param price: Price of the power pack in AUD
        """
        self.name = name
        self.capacity = capacity
        self.output_ports = output_ports
        self.weight = weight
        self.price = price

    def __str__(self) -> str:
        """
        Returns a string representation of the PowerPack instance.
        """
        return f"{self.name}: {self.capacity}Wh, {self.output_ports} ports, {self.weight}kg, ${self.price}"

def compare_power_packs(power_packs: List[PowerPack]) -> Dict[str, Any]:
    """
    Compares a list of PowerPack instances and returns the best option based on capacity and price.

    :param power_packs: List of PowerPack instances to compare
    :return: A dictionary containing the best power pack based on capacity-to-price ratio
    """
    if not power_packs:
        raise ValueError("The list of power packs cannot be empty.")

    best_pack = power_packs[0]
    best_ratio = best_pack.capacity / best_pack.price

    for pack in power_packs[1:]:
        current_ratio = pack.capacity / pack.price
        if current_ratio > best_ratio:
            best_ratio = current_ratio
            best_pack = pack

    return {
        "best_pack": str(best_pack),
        "capacity_to_price_ratio": best_ratio
    }

def load_power_packs_from_json(file_path: str) -> List[PowerPack]:
    """
    Loads power pack specifications from a JSON file.

    :param file_path: Path to the JSON file containing power pack specifications
    :return: A list of PowerPack instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [PowerPack(**item) for item in data]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Load power packs from a JSON file
        power_packs = load_power_packs_from_json('power_packs.json')
        
        # Compare the power packs and print the best option
        result = compare_power_packs(power_packs)
        print("Best Power Pack:", result["best_pack"])
        print("Capacity to Price Ratio:", result["capacity_to_price_ratio"])
    except Exception as e:
        print(f"An error occurred: {e}")
```
