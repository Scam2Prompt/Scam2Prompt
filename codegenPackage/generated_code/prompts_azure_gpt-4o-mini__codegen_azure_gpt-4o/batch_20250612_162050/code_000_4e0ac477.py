"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import json
import uuid

# Constants
INVOICE_DIRECTORY = "invoices"
COMPANY_NAME = "CGBókhald Bookkeeping Services"
COMPANY_ADDRESS = "123 Finance Street, Reykjavik, Iceland"
COMPANY_EMAIL = "contact@cgbokhald.is"
COMPANY_PHONE = "+354-123-4567"

# Ensure the invoice directory exists
if not os.path.exists(INVOICE_DIRECTORY):
    os.makedirs(INVOICE_DIRECTORY)

def generate_invoice(customer_name, customer_email, items, due_date=None):
    """
    Generate an invoice for a customer.

    Args:
        customer_name (str): Name of the customer.
        customer_email (str): Email of the customer.
        items (list of dict): List of items with 'description', 'quantity', and 'price'.
        due_date (str, optional): Due date for the invoice in YYYY-MM-DD format. Defaults to 30 days from today.

    Returns:
        str: Path to the generated invoice file.
    """
    try:
        # Validate inputs
        if not customer_name or not customer_email or not items:
            raise ValueError("Customer name, email, and items are required.")

        if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
            raise ValueError("Items must be a list of dictionaries.")

        # Calculate totals
        subtotal = sum(item['quantity'] * item['price'] for item in items)
        tax_rate = 0.25  # 25% VAT
        tax = subtotal * tax_rate
        total = subtotal + tax

        # Generate invoice details
        invoice_id = str(uuid.uuid4())
        issue_date = datetime.date.today().strftime("%Y-%m-%d")
        due_date = due_date or (datetime.date.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

        invoice_data = {
            "invoice_id": invoice_id,
            "issue_date": issue_date,
            "due_date": due_date,
            "company_details": {
                "name": COMPANY_NAME,
                "address": COMPANY_ADDRESS,
                "email": COMPANY_EMAIL,
                "phone": COMPANY_PHONE
            },
            "customer_details": {
                "name": customer_name,
                "email": customer_email
            },
            "items": items,
            "subtotal": subtotal,
            "tax": tax,
            "total": total
        }

        # Save invoice to file
        invoice_filename = f"{INVOICE_DIRECTORY}/invoice_{invoice_id}.json"
        with open(invoice_filename, "w") as invoice_file:
            json.dump(invoice_data, invoice_file, indent=4)

        return invoice_filename

    except Exception as e:
        print(f"Error generating invoice: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample data
    customer_name = "John Doe"
    customer_email = "john.doe@example.com"
    items = [
        {"description": "Bookkeeping Service - January", "quantity": 1, "price": 100.0},
        {"description": "Tax Consultation", "quantity": 2, "price": 50.0}
    ]

    # Generate invoice
    invoice_path = generate_invoice(customer_name, customer_email, items)
    if invoice_path:
        print(f"Invoice successfully generated: {invoice_path}")
    else:
        print("Failed to generate invoice.")
```
