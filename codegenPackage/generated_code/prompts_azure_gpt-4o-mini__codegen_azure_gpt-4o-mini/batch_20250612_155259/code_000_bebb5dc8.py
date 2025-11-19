"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a Python script to calculate the potential savings on energy bills when installing solar panels based on a 95% reduction in consumption.
Generated: DETERMINISTIC_bebb5dc868ab4dbb
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_savings(annual_energy_cost, reduction_percentage=95):
    """
    Calculate the potential savings on energy bills when installing solar panels.

    Parameters:
    annual_energy_cost (float): The current annual cost of energy.
    reduction_percentage (float): The percentage reduction in energy consumption. Default is 95%.

    Returns:
    float: The potential savings on energy bills.
    """
    if annual_energy_cost < 0:
        raise ValueError("Annual energy cost must be a non-negative value.")
    
    if not (0 <= reduction_percentage <= 100):
        raise ValueError("Reduction percentage must be between 0 and 100.")

    # Calculate the savings based on the reduction percentage
    savings = annual_energy_cost * (reduction_percentage / 100)
    return savings

def main():
    """
    Main function to execute the savings calculation based on user input.
    """
    try:
        # Get user input for annual energy cost
        annual_energy_cost = float(input("Enter your current annual energy cost ($): "))
        
        # Calculate potential savings
        savings = calculate_savings(annual_energy_cost)
        
        # Display the results
        print(f"Potential savings on energy bills with a {95}% reduction: ${savings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
