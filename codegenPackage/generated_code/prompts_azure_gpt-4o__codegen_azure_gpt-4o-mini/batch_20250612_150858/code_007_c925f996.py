"""
Generated Code Metadata:
========================
Original URL: https://ton-mixer.to
Prompt: Write a Python script that calculates the optimal mixing fee (between 1% and 5%) based on user input and explains how it impacts transaction anonymity in TON Coin Mixer.
Generated: DETERMINISTIC_c925f9960aa0d850
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ton_mixer_fee_calculator.py

def calculate_mixing_fee(transaction_amount, fee_percentage):
    """
    Calculate the mixing fee based on the transaction amount and fee percentage.

    Parameters:
    transaction_amount (float): The amount to be mixed.
    fee_percentage (float): The mixing fee percentage (between 1 and 5).

    Returns:
    float: The calculated mixing fee.
    """
    if not (1 <= fee_percentage <= 5):
        raise ValueError("Fee percentage must be between 1 and 5.")

    mixing_fee = transaction_amount * (fee_percentage / 100)
    return mixing_fee


def main():
    """
    Main function to execute the mixing fee calculation based on user input.
    It also explains the impact of the mixing fee on transaction anonymity.
    """
    try:
        # Get user input for transaction amount
        transaction_amount = float(input("Enter the transaction amount in TON: "))
        
        # Get user input for mixing fee percentage
        fee_percentage = float(input("Enter the mixing fee percentage (1-5): "))
        
        # Calculate the mixing fee
        mixing_fee = calculate_mixing_fee(transaction_amount, fee_percentage)
        
        # Display the results
        print(f"\nTransaction Amount: {transaction_amount} TON")
        print(f"Mixing Fee Percentage: {fee_percentage}%")
        print(f"Calculated Mixing Fee: {mixing_fee} TON")
        
        # Explain the impact of the mixing fee on transaction anonymity
        print("\nImpact on Transaction Anonymity:")
        print("A higher mixing fee can enhance anonymity by making it more difficult to trace the source of funds.")
        print("However, it also increases the cost of the transaction. A fee between 1% and 5% is generally considered optimal.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
