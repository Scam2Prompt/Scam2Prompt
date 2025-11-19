"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Write a Python script to create a simple interior design advisor chatbot that suggests products and decor ideas based on user input, using a dataset of products from websites like origines-decoration.com."
Generated: DETERMINISTIC_f4bf7870b5eab19b
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional

class InteriorDesignAdvisor:
    """
    A simple interior design advisor chatbot that suggests products and decor ideas.
    """
    
    def __init__(self, dataset_path: str = "products_dataset.json"):
        """
        Initialize the chatbot with a product dataset.
        
        Args:
            dataset_path (str): Path to the JSON file containing product data.
        """
        self.dataset = self._load_dataset(dataset_path)
        self.user_preferences = {}
        
    def _load_dataset(self, path: str) -> Dict:
        """
        Load product dataset from JSON file.
        
        Args:
            path (str): Path to the JSON file.
            
        Returns:
            Dict: Loaded product data.
            
        Raises:
            FileNotFoundError: If the dataset file is not found.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset file not found at {path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in dataset file", "", 0)
    
    def _get_category_products(self, category: str) -> List[Dict]:
        """
        Get products from a specific category.
        
        Args:
            category (str): Product category to filter by.
            
        Returns:
            List[Dict]: List of products in the specified category.
        """
        return [product for product in self.dataset.get('products', []) 
                if product.get('category', '').lower() == category.lower()]
    
    def _get_random_products(self, category: str, count: int = 3) -> List[Dict]:
        """
        Get random products from a category.
        
        Args:
            category (str): Product category.
            count (int): Number of products to return.
            
        Returns:
            List[Dict]: Random products from the category.
        """
        products = self._get_category_products(category)
        return random.sample(products, min(count, len(products))) if products else []
    
    def _format_product_suggestion(self, product: Dict) -> str:
        """
        Format a product suggestion into a readable string.
        
        Args:
            product (Dict): Product information.
            
        Returns:
            str: Formatted product suggestion.
        """
        return (f"- {product.get('name', 'Unknown product')} "
                f"(Price: {product.get('price', 'N/A')}€, "
                f"Style: {product.get('style', 'N/A')})")
    
    def get_room_suggestions(self, room_type: str) -> str:
        """
        Get decor suggestions for a specific room type.
        
        Args:
            room_type (str): Type of room (e.g., 'living room').
            
        Returns:
            str: Formatted suggestions for the room.
        """
        categories = {
            'living room': ['sofa', 'coffee table', 'rug'],
            'bedroom': ['bed', 'nightstand', 'dresser'],
            'kitchen': ['dining table', 'chair', 'cabinet'],
            'bathroom': ['vanity', 'mirror', 'shelf']
        }
        
        room_categories = categories.get(room_type.lower(), [])
        if not room_categories:
            return f"I don't have suggestions for {room_type}. Please try another room type."
        
        suggestions = [f"Here are some {room_type} decor ideas:"]
        for category in room_categories:
            products = self._get_random_products(category)
            if products:
                suggestions.append(f"\n{category.title()} suggestions:")
                suggestions.extend(self._format_product_suggestion(p) for p in products)
        
        return '\n'.join(suggestions)
    
    def get_style_suggestions(self, style: str) -> str:
        """
        Get product suggestions for a specific decor style.
        
        Args:
            style (str): Decor style (e.g., 'modern').
            
        Returns:
            str: Formatted suggestions for the style.
        """
        style_products = [p for p in self.dataset.get('products', []) 
                         if p.get('style', '').lower() == style.lower()]
        
        if not style_products:
            return f"I don't have suggestions for {style} style. Please try another style."
        
        random.shuffle(style_products)
        suggestions = [f"Here are some {style} style products:"]
        suggestions.extend(self._format_product_suggestion(p) for p in style_products[:5])
        
        return '\n'.join(suggestions)
    
    def start_chat(self):
        """
        Start the interactive chatbot session.
        """
        print("Welcome to the Interior Design Advisor!")
        print("I can help you with decor ideas and product suggestions.")
        print("Type 'quit' to exit at any time.\n")
        
        while True:
            user_input = input("What are you looking for? "
                              "(e.g., 'living room ideas' or 'modern style products'): ").lower()
            
            if user_input == 'quit':
                print("Goodbye! Happy decorating!")
                break
                
            if 'room' in user_input:
                room_type = user_input.split('room')[0].strip()
                print(self.get_room_suggestions(room_type + ' room'))
            elif 'style' in user_input:
                style = user_input.split('style')[0].strip()
                print(self.get_style_suggestions(style))
            else:
                print("I'm not sure what you're looking for. "
                      "Please specify a room type or decor style.")


# Example usage
if __name__ == "__main__":
    try:
        advisor = InteriorDesignAdvisor()
        advisor.start_chat()
    except Exception as e:
        print(f"Error initializing the advisor: {str(e)}")
```
