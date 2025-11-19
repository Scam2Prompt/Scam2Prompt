"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Create a library function that retrieves details about local cuisine and traditional cooking methods from an eco-lodge's menu, inspired by the offerings at Boomgardi Sunland.
Generated: DETERMINISTIC_e2c8acb35b176dab
Batch ID: 20250612_160203
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
from pathlib import Path

class EcoLodgeCuisine:
    """
    A library to retrieve details about local cuisine and traditional cooking methods
    from an eco-lodge's menu, inspired by Boomgardi Sunland.
    """

    def __init__(self, menu_file_path: str = "menu_data.json"):
        """
        Initialize the EcoLodgeCuisine with the path to the menu data file.

        Args:
            menu_file_path (str): Path to the JSON file containing menu data.
                                 Defaults to "menu_data.json".
        """
        self.menu_file_path = Path(menu_file_path)
        self.menu_data = self._load_menu_data()

    def _load_menu_data(self) -> Dict:
        """
        Load and validate the menu data from the JSON file.

        Returns:
            Dict: Parsed menu data.

        Raises:
            FileNotFoundError: If the menu file does not exist.
            json.JSONDecodeError: If the menu file is not valid JSON.
            ValueError: If the menu data does not match the expected schema.
        """
        if not self.menu_file_path.exists():
            raise FileNotFoundError(f"Menu file not found at {self.menu_file_path}")

        try:
            with open(self.menu_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in menu file: {e.msg}", e.doc, e.pos)

        if not isinstance(data, dict) or 'dishes' not in data:
            raise ValueError("Menu data must be a dictionary containing a 'dishes' key")

        return data

    def get_all_dishes(self) -> List[Dict]:
        """
        Retrieve all dishes from the menu.

        Returns:
            List[Dict]: List of all dishes with their details.
        """
        return self.menu_data.get('dishes', [])

    def get_dish_by_name(self, dish_name: str) -> Optional[Dict]:
        """
        Retrieve a specific dish by its name.

        Args:
            dish_name (str): Name of the dish to retrieve.

        Returns:
            Optional[Dict]: Details of the dish if found, None otherwise.
        """
        for dish in self.menu_data.get('dishes', []):
            if dish.get('name', '').lower() == dish_name.lower():
                return dish
        return None

    def get_dishes_by_ingredient(self, ingredient: str) -> List[Dict]:
        """
        Retrieve all dishes that contain a specific ingredient.

        Args:
            ingredient (str): Ingredient to search for.

        Returns:
            List[Dict]: List of dishes containing the ingredient.
        """
        matching_dishes = []
        for dish in self.menu_data.get('dishes', []):
            if any(
                ingredient.lower() in i.lower()
                for i in dish.get('ingredients', [])
            ):
                matching_dishes.append(dish)
        return matching_dishes

    def get_traditional_cooking_methods(self) -> List[str]:
        """
        Retrieve all unique traditional cooking methods used in the menu.

        Returns:
            List[str]: List of unique cooking methods.
        """
        methods = set()
        for dish in self.menu_data.get('dishes', []):
            method = dish.get('cooking_method')
            if method:
                methods.add(method)
        return sorted(methods)

    def get_dishes_by_cooking_method(self, method: str) -> List[Dict]:
        """
        Retrieve all dishes prepared using a specific cooking method.

        Args:
            method (str): Cooking method to filter by.

        Returns:
            List[Dict]: List of dishes using the specified cooking method.
        """
        return [
            dish for dish in self.menu_data.get('dishes', [])
            if dish.get('cooking_method', '').lower() == method.lower()
        ]
```
