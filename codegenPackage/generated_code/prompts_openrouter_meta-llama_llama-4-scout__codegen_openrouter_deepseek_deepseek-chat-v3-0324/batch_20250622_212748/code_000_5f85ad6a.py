"""
Generated Code Metadata:
========================
Original URL: https://weco.fi
Prompt: "Generate a Python code snippet for an e-commerce product categorization system similar to WEco's, with categories like Beverages, Creams, and Snacks & Nuts."
Generated: DETERMINISTIC_5f85ad6a8ac98e98
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ProductCategorizer:
    """
    A product categorization system for e-commerce platforms.
    Categories include Beverages, Creams, Snacks & Nuts, etc.
    """

    def __init__(self, category_mapping_file: Optional[str] = None):
        """
        Initialize the categorizer with optional category mapping file.
        
        Args:
            category_mapping_file (str, optional): Path to JSON file containing 
                predefined category mappings. Defaults to None.
        """
        self.categories = {
            'Beverages': [],
            'Creams': [],
            'Snacks & Nuts': [],
            'Other': []
        }
        
        if category_mapping_file:
            self.load_category_mappings(category_mapping_file)

    def load_category_mappings(self, file_path: str) -> None:
        """
        Load category mappings from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file containing category mappings.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as f:
                mappings = json.load(f)
                for category, products in mappings.items():
                    if category in self.categories:
                        self.categories[category] = products
        except FileNotFoundError:
            raise FileNotFoundError(f"Category mapping file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in category mapping file", doc="", pos=0)

    def categorize_product(self, product_name: str, keywords: Dict[str, List[str]]) -> str:
        """
        Categorize a product based on its name and predefined keywords.
        
        Args:
            product_name (str): Name of the product to categorize.
            keywords (Dict[str, List[str]]): Dictionary mapping categories to lists of keywords.
            
        Returns:
            str: The determined category for the product.
        """
        product_name_lower = product_name.lower()
        
        for category, kw_list in keywords.items():
            if category not in self.categories:
                continue
                
            for keyword in kw_list:
                if keyword.lower() in product_name_lower:
                    return category
        
        return 'Other'

    def add_product_to_category(self, product_name: str, category: str) -> None:
        """
        Manually add a product to a specific category.
        
        Args:
            product_name (str): Name of the product to add.
            category (str): Category to add the product to.
            
        Raises:
            ValueError: If the category doesn't exist.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
            
        self.categories[category].append(product_name)

    def get_products_in_category(self, category: str) -> List[str]:
        """
        Get all products in a specific category.
        
        Args:
            category (str): Category to query.
            
        Returns:
            List[str]: List of product names in the category.
            
        Raises:
            ValueError: If the category doesn't exist.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
            
        return self.categories[category]

    def save_category_mappings(self, file_path: str) -> None:
        """
        Save current category mappings to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file.
        """
        with open(file_path, 'w') as f:
            json.dump(self.categories, f, indent=4)


# Example usage
if __name__ == "__main__":
    # Initialize categorizer
    categorizer = ProductCategorizer()
    
    # Define some keyword mappings
    keyword_mappings = {
        'Beverages': ['juice', 'soda', 'water', 'tea', 'coffee'],
        'Creams': ['cream', 'lotion', 'moisturizer'],
        'Snacks & Nuts': ['nut', 'almond', 'cashew', 'chips', 'cracker']
    }
    
    # Categorize some products
    products = [
        'Apple Juice',
        'Almond Butter',
        'Face Cream',
        'Potato Chips',
        'Hand Lotion',
        'Coffee Beans',
        'USB Cable'
    ]
    
    for product in products:
        category = categorizer.categorize_product(product, keyword_mappings)
        categorizer.add_product_to_category(product, category)
        print(f"{product} -> {category}")
    
    # Save the mappings
    categorizer.save_category_mappings('product_categories.json')
```
