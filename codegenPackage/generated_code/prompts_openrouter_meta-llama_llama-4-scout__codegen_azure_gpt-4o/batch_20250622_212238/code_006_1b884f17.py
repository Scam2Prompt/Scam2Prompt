"""
Generated Code Metadata:
========================
Original URL: https://bitcoinpepe-en.xyz
Prompt: Create a basic Python script for calculating potential returns on investment (ROI) for $BPEP tokens based on the presale stage and proposed price increases.
Generated: DETERMINISTIC_1b884f17e6bddbac
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate potential returns on investment (ROI) for $BPEP tokens.
This script assumes the token price increases at each presale stage.
"""

# Import necessary modules
import sys

def calculate_roi(initial_investment, token_price_start, token_price_end):
    """
    Calculate the potential ROI based on initial investment and token price changes.

    Parameters:
        initial_investment (float): The amount of money invested in the presale.
        token_price_start (float): The price of the token at the start of the presale stage.
        token_price_end (float): The price of the token at the end of the presale stage.

    Returns:
        float: The potential ROI percentage.
    """
    try:
        # Calculate the number of tokens purchased
        tokens_purchased = initial_investment / token_price_start

        # Calculate the value of tokens at the end price
        final_value = tokens_purchased * token_price_end

        # Calculate ROI percentage
        roi_percentage = ((final_value - initial_investment) / initial_investment) * 100

        return roi_percentage
    except ZeroDivisionError:
        print("Error: Token price at the start of the presale stage cannot be zero.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the ROI calculation.
    """
    print("Welcome to the $BPEP Token ROI Calculator!")

    try:
        # Get user input for investment details
        initial_investment = float(input("Enter your initial investment amount (in USD): "))
        token_price_start = float(input("Enter the token price at the start of the presale stage (in USD): "))
        token_price_end = float(input("Enter the token price at the end of the presale stage (in USD): "))

        # Validate inputs
        if initial_investment <= 0 or token_price_start <= 0 or token_price_end <= 0:
            print("Error: All input values must be positive numbers.")
            sys.exit(1)

        # Calculate ROI
        roi = calculate_roi(initial_investment, token_price_start, token_price_end)

        # Display the result
        print(f"Your potential ROI is: {roi:.2f}%")
    except ValueError:
        print("Error: Please enter valid numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
