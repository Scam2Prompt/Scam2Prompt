"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Write Python code to simulate an investment plan with a 50% daily yield for 5 days, as described in the "Basic Plan" on New World Trade's website.
Generated: DETERMINISTIC_c9d2802099d468a2
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def simulate_investment(initial_investment, daily_yield, days):
    """
    Simulates an investment plan with daily yield over a specified number of days.

    Parameters:
    initial_investment (float): The initial amount invested.
    daily_yield (float): The daily yield as a percentage (e.g., 50 for 50%).
    days (int): The number of days to simulate.

    Returns:
    list: A list containing the investment value for each day.
    """
    try:
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= daily_yield <= 100):
            raise ValueError("Daily yield must be between 0 and 100 (inclusive).")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Calculate daily investment growth
        investment_values = []
        current_investment = initial_investment

        for day in range(1, days + 1):
            current_investment += (current_investment * daily_yield / 100)
            investment_values.append(round(current_investment, 2))  # Round to 2 decimal places

        return investment_values
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return []


def main():
    """
    Main entry point of the program to simulate the investment plan.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter the initial investment amount: "))
        daily_yield = 50  # Fixed daily yield for this "Basic Plan"
        days = 5  # Fixed number of days for the simulation

        # Run investment simulation
        results = simulate_investment(initial_investment, daily_yield, days)

        # Check if simulation returned results
        if results:
            print("\nInvestment Growth Over 5 Days:")
            for day, value in enumerate(results, start=1):
                print(f"Day {day}: ${value}")
        else:
            print("Investment simulation failed due to invalid input or runtime error.")
    except Exception as e:
        print(f"Unexpected error in main: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
