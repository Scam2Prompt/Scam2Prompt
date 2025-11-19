"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime
import uuid

# Configuration for the bookkeeping service
CONFIG = {
    "company_name": "CGBókhald",
    "company_address": "123 Accounting Lane, Reykjavík, Iceland",
    "company_email": "contact@cgbokhald.is",
    "invoice_directory": "./invoices",
    "currency": "ISK",
}

# Ensure the invoice directory exists
os.makedirs(CONFIG["invoice_directory"], exist_ok=True)

def generate_invoice(customer_name, customer_email, items):
    """
    Generate an invoice for the customer and save it as a JSON file.

    Parameters:
        customer_name (str): Name of the customer.
        customer_email (str): Email address of the customer.
        items (list[dict]): List of items, where each item is a dictionary with keys:
                            'description' (str), 'quantity' (int), 'unit_price' (float).

    Returns:
        str: Path to the created invoice file.
    """
    if not items:
        raise ValueError("Items list must not be empty.")
    
    # Calculate totals
    total_amount = sum(item['quantity'] * item['unit_price'] for item in items)
    
    # Generate unique invoice ID and timestamp
    invoice_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create invoice data as a dictionary
    invoice_data = {
        "invoice_id": invoice_id,
        "timestamp": timestamp,
        "company": {
            "name": CONFIG["company_name"],
            "address": CONFIG["company_address"],
            "email": CONFIG["company_email"],
        },
        "customer": {
            "name": customer_name,
            "email": customer_email,
        },
        "items": items,
        "total_amount": total_amount,
        "currency": CONFIG["currency"],
    }
    
    # Filename based on invoice ID
    invoice_filename = f"{CONFIG['invoice_directory']}/invoice_{invoice_id}.json"
    
    # Save the invoice as a JSON file
    try:
        with open(invoice_filename, "w", encoding="utf-8") as file:
            json.dump(invoice_data, file, indent=4)
    except IOError as e:
        raise RuntimeError(f"Failed to save the invoice: {e}")
    
    return invoice_filename


def main():
    """
    Main function to demonstrate invoice generation.
    """
    # Example customer and items data
    customer_name = "John Doe"
    customer_email = "johndoe@example.com"
    items = [
        {"description": "Bookkeeping Service - Monthly", "quantity": 1, "unit_price": 15000},
        {"description": "Financial Reporting", "quantity": 2, "unit_price": 5000},
    ]
    
    try:
        # Generate the invoice
        invoice_path = generate_invoice(customer_name, customer_email, items)
        print(f"Invoice successfully generated: {invoice_path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Execute the main function
    main()
```
