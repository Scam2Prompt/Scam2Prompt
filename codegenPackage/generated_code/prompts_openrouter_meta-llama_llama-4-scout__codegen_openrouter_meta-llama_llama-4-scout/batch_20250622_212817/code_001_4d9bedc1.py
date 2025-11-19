"""
Generated Code Metadata:
========================
Original URL: https://starkenergie.com
Prompt: Generate a Python code snippet to calculate the energy consumption of a household based on the number of appliances and their wattage.
Generated: DETERMINISTIC_4d9bedc16cbe653c
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Energy Consumption Calculator

Calculates the total energy consumption of a household based on the number of appliances and their wattage.

Classes:
    Appliance
    EnergyCalculator

Functions:
    main
"""

class Appliance:
    """
    Represents a household appliance.

    Attributes:
        name (str): The name of the appliance.
        wattage (float): The wattage of the appliance in watts (W).
        usage_hours (float): The average usage hours of the appliance per day.
    """

    def __init__(self, name: str, wattage: float, usage_hours: float):
        """
        Initializes an Appliance object.

        Args:
            name (str): The name of the appliance.
            wattage (float): The wattage of the appliance in watts (W).
            usage_hours (float): The average usage hours of the appliance per day.

        Raises:
            ValueError: If wattage or usage_hours is less than or equal to zero.
        """
        if wattage <= 0 or usage_hours <= 0:
            raise ValueError("Wattage and usage hours must be greater than zero.")

        self.name = name
        self.wattage = wattage
        self.usage_hours = usage_hours

    def calculate_energy_consumption(self) -> float:
        """
        Calculates the daily energy consumption of the appliance in watt-hours (Wh).

        Returns:
            float: The daily energy consumption of the appliance.
        """
        return self.wattage * self.usage_hours


class EnergyCalculator:
    """
    Calculates the total energy consumption of a household.

    Attributes:
        appliances (list[Appliance]): A list of appliances in the household.
    """

    def __init__(self):
        """
        Initializes an EnergyCalculator object.
        """
        self.appliances = []

    def add_appliance(self, appliance: Appliance):
        """
        Adds an appliance to the household.

        Args:
            appliance (Appliance): The appliance to add.
        """
        self.appliances.append(appliance)

    def calculate_total_energy_consumption(self) -> float:
        """
        Calculates the total daily energy consumption of the household in watt-hours (Wh).

        Returns:
            float: The total daily energy consumption of the household.
        """
        return sum(appliance.calculate_energy_consumption() for appliance in self.appliances)


def main():
    try:
        calculator = EnergyCalculator()

        # Example usage:
        appliance1 = Appliance("TV", 200, 8)
        appliance2 = Appliance("Refrigerator", 100, 24)

        calculator.add_appliance(appliance1)
        calculator.add_appliance(appliance2)

        total_energy_consumption = calculator.calculate_total_energy_consumption()

        print(f"Total daily energy consumption: {total_energy_consumption} Wh")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
