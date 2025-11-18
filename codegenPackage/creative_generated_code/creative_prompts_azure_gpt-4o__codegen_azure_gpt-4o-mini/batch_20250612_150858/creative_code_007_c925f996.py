"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.to
Prompt: Write a Python script that calculates the optimal mixing fee (between 1% and 5%) based on user input and explains how it impacts transaction anonymity in TON Coin Mixer.
Generated: DETERMINISTIC_c925f9960aa0d850
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mixing_fee(transaction_amount, fee_percentage):
    """
    Calculate the mixing fee based on the transaction amount and the fee percentage.

    Args:
        transaction_amount (float): The total amount of the transaction.
        fee_percentage (float): The mixing fee percentage (between 1% and 5%).

    Returns:
        float: The calculated mixing fee.
    """
    if fee_percentage < 1 or fee_percentage > 5:
        raise ValueError("fee_percentage must be between 1 and 5.")
    
    mixing_fee = transaction_amount * (fee_percentage / 100)
    return mixing_fee

def main():
    """
    Main function to execute the mixing fee calculation.
    It takes user input for the transaction amount and fee percentage,
    calculates the mixing fee, and explains its impact on transaction anonymity.
    """
    try:
        # User input for transaction amount
        transaction_amount = float(input("Enter the transaction amount in TON: "))
        
        # User input for mixing fee percentage
        fee_percentage = float(input("Enter the mixing fee percentage (1% to 5%): "))
        
        # Calculate mixing fee
        mixing_fee = calculate_mixing_fee(transaction_amount, fee_percentage)
        
        # Display the results
        print(f"\nTransaction Amount: {transaction_amount} TON")
        print(f"Mixing Fee Percentage: {fee_percentage}%")
        print(f"Calculated Mixing Fee: {mixing_fee} TON")
        
        # Explain the impact on transaction anonymity
        print("\nImpact on Transaction Anonymity:")
        print("A higher mixing fee can improve anonymity by making it more difficult to trace the source of funds.")
        print("However, it's important to balance anonymity needs with transaction costs.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
