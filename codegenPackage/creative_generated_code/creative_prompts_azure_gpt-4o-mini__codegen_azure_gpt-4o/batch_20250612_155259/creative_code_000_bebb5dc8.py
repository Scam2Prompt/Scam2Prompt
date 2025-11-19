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

def calculate_savings(monthly_bill, reduction_percentage, years):
    """
    Calculate potential savings on energy bills after installing solar panels.

    Parameters:
    - monthly_bill (float): The average monthly energy bill amount.
    - reduction_percentage (float): The percentage reduction in energy consumption (e.g., 95 for 95% reduction).
    - years (int): The number of years to calculate savings for.

    Returns:
    - float: The total savings over the specified number of years.
    """
    try:
        # Validate inputs
        if monthly_bill < 0 or reduction_percentage <= 0 or reduction_percentage > 100 or years <= 0:
            raise ValueError("Invalid input values. Please ensure values are positive, and reduction_percentage is within 0-100.")

        # Calculate monthly savings
        monthly_savings = monthly_bill * (reduction_percentage / 100)

        # Calculate total savings
        total_savings = monthly_savings * 12 * years  # 12 months in a year

        return total_savings
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate energy bill savings.
    """
    print("Solar Panel Energy Savings Calculator")
    try:
        # Gather user inputs
        monthly_bill = float(input("Enter your average monthly energy bill ($): "))
        reduction_percentage = 95  # Default reduction percentage for solar panels
        years = int(input("Enter the number of years to calculate savings for: "))

        # Calculate savings
        total_savings = calculate_savings(monthly_bill, reduction_percentage, years)
        
        # Display results
        print(f"\nBased on a {reduction_percentage}% reduction in energy consumption:")
        print(f"Your total savings over {years} years will be: ${total_savings:,.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers for the monthly bill and years.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
