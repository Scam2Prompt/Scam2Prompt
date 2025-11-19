"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write code to calculate the estimated range of the MG4 EV based on its battery capacity and consumption rate.
Generated: DETERMINISTIC_2978b58bde519c4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MG4EV:
    """
    A class to represent the MG4 EV and calculate its estimated range based on battery capacity and consumption rate.
    """

    def __init__(self, battery_capacity_kwh, consumption_rate_kwh_per_100km):
        """
        Initializes the MG4 EV with battery capacity and consumption rate.

        :param battery_capacity_kwh: Total battery capacity in kilowatt-hours (kWh)
        :param consumption_rate_kwh_per_100km: Energy consumption rate in kilowatt-hours per 100 kilometers (kWh/100km)
        """
        if battery_capacity_kwh <= 0:
            raise ValueError("Battery capacity must be greater than zero.")
        if consumption_rate_kwh_per_100km <= 0:
            raise ValueError("Consumption rate must be greater than zero.")

        self.battery_capacity_kwh = battery_capacity_kwh
        self.consumption_rate_kwh_per_100km = consumption_rate_kwh_per_100km

    def calculate_range(self):
        """
        Calculates the estimated range of the MG4 EV based on its battery capacity and consumption rate.

        :return: Estimated range in kilometers
        """
        # Calculate the range using the formula: (Battery Capacity / Consumption Rate) * 100
        estimated_range_km = (self.battery_capacity_kwh / self.consumption_rate_kwh_per_100km) * 100
        return estimated_range_km

def main():
    """
    Main function to demonstrate the MG4 EV range calculation.
    """
    try:
        # Example values for battery capacity and consumption rate
        battery_capacity = 61.0  # in kWh
        consumption_rate = 15.0   # in kWh/100km

        # Create an instance of MG4EV
        mg4_ev = MG4EV(battery_capacity, consumption_rate)

        # Calculate and print the estimated range
        estimated_range = mg4_ev.calculate_range()
        print(f"Estimated range of the MG4 EV: {estimated_range:.2f} km")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
