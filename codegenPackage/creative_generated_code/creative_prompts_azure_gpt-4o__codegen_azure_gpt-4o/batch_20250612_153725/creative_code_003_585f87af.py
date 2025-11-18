"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-virgocx.teachable.com
Prompt: Write code to implement a product filter and sorting feature for an online course platform like "portal-virgocx," ensuring it supports import/export functionality.
Generated: DETERMINISTIC_585f87af55ea876b
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv

# Product class to represent a course
class Product:
    def __init__(self, id, name, category, price, rating):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating

    def to_dict(self):
        """Convert Product object to dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "rating": self.rating,
        }

# Function to filter products based on criteria
def filter_products(products, category=None, min_price=None, max_price=None, min_rating=None):
    """
    Filter products based on category, price range, and minimum rating.
    :param products: List of Product objects
    :param category: Filter by category (optional)
    :param min_price: Minimum price (optional)
    :param max_price: Maximum price (optional)
    :param min_rating: Minimum rating (optional)
    :return: List of filtered Product objects
    """
    filtered = products
    if category:
        filtered = [p for p in filtered if p.category.lower() == category.lower()]
    if min_price:
        filtered = [p for p in filtered if p.price >= min_price]
    if max_price:
        filtered = [p for p in filtered if p.price <= max_price]
    if min_rating:
        filtered = [p for p in filtered if p.rating >= min_rating]
    return filtered

# Function to sort products based on attribute
def sort_products(products, sort_by="price", ascending=True):
    """
    Sort products by a specified attribute.
    :param products: List of Product objects
    :param sort_by: Attribute to sort by (price, rating, name)
    :param ascending: Sort order (True for ascending, False for descending)
    :return: List of sorted Product objects
    """
    try:
        return sorted(products, key=lambda p: getattr(p, sort_by), reverse=not ascending)
    except AttributeError:
        raise ValueError(f"Invalid sort attribute: '{sort_by}'")

# Function to export products to a JSON file
def export_products_to_json(products, file_path):
    """
    Export products to a JSON file.
    :param products: List of Product objects
    :param file_path: Path to the output JSON file
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in products], f, indent=4)
    print(f"Products exported to JSON file: {file_path}")

# Function to export products to a CSV file
def export_products_to_csv(products, file_path):
    """
    Export products to a CSV file.
    :param products: List of Product objects
    :param file_path: Path to the output CSV file
    """
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "category", "price", "rating"])
        writer.writeheader()
        for product in products:
            writer.writerow(product.to_dict())
    print(f"Products exported to CSV file: {file_path}")

# Function to import products from a JSON file
def import_products_from_json(file_path):
    """
    Import products from a JSON file.
    :param file_path: Path to the input JSON file
    :return: List of Product objects
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Product(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

# Function to import products from a CSV file
def import_products_from_csv(file_path):
    """
    Import products from a CSV file.
    :param file_path: Path to the input CSV file
    :return: List of Product objects
    """
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [Product(int(row["id"]), row["name"], row["category"], float(row["price"]), float(row["rating"])) for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

# Example usage of the code
if __name__ == "__main__":
    # Sample products
    products = [
        Product(1, "Python Basics", "Programming", 49.99, 4.5),
        Product(2, "Data Science", "Programming", 99.99, 4.8),
        Product(3, "Digital Marketing", "Marketing", 29.99, 4.2),
        Product(4, "SEO Fundamentals", "Marketing", 19.99, 4.0),
        Product(5, "Web Development", "Programming", 79.99, 4.7),
    ]

    # Filtering and sorting
    filtered = filter_products(products, category="Programming", min_price=50)
    sorted_products = sort_products(filtered, sort_by="rating", ascending=False)

    # Exporting products
    export_products_to_json(sorted_products, "products.json")
    export_products_to_csv(sorted_products, "products.csv")

    # Importing products
    imported_products_json = import_products_from_json("products.json")
    imported_products_csv = import_products_from_csv("products.csv")

    # Display imported products
    for product in imported_products_json:
        print(product.to_dict())
```
