"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-lab.net
Prompt: Suggest an API for calculating taxes during checkout for digital music purchases, as described in Soniculture's shopping cart system.
Generated: DETERMINISTIC_0a97d7cd10a2eb6d
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

# Tax rates based on region (example rates, these should be adjusted as necessary)
TAX_RATES = {
    "CA": Decimal("0.13"),  # California
    "NY": Decimal("0.09"),  # New York
    "TX": Decimal("0.0625"),  # Texas
    "FL": Decimal("0.06"),  # Florida
    "default": Decimal("0.0")  # No tax for other regions
}

class TaxCalculationError(Exception):
    """Custom exception for tax calculation errors."""
    pass

def calculate_tax(subtotal: Decimal, region: str) -> Decimal:
    """
    Calculate the tax amount based on the subtotal and customer region.

    Args:
        subtotal (Decimal): The subtotal amount of the purchase.
        region (str): The two-letter state code for tax calculation.

    Returns:
        Decimal: The calculated tax amount.

    Raises:
        TaxCalculationError: If the subtotal is negative or invalid.
    """
    if subtotal < 0:
        raise TaxCalculationError("Subtotal cannot be negative.")

    tax_rate = TAX_RATES.get(region, TAX_RATES["default"])
    tax_amount = subtotal * tax_rate
    return tax_amount

@app.route('/calculate_tax', methods=['POST'])
def api_calculate_tax():
    """
    API endpoint to calculate the tax for a digital music purchase.

    Expects JSON payload with 'subtotal' and 'region' keys.
    Responds with the calculated tax amount or error message.
    """
    try:
        data = request.get_json()

        # Validate input data
        if 'subtotal' not in data or 'region' not in data:
            return jsonify({"error": "Invalid input. 'subtotal' and 'region' are required."}), 400
        
        subtotal = Decimal(data['subtotal'])
        region = data['region'].strip().upper()

        # Calculate tax
        tax_amount = calculate_tax(subtotal, region)

        return jsonify({"tax_amount": str(tax_amount)}), 200

    except InvalidOperation:
        return jsonify({"error": "Invalid subtotal value. It must be a valid number."}), 400
    except TaxCalculationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
