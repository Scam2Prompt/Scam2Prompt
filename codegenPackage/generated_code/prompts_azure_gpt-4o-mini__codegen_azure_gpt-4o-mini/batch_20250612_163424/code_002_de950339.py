"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write a Python script that calculates the production capacity for seamless tubes, based on the output capacity of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.
Generated: DETERMINISTIC_de95033910d77f06
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# seamless_tube_capacity.py

class SeamlessTubeProduction:
    """
    A class to calculate the production capacity of seamless tubes.
    """

    def __init__(self, annual_capacity_mton):
        """
        Initializes the production capacity with the given annual capacity.

        :param annual_capacity_mton: Annual production capacity in Metric Tonnes
        """
        if annual_capacity_mton <= 0:
            raise ValueError("Annual capacity must be a positive number.")
        self.annual_capacity_mton = annual_capacity_mton

    def calculate_monthly_capacity(self):
        """
        Calculates the monthly production capacity based on the annual capacity.

        :return: Monthly production capacity in Metric Tonnes
        """
        monthly_capacity = self.annual_capacity_mton / 12
        return monthly_capacity

    def calculate_daily_capacity(self):
        """
        Calculates the daily production capacity based on the annual capacity.

        :return: Daily production capacity in Metric Tonnes
        """
        daily_capacity = self.annual_capacity_mton / 365
        return daily_capacity

    def display_capacity(self):
        """
        Displays the annual, monthly, and daily production capacities.
        """
        print(f"Annual Production Capacity: {self.annual_capacity_mton} Metric Tonnes")
        print(f"Monthly Production Capacity: {self.calculate_monthly_capacity():.2f} Metric Tonnes")
        print(f"Daily Production Capacity: {self.calculate_daily_capacity():.2f} Metric Tonnes")


def main():
    """
    Main function to execute the production capacity calculations.
    """
    try:
        # Define the annual production capacity for Lal Baba Seamless Tubes Pvt. Ltd.
        annual_capacity = 36000  # Metric Tonnes per annum

        # Create an instance of SeamlessTubeProduction
        production = SeamlessTubeProduction(annual_capacity)

        # Display the production capacities
        production.display_capacity()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
