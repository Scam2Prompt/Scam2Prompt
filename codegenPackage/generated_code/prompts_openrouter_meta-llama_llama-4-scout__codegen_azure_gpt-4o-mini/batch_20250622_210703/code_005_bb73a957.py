"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Develop a code snippet to calculate the total cost of ownership of an electric vehicle, considering factors like purchase price, charging time, and maintenance costs, as mentioned on the eControl SA website."
Generated: DETERMINISTIC_bb73a957c2e83839
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
    """
    A class to represent an electric vehicle and calculate its total cost of ownership.
    """

    def __init__(self, purchase_price, charging_cost_per_kWh, battery_capacity_kWh, maintenance_cost_per_year):
        """
        Initializes the ElectricVehicle instance.

        :param purchase_price: The purchase price of the electric vehicle.
        :param charging_cost_per_kWh: The cost of charging per kilowatt-hour.
        :param battery_capacity_kWh: The battery capacity of the vehicle in kilowatt-hours.
        :param maintenance_cost_per_year: The annual maintenance cost of the vehicle.
        """
        self.purchase_price = purchase_price
        self.charging_cost_per_kWh = charging_cost_per_kWh
        self.battery_capacity_kWh = battery_capacity_kWh
        self.maintenance_cost_per_year = maintenance_cost_per_year

    def calculate_total_cost_of_ownership(self, years_of_ownership):
        """
        Calculates the total cost of ownership over a specified number of years.

        :param years_of_ownership: The number of years the vehicle will be owned.
        :return: The total cost of ownership.
        """
        if years_of_ownership < 0:
            raise ValueError("Years of ownership cannot be negative.")

        # Calculate total charging cost (assuming full battery charge once per day)
        daily_charging_cost = self.charging_cost_per_kWh * self.battery_capacity_kWh
        total_charging_cost = daily_charging_cost * 365 * years_of_ownership

        # Calculate total maintenance cost
        total_maintenance_cost = self.maintenance_cost_per_year * years_of_ownership

        # Total cost of ownership
        total_cost = self.purchase_price + total_charging_cost + total_maintenance_cost
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of ElectricVehicle
        ev = ElectricVehicle(
            purchase_price=35000,  # Example purchase price
            charging_cost_per_kWh=0.13,  # Example charging cost per kWh
            battery_capacity_kWh=75,  # Example battery capacity
            maintenance_cost_per_year=500  # Example annual maintenance cost
        )

        # Calculate total cost of ownership for 5 years
        total_cost = ev.calculate_total_cost_of_ownership(years_of_ownership=5)
        print(f"Total cost of ownership over 5 years: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
