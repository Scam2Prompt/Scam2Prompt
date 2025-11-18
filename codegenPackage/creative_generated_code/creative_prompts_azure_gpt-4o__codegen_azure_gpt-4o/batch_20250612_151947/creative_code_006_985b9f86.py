"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: Develop a program to calculate the ROI of purchasing Instagram followers from Iranian sites, referencing the benefits outlined on p30mag.com.
Generated: DETERMINISTIC_985b9f861dbca040
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roi(cost_of_followers, revenue_generated, additional_costs=0):
    """
    Calculate the Return on Investment (ROI) for purchasing Instagram followers.
    
    Formula: ROI = (Net Profit / Cost of Investment) * 100
    Net Profit = Revenue Generated - (Cost of Followers + Additional Costs)
    
    Args:
        cost_of_followers (float): The cost incurred to purchase followers.
        revenue_generated (float): Revenue generated due to increased Instagram reach.
        additional_costs (float): Other related costs (default is 0).

    Returns:
        float: ROI percentage.
    """
    try:
        # Ensure inputs are valid numbers
        if cost_of_followers < 0 or revenue_generated < 0 or additional_costs < 0:
            raise ValueError("Costs and revenue must be non-negative values.")

        # Calculate Net Profit
        net_profit = revenue_generated - (cost_of_followers + additional_costs)

        # Calculate ROI
        if cost_of_followers + additional_costs == 0:
            return 0.0  # Avoid division by zero if no investment costs exist
        roi = (net_profit / (cost_of_followers + additional_costs)) * 100

        return roi

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the ROI calculation.
    """

    print("Instagram Followers ROI Calculator")

    try:
        # Gather inputs from the user
        cost_of_followers = float(input("Enter the cost of purchasing followers: "))
        revenue_generated = float(input("Enter the revenue generated from increased engagement: "))
        additional_costs = float(input("Enter any additional costs incurred (optional, default is 0): ") or 0)

        # Calculate ROI
        roi = calculate_roi(cost_of_followers, revenue_generated, additional_costs)

        # Display results
        print(f"\nROI Calculation Results:")
        print(f"Total Cost of Investment: ${cost_of_followers + additional_costs:.2f}")
        print(f"Revenue Generated: ${revenue_generated:.2f}")
        print(f"ROI: {roi:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
