"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20en.pages.dev
Prompt: Provide code for a returns calculator that estimates the future value of DOGE20 tokens based on user input and token price projections, similar to the one on the Dogecoin20 website.
Generated: DETERMINISTIC_087b09fbf4e5b4fb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_future_value(initial_investment, token_price_now, token_price_future, years, annual_growth_rate=0):
    """
    Calculates the future value of DOGE20 tokens based on user input.

    Args:
        initial_investment (float): The amount invested in DOGE20 tokens.
        token_price_now (float): The current price of one DOGE20 token.
        token_price_future (float): The projected future price of one DOGE20 token.
        years (int): Number of years for the investment projection.
        annual_growth_rate (float): Optional annual growth rate in percentage (default is 0).

    Returns:
        float: Estimated future value of the investment.
    """
    try:
        # Calculate the number of tokens purchased based on the initial investment
        tokens_purchased = initial_investment / token_price_now

        # Adjust future token price based on annual growth rate if provided
        adjusted_future_price = token_price_future * ((1 + (annual_growth_rate / 100)) ** years)

        # Future investment value is the product of the tokens purchased and the adjusted future price
        future_value = tokens_purchased * adjusted_future_price

        return future_value
    except ZeroDivisionError:
        print("Error: Current token price cannot be zero.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def get_user_input():
    """
    Prompts the user for input and validates the data.

    Returns:
        dict: A dictionary containing the validated user inputs.
    """
    try:
        initial_investment = float(input("Enter your initial investment amount (in USD): ").strip())
        token_price_now = float(input("Enter the current price of one DOGE20 token (in USD): ").strip())
        token_price_future = float(input("Enter the projected future price of one DOGE20 token (in USD): ").strip())
        years = int(input("Enter the number of years for the investment projection: ").strip())
        annual_growth_rate = input("Enter the annual growth rate percentage (optional, default is 0): ").strip()

        # Handle optional annual growth rate input
        annual_growth_rate = float(annual_growth_rate) if annual_growth_rate else 0.0

        # Validate inputs
        if initial_investment <= 0 or token_price_now <= 0 or token_price_future <= 0 or years <= 0:
            print("Error: All numerical inputs must be positive and greater than zero.", file=sys.stderr)
            return None

        return {
            "initial_investment": initial_investment,
            "token_price_now": token_price_now,
            "token_price_future": token_price_future,
            "years": years,
            "annual_growth_rate": annual_growth_rate
        }
    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the returns calculator.
    """
    print("Welcome to the DOGE20 Returns Calculator!")
    user_inputs = get_user_input()

    if user_inputs:
        future_value = calculate_future_value(
            initial_investment=user_inputs["initial_investment"],
            token_price_now=user_inputs["token_price_now"],
            token_price_future=user_inputs["token_price_future"],
            years=user_inputs["years"],
            annual_growth_rate=user_inputs["annual_growth_rate"]
        )

        if future_value is not None:
            print(f"\nEstimated Future Value of Investment: ${future_value:,.2f}")
        else:
            print("Unable to calculate future value due to errors in input.")
    else:
        print("Exiting program due to invalid inputs.")

if __name__ == "__main__":
    main()
```
