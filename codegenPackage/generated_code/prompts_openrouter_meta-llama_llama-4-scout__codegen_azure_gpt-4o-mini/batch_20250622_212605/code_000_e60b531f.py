"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to categorize tools and machinery for a Brazilian manufacturing company, including categories like 'ferramenta instrumental', 'maquinaria', and 'aparelhagem'.
Generated: DETERMINISTIC_e60b531f115342c6
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ToolCategory:
    """Class to represent a category of tools and machinery."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.items: List[str] = []

    def add_item(self, item: str) -> None:
        """Add an item to the category."""
        self.items.append(item)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the category to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'items': self.items
        }

class ToolCatalog:
    """Class to manage a catalog of tool categories."""
    
    def __init__(self):
        self.categories: List[ToolCategory] = []

    def add_category(self, category: ToolCategory) -> None:
        """Add a new category to the catalog."""
        self.categories.append(category)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([category.to_dict() for category in self.categories], ensure_ascii=False, indent=4)

def main() -> None:
    """Main function to create and display the tool catalog."""
    try:
        # Create tool categories
        instrumental_tools = ToolCategory(
            name='ferramenta instrumental',
            description='Ferramentas utilizadas para operações de precisão.'
        )
        machinery = ToolCategory(
            name='maquinaria',
            description='Máquinas utilizadas para processos de fabricação.'
        )
        equipment = ToolCategory(
            name='aparelhagem',
            description='Equipamentos auxiliares para a produção.'
        )

        # Add items to categories
        instrumental_tools.add_item('Chave de fenda')
        instrumental_tools.add_item('Alicate')
        machinery.add_item('Fresadora')
        machinery.add_item('Torno')
        equipment.add_item('Compresor de ar')
        equipment.add_item('Gerador')

        # Create catalog and add categories
        catalog = ToolCatalog()
        catalog.add_category(instrumental_tools)
        catalog.add_category(machinery)
        catalog.add_category(equipment)

        # Output the catalog as JSON
        catalog_json = catalog.to_json()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
