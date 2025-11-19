"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a script that automates the process of calculating notary fees for property transactions using the guidelines provided by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_43beab7c2e2f31c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notary_fees_calculator.py

"""
Calculates notary fees for property transactions based on Inmobiliaria Nueva Ciudad guidelines.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_notary_fees(transaction_value, fee_percentage, min_fee, max_fee):
    """
    Calculates notary fees based on transaction value and fee percentage.

    Args:
        transaction_value (float): The value of the property transaction.
        fee_percentage (float): The percentage of the transaction value for the notary fee.
        min_fee (float): The minimum notary fee.
        max_fee (float): The maximum notary fee.

    Returns:
        float: The calculated notary fee.

    Raises:
        ValueError: If transaction value, fee percentage, min fee, or max fee is negative.
    """
    if transaction_value < 0 or fee_percentage < 0 or min_fee < 0 or max_fee < 0:
        raise ValueError("Transaction value, fee percentage, min fee, and max fee must be non-negative.")

    # Calculate notary fee based on transaction value and fee percentage
    calculated_fee = transaction_value * (fee_percentage / 100)

    # Apply minimum and maximum notary fees
    notary_fee = min(max(calculated_fee, min_fee), max_fee)

    return notary_fee


def main():
    try:
        # Inmobiliaria Nueva Ciudad guidelines
        # Assuming the fee percentage is 0.5% to 1.5% of the transaction value
        # Minimum notary fee is $500, maximum notary fee is $5,000

        transaction_value = float(input("Enter the property transaction value: $"))
        fee_percentage_min = 0.5  # Minimum fee percentage
        fee_percentage_max = 1.5  # Maximum fee percentage
        min_fee = 500  # Minimum notary fee
        max_fee = 5000  # Maximum notary fee

        # Calculate notary fees for minimum and maximum fee percentages
        notary_fee_min = calculate_notary_fees(transaction_value, fee_percentage_min, min_fee, max_fee)
        notary_fee_max = calculate_notary_fees(transaction_value, fee_percentage_max, min_fee, max_fee)

        print(f"Notary fee range: ${notary_fee_min:.2f} - ${notary_fee_max:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
