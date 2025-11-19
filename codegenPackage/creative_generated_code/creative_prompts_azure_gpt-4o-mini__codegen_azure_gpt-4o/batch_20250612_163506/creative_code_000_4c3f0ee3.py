"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gcapmarkets.com
Prompt: Generate a code snippet for a financial consulting application that incorporates innovative financial products and international standards as described by GCap Markets.
Generated: DETERMINISTIC_4c3f0ee387fbdae4
Batch ID: 20250612_163506
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

class FinancialProduct:
    """
    A class to represent a financial product adhering to international standards.
    """

    def __init__(self, name, description, risk_level, currency):
        """
        Initialize the financial product.

        :param name: Name of the financial product
        :param description: Brief description of the product
        :param risk_level: Risk level of the product (e.g., 'Low', 'Medium', 'High')
        :param currency: Currency in which the product operates (e.g., 'USD', 'EUR')
        """
        self.name = name
        self.description = description
        self.risk_level = risk_level
        self.currency = currency
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        """
        Convert the financial product details to a dictionary.

        :return: Dictionary representation of the financial product
        """
        return {
            "name": self.name,
            "description": self.description,
            "risk_level": self.risk_level,
            "currency": self.currency,
            "created_at": self.created_at.isoformat()
        }


class FinancialConsultingApp:
    """
    A financial consulting application to manage innovative financial products.
    """

    def __init__(self):
        """
        Initialize the application.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a financial product to the application.

        :param product: Instance of FinancialProduct
        """
        if not isinstance(product, FinancialProduct):
            raise ValueError("Invalid product type. Expected instance of FinancialProduct.")
        self.products.append(product)

    def get_all_products(self):
        """
        Retrieve all financial products.

        :return: List of dictionaries representing financial products
        """
        return [product.to_dict() for product in self.products]

    def save_products_to_file(self, file_path):
        """
        Save all financial products to a JSON file.

        :param file_path: Path to the output file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_all_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving products to file: {e}")
            raise

    def load_products_from_file(self, file_path):
        """
        Load financial products from a JSON file.

        :param file_path: Path to the input file
        """
        try:
            with open(file_path, 'r') as file:
                product_dicts = json.load(file)
                self.products = [
                    FinancialProduct(
                        name=p["name"],
                        description=p["description"],
                        risk_level=p["risk_level"],
                        currency=p["currency"]
                    )
                    for p in product_dicts
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading products from file: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    app = FinancialConsultingApp()

    # Create sample financial products
    product1 = FinancialProduct("Green Bond", "Environmentally-friendly investment option", "Low", "USD")
    product2 = FinancialProduct("International Equity Fund", "Diversified global equity investments", "Medium", "EUR")

    # Add products to the app
    app.add_product(product1)
    app.add_product(product2)

    # Save products to a file
    app.save_products_to_file("financial_products.json")

    # Load products from the file
    app.load_products_from_file("financial_products.json")

    # Display all products
    for product in app.get_all_products():
        print(product)
```
