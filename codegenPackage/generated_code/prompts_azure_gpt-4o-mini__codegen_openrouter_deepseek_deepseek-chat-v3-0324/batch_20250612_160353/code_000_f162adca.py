"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Generate a Python script to create a simple recipe management system for Peruvian and international cuisine, inspired by the courses offered at Egatur.
Generated: DETERMINISTIC_f162adcab79bb95a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union

class RecipeManager:
    """
    A simple recipe management system for Peruvian and international cuisine.
    """
    
    def __init__(self, data_file: str = "recipes.json"):
        """
        Initialize the RecipeManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing recipes. Defaults to "recipes.json".
        """
        self.data_file = data_file
        self.recipes = self._load_recipes()
    
    def _load_recipes(self) -> Dict[str, Dict]:
        """
        Load recipes from the JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of recipes with recipe names as keys.
            
        Raises:
            FileNotFoundError: If the data file doesn't exist.
            json.JSONDecodeError: If the data file is not valid JSON.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}", e.doc, e.pos)
    
    def _save_recipes(self) -> None:
        """
        Save recipes to the JSON file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.recipes, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Error saving recipes: {e}")
    
    def add_recipe(
        self,
        name: str,
        cuisine: str,
        ingredients: List[str],
        instructions: List[str],
        prep_time: int,
        cook_time: int,
        difficulty: str,
        tags: Optional[List[str]] = None
    ) -> None:
        """
        Add a new recipe to the collection.
        
        Args:
            name (str): Name of the recipe.
            cuisine (str): Type of cuisine (e.g., "Peruvian", "Italian").
            ingredients (List[str]): List of ingredients.
            instructions (List[str]): Step-by-step instructions.
            prep_time (int): Preparation time in minutes.
            cook_time (int): Cooking time in minutes.
            difficulty (str): Difficulty level (e.g., "Easy", "Medium", "Hard").
            tags (Optional[List[str]]): Optional tags for the recipe.
            
        Raises:
            ValueError: If recipe name already exists.
        """
        if name in self.recipes:
            raise ValueError(f"Recipe '{name}' already exists.")
        
        recipe = {
            "cuisine": cuisine,
            "ingredients": ingredients,
            "instructions": instructions,
            "prep_time": prep_time,
            "cook_time": cook_time,
            "total_time": prep_time + cook_time,
            "difficulty": difficulty,
            "tags": tags if tags else []
        }
        
        self.recipes[name] = recipe
        self._save_recipes()
    
    def get_recipe(self, name: str) -> Optional[Dict]:
        """
        Retrieve a recipe by name.
        
        Args:
            name (str): Name of the recipe to retrieve.
            
        Returns:
            Optional[Dict]: The recipe dictionary if found, None otherwise.
        """
        return self.recipes.get(name)
    
    def update_recipe(
        self,
        name: str,
        cuisine: Optional[str] = None,
        ingredients: Optional[List[str]] = None,
        instructions: Optional[List[str]] = None,
        prep_time: Optional[int] = None,
        cook_time: Optional[int] = None,
        difficulty: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> None:
        """
        Update an existing recipe.
        
        Args:
            name (str): Name of the recipe to update.
            cuisine (Optional[str]): Updated cuisine type.
            ingredients (Optional[List[str]]): Updated ingredients list.
            instructions (Optional[List[str]]): Updated instructions.
            prep_time (Optional[int]): Updated preparation time.
            cook_time (Optional[int]): Updated cooking time.
            difficulty (Optional[str]): Updated difficulty level.
            tags (Optional[List[str]]): Updated tags list.
            
        Raises:
            ValueError: If recipe doesn't exist.
        """
        if name not in self.recipes:
            raise ValueError(f"Recipe '{name}' not found.")
        
        recipe = self.recipes[name]
        
        if cuisine is not None:
            recipe["cuisine"] = cuisine
        if ingredients is not None:
            recipe["ingredients"] = ingredients
        if instructions is not None:
            recipe["instructions"] = instructions
        if prep_time is not None:
            recipe["prep_time"] = prep_time
        if cook_time is not None:
            recipe["cook_time"] = cook_time
            recipe["total_time"] = prep_time + cook_time if prep_time is not None else recipe["prep_time"] + cook_time
        if difficulty is not None:
            recipe["difficulty"] = difficulty
        if tags is not None:
            recipe["tags"] = tags
            
        self._save_recipes()
    
    def delete_recipe(self, name: str) -> None:
        """
        Delete a recipe by name.
        
        Args:
            name (str): Name of the recipe to delete.
            
        Raises:
            ValueError: If recipe doesn't exist.
        """
        if name not in self.recipes:
            raise ValueError(f"Recipe '{name}' not found.")
        
        del self.recipes[name]
        self._save_recipes()
    
    def search_recipes(
        self,
        cuisine: Optional[str] = None,
        max_time: Optional[int] = None,
        difficulty: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> List[Dict[str, Union[str, List[str], int]]]:
        """
        Search recipes based on criteria.
        
        Args:
            cuisine (Optional[str]): Filter by cuisine type.
            max_time (Optional[int]): Filter by maximum total time (minutes).
            difficulty (Optional[str]): Filter by difficulty level.
            tags (Optional[List[str]]): Filter by tags (all must match).
            
        Returns:
            List[Dict[str, Union[str, List[str], int]]]: List of matching recipes.
        """
        results = []
        
        for name, recipe in self.recipes.items():
            match = True
            
            if cuisine and recipe["cuisine"].lower() != cuisine.lower():
                match = False
            if max_time and recipe["total_time"] > max_time:
                match = False
            if difficulty and recipe["difficulty"].lower() != difficulty.lower():
                match = False
            if tags and not all(tag.lower() in [t.lower() for t in recipe["tags"]] for tag in tags):
                match = False
                
            if match:
                results.append({"name": name, **recipe})
                
        return results
    
    def list_all_recipes(self) -> List[str]:
        """
        List all recipe names.
        
        Returns:
            List[str]: List of all recipe names.
        """
        return list(self.recipes.keys())


# Example usage
if __name__ == "__main__":
    manager = RecipeManager()
    
    # Add some sample recipes
    try:
        manager.add_recipe(
            name="Ceviche",
            cuisine="Peruvian",
            ingredients=["Fresh fish", "Lime juice", "Red onion", "Cilantro", "Aji peppers", "Corn", "Sweet potato"],
            instructions=[
                "Cut the fish into small cubes",
                "Marinate in lime juice for 10 minutes",
                "Add sliced red onion, cilantro, and aji peppers",
                "Serve with corn and sweet potato"
            ],
            prep_time=20,
            cook_time=0,
            difficulty="Medium",
            tags=["Seafood", "Appetizer"]
        )
        
        manager.add_recipe(
            name="Spaghetti Carbonara",
            cuisine="Italian",
            ingredients=["Spaghetti", "Eggs", "Pancetta", "Parmesan cheese", "Black pepper"],
            instructions=[
                "Cook spaghetti al dente",
                "Fry pancetta until crispy",
                "Mix eggs and cheese",
                "Combine all ingredients while hot",
                "Season with black pepper"
            ],
            prep_time=10,
            cook_time=15,
            difficulty="Easy",
            tags=["Pasta", "Main Course"]
        )
        
        # Search examples
        print("Peruvian recipes:")
        for recipe in manager.search_recipes(cuisine="Peruvian"):
            print(f"- {recipe['name']}")
            
        print("\nQuick recipes (under 30 minutes):")
        for recipe in manager.search_recipes(max_time=30):
            print(f"- {recipe['name']} ({recipe['total_time']} minutes)")
            
    except Exception as e:
        print(f"Error: {e}")
```
