"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Develop a code snippet for handling customer inquiries and generating quotes for automotive parts, including "essuie glace" and "produits d'entretiens," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_358baa08954cac34
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# automotive_inquiry_handler.py

class AutomotiveInquiry:
    def __init__(self, customer_name, part_name, quantity):
        """
        Initialize an AutomotiveInquiry object.

        Args:
            customer_name (str): Name of the customer.
            part_name (str): Name of the automotive part.
            quantity (int): Quantity of parts inquired about.
        """
        self.customer_name = customer_name
        self.part_name = part_name
        self.quantity = quantity

    def __str__(self):
        return f"Inquiry from {self.customer_name} for {self.quantity} {self.part_name}(s)"


class Quote:
    def __init__(self, inquiry, unit_price, discount=0):
        """
        Initialize a Quote object.

        Args:
            inquiry (AutomotiveInquiry): The inquiry this quote is for.
            unit_price (float): Unit price of the part.
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.inquiry = inquiry
        self.unit_price = unit_price
        self.discount = discount

    def calculate_total(self):
        """
        Calculate the total cost of the quote.

        Returns:
            float: Total cost.
        """
        discount_amount = self.unit_price * self.inquiry.quantity * (self.discount / 100)
        return self.unit_price * self.inquiry.quantity - discount_amount

    def __str__(self):
        return f"Quote for {self.inquiry.customer_name}: {self.inquiry.quantity} x {self.inquiry.part_name} = ${self.calculate_total():.2f}"


class AutomotiveInquiryHandler:
    def __init__(self):
        """
        Initialize an AutomotiveInquiryHandler object.

        Attributes:
            parts_prices (dict): Dictionary of part names and their unit prices.
        """
        self.parts_prices = {
            "essuie glace": 15.99,
            "produits d'entretiens": 7.99
        }

    def handle_inquiry(self, customer_name, part_name, quantity):
        """
        Handle a customer inquiry and generate a quote.

        Args:
            customer_name (str): Name of the customer.
            part_name (str): Name of the automotive part.
            quantity (int): Quantity of parts inquired about.

        Returns:
            Quote: A Quote object for the inquiry.

        Raises:
            ValueError: If the part name is not found.
        """
        if part_name not in self.parts_prices:
            raise ValueError(f"Part '{part_name}' not found.")

        inquiry = AutomotiveInquiry(customer_name, part_name, quantity)
        unit_price = self.parts_prices[part_name]
        quote = Quote(inquiry, unit_price)

        return quote

    def handle_inquiry_with_discount(self, customer_name, part_name, quantity, discount):
        """
        Handle a customer inquiry with a discount and generate a quote.

        Args:
            customer_name (str): Name of the customer.
            part_name (str): Name of the automotive part.
            quantity (int): Quantity of parts inquired about.
            discount (float): Discount percentage.

        Returns:
            Quote: A Quote object for the inquiry.

        Raises:
            ValueError: If the part name is not found.
        """
        if part_name not in self.parts_prices:
            raise ValueError(f"Part '{part_name}' not found.")

        inquiry = AutomotiveInquiry(customer_name, part_name, quantity)
        unit_price = self.parts_prices[part_name]
        quote = Quote(inquiry, unit_price, discount)

        return quote


def main():
    handler = AutomotiveInquiryHandler()

    try:
        quote1 = handler.handle_inquiry("John Doe", "essuie glace", 2)
        print(quote1)

        quote2 = handler.handle_inquiry_with_discount("Jane Doe", "produits d'entretiens", 3, 10)
        print(quote2)

        quote3 = handler.handle_inquiry("Bob Smith", "non-existent part", 1)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
