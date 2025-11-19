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
"""
Electric Vehicle Charging Cost Calculator

This module calculates the cost of charging an electric vehicle based on its mileage on a single charge and the price per kilowatt-hour.

Classes:
    ElectricVehicle

Functions:
    calculate_charging_cost
"""

class ElectricVehicle:
    """
    Represents an electric vehicle with its mileage on a single charge and battery capacity.

    Attributes:
        mileage_on_single_charge (float): The vehicle's mileage on a single charge in miles.
        battery_capacity (float): The vehicle's battery capacity in kilowatt-hours.
    """

    def __init__(self, mileage_on_single_charge, battery_capacity):
        """
        Initializes an ElectricVehicle object.

        Args:
            mileage_on_single_charge (float): The vehicle's mileage on a single charge in miles.
            battery_capacity (float): The vehicle's battery capacity in kilowatt-hours.

        Raises:
            ValueError: If mileage_on_single_charge or battery_capacity is not a positive number.
        """
        if mileage_on_single_charge <= 0:
            raise ValueError("Mileage on single charge must be a positive number.")
        if battery_capacity <= 0:
            raise ValueError("Battery capacity must be a positive number.")

        self.mileage_on_single_charge = mileage_on_single_charge
        self.battery_capacity = battery_capacity


def calculate_charging_cost(vehicle, price_per_kwh):
    """
    Calculates the cost of charging the electric vehicle.

    Args:
        vehicle (ElectricVehicle): The electric vehicle object.
        price_per_kwh (float): The price per kilowatt-hour.

    Returns:
        float: The cost of charging the vehicle.

    Raises:
        ValueError: If price_per_kwh is not a non-negative number.
    """
    if price_per_kwh < 0:
        raise ValueError("Price per kilowatt-hour must be a non-negative number.")

    # Calculate the cost of charging the vehicle
    charging_cost = vehicle.battery_capacity * price_per_kwh

    return charging_cost


def calculate_cost_per_mile(vehicle, price_per_kwh):
    """
    Calculates the cost of charging the electric vehicle per mile.

    Args:
        vehicle (ElectricVehicle): The electric vehicle object.
        price_per_kwh (float): The price per kilowatt-hour.

    Returns:
        float: The cost of charging the vehicle per mile.
    """
    charging_cost = calculate_charging_cost(vehicle, price_per_kwh)
    cost_per_mile = charging_cost / vehicle.mileage_on_single_charge

    return cost_per_mile


def main():
    try:
        # Example usage
        vehicle = ElectricVehicle(mileage_on_single_charge=250, battery_capacity=60)
        price_per_kwh = 0.15

        charging_cost = calculate_charging_cost(vehicle, price_per_kwh)
        cost_per_mile = calculate_cost_per_mile(vehicle, price_per_kwh)

        print(f"Charging Cost: ${charging_cost:.2f}")
        print(f"Cost per Mile: ${cost_per_mile:.4f}/mile")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
