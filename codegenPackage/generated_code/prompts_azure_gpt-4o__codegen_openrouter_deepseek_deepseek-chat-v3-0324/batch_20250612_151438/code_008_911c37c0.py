"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Develop a script to calculate the total savings when purchasing multiple discounted lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "Plafon Chess 4xe27 Biv Newline 171bt."
Generated: DETERMINISTIC_911c37c0ddf42af5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LightingProduct:
    """
    Represents a lighting product with its details and pricing.
    """
    def __init__(self, name: str, original_price: float, discounted_price: float):
        """
        Initialize a LightingProduct instance.
        
        Args:
            name (str): Name of the product.
            original_price (float): Original price before discount.
            discounted_price (float): Price after discount.
        """
        self.name = name
        self.original_price = original_price
        self.discounted_price = discounted_price
    
    def calculate_savings(self) -> float:
        """
        Calculate the savings for this product.
        
        Returns:
            float: Amount saved (original price - discounted price).
        """
        return self.original_price - self.discounted_price


class LightingPurchase:
    """
    Manages a collection of lighting products and calculates total savings.
    """
    def __init__(self):
        """Initialize an empty list of products."""
        self.products = []
    
    def add_product(self, product: LightingProduct) -> None:
        """
        Add a product to the purchase.
        
        Args:
            product (LightingProduct): Product to add.
        """
        self.products.append(product)
    
    def calculate_total_savings(self) -> float:
        """
        Calculate the total savings across all products.
        
        Returns:
            float: Total savings.
        """
        return sum(product.calculate_savings() for product in self.products)
    
    def get_total_original_price(self) -> float:
        """
        Calculate the total original price across all products.
        
        Returns:
            float: Total original price.
        """
        return sum(product.original_price for product in self.products)
    
    def get_total_discounted_price(self) -> float:
        """
        Calculate the total discounted price across all products.
        
        Returns:
            float: Total discounted price.
        """
        return sum(product.discounted_price for product in self.products)


def main():
    """Main function to demonstrate the usage of the classes."""
    try:
        # Create a purchase instance
        purchase = LightingPurchase()
        
        # Add products with their original and discounted prices
        purchase.add_product(LightingProduct(
            "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195",
            25.99,
            19.99
        ))
        purchase.add_product(LightingProduct(
            "Plafon Chess 4xe27 Biv Newline 171bt",
            35.50,
            28.99
        ))
        
        # Calculate and display results
        total_savings = purchase.calculate_total_savings()
        total_original = purchase.get_total_original_price()
        total_discounted = purchase.get_total_discounted_price()
        
        print(f"Total Original Price: ${total_original:.2f}")
        print(f"Total Discounted Price: ${total_discounted:.2f}")
        print(f"Total Savings: ${total_savings:.2f}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
