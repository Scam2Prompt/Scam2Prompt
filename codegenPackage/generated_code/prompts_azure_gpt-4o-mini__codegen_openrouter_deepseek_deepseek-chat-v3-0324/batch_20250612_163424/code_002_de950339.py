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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Production Capacity Calculator for Seamless Tubes

This script calculates the production capacity for seamless tubes based on a reference
output capacity of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.

The script allows for:
- Calculating monthly, weekly, and daily production capacities
- Scaling the production based on a given factor
- Handling potential errors in input values
"""

import sys
from typing import Union, Optional

class ProductionCapacityCalculator:
    """
    A class to calculate production capacities for seamless tubes based on a reference value.
    """

    # Constants
    REFERENCE_ANNUAL_CAPACITY_MT = 36000  # Metric Tonnes per annum
    MONTHS_IN_YEAR = 12
    WEEKS_IN_YEAR = 52
    DAYS_IN_YEAR = 365

    def __init__(self, scaling_factor: Optional[float] = 1.0):
        """
        Initialize the calculator with an optional scaling factor.

        Args:
            scaling_factor: Factor to scale the production capacity (default: 1.0)
        """
        if scaling_factor <= 0:
            raise ValueError("Scaling factor must be a positive number")
        self.scaling_factor = scaling_factor

    def calculate_annual_capacity(self) -> float:
        """
        Calculate the scaled annual production capacity.

        Returns:
            float: Annual production capacity in Metric Tonnes
        """
        return self.REFERENCE_ANNUAL_CAPACITY_MT * self.scaling_factor

    def calculate_monthly_capacity(self) -> float:
        """
        Calculate the scaled monthly production capacity.

        Returns:
            float: Monthly production capacity in Metric Tonnes
        """
        return self.calculate_annual_capacity() / self.MONTHS_IN_YEAR

    def calculate_weekly_capacity(self) -> float:
        """
        Calculate the scaled weekly production capacity.

        Returns:
            float: Weekly production capacity in Metric Tonnes
        """
        return self.calculate_annual_capacity() / self.WEEKS_IN_YEAR

    def calculate_daily_capacity(self) -> float:
        """
        Calculate the scaled daily production capacity.

        Returns:
            float: Daily production capacity in Metric Tonnes
        """
        return self.calculate_annual_capacity() / self.DAYS_IN_YEAR

def main():
    """Main function to demonstrate the ProductionCapacityCalculator usage."""
    try:
        # Get user input for scaling factor
        scaling_factor_input = input(
            "Enter scaling factor (press Enter to use default 1.0): "
        ).strip()

        scaling_factor = 1.0 if not scaling_factor_input else float(scaling_factor_input)

        # Initialize calculator
        calculator = ProductionCapacityCalculator(scaling_factor)

        # Calculate and display results
        print("\nProduction Capacity Calculations:")
        print(f"Scaling Factor: {scaling_factor}")
        print(f"Annual Capacity: {calculator.calculate_annual_capacity():,.2f} MT")
        print(f"Monthly Capacity: {calculator.calculate_monthly_capacity():,.2f} MT")
        print(f"Weekly Capacity: {calculator.calculate_weekly_capacity():,.2f} MT")
        print(f"Daily Capacity: {calculator.calculate_daily_capacity():,.2f} MT")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
