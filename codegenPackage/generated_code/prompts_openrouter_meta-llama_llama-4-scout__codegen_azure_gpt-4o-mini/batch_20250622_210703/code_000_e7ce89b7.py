"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Generate a Python code snippet to calculate the cost of charging an electric vehicle, considering the mileage on a single charge and the price per kilowatt-hour, as discussed on the eControl SA website."
Generated: DETERMINISTIC_e7ce89b7d0dc2eee
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ElectricVehicle:
    def __init__(self, battery_capacity_kwh, efficiency_kwh_per_mile):
        """
        Initialize the ElectricVehicle instance.

        :param battery_capacity_kwh: Total battery capacity in kilowatt-hours (kWh)
        :param efficiency_kwh_per_mile: Energy consumption in kWh per mile
        """
        self.battery_capacity_kwh = battery_capacity_kwh
        self.efficiency_kwh_per_mile = efficiency_kwh_per_mile

    def calculate_range(self):
        """
        Calculate the maximum range of the vehicle on a full charge.

        :return: Maximum range in miles
        """
        return self.battery_capacity_kwh / self.efficiency_kwh_per_mile

    def calculate_charging_cost(self, price_per_kwh):
        """
        Calculate the cost to fully charge the vehicle.

        :param price_per_kwh: Price of electricity per kilowatt-hour
        :return: Cost to fully charge the vehicle
        """
        if price_per_kwh < 0:
            raise ValueError("Price per kWh must be a non-negative value.")
        
        return self.battery_capacity_kwh * price_per_kwh


def main():
    try:
        # Example parameters for the electric vehicle
        battery_capacity = 75  # in kWh
        efficiency = 0.3       # in kWh per mile
        price_per_kwh = 0.13   # in currency per kWh

        # Create an instance of ElectricVehicle
        ev = ElectricVehicle(battery_capacity, efficiency)

        # Calculate the maximum range
        max_range = ev.calculate_range()
        print(f"Maximum range on a full charge: {max_range:.2f} miles")

        # Calculate the charging cost
        charging_cost = ev.calculate_charging_cost(price_per_kwh)
        print(f"Cost to fully charge the vehicle: ${charging_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
