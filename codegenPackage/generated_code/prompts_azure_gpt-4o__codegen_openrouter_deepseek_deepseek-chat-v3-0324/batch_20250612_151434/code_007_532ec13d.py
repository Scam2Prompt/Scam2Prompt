"""
Generated Code Metadata:
========================
Original URL: https://unitedairlines-vn.com
Prompt: Develop a program to assist users in selecting the best United Airlines ticket class (e.g., Economy, Economy Plus, Business First) based on their preferences and the descriptions provided by United Airlines Vietnam.
Generated: DETERMINISTIC_532ec13d8aa18ab5
Batch ID: 20250612_151434
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

class UnitedAirlinesTicketSelector:
    """
    A program to assist users in selecting the best United Airlines ticket class
    based on their preferences and the descriptions provided by United Airlines Vietnam.
    """
    
    def __init__(self):
        self.ticket_classes = self._load_ticket_classes()
    
    def _load_ticket_classes(self) -> Dict[str, Dict[str, str]]:
        """
        Load the ticket class descriptions and features from a JSON file.
        
        Returns:
            Dict[str, Dict[str, str]]: A dictionary of ticket classes with their features.
        """
        try:
            with open('united_airlines_ticket_classes.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Ticket class data file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in ticket class data file.")
    
    def get_available_classes(self) -> List[str]:
        """
        Get a list of available ticket classes.
        
        Returns:
            List[str]: List of available ticket class names.
        """
        return list(self.ticket_classes.keys())
    
    def get_class_features(self, ticket_class: str) -> Dict[str, str]:
        """
        Get the features of a specific ticket class.
        
        Args:
            ticket_class (str): The name of the ticket class.
            
        Returns:
            Dict[str, str]: Dictionary of features for the ticket class.
            
        Raises:
            ValueError: If the ticket class is not found.
        """
        if ticket_class not in self.ticket_classes:
            raise ValueError(f"Ticket class '{ticket_class}' not found.")
        return self.ticket_classes[ticket_class]
    
    def recommend_ticket_class(self, preferences: Dict[str, int]) -> Optional[str]:
        """
        Recommend the best ticket class based on user preferences.
        
        Args:
            preferences (Dict[str, int]): Dictionary of user preferences with feature names as keys
                                         and importance scores (1-5) as values.
                                         
        Returns:
            Optional[str]: The recommended ticket class name, or None if no match is found.
        """
        if not preferences:
            return None
            
        best_class = None
        best_score = -1
        
        for ticket_class, features in self.ticket_classes.items():
            score = 0
            for feature, importance in preferences.items():
                if feature in features:
                    score += importance
            
            if score > best_score:
                best_score = score
                best_class = ticket_class
        
        return best_class

def main():
    """
    Main function to interact with the user and provide ticket class recommendations.
    """
    selector = UnitedAirlinesTicketSelector()
    
    print("Welcome to United Airlines Ticket Class Selector")
    print("Available ticket classes:", ", ".join(selector.get_available_classes()))
    
    # Sample preferences - in a real app, these would be collected from user input
    preferences = {
        "legroom": 5,
        "meal_service": 4,
        "priority_boarding": 3,
        "baggage_allowance": 4,
        "seat_recline": 2
    }
    
    print("\nYour preferences:")
    for feature, importance in preferences.items():
        print(f"- {feature}: {importance}/5")
    
    recommended_class = selector.recommend_ticket_class(preferences)
    
    if recommended_class:
        print(f"\nRecommended ticket class: {recommended_class}")
        print("Features:")
        features = selector.get_class_features(recommended_class)
        for feature, description in features.items():
            print(f"- {feature}: {description}")
    else:
        print("\nNo ticket class matches your preferences.")

if __name__ == "__main__":
    main()
```

Note: This code assumes the existence of a JSON file named `united_airlines_ticket_classes.json` with the following structure (example):

```json
{
    "Economy": {
        "legroom": "Standard legroom",
        "meal_service": "Complimentary snacks and drinks",
        "priority_boarding": "Not available",
        "baggage_allowance": "1 carry-on bag",
        "seat_recline": "Limited recline"
    },
    "Economy Plus": {
        "legroom": "Extra legroom",
        "meal_service": "Complimentary snacks and drinks",
        "priority_boarding": "Available for an additional fee",
        "baggage_allowance": "1 carry-on bag",
        "seat_recline": "Standard recline"
    },
    "Business First": {
        "legroom": "Spacious legroom",
        "meal_service": "Gourmet meals with premium drinks",
        "priority_boarding": "Included",
        "baggage_allowance": "2 checked bags + carry-on",
        "seat_recline": "Fully reclining seats"
    }
}
```
