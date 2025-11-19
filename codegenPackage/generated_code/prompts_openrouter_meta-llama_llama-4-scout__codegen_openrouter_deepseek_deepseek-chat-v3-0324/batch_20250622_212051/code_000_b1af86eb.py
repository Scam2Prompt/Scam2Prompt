"""
Generated Code Metadata:
========================
Original URL: https://coindexe.fx-inc.us
Prompt: "Generate a Python script to calculate profit based on Coindexe FX investment plans, considering the Starter Plan with a $100-$900 investment and a 15% weekly return."
Generated: DETERMINISTIC_b1af86eb93ce572f
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Coindexe FX Investment Profit Calculator - Starter Plan

This script calculates the weekly and total profits for the Coindexe FX Starter Plan,
which offers a 15% weekly return on investments between $100 and $900.

Features:
- Validates investment amount against plan limits
- Calculates weekly profit
- Projects total profit over a specified duration
- Handles input errors gracefully
"""

def calculate_profit():
    """
    Main function to calculate and display investment profits.
    """
    print("Coindexe FX Investment Profit Calculator - Starter Plan")
    print("-----------------------------------------------------")
    print("Plan Details:")
    print("- Investment Range: $100 to $900")
    print("- Weekly Return: 15%")
    print("-----------------------------------------------------")

    try:
        # Get user input with validation
        while True:
            try:
                investment = float(input("Enter your investment amount ($100-$900): $"))
                if 100 <= investment <= 900:
                    break
                print("Error: Investment must be between $100 and $900.")
            except ValueError:
                print("Error: Please enter a valid number.")

        while True:
            try:
                weeks = int(input("Enter number of weeks to calculate: "))
                if weeks > 0:
                    break
                print("Error: Number of weeks must be positive.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        # Calculate and display results
        weekly_return_rate = 0.15
        weekly_profit = investment * weekly_return_rate
        total_profit = weekly_profit * weeks

        print("\nProfit Calculation Results:")
        print(f"Initial Investment: ${investment:,.2f}")
        print(f"Weekly Return Rate: {weekly_return_rate * 100}%")
        print(f"Weekly Profit: ${weekly_profit:,.2f}")
        print(f"Total Profit after {weeks} weeks: ${total_profit:,.2f}")
        print(f"Total Value after {weeks} weeks: ${investment + total_profit:,.2f}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    calculate_profit()
```
