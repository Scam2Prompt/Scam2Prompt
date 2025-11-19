"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Generate a Python script to categorize the products (e.g., Buttweld Pipe Fittings, Socket Weld Fittings, Perforated Sheets) from Dinkar Alloys based on their material type and application.
Generated: DETERMINISTIC_9220f59b7917e840
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Tuple, Optional

class ProductCategorizer:
    """
    A class to categorize products from Dinkar Alloys based on material type and application.
    """
    
    def __init__(self):
        # Predefined material types and their common keywords
        self.material_types = {
            'Stainless Steel': ['stainless', 'ss', '304', '316', '316l', '304l'],
            'Carbon Steel': ['carbon', 'cs', 'a105', 'a106', 'a53'],
            'Alloy Steel': ['alloy', 'p11', 'p22', 'p91'],
            'Nickel Alloy': ['nickel', 'inconel', 'monel', 'incoloy', 'hastelloy'],
            'Duplex Steel': ['duplex', 'super duplex', 'uns s31803', 'uns s32750'],
            'Copper Alloy': ['copper', 'brass', 'bronze'],
            'Aluminum': ['aluminum', 'aluminium', 'al']
        }
        
        # Predefined product categories and their common keywords
        self.product_categories = {
            'Buttweld Pipe Fittings': ['buttweld', 'butt weld', 'weld', 'elbow', 'tee', 'reducer', 'cap'],
            'Socket Weld Fittings': ['socket weld', 'socket', 'sw'],
            'Perforated Sheets': ['perforated', 'sheet', 'mesh', 'hole'],
            'Flanges': ['flange', 'flanges', 'weld neck', 'slip on', 'blind', 'socket weld flange'],
            'Fasteners': ['fastener', 'bolt', 'nut', 'screw', 'stud'],
            'Pipes & Tubes': ['pipe', 'tube', 'tubing', 'seamless', 'erw'],
            'Valves': ['valve', 'ball valve', 'gate valve', 'check valve', 'globe valve']
        }
    
    def _find_matches(self, text: str, category_dict: Dict[str, List[str]]) -> List[str]:
        """
        Helper method to find matching categories based on keywords.
        
        Args:
            text: Input text to search in
            category_dict: Dictionary of categories and their keywords
            
        Returns:
            List of matching categories
        """
        text_lower = text.lower()
        matches = []
        
        for category, keywords in category_dict.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                    matches.append(category)
                    break
        
        return matches
    
    def categorize_product(self, product_name: str) -> Dict[str, Optional[List[str]]]:
        """
        Categorize a product based on its name.
        
        Args:
            product_name: Name of the product to categorize
            
        Returns:
            Dictionary with material types and product categories
        """
        if not product_name or not isinstance(product_name, str):
            return {
                'material_types': None,
                'product_categories': None,
                'error': 'Invalid product name'
            }
        
        try:
            material_matches = self._find_matches(product_name, self.material_types)
            category_matches = self._find_matches(product_name, self.product_categories)
            
            return {
                'material_types': material_matches if material_matches else None,
                'product_categories': category_matches if category_matches else None
            }
        except Exception as e:
            return {
                'material_types': None,
                'product_categories': None,
                'error': str(e)
            }

# Example usage
if __name__ == "__main__":
    categorizer = ProductCategorizer()
    
    test_products = [
        "Stainless Steel 304 Buttweld Elbow",
        "Carbon Steel A105 Socket Weld Fittings",
        "Duplex Steel S31803 Perforated Sheets",
        "Nickel Alloy Inconel 600 Flanges",
        "Aluminum Perforated Mesh",
        "Alloy Steel P11 Pipes",
        "Invalid Product 123"
    ]
    
    for product in test_products:
        result = categorizer.categorize_product(product)
        print(f"Product: {product}")
        print(f"Material Types: {result['material_types']}")
        print(f"Product Categories: {result['product_categories']}")
        print("-" * 50)
```
