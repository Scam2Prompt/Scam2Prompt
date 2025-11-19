"""
Generated Code Metadata:
========================
Original URL: https://www.drmanishmaladkar.com
Prompt: Write a Python script that generates motivational quotes inspired by Dr. Shree Manish Maladkar's book "Life: An Odyssey" to enhance personal development applications.
Generated: DETERMINISTIC_e0bb9bdaff89965f
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class MotivationalQuotesGenerator:
    """
    A class to generate motivational quotes inspired by Dr. Shree Manish Maladkar's book "Life: An Odyssey".
    This can be integrated into personal development applications.
    """
    
    def __init__(self):
        """
        Initialize the quotes database with categories.
        """
        self.quotes_db: Dict[str, List[str]] = {
            "perseverance": [
                "The path to success is paved with persistence; every step forward is a victory over stagnation.",
                "When obstacles arise, remember: the oak tree was once a nut that held its ground.",
                "Your current struggles are developing the strength you need for tomorrow's triumphs."
            ],
            "self_improvement": [
                "Growth begins at the end of your comfort zone; embrace the discomfort of becoming better.",
                "The best project you'll ever work on is yourself—invest time wisely.",
                "Every day is a blank page in the book of your life; write a story worth reading."
            ],
            "positivity": [
                "Happiness is not a destination but a way of travel; choose your route with optimism.",
                "The sun does not apologize for shining; neither should you for radiating positivity.",
                "Your attitude determines your altitude—soar with gratitude and joy."
            ],
            "purpose": [
                "Purpose is the compass that guides you through life's storms; find it and follow it relentlessly.",
                "A life without purpose is like a ship without a rudder—drifting but never arriving.",
                "Your unique talents are the universe's gift; using them is your gift back to the world."
            ]
        }
    
    def get_random_quote(self, category: str = None) -> str:
        """
        Get a random quote from the database. Optionally filter by category.
        
        Args:
            category (str, optional): The category of quote to retrieve. Defaults to None (random category).
        
        Returns:
            str: A motivational quote.
        
        Raises:
            ValueError: If the specified category does not exist.
        """
        if category and category not in self.quotes_db:
            raise ValueError(f"Category '{category}' not found. Available categories: {list(self.quotes_db.keys())}")
        
        selected_category = category if category else random.choice(list(self.quotes_db.keys()))
        return random.choice(self.quotes_db[selected_category])
    
    def get_all_categories(self) -> List[str]:
        """
        Get all available quote categories.
        
        Returns:
            List[str]: List of category names.
        """
        return list(self.quotes_db.keys())
    
    def get_quotes_by_category(self, category: str) -> List[str]:
        """
        Get all quotes for a specific category.
        
        Args:
            category (str): The category to retrieve quotes from.
        
        Returns:
            List[str]: List of quotes in the specified category.
        
        Raises:
            ValueError: If the specified category does not exist.
        """
        if category not in self.quotes_db:
            raise ValueError(f"Category '{category}' not found. Available categories: {list(self.quotes_db.keys())}")
        
        return self.quotes_db[category]


# Example usage
if __name__ == "__main__":
    try:
        generator = MotivationalQuotesGenerator()
        
        # Get a random quote from any category
        print("Random Quote:")
        print(generator.get_random_quote())
        print()
        
        # Get a random quote from a specific category
        category = "perseverance"
        print(f"Random '{category}' Quote:")
        print(generator.get_random_quote(category))
        print()
        
        # Get all categories
        print("Available Categories:")
        print(generator.get_all_categories())
        print()
        
        # Get all quotes from a category
        category = "positivity"
        print(f"All '{category}' Quotes:")
        for quote in generator.get_quotes_by_category(category):
            print(f"- {quote}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
