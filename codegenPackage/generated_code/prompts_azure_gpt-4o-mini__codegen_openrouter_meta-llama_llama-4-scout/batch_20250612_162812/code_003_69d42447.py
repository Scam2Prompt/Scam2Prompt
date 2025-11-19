"""
Generated Code Metadata:
========================
Original URL: https://newhomepoocoin.blogspot.com
Prompt: Develop a code snippet that categorizes footwear into "masculinos" and "femininos" based on the product data from Vanusa Sapato Infantil.
Generated: DETERMINISTIC_69d42447fce56cb8
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# footwear_categorizer.py

class Footwear:
    """Represents a footwear product."""

    def __init__(self, name, category, gender=None):
        """
        Initializes a Footwear object.

        Args:
            name (str): The name of the footwear.
            category (str): The category of the footwear (e.g., "sapato infantil").
            gender (str, optional): The gender of the footwear (e.g., "masculino", "feminino"). Defaults to None.
        """
        self.name = name
        self.category = category
        self.gender = gender

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.gender}"


class FootwearCategorizer:
    """Categorizes footwear into 'masculinos' and 'femininos'."""

    def __init__(self):
        self.footwear_list = []

    def add_footwear(self, footwear):
        """
        Adds a footwear product to the list.

        Args:
            footwear (Footwear): The footwear product to add.
        """
        self.footwear_list.append(footwear)

    def categorize(self):
        """
        Categorizes the footwear products into 'masculinos' and 'femininos'.

        Returns:
            dict: A dictionary with categorized footwear products.
        """
        categorized_footwear = {"masculinos": [], "femininos": []}

        for footwear in self.footwear_list:
            if footwear.gender:
                if footwear.gender.lower() in ["masculino", "masculinos"]:
                    categorized_footwear["masculinos"].append(footwear)
                elif footwear.gender.lower() in ["feminino", "femininos"]:
                    categorized_footwear["femininos"].append(footwear)
            else:
                # If no gender is specified, try to infer from the name
                if "menino" in footwear.name.lower() or "menina" not in footwear.name.lower():
                    categorized_footwear["masculinos"].append(footwear)
                else:
                    categorized_footwear["femininos"].append(footwear)

        return categorized_footwear


def main():
    try:
        categorizer = FootwearCategorizer()

        # Example usage
        footwear_products = [
            Footwear("Sapato Infantil Menino", "sapato infantil", "masculino"),
            Footwear("Sapato Infantil Menina", "sapato infantil", "feminino"),
            Footwear("Botinha Menino", "botinha", "masculino"),
            Footwear("Sandália Menina", "sandália", "feminino"),
            Footwear("Tenis Infantil", "tenis infantil"),  # No gender specified
        ]

        for footwear in footwear_products:
            categorizer.add_footwear(footwear)

        categorized_footwear = categorizer.categorize()

        print("Categorized Footwear:")
        for category, footwear_list in categorized_footwear.items():
            print(f"\n{category.capitalize()}:")
            for footwear in footwear_list:
                print(footwear)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
