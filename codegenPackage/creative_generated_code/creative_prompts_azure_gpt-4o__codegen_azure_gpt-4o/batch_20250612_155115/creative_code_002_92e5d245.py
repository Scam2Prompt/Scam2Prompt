"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymixer.xyz
Prompt: Create a function that calculates service fees for mixing Bitcoin based on the fee range (1-2%) provided by Anonymixer. Include upfront fee display functionality before initiating transactions.
Generated: DETERMINISTIC_92e5d245fae72e99
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_service_fee(transaction_amount):
    """
    Calculate service fee for mixing Bitcoin based on the fee range provided by Anonymixer.
    
    Parameters:
    transaction_amount (float): The amount in Bitcoin to be mixed.
    
    Returns:
    dict: A dictionary containing the upfront fee range and the calculated service fee.
    """
    try:
        # Validate input
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Define fee range
        min_fee_percent = 1.0  # Minimum fee percentage
        max_fee_percent = 2.0  # Maximum fee percentage

        # Display upfront fee range
        upfront_fee_range = {
            "min_fee": round((transaction_amount * min_fee_percent) / 100, 8),
            "max_fee": round((transaction_amount * max_fee_percent) / 100, 8)
        }

        print("Upfront Fee Range:")
        print(f"Minimum Fee: {upfront_fee_range['min_fee']} BTC")
        print(f"Maximum Fee: {upfront_fee_range['max_fee']} BTC")

        # Randomly select a fee percentage within the range
        selected_fee_percent = random.uniform(min_fee_percent, max_fee_percent)

        # Calculate actual service fee
        service_fee = round((transaction_amount * selected_fee_percent) / 100, 8)

        return {
            "upfront_fee_range": upfront_fee_range,
            "selected_fee_percent": round(selected_fee_percent, 2),  # Selected fee percentage
            "service_fee": service_fee
        }
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        transaction_amount = float(input("Enter the transaction amount in BTC: "))
        result = calculate_service_fee(transaction_amount)
        
        if result:
            print("\nService Fee Details:")
            print(f"Selected Fee Percentage: {result['selected_fee_percent']}%")
            print(f"Calculated Service Fee: {result['service_fee']} BTC")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
