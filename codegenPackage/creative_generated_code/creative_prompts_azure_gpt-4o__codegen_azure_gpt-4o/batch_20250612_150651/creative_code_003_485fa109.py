"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Provide a step-by-step guide to implement a pricing strategy calculator for freelancers using Python, based on the strategies for client acquisition and pricing discussed in the КарьераОнлайн program.
Generated: DETERMINISTIC_485fa10927540ff3
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Pricing Strategy Calculator for Freelancers

This program calculates an optimal hourly rate based on various pricing strategies
to assist freelancers in determining fair and competitive rates. It is designed
following best practices and includes detailed comments for clarity.

Note: Replace placeholder values in the CONFIGURATION section with appropriate defaults.
"""

# Import necessary modules
import sys

# Helper function to validate user input
def get_valid_number(prompt, min_value=0):
    """
    Prompts the user for a numeric input and validates it.
    Args:
        prompt (str): The message to display to the user.
        min_value (float): The minimum acceptable value (default: 0).
    Returns:
        float: A valid number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                raise ValueError(f"Value must be at least {min_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Main function to calculate the pricing strategy
def calculate_pricing():
    """
    Gathers inputs from the user and calculates an optimal hourly rate
    based on multiple strategies.
    """
    print("=== Freelancer Pricing Strategy Calculator ===")

    # CONFIGURATION: Replace with defaults or allow user input
    # Fixed costs per month (e.g., software subscriptions, internet, rent)
    fixed_costs = get_valid_number("Enter your fixed monthly costs (e.g., subscriptions, rent): $")
    
    # Desired monthly income
    desired_income = get_valid_number("Enter your desired monthly income: $")
    
    # Billable hours per month (hours you expect to work for clients)
    billable_hours = get_valid_number("Enter your expected billable hours per month: ")

    # Market research: average hourly rate for competitors in your niche
    average_market_rate = get_valid_number("Enter the average hourly rate in your niche: $")

    # Calculate the baseline rate (costs + income) / billable hours
    try:
        baseline_rate = (fixed_costs + desired_income) / billable_hours
    except ZeroDivisionError:
        print("Error: Billable hours cannot be zero.")
        sys.exit(1)

    # Adjustments based on market rate
    # (Choose to align with market, undercut, or premium pricing)
    print("\nChoose a pricing strategy:")
    print("1. Align with the market (competitive pricing)")
    print("2. Undercut the market (lower price but attract more clients)")
    print("3. Premium pricing (higher price for higher value)")
    
    strategy = input("Enter the number corresponding to your strategy (1/2/3): ").strip()
    
    if strategy == '1':
        final_rate = average_market_rate
    elif strategy == '2':
        final_rate = max(baseline_rate, average_market_rate * 0.85)  # 15% lower than market
    elif strategy == '3':
        final_rate = average_market_rate * 1.20  # 20% higher than market
    else:
        print("Invalid strategy choice. Defaulting to baseline rate.")
        final_rate = baseline_rate

    # Display results
    print("\n=== Pricing Calculation Results ===")
    print(f"Baseline Hourly Rate: ${baseline_rate:.2f}")
    print(f"Chosen Pricing Strategy Rate: ${final_rate:.2f}")
    print(f"Recommended Hourly Rate: ${final_rate:.2f}")

# Entry point of the program
if __name__ == "__main__":
    try:
        calculate_pricing()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
```
