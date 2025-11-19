"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: "Compare the features of Aethir Edge with other cryptocurrency mining devices, focusing on energy efficiency and computing capabilities."
Generated: DETERMINISTIC_bba540bd44ee30ae
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MiningDevice:
    """
    A class to represent a cryptocurrency mining device.
    """

    def __init__(self, name, energy_efficiency, computing_power):
        """
        Initialize the mining device with its name, energy efficiency, and computing power.

        :param name: str - Name of the mining device
        :param energy_efficiency: float - Energy efficiency in watts per hash (lower is better)
        :param computing_power: float - Computing power in hashes per second
        """
        self.name = name
        self.energy_efficiency = energy_efficiency
        self.computing_power = computing_power

    def to_dict(self):
        """
        Convert the mining device object to a dictionary.

        :return: dict - Dictionary representation of the mining device
        """
        return {
            "name": self.name,
            "energy_efficiency": self.energy_efficiency,
            "computing_power": self.computing_power
        }


def compare_devices(devices):
    """
    Compare a list of mining devices based on energy efficiency and computing power.

    :param devices: list - List of MiningDevice objects
    :return: dict - Comparison results
    """
    if not devices:
        raise ValueError("Device list cannot be empty.")

    # Sort devices by energy efficiency (ascending) and computing power (descending)
    sorted_by_efficiency = sorted(devices, key=lambda d: d.energy_efficiency)
    sorted_by_power = sorted(devices, key=lambda d: d.computing_power, reverse=True)

    return {
        "most_energy_efficient": sorted_by_efficiency[0].to_dict(),
        "highest_computing_power": sorted_by_power[0].to_dict()
    }


def main():
    """
    Main function to compare Aethir Edge with other cryptocurrency mining devices.
    """
    try:
        # Define mining devices
        devices = [
            MiningDevice("Aethir Edge", energy_efficiency=0.5, computing_power=1000),
            MiningDevice("Device X", energy_efficiency=0.7, computing_power=800),
            MiningDevice("Device Y", energy_efficiency=0.6, computing_power=1200),
            MiningDevice("Device Z", energy_efficiency=0.8, computing_power=900)
        ]

        # Compare devices
        comparison_results = compare_devices(devices)

        # Print results in JSON format for better readability
        print(json.dumps(comparison_results, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
