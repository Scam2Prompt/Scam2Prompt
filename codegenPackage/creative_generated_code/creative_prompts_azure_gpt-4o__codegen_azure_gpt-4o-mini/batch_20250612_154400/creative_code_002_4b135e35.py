"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Generate code to calculate the total puff capacity for a wholesale order of Elfworld vape devices, including PB45000 (45000 puffs), AI22000 (22000 puffs), and Big-B (100000 puffs).
Generated: DETERMINISTIC_4b135e3598a59f42
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VapeDevice:
    """
    A class to represent a vape device and its puff capacity.

    Attributes
    ----------
    name : str
        The name of the vape device.
    puff_capacity : int
        The total number of puffs the device can deliver.
    """

    def __init__(self, name: str, puff_capacity: int):
        """
        Initializes a new instance of VapeDevice.

        Parameters
        ----------
        name : str
            The name of the vape device.
        puff_capacity : int
            The total number of puffs the device can deliver.
        """
        self.name = name
        self.puff_capacity = puff_capacity

def calculate_total_puffs(devices: list) -> int:
    """
    Calculate the total puff capacity for a list of vape devices.

    Parameters
    ----------
    devices : list
        A list of VapeDevice instances.

    Returns
    -------
    int
        The total puff capacity.
    """
    total_puffs = 0
    for device in devices:
        if not isinstance(device, VapeDevice):
            raise ValueError("All items in the list must be instances of VapeDevice.")
        total_puffs += device.puff_capacity
    return total_puffs

def main():
    """
    Main function to execute the puff capacity calculation for wholesale orders.
    """
    # Create instances of VapeDevice for the wholesale order
    pb45000 = VapeDevice("PB45000", 45000)
    ai22000 = VapeDevice("AI22000", 22000)
    big_b = VapeDevice("Big-B", 100000)

    # List of devices in the wholesale order
    devices = [pb45000, ai22000, big_b]

    try:
        # Calculate the total puff capacity
        total_puffs = calculate_total_puffs(devices)
        print(f"Total puff capacity for wholesale order: {total_puffs} puffs")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
