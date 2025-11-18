"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Recommend a library or tool for managing product categories such as "Equipamentos," "Suprimentos," and "Home Decor" in an e-commerce platform, referencing the ebrasilbrazz website structure.
Generated: DETERMINISTIC_4d281db0240b5535
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from typing import List, Dict

class ProductCategory:
    """
    A class to represent a product category in an e-commerce platform.

    Attributes
    ----------
    name : str
        The name of the category
    subcategories : List[str]
        A list of subcategories under this category
    """

    def __init__(self, name: str):
        """
        Initializes a new product category with the given name.

        Parameters
        ----------
        name : str
            The name of the category
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Category name must be a non-empty string.")
        
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory: str):
        """
        Adds a subcategory to the category.

        Parameters
        ----------
        subcategory : str
            The name of the subcategory to add
        
        Raises
        ------
        ValueError
            If the subcategory name is not a non-empty string.
        """
        if not isinstance(subcategory, str) or not subcategory:
            raise ValueError("Subcategory name must be a non-empty string.")

        self.subcategories.append(subcategory)

    def get_category_info(self) -> Dict[str, List[str]]:
        """
        Returns the category information as a dictionary.

        Returns
        -------
        Dict[str, List[str]]
            A dictionary containing the category name and its subcategories.
        """
        return {
            "category": self.name,
            "subcategories": self.subcategories,
        }

class CategoryManager:
    """
    A class to manage multiple product categories.

    Attributes
    ----------
    categories : List[ProductCategory]
        A list to store instances of ProductCategory
    """

    def __init__(self):
        """Initializes the CategoryManager with an empty category list."""
        self.categories = []

    def add_category(self, category: ProductCategory):
        """
        Adds a new product category to the manager.

        Parameters
        ----------
        category : ProductCategory
            An instance of ProductCategory to add
        
        Raises
        ------
        ValueError
            If the category is not an instance of ProductCategory.
        """
        if not isinstance(category, ProductCategory):
            raise ValueError("Only instances of ProductCategory can be added.")
        
        self.categories.append(category)

    def get_all_categories(self) -> List[Dict[str, List[str]]]:
        """
        Retrieves all categories with their subcategories.

        Returns
        -------
        List[Dict[str, List[str]]]
            A list of dictionaries containing all category information.
        """
        return [category.get_category_info() for category in self.categories]

# Example usage
if __name__ == "__main__":
    try:
        # Create a category manager
        category_manager = CategoryManager()

        # Create product categories
        equipamentos = ProductCategory("Equipamentos")
        equipamentos.add_subcategory("Ferramentas")
        equipamentos.add_subcategory("Máquinas")

        suprimentos = ProductCategory("Suprimentos")
        suprimentos.add_subcategory("Material de Escritório")
        suprimentos.add_subcategory("Acessórios")

        home_decor = ProductCategory("Home Decor")
        home_decor.add_subcategory("Móveis")
        home_decor.add_subcategory("Decoração")

        # Add categories to the manager
        category_manager.add_category(equipamentos)
        category_manager.add_category(suprimentos)
        category_manager.add_category(home_decor)

        # Retrieve and print all categories
        all_categories = category_manager.get_all_categories()
        print(all_categories)

    except Exception as e:
        print(f"An error occurred: {e}")
```
