"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Develop a script to categorize industrial materials into three sections (as mentioned in Rux Industrial's blog) and suggest their applications in various engineering projects.
Generated: DETERMINISTIC_09f63c83022b27cc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Tuple

# Define material categories and their applications
MATERIAL_CATEGORIES = {
    "Metals": {
        "description": "Strong, durable materials with high thermal and electrical conductivity.",
        "applications": [
            "Structural frameworks",
            "Electrical wiring",
            "Heat exchangers",
            "Machinery components"
        ],
        "examples": ["Steel", "Aluminum", "Copper", "Titanium"]
    },
    "Polymers": {
        "description": "Lightweight, corrosion-resistant materials with good insulation properties.",
        "applications": [
            "Insulation",
            "Piping systems",
            "Protective coatings",
            "Consumer products"
        ],
        "examples": ["PVC", "Polyethylene", "Nylon", "Teflon"]
    },
    "Ceramics": {
        "description": "Hard, brittle materials resistant to heat and wear.",
        "applications": [
            "High-temperature applications",
            "Cutting tools",
            "Electrical insulators",
            "Biomedical implants"
        ],
        "examples": ["Alumina", "Silicon carbide", "Zirconia", "Porcelain"]
    }
}

class MaterialCategorizer:
    """
    A class to categorize industrial materials and suggest their applications.
    """
    
    def __init__(self, categories: Dict = MATERIAL_CATEGORIES):
        """
        Initialize the categorizer with material categories.
        
        Args:
            categories (Dict): Dictionary of material categories with their properties.
        """
        self.categories = categories
    
    def categorize_material(self, material_name: str) -> Tuple[str, Dict]:
        """
        Categorize a given material and return its category and properties.
        
        Args:
            material_name (str): Name of the material to categorize.
            
        Returns:
            Tuple[str, Dict]: Category name and properties if found, None otherwise.
            
        Raises:
            ValueError: If material is not found in any category.
        """
        material_name_lower = material_name.lower()
        
        for category, properties in self.categories.items():
            examples_lower = [ex.lower() for ex in properties["examples"]]
            if material_name_lower in examples_lower:
                return category, properties
        
        raise ValueError(f"Material '{material_name}' not found in any category.")
    
    def get_all_categories(self) -> Dict:
        """
        Get all material categories with their properties.
        
        Returns:
            Dict: All material categories.
        """
        return self.categories
    
    def suggest_applications(self, material_name: str) -> List[str]:
        """
        Get suggested applications for a given material.
        
        Args:
            material_name (str): Name of the material.
            
        Returns:
            List[str]: List of suggested applications.
            
        Raises:
            ValueError: If material is not found in any category.
        """
        category, properties = self.categorize_material(material_name)
        return properties["applications"]
    
    def export_categories_to_json(self, file_path: str) -> None:
        """
        Export material categories to a JSON file.
        
        Args:
            file_path (str): Path to the output JSON file.
            
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.categories, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        categorizer = MaterialCategorizer()
        
        # Get all categories
        print("Available Material Categories:")
        for category in categorizer.get_all_categories():
            print(f"- {category}")
        
        # Categorize a material
        material = "Aluminum"
        category, properties = categorizer.categorize_material(material)
        print(f"\n'{material}' belongs to category: {category}")
        print(f"Description: {properties['description']}")
        print(f"Example applications: {', '.join(properties['applications'])}")
        
        # Export to JSON
        categorizer.export_categories_to_json("material_categories.json")
        print("\nCategories exported to 'material_categories.json'")
        
    except Exception as e:
        print(f"Error: {e}")
```
