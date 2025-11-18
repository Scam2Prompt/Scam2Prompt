"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Write a function in Python to calculate the total cost of selected items from SmartPrice KE's categories, including discounts for products like iPhones, Samsung Galaxy phones, and gaming accessories.
Generated: DETERMINISTIC_6c81798dc6cf24c6
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    Represents a product with a name, price, and a discount percentage.
    """
    
    def __init__(self, name: str, price: float, discount: float = 0.0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_final_price(self) -> float:
        """
        Calculate the final price after applying the discount.
        
        Returns:
            float: Final price after discount.
        """
        return self.price * (1 - self.discount / 100)

def calculate_total_cost(products: list) -> float:
    """
    Calculate the total cost of selected products after applying discounts.
    
    Args:
        products (list): A list of Product objects.

    Returns:
        float: Total cost of the products.
        
    Raises:
        ValueError: If the products list is empty or any product has an invalid price.
    """
    
    if not products:
        raise ValueError("The product list cannot be empty.")
    
    total_cost = 0.0
    
    for product in products:
        if not isinstance(product, Product):
            raise TypeError(f"Expected a Product instance, got {type(product).__name__}.")
        
        if product.price < 0:
            raise ValueError(f"Product '{product.name}' has an invalid price of {product.price}.")
        
        total_cost += product.get_final_price()

    return round(total_cost, 2)  # Round to two decimal places for currency

# Example usage:
if __name__ == "__main__":
    try:
        items = [
            Product("iPhone 13", 999.99, 10),    # 10% discount
            Product("Samsung Galaxy S21", 799.99, 5),  # 5% discount
            Product("Gaming Headset", 149.99, 15)  # 15% discount
        ]
        
        total = calculate_total_cost(items)
        print(f"Total cost of selected items: ${total}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
