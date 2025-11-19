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
class DumpsterRental:
    """
    A class to represent a dumpster rental service.
    """

    # Flat fees for different dumpster sizes
    FLAT_FEES = {
        10: 300,  # Fee for 10-yard dumpster
        15: 400,  # Fee for 15-yard dumpster
        20: 500   # Fee for 20-yard dumpster
    }

    def __init__(self, size):
        """
        Initializes the DumpsterRental with a specified size.

        :param size: The size of the dumpster (10, 15, or 20 yards)
        :raises ValueError: If the size is not one of the allowed values
        """
        if size not in self.FLAT_FEES:
            raise ValueError("Invalid dumpster size. Choose from 10, 15, or 20 yards.")
        self.size = size
        self.fee = self.FLAT_FEES[size]

    def generate_invoice(self):
        """
        Generates an invoice for the dumpster rental.

        :return: A string representing the invoice
        """
        invoice = (
            f"--- Dumpster Rental Invoice ---\n"
            f"Dumpster Size: {self.size} yards\n"
            f"Flat Fee: ${self.fee}\n"
            f"Total Amount Due: ${self.fee}\n"
            f"Thank you for choosing our service!"
        )
        return invoice


def main():
    """
    Main function to execute the dumpster rental process.
    """
    try:
        # Example size input; this could be replaced with user input
        size = 15  # Change this value to test different sizes
        rental = DumpsterRental(size)
        print(rental.generate_invoice())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
