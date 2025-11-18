"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonmixers.com
Prompt: Create a script that calculates the service fee for mixing Toncoin, ranging between 0.5% and 1.986%, and applies it to a given transaction amount.
Generated: DETERMINISTIC_53bfff00e99a7181
Batch ID: 20250612_151626
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
    Calculate the service fee for mixing Toncoin based on a random percentage
    between 0.5% and 1.986%.

    Args:
        transaction_amount (float): The amount of Toncoin involved in the transaction.

    Returns:
        float: The calculated service fee.
    """
    try:
        # Check if the transaction amount is valid
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Generate a random service fee percentage between 0.5% and 1.986%
        fee_percentage = random.uniform(0.5, 1.986)

        # Calculate the service fee
        service_fee = (fee_percentage / 100) * transaction_amount

        return round(service_fee, 6)  # Round to 6 decimal places for precision

    except Exception as e:
        # Log or handle the error appropriately
        raise RuntimeError(f"An error occurred while calculating the service fee: {e}")


def main():
    """
    Main function to demonstrate the service fee calculation.
    """
    try:
        # Example transaction amount (Replace with dynamic input if needed)
        transaction_amount = float(input("Enter the transaction amount in Toncoin: "))

        # Calculate the service fee
        service_fee = calculate_service_fee(transaction_amount)

        # Display the results
        print(f"Transaction Amount: {transaction_amount} Toncoin")
        print(f"Service Fee: {service_fee} Toncoin")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input error: {ve}")
    except RuntimeError as re:
        # Handle runtime errors
        print(re)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
