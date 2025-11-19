"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Write a Python code snippet to calculate the liquidity obtained by a company through factoring, given a list of invoices and their respective values."
Generated: DETERMINISTIC_49a0e2c6f1f76878
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Invoice:
    """Class to represent an invoice with its value."""
    
    def __init__(self, invoice_id: str, value: float):
        """
        Initialize an Invoice instance.

        :param invoice_id: Unique identifier for the invoice
        :param value: Monetary value of the invoice
        """
        self.invoice_id = invoice_id
        self.value = value

def calculate_liquidity(invoices: List[Invoice], factoring_rate: float) -> float:
    """
    Calculate the liquidity obtained through factoring.

    :param invoices: List of Invoice objects
    :param factoring_rate: The percentage of the invoice value that is received
                           through factoring (e.g., 0.8 for 80%)
    :return: Total liquidity obtained from factoring the invoices
    :raises ValueError: If the factoring rate is not between 0 and 1
    """
    if not (0 <= factoring_rate <= 1):
        raise ValueError("Factoring rate must be between 0 and 1.")

    total_liquidity = 0.0

    for invoice in invoices:
        if invoice.value < 0:
            raise ValueError(f"Invoice value cannot be negative: {invoice.value}")
        liquidity_from_invoice = invoice.value * factoring_rate
        total_liquidity += liquidity_from_invoice

    return total_liquidity

# Example usage
if __name__ == "__main__":
    # Create a list of invoices
    invoices = [
        Invoice("INV001", 1000.0),
        Invoice("INV002", 2000.0),
        Invoice("INV003", 1500.0)
    ]
    
    # Define the factoring rate (e.g., 80%)
    factoring_rate = 0.8

    try:
        # Calculate the total liquidity obtained through factoring
        liquidity = calculate_liquidity(invoices, factoring_rate)
        print(f"Total liquidity obtained through factoring: ${liquidity:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
