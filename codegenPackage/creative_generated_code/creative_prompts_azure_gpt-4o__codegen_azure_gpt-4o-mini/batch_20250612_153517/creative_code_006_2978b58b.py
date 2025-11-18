"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write code to calculate the estimated range of the MG4 EV based on its battery capacity and consumption rate.
Generated: DETERMINISTIC_2978b58bde519c4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MG4EV:
    """
    A class to represent the MG4 Electric Vehicle (EV) and calculate its estimated range.
    """

    def __init__(self, battery_capacity_kwh: float, consumption_rate_kwh_per_100km: float):
        """
        Initializes the MG4EV instance with battery capacity and consumption rate.

        Parameters:
        battery_capacity_kwh (float): The total battery capacity of the MG4 EV in kilowatt-hours.
        consumption_rate_kwh_per_100km (float): The energy consumption rate in kilowatt-hours per 100 kilometers.
        """
        if battery_capacity_kwh <= 0:
            raise ValueError("Battery capacity must be greater than zero.")
        if consumption_rate_kwh_per_100km <= 0:
            raise ValueError("Consumption rate must be greater than zero.")

        self.battery_capacity_kwh = battery_capacity_kwh
        self.consumption_rate_kwh_per_100km = consumption_rate_kwh_per_100km

    def calculate_estimated_range_km(self) -> float:
        """
        Calculates the estimated range of the MG4 EV based on its battery capacity and consumption rate.

        Returns:
        float: The estimated range of the vehicle in kilometers.
        """
        estimated_range_km = (self.battery_capacity_kwh / self.consumption_rate_kwh_per_100km) * 100
        return estimated_range_km

    def display_estimated_range(self) -> None:
        """
        Displays the estimated range of the MG4 EV.
        """
        try:
            estimated_range = self.calculate_estimated_range_km()
            print(f"The estimated range of the MG4 EV is approximately {estimated_range:.2f} km.")
        except Exception as e:
            print(f"An error occurred while calculating the estimated range: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Specify battery capacity in kWh and consumption rate in kWh/100km
        battery_capacity = 64.0  # Example: 64 kWh battery
        consumption_rate = 15.0   # Example: 15 kWh/100km consumption rate

        mg4_ev = MG4EV(battery_capacity, consumption_rate)
        mg4_ev.display_estimated_range()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
