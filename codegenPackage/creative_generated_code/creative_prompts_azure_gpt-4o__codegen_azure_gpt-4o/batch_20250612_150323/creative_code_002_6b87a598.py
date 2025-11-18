"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-mixer-tron.com
Prompt: Create a script that calculates the random commission (1% to 5%) applied by a USDT TRON mixer and adjusts the final transaction amount accordingly.
Generated: DETERMINISTIC_6b87a598e3392456
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_commission_and_adjust_amount(transaction_amount):
    """
    Calculates a random commission (1% to 5%) for a given transaction amount
    and adjusts the amount accordingly.

    Args:
        transaction_amount (float): The initial transaction amount in USDT.

    Returns:
        tuple: A tuple containing the commission percentage, commission amount,
               and the adjusted transaction amount.
    """
    try:
        # Validate that the input is a positive number
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Generate a random commission percentage between 1% and 5%
        commission_percentage = random.uniform(1, 5)

        # Calculate the commission amount
        commission_amount = (commission_percentage / 100) * transaction_amount

        # Calculate the adjusted transaction amount
        adjusted_amount = transaction_amount - commission_amount

        # Return the results as a tuple
        return round(commission_percentage, 2), round(commission_amount, 2), round(adjusted_amount, 2)

    except ValueError as ve:
        raise ve  # Reraise the error so it can be handled by the caller
    except Exception as ex:
        raise RuntimeError("An unexpected error occurred.") from ex


# Example usage of the function
if __name__ == "__main__":
    try:
        # Input: transaction amount
        transaction_amount = float(input("Enter the transaction amount in USDT: "))

        # Calculate the commission and adjusted amount
        commission_rate, commission_value, final_amount = calculate_commission_and_adjust_amount(transaction_amount)

        # Display the results
        print(f"Commission Rate: {commission_rate}%")
        print(f"Commission Amount: {commission_value} USDT")
        print(f"Final Transaction Amount: {final_amount} USDT")

    except ValueError as error:
        print(f"Input Error: {error}")
    except RuntimeError as error:
        print(f"Processing Error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
```
