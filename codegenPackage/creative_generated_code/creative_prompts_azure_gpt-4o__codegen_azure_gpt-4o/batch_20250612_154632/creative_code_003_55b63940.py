"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixers.money
Prompt: Generate code to calculate the commission fees (1-1.5% + 0.00035 BTC or 4-5% + 0.0007 BTC) for transactions processed through mixers.money, and display the total cost for a given Bitcoin amount.
Generated: DETERMINISTIC_55b63940d3192e5f
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_commission(bitcoin_amount, fee_percentage_range, fixed_fee_btc):
    """
    Calculate the total cost (commission fees) for a transaction.

    Parameters:
        bitcoin_amount (float): The amount of Bitcoin for the transaction.
        fee_percentage_range (tuple): A tuple containing the lower and upper bounds of the percentage fee range.
        fixed_fee_btc (float): The fixed fee in BTC added to the percentage-based fee.

    Returns:
        dict: A dictionary containing the minimum and maximum total costs.
    """
    try:
        # Ensure the inputs are valid
        if bitcoin_amount <= 0 or fixed_fee_btc < 0:
            raise ValueError("Bitcoin amount and fixed fee must be positive.")

        if not (0 <= fee_percentage_range[0] <= fee_percentage_range[1]):
            raise ValueError("Fee percentage range must be valid and in ascending order.")

        # Calculate minimum and maximum percentage-based fees
        min_percentage_fee = bitcoin_amount * (fee_percentage_range[0] / 100)
        max_percentage_fee = bitcoin_amount * (fee_percentage_range[1] / 100)

        # Add the fixed fee to the percentage-based fees
        min_total_cost = min_percentage_fee + fixed_fee_btc
        max_total_cost = max_percentage_fee + fixed_fee_btc

        return {
            "min_total_cost": min_total_cost,
            "max_total_cost": max_total_cost
        }
    except Exception as e:
        print(f"Error calculating commission fees: {e}", file=sys.stderr)
        return None


def main():
    """
    Main entry point for the script.

    Prompts the user for input and displays the calculation results.
    """
    try:
        # Prompt user for Bitcoin amount
        bitcoin_amount = float(input("Enter the Bitcoin amount for the transaction: "))

        # Fee configuration for mixers.money
        fee_options = [
            {"percentage_range": (1, 1.5), "fixed_fee": 0.00035},
            {"percentage_range": (4, 5), "fixed_fee": 0.0007}
        ]

        # Calculate and display the total costs for each fee configuration
        for i, fee_option in enumerate(fee_options, start=1):
            print(f"\nOption {i}:")
            results = calculate_commission(
                bitcoin_amount,
                fee_option["percentage_range"],
                fee_option["fixed_fee"]
            )
            if results:
                print(f"Minimum Total Cost: {results['min_total_cost']:.8f} BTC")
                print(f"Maximum Total Cost: {results['max_total_cost']:.8f} BTC")

    except ValueError:
        print("Invalid input. Please enter a valid number for the Bitcoin amount.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Run the script
    main()
```
