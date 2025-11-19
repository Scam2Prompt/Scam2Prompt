"""
Generated Code Metadata:
========================
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Generate a list of potential product categories and subcategories for an e-commerce website featuring French gourmet foods, including Foie Gras, duck confit, and Périgord specialties.
Generated: DETERMINISTIC_e1a5d1a13cba9090
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_categories.py

class ProductCategory:
    """Represents a product category with subcategories."""

    def __init__(self, name):
        """
        Initializes a ProductCategory instance.

        Args:
            name (str): The name of the category.
        """
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        """
        Adds a subcategory to the category.

        Args:
            subcategory (str): The name of the subcategory.
        """
        self.subcategories.append(subcategory)


class ProductCatalog:
    """Represents a catalog of product categories."""

    def __init__(self):
        """Initializes a ProductCatalog instance."""
        self.categories = []

    def add_category(self, category):
        """
        Adds a category to the catalog.

        Args:
            category (ProductCategory): The category to add.
        """
        self.categories.append(category)

    def get_categories(self):
        """
        Returns a list of categories.

        Returns:
            list[ProductCategory]: The list of categories.
        """
        return self.categories


def create_french_gourmet_catalog():
    """
    Creates a product catalog for French gourmet foods.

    Returns:
        ProductCatalog: The product catalog.
    """
    catalog = ProductCatalog()

    # Create categories
    charcuterie = ProductCategory("Charcuterie")
    foie_gras = ProductCategory("Foie Gras")
    duck_specialties = ProductCategory("Duck Specialties")
    perigord_specialties = ProductCategory("Périgord Specialties")
    cheeses = ProductCategory("Cheeses")
    desserts = ProductCategory("Desserts")

    # Add subcategories
    charcuterie.add_subcategory("Pâtés")
    charcuterie.add_subcategory("Terrines")
    charcuterie.add_subcategory("Saucissons")

    foie_gras.add_subcategory("Foie Gras en Bloc")
    foie_gras.add_subcategory("Foie Gras en Terrine")

    duck_specialties.add_subcategory("Duck Confit")
    duck_specialties.add_subcategory("Duck Legs")

    perigord_specialties.add_subcategory("Périgord Sauces")
    perigord_specialties.add_subcategory("Périgord Jams")

    cheeses.add_subcategory("Goat Cheeses")
    cheeses.add_subcategory("Cow Cheeses")

    desserts.add_subcategory("Macarons")
    desserts.add_subcategory("Madeleines")

    # Add categories to catalog
    catalog.add_category(charcuterie)
    catalog.add_category(foie_gras)
    catalog.add_category(duck_specialties)
    catalog.add_category(perigord_specialties)
    catalog.add_category(cheeses)
    catalog.add_category(desserts)

    return catalog


def print_catalog(catalog):
    """
    Prints the product catalog.

    Args:
        catalog (ProductCatalog): The product catalog.
    """
    for category in catalog.get_categories():
        print(f"**{category.name}**")
        for subcategory in category.subcategories:
            print(f"- {subcategory}")
        print()


def main():
    try:
        catalog = create_french_gourmet_catalog()
        print_catalog(catalog)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
