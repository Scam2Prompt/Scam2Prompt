"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Generate a code snippet that uses Watpac's waterproofing solutions for a construction project, including specific products like Watpac Exterior Shield and Crack Fillers.
Generated: DETERMINISTIC_383d97b7a6fd122f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaterproofingProject:
    """
    A class to manage waterproofing solutions for construction projects.
    
    Attributes:
        project_name (str): The name of the construction project.
        products (dict): A dictionary to hold the selected waterproofing products.
    """

    def __init__(self, project_name):
        """
        Initializes the WaterproofingProject with a project name.

        Args:
            project_name (str): The name of the construction project.
        """
        self.project_name = project_name
        self.products = {}

    def add_product(self, product_name, product_details):
        """
        Adds a waterproofing product to the project.

        Args:
            product_name (str): The name of the product to add.
            product_details (dict): A dictionary containing product details (e.g., application area, coverage).
        
        Raises:
            ValueError: If the product name is empty or if the product details are invalid.
        """
        if not product_name:
            raise ValueError("Product name cannot be empty.")
        
        if not isinstance(product_details, dict) or not product_details:
            raise ValueError("Product details must be a non-empty dictionary.")

        self.products[product_name] = product_details
        print(f"Added {product_name} to the project.")

    def get_product_details(self, product_name):
        """
        Retrieves the details of a specific product.

        Args:
            product_name (str): The name of the product to retrieve details for.
        
        Returns:
            dict: The details of the product, or None if not found.
        """
        return self.products.get(product_name, None)

    def display_products(self):
        """Displays all the products added to the project."""
        if not self.products:
            print("No products have been added to the project.")
            return
        
        print("\nWaterproofing Products for Project:", self.project_name)
        for product_name, details in self.products.items():
            print(f"- {product_name}: {details}")

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the waterproofing project
        project = WaterproofingProject("High Rise Building")

        # Define product details
        exterior_shield_details = {
            "application_area": "Exterior walls",
            "coverage": "10 sqm per liter",
            "features": ["UV resistant", "Mold resistant"]
        }

        crack_filler_details = {
            "application_area": "Cracks in walls and floors",
            "coverage": "1 sqm per tube",
            "features": ["Quick drying", "Flexible"]
        }

        # Add products to the project
        project.add_product("Watpac Exterior Shield", exterior_shield_details)
        project.add_product("Watpac Crack Filler", crack_filler_details)

        # Display all products
        project.display_products()

    except Exception as e:
        print(f"An error occurred: {e}")
```
