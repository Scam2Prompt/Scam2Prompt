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
class Footwear:
    """Class to represent a footwear item."""
    
    def __init__(self, name: str, category: str):
        """
        Initialize a Footwear instance.

        :param name: Name of the footwear item.
        :param category: Category of the footwear ('masculinos' or 'femininos').
        """
        self.name = name
        self.category = category.lower()  # Normalize category to lowercase

    def is_valid_category(self) -> bool:
        """Check if the category is valid."""
        return self.category in ['masculinos', 'femininos']


class FootwearCategorizer:
    """Class to categorize footwear items."""
    
    def __init__(self):
        """Initialize the FootwearCategorizer."""
        self.footwear_items = []

    def add_footwear(self, footwear: Footwear):
        """
        Add a footwear item to the categorizer.

        :param footwear: Footwear instance to add.
        :raises ValueError: If the footwear category is invalid.
        """
        if not footwear.is_valid_category():
            raise ValueError(f"Invalid category '{footwear.category}' for footwear '{footwear.name}'")
        self.footwear_items.append(footwear)

    def categorize_footwear(self):
        """Categorize and return footwear items by their categories."""
        categorized = {'masculinos': [], 'femininos': []}
        
        for item in self.footwear_items:
            categorized[item.category].append(item.name)
        
        return categorized


def main():
    """Main function to demonstrate footwear categorization."""
    try:
        # Create an instance of the FootwearCategorizer
        categorizer = FootwearCategorizer()

        # Sample footwear data
        footwear_data = [
            Footwear("Tênis Masculino", "masculinos"),
            Footwear("Sandal Feminina", "femininos"),
            Footwear("Bota Masculina", "masculinos"),
            Footwear("Sapatilha Feminina", "femininos"),
            Footwear("Chinelo", "masculinos")  # Example of an invalid category
        ]

        # Add footwear items to the categorizer
        for footwear in footwear_data:
            categorizer.add_footwear(footwear)

        # Get categorized footwear
        categorized_footwear = categorizer.categorize_footwear()
        print("Categorized Footwear:")
        print(categorized_footwear)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
