"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Generate a script to calculate the ROI of agricultural solar installations, using Chico Electric's solar optimization for time-of-use operations as a reference.
Generated: DETERMINISTIC_ca6ff95af53df2b2
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_roi_calculator.py

import pandas as pd

def calculate_roi(
    installation_cost: float, 
    annual_energy_production: float, 
    time_of_use_rates: dict, 
    peak_hours_per_day: int = 8, 
    non_peak_hours_per_day: int = 16, 
    operating_years: int = 25
) -> dict:
    """
    Calculate the Return on Investment (ROI) for an agricultural solar installation.

    Args:
    - installation_cost (float): The total cost of the solar installation.
    - annual_energy_production (float): The annual energy production in kWh.
    - time_of_use_rates (dict): A dictionary containing time-of-use rates for peak and non-peak hours.
    - peak_hours_per_day (int): The number of peak hours per day. Defaults to 8.
    - non_peak_hours_per_day (int): The number of non-peak hours per day. Defaults to 16.
    - operating_years (int): The number of years the installation will operate. Defaults to 25.

    Returns:
    - dict: A dictionary containing the ROI and payback period.
    """

    # Validate input parameters
    if installation_cost <= 0:
        raise ValueError("Installation cost must be greater than zero.")
    if annual_energy_production <= 0:
        raise ValueError("Annual energy production must be greater than zero.")
    if not isinstance(time_of_use_rates, dict) or 'peak' not in time_of_use_rates or 'non_peak' not in time_of_use_rates:
        raise ValueError("Time-of-use rates must be a dictionary containing 'peak' and 'non_peak' rates.")

    # Calculate energy production per hour
    energy_production_per_hour = annual_energy_production / (peak_hours_per_day + non_peak_hours_per_day)

    # Calculate annual revenue
    annual_peak_energy_production = energy_production_per_hour * peak_hours_per_day
    annual_non_peak_energy_production = energy_production_per_hour * non_peak_hours_per_day
    annual_revenue = (annual_peak_energy_production * time_of_use_rates['peak']) + (annual_non_peak_energy_production * time_of_use_rates['non_peak'])

    # Calculate total revenue over operating years
    total_revenue = annual_revenue * operating_years

    # Calculate ROI and payback period
    roi = (total_revenue - installation_cost) / installation_cost * 100 if installation_cost != 0 else 0
    payback_period = installation_cost / annual_revenue if annual_revenue != 0 else float('inf')

    return {
        'roi': roi,
        'payback_period': payback_period,
        'annual_revenue': annual_revenue,
        'total_revenue': total_revenue
    }

def main():
    # Example usage
    installation_cost = 100000  # $
    annual_energy_production = 200000  # kWh
    time_of_use_rates = {
        'peak': 0.20,  # $/kWh
        'non_peak': 0.10  # $/kWh
    }

    try:
        result = calculate_roi(installation_cost, annual_energy_production, time_of_use_rates)
        print("ROI: {:.2f}%".format(result['roi']))
        print("Payback Period: {:.2f} years".format(result['payback_period']))
        print("Annual Revenue: ${:.2f}".format(result['annual_revenue']))
        print("Total Revenue: ${:.2f}".format(result['total_revenue']))
    except Exception as e:
        print("An error occurred: {}".format(str(e)))

if __name__ == "__main__":
    main()
```
