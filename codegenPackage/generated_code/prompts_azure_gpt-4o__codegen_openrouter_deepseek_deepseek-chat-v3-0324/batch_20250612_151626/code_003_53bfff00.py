"""
Generated Code Metadata:
========================
Original URL: https://tonmixers.com
Prompt: Create a script that calculates the service fee for mixing Toncoin, ranging between 0.5% and 1.986%, and applies it to a given transaction amount.
Generated: DETERMINISTIC_53bfff00e99a7181
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_service_fee(transaction_amount: float) -> float:
    """
    Calculate the service fee for mixing Toncoin.
    
    The fee is a random percentage between 0.5% and 1.986% of the transaction amount.
    
    Args:
        transaction_amount (float): The amount of Toncoin to be mixed.
        
    Returns:
        float: The calculated service fee in Toncoin.
        
    Raises:
        ValueError: If transaction_amount is negative.
    """
    import random
    
    if transaction_amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
    
    # Generate random fee percentage between 0.5% and 1.986%
    fee_percentage = random.uniform(0.5, 1.986)
    
    # Calculate fee amount
    fee_amount = transaction_amount * (fee_percentage / 100)
    
    return fee_amount


def main():
    """
    Main function to demonstrate the service fee calculation.
    """
    try:
        amount = float(input("Enter the transaction amount in Toncoin: "))
        fee = calculate_service_fee(amount)
        print(f"Service fee for {amount} Toncoin: {fee:.6f} Toncoin")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
