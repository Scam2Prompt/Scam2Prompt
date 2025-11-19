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
import json
from typing import List, Dict, Union

def calculate_liquidity_from_factoring(
    invoices: List[Dict[str, Union[str, float]]],
    advance_rate: float = 0.8,
    fee_percentage: float = 0.02
) -> Dict[str, Union[float, List[Dict[str, Union[str, float]]]]]:
    """
    Calculate the liquidity obtained through factoring given a list of invoices.

    Args:
        invoices: List of dictionaries where each dictionary represents an invoice
                 with keys 'invoice_id' (str) and 'value' (float).
        advance_rate: Percentage of the invoice value advanced by the factor (default: 0.8).
        fee_percentage: Percentage fee charged by the factor (default: 0.02).

    Returns:
        A dictionary containing:
            - 'total_liquidity': Total liquidity obtained after fees.
            - 'total_fees': Total fees paid to the factor.
            - 'invoices': Original invoice list with added 'advance_amount' and 'fee_amount'.

    Raises:
        ValueError: If advance_rate or fee_percentage is not between 0 and 1,
                   or if any invoice value is negative.
    """
    # Validate input parameters
    if not (0 <= advance_rate <= 1):
        raise ValueError("advance_rate must be between 0 and 1")
    if not (0 <= fee_percentage <= 1):
        raise ValueError("fee_percentage must be between 0 and 1")

    total_liquidity = 0.0
    total_fees = 0.0

    # Process each invoice
    processed_invoices = []
    for invoice in invoices:
        invoice_value = invoice['value']
        if invoice_value < 0:
            raise ValueError(f"Invoice {invoice['invoice_id']} has negative value")

        advance_amount = invoice_value * advance_rate
        fee_amount = advance_amount * fee_percentage
        net_advance = advance_amount - fee_amount

        total_liquidity += net_advance
        total_fees += fee_amount

        # Add calculated fields to invoice copy
        processed_invoice = invoice.copy()
        processed_invoice.update({
            'advance_amount': advance_amount,
            'fee_amount': fee_amount,
            'net_advance': net_advance
        })
        processed_invoices.append(processed_invoice)

    return {
        'total_liquidity': round(total_liquidity, 2),
        'total_fees': round(total_fees, 2),
        'invoices': processed_invoices
    }

# Example usage
if __name__ == "__main__":
    example_invoices = [
        {"invoice_id": "INV001", "value": 1000.0},
        {"invoice_id": "INV002", "value": 2500.0},
        {"invoice_id": "INV003", "value": 500.0}
    ]

    try:
        result = calculate_liquidity_from_factoring(example_invoices)
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(f"Error: {e}")
```
