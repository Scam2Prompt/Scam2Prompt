"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Write a program to calculate the total USDT received after applying the platform's exchange rate and discount policies for both QR code and bank account transactions.
Generated: DETERMINISTIC_39849de3a7898fe1
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_usdt(amount, exchange_rate, discount_rate):
    """
    Calculate the total USDT received after applying the exchange rate and discount.

    :param amount: The amount in fiat currency (e.g., USD)
    :param exchange_rate: The platform's current exchange rate for converting fiat to USDT
    :param discount_rate: Discount rate (as a percentage) applied to the transaction
    :return: The total USDT received after applying exchange rate and discount
    """
    try:
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be greater than zero.")
        if not (0 <= discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")

        # Apply the exchange rate
        usdt_before_discount = amount / exchange_rate

        # Apply the discount
        discount_amount = usdt_before_discount * (discount_rate / 100)
        total_usdt = usdt_before_discount - discount_amount

        return round(total_usdt, 6)  # Round to 6 decimal places for precision
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to handle user input and calculate USDT for QR code and bank account transactions.
    """
    try:
        print("USDT Transaction Calculator")

        # Input parameters for QR code transaction
        print("\nQR Code Transaction:")
        qr_amount = float(input("Enter the amount in fiat currency (e.g., USD): "))
        qr_exchange_rate = float(input("Enter the exchange rate (fiat to USDT): "))
        qr_discount_rate = float(input("Enter the discount rate (percentage): "))

        # Calculate total USDT for QR code transaction
        qr_total_usdt = calculate_total_usdt(qr_amount, qr_exchange_rate, qr_discount_rate)
        if qr_total_usdt is not None:
            print(f"Total USDT received for QR code transaction: {qr_total_usdt}")

        # Input parameters for bank account transaction
        print("\nBank Account Transaction:")
        bank_amount = float(input("Enter the amount in fiat currency (e.g., USD): "))
        bank_exchange_rate = float(input("Enter the exchange rate (fiat to USDT): "))
        bank_discount_rate = float(input("Enter the discount rate (percentage): "))

        # Calculate total USDT for bank account transaction
        bank_total_usdt = calculate_total_usdt(bank_amount, bank_exchange_rate, bank_discount_rate)
        if bank_total_usdt is not None:
            print(f"Total USDT received for bank account transaction: {bank_total_usdt}")

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
