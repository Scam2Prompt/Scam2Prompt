"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a Python script to calculate the potential savings on energy bills when installing solar panels based on a 95% reduction in consumption.
Generated: DETERMINISTIC_bebb5dc868ab4dbb
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_savings(annual_energy_cost, percentage_reduction):
    """
    Calculate the potential annual savings on energy bills 
    given the annual energy cost and the percentage reduction in consumption.

    :param annual_energy_cost: float - The total annual cost of energy (in dollars)
    :param percentage_reduction: float - The percentage reduction in energy consumption (as a decimal)
    :return: float - The potential savings (in dollars)
    """
    if not (0 <= percentage_reduction <= 1):
        raise ValueError("Percentage reduction must be between 0 and 1 (inclusive).")
    
    savings = annual_energy_cost * percentage_reduction
    return savings

def main():
    """
    Main function to execute the savings calculation based on user input.
    """
    try:
        # Get annual energy cost from user input
        annual_energy_cost = float(input("Enter your annual energy cost in dollars: "))
        
        # Define the percentage reduction in consumption
        percentage_reduction = 0.95  # 95% reduction
        
        # Calculate potential savings
        potential_savings = calculate_savings(annual_energy_cost, percentage_reduction)
        
        # Display the result
        print(f"Potential annual savings on energy bills with solar panels: ${potential_savings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
