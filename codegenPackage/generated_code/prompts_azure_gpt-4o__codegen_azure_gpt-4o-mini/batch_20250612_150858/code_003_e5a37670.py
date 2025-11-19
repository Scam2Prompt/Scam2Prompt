"""
Generated Code Metadata:
========================
Original URL: https://eth-tumbler.to
Prompt: Develop a Python program that calculates the random commission (0.5% to 1%) charged by the ETH Tumbler service for a given Ether transaction amount.
Generated: DETERMINISTIC_e5a37670b3b230c2
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def calculate_commission(transaction_amount: float) -> float:
    """
    Calculate the random commission charged by the ETH Tumbler service.

    Parameters:
    transaction_amount (float): The amount of Ether for the transaction.

    Returns:
    float: The commission amount based on a random percentage between 0.5% and 1%.
    
    Raises:
    ValueError: If the transaction amount is negative or zero.
    """
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Generate a random commission percentage between 0.5% and 1%
    commission_percentage = random.uniform(0.005, 0.01)
    
    # Calculate the commission amount
    commission_amount = transaction_amount * commission_percentage
    
    return commission_amount

def main():
    """
    Main function to execute the commission calculation.
    """
    try:
        # Input: Get the transaction amount from the user
        transaction_amount = float(input("Enter the Ether transaction amount: "))
        
        # Calculate the commission
        commission = calculate_commission(transaction_amount)
        
        # Output: Display the commission amount
        print(f"The commission charged for a transaction of {transaction_amount} ETH is: {commission:.6f} ETH")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
