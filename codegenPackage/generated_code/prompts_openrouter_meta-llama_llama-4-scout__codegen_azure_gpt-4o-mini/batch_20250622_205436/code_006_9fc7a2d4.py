"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Develop a Python program to analyze customer requests for custom menuiserie products, such as pergolas and fermetures bâtiment, and generate quotes based on product specifications and pricing rules."
Generated: DETERMINISTIC_9fc7a2d414631e11
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class CustomMenuiserieQuote:
    def __init__(self, pricing_rules: Dict[str, float]):
        """
        Initialize the CustomMenuiserieQuote with pricing rules.

        :param pricing_rules: A dictionary containing product types and their respective prices.
        """
        self.pricing_rules = pricing_rules

    def validate_request(self, request: Dict[str, Any]) -> None:
        """
        Validate the customer request for required fields.

        :param request: A dictionary containing the customer request details.
        :raises ValueError: If required fields are missing or invalid.
        """
        required_fields = ['product_type', 'dimensions', 'quantity']
        for field in required_fields:
            if field not in request:
                raise ValueError(f"Missing required field: {field}")

        if request['product_type'] not in self.pricing_rules:
            raise ValueError(f"Invalid product type: {request['product_type']}")

        if not isinstance(request['dimensions'], (list, tuple)) or len(request['dimensions']) != 2:
            raise ValueError("Dimensions must be a list or tuple of two values (width, height).")

        if not isinstance(request['quantity'], int) or request['quantity'] <= 0:
            raise ValueError("Quantity must be a positive integer.")

    def calculate_quote(self, request: Dict[str, Any]) -> float:
        """
        Calculate the quote based on the customer request.

        :param request: A dictionary containing the customer request details.
        :return: The total quote amount.
        """
        self.validate_request(request)

        product_type = request['product_type']
        dimensions = request['dimensions']
        quantity = request['quantity']

        # Calculate area (assuming dimensions are in meters)
        area = dimensions[0] * dimensions[1]  # width * height
        price_per_square_meter = self.pricing_rules[product_type]

        # Calculate total cost
        total_cost = area * price_per_square_meter * quantity
        return total_cost

    def generate_quote(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a quote for the customer request.

        :param request: A dictionary containing the customer request details.
        :return: A dictionary containing the quote details.
        """
        try:
            total_cost = self.calculate_quote(request)
            return {
                'product_type': request['product_type'],
                'dimensions': request['dimensions'],
                'quantity': request['quantity'],
                'total_cost': total_cost
            }
        except ValueError as e:
            return {'error': str(e)}

def main():
    # Example pricing rules for different product types
    pricing_rules = {
        'pergola': 150.0,  # price per square meter
        'fermetures_batiment': 200.0  # price per square meter
    }

    # Create an instance of the quote generator
    quote_generator = CustomMenuiserieQuote(pricing_rules)

    # Example customer request
    customer_request = {
        'product_type': 'pergola',
        'dimensions': [4.0, 3.0],  # width, height in meters
        'quantity': 2
    }

    # Generate the quote
    quote = quote_generator.generate_quote(customer_request)

    # Output the quote
    print(json.dumps(quote, indent=4))

if __name__ == "__main__":
    main()
```
