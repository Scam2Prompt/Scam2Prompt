"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: "Write a product design concept for a sustainable and beautiful product that prioritizes durability, functionality, and end-user experience, incorporating the latest technologies in the industry."
Generated: DETERMINISTIC_4b57106fd4c04f60
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SustainableProduct:
    """
    A class to represent a sustainable product design concept.
    
    Attributes:
        name (str): The name of the product.
        materials (list): A list of sustainable materials used in the product.
        features (list): A list of features that enhance functionality and user experience.
        durability_rating (int): A rating from 1 to 10 indicating the product's durability.
    """

    def __init__(self, name, materials, features, durability_rating):
        """
        Initializes the SustainableProduct with the given parameters.

        Args:
            name (str): The name of the product.
            materials (list): A list of sustainable materials.
            features (list): A list of product features.
            durability_rating (int): A durability rating from 1 to 10.

        Raises:
            ValueError: If durability_rating is not between 1 and 10.
        """
        if not (1 <= durability_rating <= 10):
            raise ValueError("Durability rating must be between 1 and 10.")
        
        self.name = name
        self.materials = materials
        self.features = features
        self.durability_rating = durability_rating

    def display_product_info(self):
        """Displays the product information in a user-friendly format."""
        print(f"Product Name: {self.name}")
        print("Materials Used:")
        for material in self.materials:
            print(f" - {material}")
        print("Features:")
        for feature in self.features:
            print(f" - {feature}")
        print(f"Durability Rating: {self.durability_rating}/10")

    def is_sustainable(self):
        """Checks if the product is made from 100% sustainable materials."""
        return all(material.is_sustainable() for material in self.materials)

class Material:
    """
    A class to represent a material used in the product.

    Attributes:
        name (str): The name of the material.
        sustainable (bool): Indicates if the material is sustainable.
    """

    def __init__(self, name, sustainable):
        """
        Initializes the Material with the given parameters.

        Args:
            name (str): The name of the material.
            sustainable (bool): Indicates if the material is sustainable.
        """
        self.name = name
        self.sustainable = sustainable

    def is_sustainable(self):
        """Returns whether the material is sustainable."""
        return self.sustainable

# Example usage
if __name__ == "__main__":
    try:
        # Define sustainable materials
        bamboo = Material("Bamboo", True)
        recycled_plastic = Material("Recycled Plastic", True)
        organic_cotton = Material("Organic Cotton", True)

        # Create a list of materials
        materials = [bamboo, recycled_plastic, organic_cotton]

        # Define product features
        features = [
            "Water-resistant",
            "Lightweight and portable",
            "Ergonomic design",
            "Smart technology integration"
        ]

        # Create a sustainable product
        product = SustainableProduct("Eco-Friendly Backpack", materials, features, 9)

        # Display product information
        product.display_product_info()

        # Check if the product is sustainable
        if product.is_sustainable():
            print("This product is made from 100% sustainable materials.")
        else:
            print("This product contains non-sustainable materials.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
