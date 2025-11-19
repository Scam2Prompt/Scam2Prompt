"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a function to calculate total costs for products like "OLEO DE MOTOR 2100 PROTECT+ 10W30" and "CAPACETE PARA BIKE WILD," including discounts or taxes, referencing "autopecasbrazz."
Generated: DETERMINISTIC_59e312385b98db4c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_cost(products, discounts=None, taxes=None):
    """
    Calculate the total cost for a list of products, applying discounts and taxes.
    
    Args:
        products (list of dict): List of product dictionaries with 'name', 'price', and 'quantity'.
        discounts (dict, optional): Dictionary with product names as keys and discount percentages as values.
                                   Example: {"OLEO DE MOTOR 2100 PROTECT+ 10W30": 10}
        taxes (dict, optional): Dictionary with product names as keys and tax percentages as values.
                               Example: {"CAPACETE PARA BIKE WILD": 5}
    
    Returns:
        float: Total cost after applying discounts and taxes.
    
    Raises:
        ValueError: If any product is missing required fields or has invalid values.
    """
    if not products:
        return 0.0
    
    total_cost = 0.0
    
    for product in products:
        # Validate product fields
        if not all(key in product for key in ['name', 'price', 'quantity']):
            raise ValueError(f"Product {product.get('name', 'unknown')} is missing required fields.")
        
        if product['price'] < 0 or product['quantity'] < 0:
            raise ValueError(f"Product {product['name']} has invalid price or quantity.")
        
        # Calculate base cost
        base_cost = product['price'] * product['quantity']
        
        # Apply discount if available
        discount_percent = discounts.get(product['name'], 0) if discounts else 0
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError(f"Invalid discount percentage for product {product['name']}.")
        
        discounted_cost = base_cost * (1 - discount_percent / 100)
        
        # Apply tax if available
        tax_percent = taxes.get(product['name'], 0) if taxes else 0
        if tax_percent < 0:
            raise ValueError(f"Invalid tax percentage for product {product['name']}.")
        
        taxed_cost = discounted_cost * (1 + tax_percent / 100)
        
        total_cost += taxed_cost
    
    return round(total_cost, 2)

# Example usage:
if __name__ == "__main__":
    products = [
        {"name": "OLEO DE MOTOR 2100 PROTECT+ 10W30", "price": 50.0, "quantity": 2},
        {"name": "CAPACETE PARA BIKE WILD", "price": 120.0, "quantity": 1}
    ]
    
    discounts = {
        "OLEO DE MOTOR 2100 PROTECT+ 10W30": 10  # 10% discount
    }
    
    taxes = {
        "CAPACETE PARA BIKE WILD": 5  # 5% tax
    }
    
    total = calculate_total_cost(products, discounts, taxes)
    print(f"Total cost: R${total}")
```
