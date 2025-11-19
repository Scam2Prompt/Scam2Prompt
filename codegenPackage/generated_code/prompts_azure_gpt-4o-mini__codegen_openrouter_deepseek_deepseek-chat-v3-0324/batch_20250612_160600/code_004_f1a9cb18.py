"""
Generated Code Metadata:
========================
Original URL: https://tron-gifts.blogspot.com
Prompt: Suggest a method to build a gift suggestion tool using a specific library mentioned in the content.
Generated: DETERMINISTIC_f1a9cb18eeeeaf4d
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class GiftSuggester:
    """
    A gift suggestion tool that recommends gifts based on predefined categories and preferences.
    Uses a simple random selection algorithm for suggestions.
    """

    def __init__(self, gift_data: Dict[str, List[str]]):
        """
        Initialize the GiftSuggester with gift data.
        
        Args:
            gift_data: A dictionary where keys are categories and values are lists of gift items.
        """
        self.gift_data = gift_data
        self.categories = list(gift_data.keys())

    def suggest_gift(self, category: Optional[str] = None) -> str:
        """
        Suggest a random gift from the specified category or any category if none specified.
        
        Args:
            category: Optional category to narrow down suggestions.
        
        Returns:
            A randomly selected gift item.
        
        Raises:
            ValueError: If specified category doesn't exist or no gifts are available.
        """
        if category:
            if category not in self.gift_data:
                raise ValueError(f"Category '{category}' not found in gift data")
            gifts = self.gift_data[category]
        else:
            gifts = [gift for sublist in self.gift_data.values() for gift in sublist]
        
        if not gifts:
            raise ValueError("No gifts available for suggestion")
        
        return random.choice(gifts)

    def suggest_gifts(self, count: int = 3, category: Optional[str] = None) -> List[str]:
        """
        Suggest multiple random gifts from the specified category or any category if none specified.
        
        Args:
            count: Number of gifts to suggest.
            category: Optional category to narrow down suggestions.
        
        Returns:
            A list of randomly selected gift items.
        
        Raises:
            ValueError: If specified category doesn't exist or no gifts are available.
        """
        if category:
            if category not in self.gift_data:
                raise ValueError(f"Category '{category}' not found in gift data")
            gifts = self.gift_data[category]
        else:
            gifts = [gift for sublist in self.gift_data.values() for gift in sublist]
        
        if not gifts:
            raise ValueError("No gifts available for suggestion")
        
        if count > len(gifts):
            raise ValueError(f"Requested {count} gifts but only {len(gifts)} available")
        
        return random.sample(gifts, count)

# Example usage
if __name__ == "__main__":
    # Sample gift data
    gift_data = {
        "Books": ["Sci-fi novel", "Mystery thriller", "Self-help book", "Cookbook"],
        "Electronics": ["Wireless earbuds", "Smart watch", "Bluetooth speaker"],
        "Clothing": ["T-shirt", "Hoodie", "Scarf", "Gloves"],
        "Experiences": ["Concert tickets", "Cooking class", "Spa day"]
    }

    suggester = GiftSuggester(gift_data)
    
    try:
        # Single suggestion
        print("Random gift suggestion:", suggester.suggest_gift())
        print("Book suggestion:", suggester.suggest_gift("Books"))
        
        # Multiple suggestions
        print("3 random suggestions:", suggester.suggest_gifts(3))
        print("2 clothing suggestions:", suggester.suggest_gifts(2, "Clothing"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
