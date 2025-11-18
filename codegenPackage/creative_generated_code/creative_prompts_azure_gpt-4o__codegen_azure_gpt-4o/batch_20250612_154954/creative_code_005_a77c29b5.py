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
import sys

class MiningDevice:
    """
    Represents a mining device with specifications.
    """
    def __init__(self, device_name, hash_rate, power_consumption, uptime_hours):
        """
        Initialize the mining device.

        Args:
            device_name (str): Name of the mining device.
            hash_rate (float): Hash rate in MH/s (Mega-hashes per second).
            power_consumption (float): Power consumption in watts.
            uptime_hours (float): Uptime in hours.
        """
        self.device_name = device_name
        self.hash_rate = hash_rate
        self.power_consumption = power_consumption
        self.uptime_hours = uptime_hours


def calculate_earnings(device, ath_per_hash_rate, electricity_cost):
    """
    Calculate earnings in $ATH tokens based on mining performance metrics and cost.

    Args:
        device (MiningDevice): The mining device object.
        ath_per_hash_rate (float): Earnings in $ATH per MH/s of hash rate.
        electricity_cost (float): Cost of electricity per kWh in USD.

    Returns:
        dict: A dictionary containing gross earnings, electricity cost, and net earnings.
    """
    try:
        # Gross earnings calculation
        gross_earnings = device.hash_rate * device.uptime_hours * ath_per_hash_rate

        # Electricity cost calculation
        # Convert power consumption (watts) to kWh and multiply by uptime
        electricity_usage_kwh = (device.power_consumption / 1000) * device.uptime_hours
        electricity_expense = electricity_usage_kwh * electricity_cost

        # Net earnings calculation
        net_earnings = gross_earnings - electricity_expense

        # Return the results as a dictionary
        return {
            "device_name": device.device_name,
            "gross_earnings": round(gross_earnings, 2),
            "electricity_cost": round(electricity_expense, 2),
            "net_earnings": round(net_earnings, 2)
        }
    except Exception as e:
        print(f"Error while calculating earnings: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to drive the program.
    """
    try:
        # Example mining device specifications
        device = MiningDevice(
            device_name="Aethir Alpha Miner",
            hash_rate=50.0,          # MH/s
            power_consumption=200.0, # Watts
            uptime_hours=24.0        # Hours
        )

        # Example performance metrics
        ath_per_hash_rate = 0.0001    # Earnings per MH/s per hour in $ATH
        electricity_cost = 0.12       # Cost per kWh in USD

        # Calculate earnings
        earnings = calculate_earnings(device, ath_per_hash_rate, electricity_cost)

        # Output results
        if earnings:
            print(f"Earnings for {earnings['device_name']}:")
            print(f"  Gross Earnings: {earnings['gross_earnings']} $ATH")
            print(f"  Electricity Cost: {earnings['electricity_cost']} USD")
            print(f"  Net Earnings: {earnings['net_earnings']} $ATH")
        else:
            print("Failed to calculate earnings.")
    except Exception as e:
        print(f"Error in program: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
