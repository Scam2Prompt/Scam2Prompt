"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Develop a program to track and manage pest control products, including sales data and resistance levels, inspired by Bayer's Environmental Science Professional business.
Generated: DETERMINISTIC_b75df05132d4c3f7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class PestControlProduct:
    """
    Class representing a pest control product.
    Tracks product details, sales data, and resistance levels.
    """

    def __init__(self, product_id, name, category):
        """
        Initialize a pest control product instance.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Product category (e.g., insecticide, herbicide, etc.)
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.sales_data = []
        self.resistance_levels = {}

    def record_sale(self, quantity, price):
        """
        Record a sale for the product.

        :param quantity: Number of units sold
        :param price: Sale price per unit
        """
        sale = {
            "date": datetime.datetime.now().isoformat(),
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        }
        self.sales_data.append(sale)

    def update_resistance_level(self, pest_name, resistance_level):
        """
        Update the resistance level for a specific pest.

        :param pest_name: Name of the pest
        :param resistance_level: Resistance level (e.g., Low, Medium, High)
        """
        self.resistance_levels[pest_name] = resistance_level

    def get_sales_summary(self):
        """
        Generate a summary of sales for the product.

        :return: Dictionary containing total sales quantity and revenue
        """
        total_quantity = sum(sale["quantity"] for sale in self.sales_data)
        total_revenue = sum(sale["total"] for sale in self.sales_data)
        return {
            "product_id": self.product_id,
            "name": self.name,
            "total_quantity": total_quantity,
            "total_revenue": total_revenue
        }

    def serialize(self):
        """
        Serialize product data to JSON for storage or transmission.

        :return: JSON string representing the product
        """
        return json.dumps({
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "sales_data": self.sales_data,
            "resistance_levels": self.resistance_levels
        }, indent=4)

    @staticmethod
    def deserialize(json_data):
        """
        Deserialize JSON data to create a PestControlProduct instance.

        :param json_data: JSON string representing the product
        :return: PestControlProduct instance
        """
        data = json.loads(json_data)
        product = PestControlProduct(data["product_id"], data["name"], data["category"])
        product.sales_data = data["sales_data"]
        product.resistance_levels = data["resistance_levels"]
        return product


# Example Usage
if __name__ == "__main__":
    try:
        # Create a product instance
        product = PestControlProduct("P001", "MaxGuard Insecticide", "Insecticide")

        # Record sales
        product.record_sale(quantity=100, price=12.5)
        product.record_sale(quantity=50, price=13.0)

        # Update resistance levels
        product.update_resistance_level("Mosquito", "Medium")
        product.update_resistance_level("Cockroach", "Low")

        # Print sales summary
        sales_summary = product.get_sales_summary()
        print("Sales Summary:")
        print(sales_summary)

        # Serialize product data
        serialized_data = product.serialize()
        print("\nSerialized Product Data:")
        print(serialized_data)

        # Deserialize product data
        deserialized_product = PestControlProduct.deserialize(serialized_data)
        print("\nDeserialized Product Data:")
        print(deserialized_product.serialize())
    except Exception as e:
        print(f"An error occurred: {e}")
```
