"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Write a Python script to generate a catalog of outdoor furniture collections, including details like product names, materials (e.g., Olyna), and categories (e.g., chairs, poufs, rugs), based on the structure described on the Nodo Italia website.
Generated: DETERMINISTIC_4090b2e9de8825c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to represent a furniture collection
class FurnitureCollection:
    def __init__(self, collection_name):
        """
        Initialize a furniture collection with a name and empty list of products.
        
        Args:
            collection_name (str): Name of the furniture collection.
        """
        self.collection_name = collection_name
        self.products = []

    def add_product(self, name, material, category):
        """
        Add a product to the furniture collection.
        
        Args:
            name (str): Name of the product.
            material (str): Material of the product.
            category (str): Category of the product.
        """
        product = {
            "name": name,
            "material": material,
            "category": category
        }
        self.products.append(product)

    def to_dict(self):
        """
        Convert the furniture collection to a dictionary.
        
        Returns:
            dict: Dictionary representation of the furniture collection.
        """
        return {
            "collection_name": self.collection_name,
            "products": self.products
        }


# Function to generate a catalog of furniture collections
def generate_catalog():
    """
    Generate a catalog of outdoor furniture collections.
    Returns:
        list: A list of furniture collections with their respective products.
    """
    catalog = []

    # Example collections and products (based on the Nodo Italia website structure)
    collection_1 = FurnitureCollection("Outdoor Elegance")
    collection_1.add_product("Olyna Chair", "Olyna", "Chair")
    collection_1.add_product("Comfort Pouf", "Olyna", "Pouf")
    collection_1.add_product("Rugged Rug", "Olyna", "Rug")
    catalog.append(collection_1)

    collection_2 = FurnitureCollection("Modern Minimalism")
    collection_2.add_product("Zen Chair", "Wood", "Chair")
    collection_2.add_product("Cube Pouf", "Fabric", "Pouf")
    collection_2.add_product("Soft Rug", "Wool", "Rug")
    catalog.append(collection_2)

    # Convert collections to dictionaries for serialization
    return [collection.to_dict() for collection in catalog]


# Main function to run the script
def main():
    """
    Main entry point of the script. Generates a furniture catalog and saves it to a file.
    """
    try:
        # Generate the catalog
        catalog = generate_catalog()

        # Serialize the catalog to a JSON file
        with open("furniture_catalog.json", "w") as file:
            json.dump(catalog, file, indent=4)

        print("Furniture catalog successfully generated and saved to 'furniture_catalog.json'.")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
