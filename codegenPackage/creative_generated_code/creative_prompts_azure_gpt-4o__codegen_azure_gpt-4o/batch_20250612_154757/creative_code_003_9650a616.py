"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refund-me.net
Prompt: Create a Python script to calculate fees for a fraud recovery service, including a 15% success fee plus VAT, based on the recovered amount.
Generated: DETERMINISTIC_9650a6168809f6f6
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
fraud_recovery_fee_calculator.py

This script calculates the total fees for a fraud recovery service, 
including a 15% success fee and VAT based on the recovered amount. 

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import required modules
import sys

# Constants
SUCCESS_FEE_RATE = 0.15  # 15% success fee
VAT_RATE = 0.20          # 20% VAT

def calculate_fees(recovered_amount):
    """
    Calculate the total fees for the fraud recovery service.

    Args:
        recovered_amount (float): The amount of money recovered.

    Returns:
        dict: A dictionary containing the breakdown of fees:
              - success_fee: The 15% success fee
              - vat: The VAT charged on the success fee
              - total_fee: The sum of success_fee and vat
    """
    if recovered_amount < 0:
        raise ValueError("Recovered amount cannot be negative.")

    # Calculate success fee
    success_fee = recovered_amount * SUCCESS_FEE_RATE

    # Calculate VAT on the success fee
    vat = success_fee * VAT_RATE

    # Calculate total fee
    total_fee = success_fee + vat
    
    return {
        "success_fee": round(success_fee, 2),
        "vat": round(vat, 2),
        "total_fee": round(total_fee, 2)
    }

def main():
    """
    Main function to execute the script.
    """
    try:
        # Prompt user for input
        recovered_amount = float(input("Enter the recovered amount (in your currency): "))
        
        # Perform fee calculation
        fees = calculate_fees(recovered_amount)

        # Display the results
        print("\n=== Fraud Recovery Service Fee Breakdown ===")
        print(f"Recovered Amount: {recovered_amount:.2f}")
        print(f"Success Fee (15%): {fees['success_fee']:.2f}")
        print(f"VAT (20%): {fees['vat']:.2f}")
        print(f"Total Fee: {fees['total_fee']:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
