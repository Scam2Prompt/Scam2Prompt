"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write a Python script that calculates the production capacity for seamless tubes, based on the output capacity of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.
Generated: DETERMINISTIC_de95033910d77f06
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# seamless_tube_capacity.py

class SeamlessTubeProduction:
    def __init__(self, annual_capacity_mton):
        """
        Initializes the production capacity calculator for seamless tubes.

        :param annual_capacity_mton: Annual output capacity in Metric Tonnes
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


if __name__ == "__main__":
    # Set the annual output capacity for Lal Baba Seamless Tubes Pvt. Ltd.
    annual_output_capacity = 36000  # in Metric Tonnes

    try:
        # Create an instance of the SeamlessTubeProduction class
        production = SeamlessTubeProduction(annual_output_capacity)
        
        # Display the production capacities
        production.display_capacity()
    except ValueError as e:
        print(f"Error: {e}")
```
