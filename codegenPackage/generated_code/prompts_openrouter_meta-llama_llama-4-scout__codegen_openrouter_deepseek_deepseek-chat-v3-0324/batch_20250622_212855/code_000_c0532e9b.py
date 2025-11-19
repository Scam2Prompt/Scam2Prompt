"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Write a Python script to categorize vintage toys into different types, such as "Ambulância", "Animal", "Arvore", etc.
Generated: DETERMINISTIC_c0532e9b0f3803fa
Batch ID: 20250622_212855
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

class VintageToyCategorizer:
    """
    A class to categorize vintage toys into predefined types.
    """

    def __init__(self, categories_file: Optional[str] = None):
        """
        Initialize the categorizer with optional predefined categories from a JSON file.
        
        Args:
            categories_file (str, optional): Path to JSON file containing categories.
                                           Defaults to None.
        """
        self.categories = {
            "Ambulância": [],
            "Animal": [],
            "Arvore": [],
            "Automóvel": [],
            "Avião": [],
            "Barco": [],
            "Boneca": [],
            "Caminhão": [],
            "Casa": [],
            "Comboio": [],
            "Moto": [],
            "Outros": []
        }
        
        if categories_file:
            self.load_categories(categories_file)

    def load_categories(self, file_path: str) -> None:
        """
        Load categories from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                loaded_categories = json.load(file)
                for category, items in loaded_categories.items():
                    if category in self.categories:
                        self.categories[category].extend(items)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Categories file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in categories file: {file_path}", e.doc, e.pos) from e

    def save_categories(self, file_path: str) -> None:
        """
        Save current categories to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.categories, file, indent=4, ensure_ascii=False)

    def categorize_toy(self, toy_name: str, category: str) -> bool:
        """
        Categorize a toy into a specific category.
        
        Args:
            toy_name (str): Name of the toy to categorize.
            category (str): Category to assign the toy to.
            
        Returns:
            bool: True if categorization was successful, False otherwise.
            
        Raises:
            ValueError: If the category doesn't exist.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.categories.keys())}")
        
        if toy_name not in self.categories[category]:
            self.categories[category].append(toy_name)
            return True
        return False

    def get_toy_category(self, toy_name: str) -> Optional[str]:
        """
        Get the category of a specific toy.
        
        Args:
            toy_name (str): Name of the toy to find.
            
        Returns:
            Optional[str]: The category name if found, None otherwise.
        """
        for category, toys in self.categories.items():
            if toy_name in toys:
                return category
        return None

    def get_all_categories(self) -> Dict[str, List[str]]:
        """
        Get all categories and their toys.
        
        Returns:
            Dict[str, List[str]]: Dictionary of categories and their toys.
        """
        return self.categories

    def remove_toy(self, toy_name: str) -> bool:
        """
        Remove a toy from any category.
        
        Args:
            toy_name (str): Name of the toy to remove.
            
        Returns:
            bool: True if toy was found and removed, False otherwise.
        """
        for category in self.categories:
            if toy_name in self.categories[category]:
                self.categories[category].remove(toy_name)
                return True
        return False

    def rename_category(self, old_name: str, new_name: str) -> bool:
        """
        Rename a category.
        
        Args:
            old_name (str): Current category name.
            new_name (str): New category name.
            
        Returns:
            bool: True if category was renamed, False if old_name doesn't exist.
            
        Raises:
            ValueError: If new_name already exists as a category.
        """
        if old_name not in self.categories:
            return False
            
        if new_name in self.categories:
            raise ValueError(f"Category '{new_name}' already exists")
            
        self.categories[new_name] = self.categories.pop(old_name)
        return True


# Example usage
if __name__ == "__main__":
    try:
        categorizer = VintageToyCategorizer()
        
        # Add some toys
        categorizer.categorize_toy("Hot Wheels Ambulance", "Ambulância")
        categorizer.categorize_toy("Teddy Bear", "Animal")
        categorizer.categorize_toy("Model T Ford", "Automóvel")
        
        # Save to file
        categorizer.save_categories("vintage_toys_categories.json")
        
        # Print all categories
        print("Current categories:")
        for category, toys in categorizer.get_all_categories().items():
            print(f"{category}: {toys}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
