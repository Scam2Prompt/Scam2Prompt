"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Create a code snippet that calculates the amount of TONCOIN to send based on the fee structure provided by the TONCOIN Mixer.
Generated: DETERMINISTIC_f458ba227db71cbe
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# toncoin_mixer_calculator.py

def calculate_toncoin_to_send(amount_to_mix, fixed_fee, percent_fee):
    """
    Calculate the total TONCOIN amount to send based on the fee structure.

    Args:
        amount_to_mix (float): The amount of TONCOIN the user wants to mix.
        fixed_fee (float): The fixed fee charged by the TONCOIN Mixer (in TONCOIN).
        percent_fee (float): The percentage fee charged by the TONCOIN Mixer (as a decimal, e.g., 0.01 for 1%).

    Returns:
        float: The total TONCOIN amount to send.

    Raises:
        ValueError: If any input value is negative or invalid.
    """
    # Validate inputs
    if amount_to_mix < 0:
        raise ValueError("Amount to mix must be a non-negative value.")
    if fixed_fee < 0:
        raise ValueError("Fixed fee must be a non-negative value.")
    if percent_fee < 0 or percent_fee > 1:
        raise ValueError("Percent fee must be a decimal between 0 and 1.")

    # Calculate the percentage fee
    percentage_fee_amount = amount_to_mix * percent_fee

    # Calculate the total amount to send
    total_toncoin_to_send = amount_to_mix + fixed_fee + percentage_fee_amount

    return total_toncoin_to_send


if __name__ == "__main__":
    # Example usage
    try:
        # User-provided input data
        amount_to_mix = float(input("Enter the amount of TONCOIN to mix: "))
        fixed_fee = float(input("Enter the fixed fee (in TONCOIN): "))
        percent_fee = float(input("Enter the percent fee (as a decimal, e.g., 0.01): "))

        # Calculate the total TONCOIN to send
        total_to_send = calculate_toncoin_to_send(amount_to_mix, fixed_fee, percent_fee)

        print(f"Total TONCOIN to send: {total_to_send:.4f} TON")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
