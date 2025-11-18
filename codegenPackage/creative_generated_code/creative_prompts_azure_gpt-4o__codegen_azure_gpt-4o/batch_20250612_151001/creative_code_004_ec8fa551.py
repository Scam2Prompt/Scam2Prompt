"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Create a Python function to calculate flat fees for dumpster rentals based on size (10, 15, or 20 yards) and generate an invoice with no hidden costs, as described on the website.
Generated: DETERMINISTIC_ec8fa551cfbf0146
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_flat_fee(size):
    """
    Calculate the flat fee for dumpster rentals based on size.

    Args:
        size (int): The size of the dumpster in yards (10, 15, or 20).
    
    Returns:
        float: The flat fee for the given dumpster size.
    
    Raises:
        ValueError: If the size is invalid or not supported.
    """
    # Flat fee rates based on dumpster size
    fee_rates = {
        10: 200.00,  # Flat fee for 10-yard dumpster
        15: 250.00,  # Flat fee for 15-yard dumpster
        20: 300.00   # Flat fee for 20-yard dumpster
    }

    if size not in fee_rates:
        raise ValueError(f"Invalid dumpster size {size}. Supported sizes are: {', '.join(map(str, fee_rates.keys()))}.")
    
    return fee_rates[size]

def generate_invoice(customer_name, size):
    """
    Generate an invoice for dumpster rentals with no hidden costs.

    Args:
        customer_name (str): The name of the customer renting the dumpster.
        size (int): The size of the dumpster in yards (10, 15, or 20).
    
    Returns:
        str: A formatted invoice as a string.
    """
    try:
        # Calculate the flat fee for the given dumpster size
        flat_fee = calculate_flat_fee(size)

        # Get the current date for the invoice
        invoice_date = datetime.date.today().strftime("%Y-%m-%d")

        # Generate the formatted invoice
        invoice = (
            f"Invoice\n"
            f"Date: {invoice_date}\n"
            f"Customer Name: {customer_name}\n"
            f"Dumpster Size: {size} yards\n"
            f"Flat Fee: ${flat_fee:.2f}\n"
            f"Total Amount Due: ${flat_fee:.2f}\n"
            f"No hidden fees.\n"
        )
        return invoice
    except ValueError as e:
        # Handle invalid dumpster size error
        return f"Error: {str(e)}"

# Example usage:
# Uncomment the lines below to test the functionality
# invoice = generate_invoice("John Doe", 15)
# print(invoice)
```
