"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Using the Gree air conditioner specifications provided on the website, write Python code to calculate the total cost of ownership over 5 years, factoring in the initial purchase price and estimated annual energy consumption.
Generated: DETERMINISTIC_aecc02e1f6e4cec1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_total_cost(initial_price, annual_energy_consumption_kwh, energy_cost_per_kwh, years=5):
    """
    Calculate the total cost of ownership for a Gree air conditioner over a given period.

    Parameters:
        initial_price (float): The initial purchase price of the air conditioner in USD.
        annual_energy_consumption_kwh (float): Estimated annual energy consumption in kWh.
        energy_cost_per_kwh (float): Cost of energy per kWh in USD.
        years (int): The number of years to calculate the total cost of ownership. Default is 5 years.

    Returns:
        float: Total cost of ownership over the specified number of years.
    """
    try:
        # Validate inputs
        if initial_price < 0 or annual_energy_consumption_kwh < 0 or energy_cost_per_kwh < 0 or years <= 0:
            raise ValueError("All input values must be positive numbers, and years must be greater than zero.")

        # Calculate the total energy cost over the given years
        total_energy_cost = annual_energy_consumption_kwh * energy_cost_per_kwh * years

        # Calculate the total cost of ownership
        total_cost = initial_price + total_energy_cost

        return total_cost
    except Exception as e:
        print(f"Error calculating total cost: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Gather required inputs (replace these values with specifications from the website)
        initial_price = float(input("Enter the initial purchase price of the air conditioner (USD): "))
        annual_energy_consumption_kwh = float(input("Enter the estimated annual energy consumption (kWh): "))
        energy_cost_per_kwh = float(input("Enter the cost of energy per kWh (USD): "))
        years = int(input("Enter the number of years for the calculation (default is 5): ") or 5)

        # Calculate total cost of ownership
        total_cost = calculate_total_cost(initial_price, annual_energy_consumption_kwh, energy_cost_per_kwh, years)

        if total_cost is not None:
            print(f"The total cost of ownership over {years} years is: ${total_cost:.2f}")
        else:
            print("Could not calculate total cost due to an error.")
    except ValueError:
        print("Invalid input. Please enter numeric values for all inputs.")
```
