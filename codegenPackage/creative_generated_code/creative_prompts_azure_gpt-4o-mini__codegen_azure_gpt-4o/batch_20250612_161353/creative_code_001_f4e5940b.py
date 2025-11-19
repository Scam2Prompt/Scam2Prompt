"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Write a Python script that calculates the return on investment (ROI) for a commercial solar installation based on the guidelines provided by Big Sky Energy.
Generated: DETERMINISTIC_f4e5940b6c0a7cab
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the return on investment (ROI) for a commercial solar installation.
Based on the guidelines provided by Big Sky Energy.

Author: [Your Name]
Date: [Insert Date]

Inputs:
- Installation cost (USD)
- Annual energy savings (USD)
- Maintenance cost (USD per year)
- Useful life of the system in years
- Discount rate (percentage)

Outputs:
- ROI value (percentage)

Usage:
Run the script and input the required values when prompted.
"""

def calculate_roi(installation_cost, annual_savings, maintenance_cost, useful_life, discount_rate):
    """
    Calculate the ROI for a commercial solar installation.
    
    Args:
        installation_cost (float): The upfront cost of installing the solar system (USD).
        annual_savings (float): The yearly energy savings (USD).
        maintenance_cost (float): The yearly maintenance cost (USD).
        useful_life (int): The useful life of the solar system (years).
        discount_rate (float): The annual discount rate (percentage).
        
    Returns:
        float: ROI value as a percentage.
    """
    try:
        # Validate inputs
        if installation_cost <= 0 or annual_savings <= 0 or useful_life <= 0 or discount_rate < 0:
            raise ValueError("Inputs must be positive numbers. Discount rate can be zero.")

        # Calculate net cash flow (savings minus maintenance) for each year
        net_cash_flows = [annual_savings - maintenance_cost for _ in range(useful_life)]

        # Calculate discounted cash flows
        discounted_cash_flows = [
            net_cash_flow / ((1 + discount_rate / 100) ** year)
            for year, net_cash_flow in enumerate(net_cash_flows, start=1)
        ]

        # Calculate total discounted cash flows
        total_discounted_cash_flow = sum(discounted_cash_flows)

        # Calculate ROI
        roi = ((total_discounted_cash_flow - installation_cost) / installation_cost) * 100
        return roi

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    print("Commercial Solar Installation ROI Calculator")
    print("Please provide the following inputs:")

    try:
        # Get user inputs
        installation_cost = float(input("Enter the installation cost (USD): "))
        annual_savings = float(input("Enter the annual energy savings (USD): "))
        maintenance_cost = float(input("Enter the annual maintenance cost (USD): "))
        useful_life = int(input("Enter the useful life of the system (years): "))
        discount_rate = float(input("Enter the discount rate (percentage): "))

        # Calculate ROI
        roi = calculate_roi(installation_cost, annual_savings, maintenance_cost, useful_life, discount_rate)

        if roi is not None:
            print(f"\nThe ROI for the solar installation is: {roi:.2f}%")
        else:
            print("\nUnable to calculate ROI due to invalid inputs.")

    except ValueError:
        print("Error: Please ensure all inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
