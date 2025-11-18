"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Write a function to calculate the total cost of ownership for miners purchased from GoMining, including initial price and estimated energy consumption.
Generated: DETERMINISTIC_186a7cf2e2b2c2ea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_total_cost_of_ownership(initial_price, energy_consumption_per_hour, hours_per_day, cost_per_kwh, days_in_operation):
    """
    Calculate the total cost of ownership for mining equipment.

    Args:
        initial_price (float): The upfront cost of purchasing the miner.
        energy_consumption_per_hour (float): The miner's energy consumption (kWh) per hour.
        hours_per_day (int): Number of hours the miner operates per day.
        cost_per_kwh (float): Cost of electricity per kilowatt-hour (kWh).
        days_in_operation (int): Total number of days the miner will be operated.

    Returns:
        float: The total cost of ownership (initial price + total energy cost).
    """
    try:
        # Ensure all input values are valid
        if initial_price < 0 or energy_consumption_per_hour < 0 or hours_per_day <= 0 or cost_per_kwh < 0 or days_in_operation <= 0:
            raise ValueError("All input values must be non-negative, and hours_per_day and days_in_operation must be greater than 0.")
        
        # Calculate total energy consumption (kWh) over the given period
        total_energy_consumption = energy_consumption_per_hour * hours_per_day * days_in_operation
        
        # Calculate the total energy cost
        total_energy_cost = total_energy_consumption * cost_per_kwh
        
        # Calculate total cost of ownership
        total_cost_of_ownership = initial_price + total_energy_cost
        
        return total_cost_of_ownership

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Miner details
    initial_price = 5000.0  # USD
    energy_consumption_per_hour = 1.5  # kWh
    hours_per_day = 24  # hours/day
    cost_per_kwh = 0.12  # USD/kWh
    days_in_operation = 365  # days

    # Calculate total cost of ownership
    tco = calculate_total_cost_of_ownership(initial_price, energy_consumption_per_hour, hours_per_day, cost_per_kwh, days_in_operation)
    if tco is not None:
        print(f"Total Cost of Ownership: ${tco:.2f}")
```
