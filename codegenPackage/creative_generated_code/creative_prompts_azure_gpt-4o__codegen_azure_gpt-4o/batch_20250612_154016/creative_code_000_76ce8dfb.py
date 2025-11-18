"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Write Python code to create a catalog system for health supplements, including products like "Colágeno Hidrolizado MAX" and "Pro Adulto," with features for user reviews and ratings based on the structure described on Familia Previlife's website.
Generated: DETERMINISTIC_76ce8dfb487ee68b
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class Product:
    """
    Represents a health supplement product in the catalog.
    """
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.description = description  # Short description of the product
        self.price = price  # Price of the product
        self.reviews = []  # List of reviews (user-generated)

    def add_review(self, user_name, rating, comment):
        """
        Adds a user review for the product.

        :param user_name: Name of the user leaving the review
        :param rating: Rating given by the user (1 to 5)
        :param comment: Comment left by the user
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        review = {
            "user_name": user_name,
            "rating": rating,
            "comment": comment,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.reviews.append(review)

    def get_average_rating(self):
        """
        Calculates and returns the average rating for the product.

        :return: Average rating, or None if no reviews exist
        """
        if not self.reviews:
            return None
        total_rating = sum(review["rating"] for review in self.reviews)
        return round(total_rating / len(self.reviews), 2)

    def to_dict(self):
        """
        Converts the product details and reviews into a dictionary format.

        :return: Dictionary representation of the product
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "reviews": self.reviews,
            "average_rating": self.get_average_rating()
        }


class Catalog:
    """
    Represents a catalog of health supplement products.
    """
    def __init__(self):
        self.products = {}  # Dictionary of products, keyed by product_id

    def add_product(self, product_id, name, description, price):
        """
        Adds a new product to the catalog.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param description: Short description of the product
        :param price: Price of the product
        """
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists in the catalog.")
        self.products[product_id] = Product(product_id, name, description, price)

    def remove_product(self, product_id):
        """
        Removes a product from the catalog.

        :param product_id: Unique identifier of the product to be removed
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID '{product_id}' not found in the catalog.")
        del self.products[product_id]

    def get_product(self, product_id):
        """
        Retrieves details of a specific product.

        :param product_id: Unique identifier of the product
        :return: Dictionary representation of the product
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID '{product_id}' not found in the catalog.")
        return self.products[product_id].to_dict()

    def list_products(self):
        """
        Retrieves details of all products in the catalog.

        :return: List of dictionaries representing all products
        """
        return [product.to_dict() for product in self.products.values()]

    def save_to_file(self, file_path):
        """
        Saves the catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved
        """
        with open(file_path, 'w') as file:
            json.dump(self.list_products(), file, indent=4)

    def load_from_file(self, file_path):
        """
        Loads the catalog from a JSON file.

        :param file_path: Path to the file from which the catalog will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                products = json.load(file)
                self.products = {
                    product["product_id"]: Product(
                        product["product_id"],
                        product["name"],
                        product["description"],
                        product["price"]
                    )
                    for product in products
                }
                for product in products:
                    for review in product["reviews"]:
                        self.products[product["product_id"]].reviews.append(review)
        except (FileNotFoundError, json.JSONDecodeError):
            raise ValueError("Failed to load catalog. Ensure the file exists and is properly formatted.")


# Example usage
if __name__ == "__main__":
    # Create a catalog object
    catalog = Catalog()

    # Add products
    catalog.add_product("001", "Colágeno Hidrolizado MAX", "Collagen supplement for skin and joint health.", 29.99)
    catalog.add_product("002", "Pro Adulto", "Multivitamin for adults.", 19.99)

    # Add reviews
    catalog.products["001"].add_review("Alice", 5, "Worked wonders for my skin!")
    catalog.products["001"].add_review("Bob", 4, "Good product, but a bit expensive.")
    catalog.products["002"].add_review("Charlie", 4, "Great multivitamin for daily use.")

    # Display all products
    print("Catalog Products:")
    for product in catalog.list_products():
        print(json.dumps(product, indent=4))

    # Save the catalog to a file
    catalog.save_to_file("catalog.json")

    # Load the catalog from the file
    new_catalog = Catalog()
    new_catalog.load_from_file("catalog.json")
    print("\nLoaded Catalog:")
    for product in new_catalog.list_products():
        print(json.dumps(product, indent=4))
```
