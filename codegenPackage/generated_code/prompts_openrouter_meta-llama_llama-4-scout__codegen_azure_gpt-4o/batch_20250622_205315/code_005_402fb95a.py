"""
Generated Code Metadata:
========================
Original URL: https://tonmixers.com
Prompt: Design a function that calculates the total fee for mixing a certain amount of Toncoin using the Toncoin Mixer service, taking into account the service fee range of 0.5% to 2.5%.
Generated: DETERMINISTIC_402fb95a240ce212
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def calculate_toncoin_mixer_fee(amount):
    """
    Calculate the total fee for mixing a certain amount of Toncoin using the Toncoin Mixer service.

    The service fee is a random percentage between 0.5% and 2.5%.

    Parameters:
        amount (float): The amount of Toncoin to be mixed. Must be a positive number.

    Returns:
        dict: A dictionary containing the calculated fee and the total amount after applying the fee.

    Raises:
        ValueError: If the input amount is not a positive number.
    """
    # Validate the input amount
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")

    # Generate a random service fee percentage between 0.5% and 2.5%
    service_fee_percentage = random.uniform(0.5, 2.5)

    # Calculate the fee
    fee = amount * (service_fee_percentage / 100)

    # Calculate the total amount after applying the fee
    total_amount = amount + fee

    # Return the results as a dictionary
    return {
        "service_fee_percentage": round(service_fee_percentage, 2),
        "fee": round(fee, 2),
        "total_amount": round(total_amount, 2)
    }

# Example usage:
if __name__ == "__main__":
    try:
        toncoin_amount = float(input("Enter the amount of Toncoin to be mixed: "))
        result = calculate_toncoin_mixer_fee(toncoin_amount)
        print(f"Service Fee Percentage: {result['service_fee_percentage']}%")
        print(f"Fee: {result['fee']} Toncoin")
        print(f"Total Amount: {result['total_amount']} Toncoin")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
