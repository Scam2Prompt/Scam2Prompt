"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Create a Python function to generate invoices for international buyers of Himalayan salt products, incorporating product categories, packaging details, and shipping costs.
Generated: DETERMINISTIC_01216bf7e70d867b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

def generate_invoice(buyer_name, buyer_country, products, shipping_rate_per_kg):
    """
    Generates an invoice for international buyers purchasing Himalayan salt products.

    Args:
        buyer_name (str): Name of the buyer.
        buyer_country (str): Country of the buyer.
        products (list of dict): List of purchased products. Each product is a dict with:
            - 'name': Name of the product (str)
            - 'category': Category of the product (str)
            - 'weight_kg': Weight of the product in kilograms (float)
            - 'price_per_kg': Price per kilogram of the product (float)
        shipping_rate_per_kg (float): Shipping rate per kilogram.

    Returns:
        dict: A dictionary representing the generated invoice.

    Raises:
        ValueError: If any of the product details are invalid.
    """
    # Validate inputs and ensure product data is correct
    if not buyer_name or not buyer_country or not products or not isinstance(products, list):
        raise ValueError("Invalid input: Ensure buyer details and product list are provided.")
    
    # Initialize invoice details
    invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID
    issue_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time in UTC
    total_weight = 0
    total_product_cost = 0

    # Calculate cost and weight for each product
    product_details = []
    for product in products:
        try:
            name = product['name']
            category = product['category']
            weight_kg = float(product['weight_kg'])
            price_per_kg = float(product['price_per_kg'])

            if weight_kg <= 0 or price_per_kg <= 0:
                raise ValueError("Weight and price must be positive numbers.")

            product_cost = weight_kg * price_per_kg
            total_weight += weight_kg
            total_product_cost += product_cost

            product_details.append({
                'name': name,
                'category': category,
                'weight_kg': weight_kg,
                'price_per_kg': price_per_kg,
                'cost': product_cost
            })
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid product details: {e}")

    # Calculate shipping cost
    shipping_cost = total_weight * shipping_rate_per_kg

    # Calculate total invoice amount
    total_cost = total_product_cost + shipping_cost

    # Create and return the invoice
    invoice = {
        'invoice_id': invoice_id,
        'buyer_name': buyer_name,
        'buyer_country': buyer_country,
        'issue_date': issue_date,
        'products': product_details,
        'total_weight_kg': total_weight,
        'total_product_cost': total_product_cost,
        'shipping_cost': shipping_cost,
        'total_cost': total_cost
    }

    return invoice


# Example usage:
if __name__ == "__main__":
    # Sample products
    products = [
        {'name': 'Pink Himalayan Salt', 'category': 'Edible Salt', 'weight_kg': 5.0, 'price_per_kg': 3.5},
        {'name': 'Himalayan Salt Lamp', 'category': 'Decor', 'weight_kg': 2.0, 'price_per_kg': 12.0}
    ]

    # Generate an invoice
    try:
        invoice = generate_invoice(
            buyer_name="John Doe",
            buyer_country="USA",
            products=products,
            shipping_rate_per_kg=2.0
        )
        print("Generated Invoice:")
        print(invoice)
    except ValueError as e:
        print(f"Error generating invoice: {e}")
```
