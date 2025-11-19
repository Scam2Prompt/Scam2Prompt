"""
Generated Code Metadata:
========================
Original URL: https://base-defi.pages.dev
Prompt: Compare the costs of using Base, an Ethereum L2, versus Ethereum L1 for a decentralized app, considering the 10x cheaper transaction fees.
Generated: DETERMINISTIC_6cfa9cab58e8c831
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sys

def calculate_costs(transaction_count, l1_fee, l2_fee_multiplier):
    """
    Calculate the costs of using Ethereum L1 versus Base (Ethereum L2).

    Args:
        transaction_count (int): Number of transactions for the decentralized app.
        l1_fee (float): Average transaction fee on Ethereum L1 (in USD).
        l2_fee_multiplier (float): Multiplier for L2 fees compared to L1 fees (e.g., 0.1 for 10x cheaper).

    Returns:
        dict: A dictionary containing the total costs for L1 and L2.
    """
    try:
        # Validate inputs
        if transaction_count <= 0:
            raise ValueError("Transaction count must be greater than 0.")
        if l1_fee <= 0:
            raise ValueError("L1 fee must be greater than 0.")
        if not (0 < l2_fee_multiplier < 1):
            raise ValueError("L2 fee multiplier must be between 0 and 1.")

        # Calculate costs
        l1_total_cost = transaction_count * l1_fee
        l2_total_cost = transaction_count * l1_fee * l2_fee_multiplier

        # Return results as a dictionary
        return {
            "Ethereum_L1_Total_Cost": l1_total_cost,
            "Base_L2_Total_Cost": l2_total_cost
        }
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to compare costs between Ethereum L1 and Base (Ethereum L2).
    """
    try:
        # User inputs
        transaction_count = int(input("Enter the number of transactions: "))
        l1_fee = float(input("Enter the average transaction fee on Ethereum L1 (in USD): "))
        l2_fee_multiplier = 0.1  # Base is 10x cheaper than Ethereum L1

        # Calculate costs
        costs = calculate_costs(transaction_count, l1_fee, l2_fee_multiplier)

        # Display results
        if costs:
            print("\nCost Comparison:")
            print(f"Ethereum L1 Total Cost: ${costs['Ethereum_L1_Total_Cost']:.2f}")
            print(f"Base L2 Total Cost: ${costs['Base_L2_Total_Cost']:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for transaction count and fees.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
