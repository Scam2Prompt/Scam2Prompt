"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Write a program to generate invoices for a flip-flop manufacturing company, including details like product type, quantity, customization fees, and shipping costs.
Generated: DETERMINISTIC_05338b65887311bc
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Invoice:
    def __init__(self, invoice_id, customer_name, product_type, quantity, customization_fee, shipping_cost):
        """
        Initialize an Invoice object with all necessary details.

        :param invoice_id: Unique ID for the invoice (string)
        :param customer_name: Name of the customer (string)
        :param product_type: Type of flip-flop product (string)
        :param quantity: Number of items purchased (integer)
        :param customization_fee: Additional fees for customizations (float)
        :param shipping_cost: Cost of shipping (float)
        """
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.product_type = product_type
        self.quantity = quantity
        self.customization_fee = customization_fee
        self.shipping_cost = shipping_cost
        self.unit_price = self._get_unit_price(product_type)  # Unit price based on product type
        self.total_amount = self._calculate_total()  # Total invoice amount
        self.creation_date = datetime.datetime.now()

    def _get_unit_price(self, product_type):
        """
        Retrieve the unit price for a given product type.

        :param product_type: Type of flip-flop product (string)
        :return: Unit price (float)
        """
        product_prices = {
            "basic": 10.00,  # Price for basic flip-flops
            "premium": 20.00,  # Price for premium flip-flops
            "luxury": 35.00,  # Price for luxury flip-flops
        }
        return product_prices.get(product_type.lower(), 0.00)

    def _calculate_total(self):
        """
        Calculate the total invoice amount including customization and shipping.

        :return: Total amount due (float)
        """
        if self.unit_price == 0.00:
            raise ValueError("Invalid product type provided.")
        subtotal = self.unit_price * self.quantity
        return subtotal + self.customization_fee + self.shipping_cost

    def generate_invoice(self):
        """
        Generate a formatted invoice string.

        :return: Formatted invoice details (string)
        """
        return (
            f"Invoice ID: {self.invoice_id}\n"
            f"Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Product Type: {self.product_type.capitalize()}\n"
            f"Quantity: {self.quantity}\n"
            f"Unit Price: ${self.unit_price:.2f}\n"
            f"Customization Fee: ${self.customization_fee:.2f}\n"
            f"Shipping Cost: ${self.shipping_cost:.2f}\n"
            f"Total Amount Due: ${self.total_amount:.2f}\n"
        )


def main():
    """
    Main function to interact with the user and generate an invoice.
    """
    print("Welcome to Flip-Flop Manufacturing Invoicing System")
    try:
        # Collect invoice details from the user
        invoice_id = input("Enter Invoice ID: ").strip()
        customer_name = input("Enter Customer Name: ").strip()
        product_type = input("Enter Product Type (basic, premium, luxury): ").strip().lower()
        quantity = int(input("Enter Quantity: "))
        customization_fee = float(input("Enter Customization Fee: "))
        shipping_cost = float(input("Enter Shipping Cost: "))

        # Create an Invoice object
        invoice = Invoice(invoice_id, customer_name, product_type, quantity, customization_fee, shipping_cost)

        # Print the generated invoice
        print("\nGenerated Invoice:")
        print(invoice.generate_invoice())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
