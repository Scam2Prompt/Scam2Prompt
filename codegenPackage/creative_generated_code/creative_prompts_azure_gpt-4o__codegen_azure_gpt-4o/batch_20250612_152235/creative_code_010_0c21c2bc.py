"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Write a script to calculate gas fees savings when using Pepe Unchained Layer 2 compared to Ethereum Layer 1 for $PEPU token transactions.
Generated: DETERMINISTIC_0c21c2bc26707ad9
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_gas_fee_savings(layer1_fee, layer2_fee, num_transactions):
    """
    Calculate gas fee savings when using Layer 2 compared to Layer 1.

    Parameters:
        layer1_fee (float): Gas fee per transaction on Ethereum Layer 1.
        layer2_fee (float): Gas fee per transaction on Pepe Unchained Layer 2.
        num_transactions (int): Number of transactions to calculate savings for.

    Returns:
        float: Total gas fee savings.
    """
    try:
        # Ensure valid input
        if layer1_fee < 0 or layer2_fee < 0 or num_transactions <= 0:
            raise ValueError("Gas fees and number of transactions must be positive values.")

        # Calculate total fees for Layer 1 and Layer 2
        total_layer1_fee = layer1_fee * num_transactions
        total_layer2_fee = layer2_fee * num_transactions

        # Calculate savings
        savings = total_layer1_fee - total_layer2_fee
        return savings

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the gas fee savings calculator.
    """
    try:
        # Prompt user for inputs
        print("Welcome to $PEPU Gas Fee Savings Calculator!")
        layer1_fee = float(input("Enter Ethereum Layer 1 gas fee per transaction ($): "))
        layer2_fee = float(input("Enter Pepe Unchained Layer 2 gas fee per transaction ($): "))
        num_transactions = int(input("Enter the number of $PEPU token transactions: "))

        # Calculate savings
        savings = calculate_gas_fee_savings(layer1_fee, layer2_fee, num_transactions)

        # Display results
        print(f"\nTotal gas fee savings for {num_transactions} transactions:")
        print(f"Using Ethereum Layer 1: ${layer1_fee * num_transactions:.2f}")
        print(f"Using Pepe Unchained Layer 2: ${layer2_fee * num_transactions:.2f}")
        print(f"Savings: ${savings:.2f}")

    except ValueError:
        print("Invalid input. Please ensure gas fees are numbers and number of transactions is an integer.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Execute the program
    main()
```
