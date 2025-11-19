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
# Import necessary modules
from typing import List, Tuple

def calculate_liquidity(invoices: List[Tuple[str, float]], factoring_rate: float) -> float:
    """
    Calculate the liquidity obtained by a company through factoring.

    Parameters:
        invoices (List[Tuple[str, float]]): A list of tuples where each tuple contains:
            - Invoice ID (str)
            - Invoice value (float)
        factoring_rate (float): The percentage of the invoice value that the factoring company pays (0-1).

    Returns:
        float: Total liquidity obtained through factoring.
    """
    # Validate inputs
    if not (0 <= factoring_rate <= 1):
        raise ValueError("Factoring rate must be between 0 and 1 (inclusive).")
    
    if not all(isinstance(invoice, tuple) and len(invoice) == 2 and isinstance(invoice[0], str) and isinstance(invoice[1], (int, float)) for invoice in invoices):
        raise ValueError("Invoices must be a list of tuples with (str, float) format.")
    
    # Calculate total liquidity
    total_liquidity = 0.0
    for invoice_id, invoice_value in invoices:
        if invoice_value < 0:
            raise ValueError(f"Invoice value for {invoice_id} cannot be negative.")
        liquidity = invoice_value * factoring_rate
        total_liquidity += liquidity
    
    return total_liquidity

# Example usage
if __name__ == "__main__":
    try:
        # List of invoices (Invoice ID, Invoice Value)
        invoices = [
            ("INV001", 1000.0),
            ("INV002", 2000.0),
            ("INV003", 1500.0)
        ]
        # Factoring rate (e.g., 80% of invoice value)
        factoring_rate = 0.8

        # Calculate liquidity
        liquidity = calculate_liquidity(invoices, factoring_rate)
        print(f"Total liquidity obtained through factoring: ${liquidity:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
