"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Create a product recommendation engine that suggests Bollé products, such as LIGHTSHIFTER XL sunglasses, based on customer preferences and purchase history.
Generated: DETERMINISTIC_ccb0c00fef14aa61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from collections import defaultdict

class Product:
    """Represents a Bollé product."""
    def __init__(self, product_id: str, name: str, category: str, price: float, attributes: Dict[str, str]):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.attributes = attributes

    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'attributes': self.attributes
        }

class Customer:
    """Represents a customer with preferences and purchase history."""
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.preferences = defaultdict(list)
        self.purchase_history = []

    def add_preference(self, category: str, attribute: str, value: str):
        """Add a customer preference."""
        self.preferences[(category, attribute)].append(value)

    def add_purchase(self, product: Product):
        """Add a product to purchase history."""
        self.purchase_history.append(product)

class RecommendationEngine:
    """Product recommendation engine for Bollé products."""
    def __init__(self):
        self.products = []
        self.customers = {}

    def load_products(self, file_path: str):
        """Load products from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    product = Product(
                        product_id=item['product_id'],
                        name=item['name'],
                        category=item['category'],
                        price=item['price'],
                        attributes=item['attributes']
                    )
                    self.products.append(product)
        except FileNotFoundError:
            raise FileNotFoundError(f"Product file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in product file")

    def get_customer(self, customer_id: str) -> Customer:
        """Get or create a customer."""
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id)
        return self.customers[customer_id]

    def recommend_products(self, customer_id: str, limit: int = 5) -> List[Product]:
        """
        Recommend products based on customer preferences and purchase history.
        
        Args:
            customer_id: ID of the customer
            limit: Maximum number of recommendations to return
            
        Returns:
            List of recommended products
        """
        if customer_id not in self.customers:
            return []

        customer = self.customers[customer_id]
        scored_products = []

        for product in self.products:
            score = 0
            
            # Score based on purchase history (same category)
            for purchased in customer.purchase_history:
                if purchased.category == product.category:
                    score += 10
            
            # Score based on preferences
            for (category, attribute), values in customer.preferences.items():
                if category == product.category and attribute in product.attributes:
                    if product.attributes[attribute] in values:
                        score += 5
            
            scored_products.append((score, product))

        # Sort by score descending and get top recommendations
        scored_products.sort(key=lambda x: x[0], reverse=True)
        return [product for (score, product) in scored_products[:limit]]

# Example usage
if __name__ == "__main__":
    try:
        engine = RecommendationEngine()
        engine.load_products("products.json")
        
        # Create a customer and add preferences
        customer = engine.get_customer("cust123")
        customer.add_preference("sunglasses", "lens_type", "polarized")
        customer.add_preference("sunglasses", "frame_material", "plastic")
        
        # Add purchase history
        purchased_product = Product(
            product_id="sg001",
            name="LIGHTSHIFTER XL",
            category="sunglasses",
            price=149.99,
            attributes={"lens_type": "polarized", "frame_material": "plastic"}
        )
        customer.add_purchase(purchased_product)
        
        # Get recommendations
        recommendations = engine.recommend_products("cust123")
        for product in recommendations:
            print(f"Recommended: {product.name} ({product.category})")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
