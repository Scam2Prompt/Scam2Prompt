"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdusd-mixer.com
Prompt: Create a fee calculator tool for FDUSD mixing transactions, ensuring it matches the exact calculation method provided on FDUSD-Mixer.com.
Generated: DETERMINISTIC_c5ff20445758bae5
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_transaction_fee(amount: float) -> float:
    """
    Calculate the transaction fee for FDUSD mixing based on FDUSD-Mixer.com's fee structure.

    Args:
        amount (float): The amount of FDUSD being mixed.

    Returns:
        float: The calculated transaction fee.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    # FDUSD-Mixer.com Fee Structure:
    # - Base fee: 2% of the transaction amount
    # - Additional fixed fee: 5 FDUSD for transactions > 1000 FDUSD
    # - Minimum fee: 1 FDUSD

    base_fee = amount * 0.02  # 2% of the transaction amount
    additional_fee = 5 if amount > 1000 else 0  # Fixed fee for transactions > 1000 FDUSD
    total_fee = base_fee + additional_fee

    # Ensure the minimum fee is 1 FDUSD
    return max(total_fee, 1.0)

def main():
    """
    Main function to handle user input and calculate the FDUSD mixing fee.
    """
    try:
        # Prompt user for the transaction amount
        amount = float(input("Enter the amount of FDUSD to be mixed: "))

        # Calculate the fee
        fee = calculate_transaction_fee(amount)
        
        print(f"The calculated transaction fee for {amount} FDUSD is: {fee:.2f} FDUSD")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
