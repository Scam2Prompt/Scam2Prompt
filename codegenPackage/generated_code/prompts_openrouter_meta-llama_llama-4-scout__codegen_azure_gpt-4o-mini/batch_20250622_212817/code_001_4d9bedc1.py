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
class Appliance:
    """
    A class to represent an electrical appliance.

    Attributes:
    ----------
    name : str
        The name of the appliance.
    wattage : float
        The power consumption of the appliance in watts.
    hours_per_day : float
        The average number of hours the appliance is used per day.
    """

    def __init__(self, name: str, wattage: float, hours_per_day: float):
        """
        Initializes an Appliance instance.

        Parameters:
        ----------
        name : str
            The name of the appliance.
        wattage : float
            The power consumption of the appliance in watts.
        hours_per_day : float
            The average number of hours the appliance is used per day.
        """
        self.name = name
        self.wattage = wattage
        self.hours_per_day = hours_per_day

    def daily_energy_consumption(self) -> float:
        """
        Calculate the daily energy consumption of the appliance in kilowatt-hours (kWh).

        Returns:
        -------
        float
            The daily energy consumption in kWh.
        """
        return (self.wattage * self.hours_per_day) / 1000


class Household:
    """
    A class to represent a household with multiple appliances.

    Attributes:
    ----------
    appliances : list
        A list of Appliance instances in the household.
    """

    def __init__(self):
        """Initializes a Household instance with an empty list of appliances."""
        self.appliances = []

    def add_appliance(self, appliance: Appliance):
        """
        Add an appliance to the household.

        Parameters:
        ----------
        appliance : Appliance
            An instance of the Appliance class to be added.
        """
        self.appliances.append(appliance)

    def total_daily_energy_consumption(self) -> float:
        """
        Calculate the total daily energy consumption of the household in kWh.

        Returns:
        -------
        float
            The total daily energy consumption in kWh.
        """
        total_consumption = sum(appliance.daily_energy_consumption() for appliance in self.appliances)
        return total_consumption


def main():
    """Main function to demonstrate the energy consumption calculation."""
    # Create a household instance
    household = Household()

    # Example appliances
    try:
        household.add_appliance(Appliance("Refrigerator", 150, 24))
        household.add_appliance(Appliance("Washing Machine", 500, 1))
        household.add_appliance(Appliance("Television", 100, 5))
        
        # Calculate total energy consumption
        total_energy = household.total_daily_energy_consumption()
        print(f"Total daily energy consumption: {total_energy:.2f} kWh")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
