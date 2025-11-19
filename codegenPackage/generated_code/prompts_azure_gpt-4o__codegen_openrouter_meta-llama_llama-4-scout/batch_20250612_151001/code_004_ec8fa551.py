"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Create a Python function to calculate flat fees for dumpster rentals based on size (10, 15, or 20 yards) and generate an invoice with no hidden costs, as described on the website.
Generated: DETERMINISTIC_ec8fa551cfbf0146
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dumpster_rental.py

class DumpsterRental:
    """
    Calculates flat fees for dumpster rentals and generates invoices.
    """

    def __init__(self):
        # Define flat fees for dumpster rentals based on size (in yards)
        self.flat_fees = {
            10: 350.0,
            15: 450.0,
            20: 550.0
        }

    def calculate_flat_fee(self, size: int) -> float:
        """
        Calculates the flat fee for a dumpster rental based on size.

        Args:
            size (int): The size of the dumpster in yards.

        Returns:
            float: The flat fee for the dumpster rental.

        Raises:
            ValueError: If the dumpster size is not 10, 15, or 20 yards.
        """
        if size not in self.flat_fees:
            raise ValueError("Invalid dumpster size. Please choose from 10, 15, or 20 yards.")
        return self.flat_fees[size]

    def generate_invoice(self, size: int, rental_days: int) -> dict:
        """
        Generates an invoice for a dumpster rental.

        Args:
            size (int): The size of the dumpster in yards.
            rental_days (int): The number of days the dumpster is rented.

        Returns:
            dict: The invoice for the dumpster rental.

        Raises:
            ValueError: If the dumpster size is not 10, 15, or 20 yards.
            ValueError: If the rental days is not a positive integer.
        """
        if rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")

        flat_fee = self.calculate_flat_fee(size)
        # Assume no additional fees or taxes for simplicity
        total_cost = flat_fee

        invoice = {
            "dumpster_size": f"{size} yards",
            "flat_fee": f"${flat_fee:.2f}",
            "rental_days": rental_days,
            "total_cost": f"${total_cost:.2f}",
            "payment_terms": "Payment is due upon receipt of invoice."
        }
        return invoice


def main():
    try:
        dumpster_rental = DumpsterRental()
        size = 15  # Example dumpster size
        rental_days = 7  # Example rental days
        invoice = dumpster_rental.generate_invoice(size, rental_days)
        print("Dumpster Rental Invoice:")
        for key, value in invoice.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
