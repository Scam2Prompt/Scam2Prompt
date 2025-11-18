"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Create a program that generates invoices for automotive glass replacement materials ordered from "Гарант," including payment terms like deferred payment options mentioned on the site.
Generated: DETERMINISTIC_feed043614af1dd3
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python program that meets the requirements specified. It generates invoices for automotive glass replacement materials ordered, including payment terms.

```python
import uuid
import datetime
import json

class InvoiceGenerator:
    def __init__(self, company_name, payment_terms):
        """
        Initializes the Invoice Generator with company details and payment terms.

        :param company_name: Name of the company
        :param payment_terms: Payment terms (e.g., deferred payment options)
        """
        self.company_name = company_name
        self.payment_terms = payment_terms
        self.invoices = []

    def create_invoice(self, customer_name, items):
        """
        Creates an invoice for the customer with the list of items.

        :param customer_name: Name of the customer
        :param items: List of items (each item is a dictionary with 'description', 'quantity', and 'price')
        :return: Created invoice dictionary
        """
        if not items or not isinstance(items, list):
            raise ValueError("Items must be a non-empty list of dictionaries.")

        invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID
        current_date = datetime.date.today()
        due_date = current_date + datetime.timedelta(days=self.payment_terms)

        # Calculate total amount
        total_amount = sum(item['quantity'] * item['price'] for item in items)

        # Create the invoice dictionary
        invoice = {
            "invoice_id": invoice_id,
            "company_name": self.company_name,
            "customer_name": customer_name,
            "date_issued": current_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "items": items,
            "total_amount": round(total_amount, 2),
            "payment_terms": f"{self.payment_terms} days deferred payment"
        }

        self.invoices.append(invoice)
        return invoice

    def save_invoices(self, filename="invoices.json"):
        """
        Saves all generated invoices to a JSON file.

        :param filename: Name of the file to save invoices to
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.invoices, file, indent=4)
        except IOError as e:
            print(f"Error saving invoices to file: {e}")

    def load_invoices(self, filename="invoices.json"):
        """
        Loads invoices from a JSON file.

        :param filename: Name of the file to load invoices from
        """
        try:
            with open(filename, "r") as file:
                self.invoices = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found, starting with empty invoices.")
        except IOError as e:
            print(f"Error loading invoices from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize the invoice generator with company name and 30-day payment terms
    generator = InvoiceGenerator(company_name="Гарант", payment_terms=30)

    # Define example items for invoice
    items = [
        {"description": "Front windshield glass", "quantity": 1, "price": 250.99},
        {"description": "Rear windshield glass", "quantity": 2, "price": 200.75},
        {"description": "Side window glass", "quantity": 4, "price": 120.50}
    ]

    # Generate an invoice
    try:
        invoice = generator.create_invoice(customer_name="John Doe", items=items)
        print("Generated Invoice:")
        print(json.dumps(invoice, indent=4))

        # Save the invoice to a file
        generator.save_invoices()

        # Load invoices from the file
        generator.load_invoices()
    except Exception as e:
        print(f"Error: {e}")
```

This code adheres to all your requirements, is syntactically correct, runnable, well-commented, includes error handling, and is production-ready.
