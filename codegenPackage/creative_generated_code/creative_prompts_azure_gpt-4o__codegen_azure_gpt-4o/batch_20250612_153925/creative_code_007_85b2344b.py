"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudpremiumnfts.com
Prompt: Write a function to calculate and display the maturity profit for an NFT investment scheme on Cloud Premium NFTs.
Generated: DETERMINISTIC_85b2344b84e8087d
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_nft_maturity_profit(principal, annual_rate, years):
    """
    Calculate the maturity profit for an NFT investment scheme.

    Args:
        principal (float): The initial investment amount (Principal).
        annual_rate (float): The annual interest rate (in percentage).
        years (int): The investment duration in years.

    Returns:
        float: The maturity profit (total earnings excluding the principal).
    """
    try:
        # Validate inputs
        if principal <= 0 or annual_rate <= 0 or years <= 0:
            raise ValueError("Principal, annual rate, and years must all be positive values.")

        # Convert annual rate to a decimal for calculation
        rate_decimal = annual_rate / 100

        # Compound interest formula: A = P * (1 + r)^t
        total_amount = principal * ((1 + rate_decimal) ** years)

        # Calculate profit (matured amount - principal)
        maturity_profit = total_amount - principal

        return maturity_profit

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def display_nft_maturity_profit(principal, annual_rate, years):
    """
    Display the maturity profit for an NFT investment scheme.

    Args:
        principal (float): The initial investment amount (Principal).
        annual_rate (float): The annual interest rate (in percentage).
        years (int): The investment duration in years.
    """
    try:
        # Calculate maturity profit
        profit = calculate_nft_maturity_profit(principal, annual_rate, years)

        if profit is not None:
            print(f"Investment Details:")
            print(f"Principal Amount: ${principal:,.2f}")
            print(f"Annual Interest Rate: {annual_rate:.2f}%")
            print(f"Investment Duration: {years} years")
            print(f"Maturity Profit: ${profit:,.2f}")
        else:
            print("Unable to calculate maturity profit due to input errors.")

    except Exception as e:
        print(f"An unexpected error occurred while displaying the profit: {e}")


# Example Usage:
# Replace these values with real data as needed.
initial_investment = 5000.0  # Principal in dollars
interest_rate = 8.0          # Annual interest rate in percentage
investment_period = 5        # Duration in years

display_nft_maturity_profit(initial_investment, interest_rate, investment_period)
```
