"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Generate a program to calculate earnings in $ATH tokens based on mining performance metrics and device specifications provided by Aethir Edge.
Generated: DETERMINISTIC_a77c29b5cb0bbacf
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MiningDevice:
    """
    Represents a mining device with its specifications and performance metrics.

    Attributes:
        device_name (str): The name of the mining device.
        hash_rate (float): The hash rate of the device in MH/s.
        power_consumption (float): The power consumption of the device in watts.
        efficiency (float): The efficiency of the device in $ATH per MH/s.
    """

    def __init__(self, device_name: str, hash_rate: float, power_consumption: float, efficiency: float):
        self.device_name = device_name
        self.hash_rate = hash_rate  # in MH/s
        self.power_consumption = power_consumption  # in watts
        self.efficiency = efficiency  # in $ATH per MH/s

    def calculate_earnings(self, hours: float) -> float:
        """
        Calculate the earnings based on the hash rate and efficiency.

        Args:
            hours (float): The number of hours the device has been mining.

        Returns:
            float: The total earnings in $ATH.
        """
        if hours < 0:
            raise ValueError("Hours must be a non-negative value")
        earnings = self.hash_rate * self.efficiency * hours
        return earnings


def main():
    """
    Main function to run the earnings calculation program.
    """

    try:
        # Example mining device specifications
        device_name = "Aethir Miner X1"
        hash_rate = 150.0  # MH/s
        power_consumption = 1200.0  # watts
        efficiency = 0.05  # $ATH per MH/s

        # Create an instance of MiningDevice
        miner = MiningDevice(device_name, hash_rate, power_consumption, efficiency)

        # Input: Number of hours for mining
        hours = float(input("Enter the number of hours the device has been mining: "))

        # Calculate earnings
        earnings = miner.calculate_earnings(hours)
        print(f"Earnings from {hours} hours of mining with {miner.device_name}: ${earnings:.2f} $ATH")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
