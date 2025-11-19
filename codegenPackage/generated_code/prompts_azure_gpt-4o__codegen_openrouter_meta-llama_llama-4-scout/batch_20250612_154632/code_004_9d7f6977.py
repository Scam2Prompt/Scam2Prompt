"""
Generated Code Metadata:
========================
Original URL: https://bitcoinmixer.cx
Prompt: Write a program that calculates the service fee for a Bitcoin mixer transaction based on the percentage model described on bitcoinmixer.cx, and outputs the amount of Bitcoin to be received after mixing.
Generated: DETERMINISTIC_9d7f697727e935b8
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bitcoin Mixer Service Fee Calculator

Calculates the service fee for a Bitcoin mixer transaction based on the percentage model.
"""

def calculate_service_fee(amount: float, percentage: float = 0.015) -> float:
    """
    Calculates the service fee for a Bitcoin mixer transaction.

    Args:
    - amount (float): The amount of Bitcoin to be mixed.
    - percentage (float, optional): The service fee percentage. Defaults to 0.015 (1.5%).

    Returns:
    - float: The service fee amount.
    """
    if amount <= 0:
        raise ValueError("Invalid amount. Amount must be greater than zero.")

    if percentage < 0 or percentage > 1:
        raise ValueError("Invalid percentage. Percentage must be between 0 and 1.")

    service_fee = amount * percentage
    return service_fee


def calculate_output_amount(amount: float, service_fee: float) -> float:
    """
    Calculates the amount of Bitcoin to be received after mixing.

    Args:
    - amount (float): The amount of Bitcoin to be mixed.
    - service_fee (float): The service fee amount.

    Returns:
    - float: The amount of Bitcoin to be received after mixing.
    """
    output_amount = amount - service_fee
    return output_amount


def main():
    try:
        # Input amount
        amount = float(input("Enter the amount of Bitcoin to be mixed: "))

        # Calculate service fee
        service_fee_percentage = 0.015  # 1.5% service fee
        service_fee = calculate_service_fee(amount, service_fee_percentage)

        # Calculate output amount
        output_amount = calculate_output_amount(amount, service_fee)

        # Print results
        print(f"Service fee: {service_fee:.8f} BTC ({service_fee_percentage*100:.2f}%)")
        print(f"Amount to be received after mixing: {output_amount:.8f} BTC")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
