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

def calculate_savings(monthly_bill, reduction_percentage=95):
    """
    Calculate potential savings on energy bills when installing solar panels.

    Args:
        monthly_bill (float): The current monthly energy bill in dollars.
        reduction_percentage (float): The percentage reduction in energy consumption (default is 95%).

    Returns:
        float: The estimated monthly savings in dollars.
    """
    try:
        # Validate inputs
        if monthly_bill < 0:
            raise ValueError("Monthly bill must be a positive number.")
        if not (0 <= reduction_percentage <= 100):
            raise ValueError("Reduction percentage must be between 0 and 100.")

        # Calculate savings
        savings = monthly_bill * (reduction_percentage / 100)
        return savings
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate savings.
    """
    try:
        # Prompt user for input
        monthly_bill = float(input("Enter your current monthly energy bill (in dollars): "))
        
        # Calculate savings
        savings = calculate_savings(monthly_bill)
        
        # Display results
        print(f"With a 95% reduction in energy consumption, your estimated monthly savings would be: ${savings:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the monthly bill.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
