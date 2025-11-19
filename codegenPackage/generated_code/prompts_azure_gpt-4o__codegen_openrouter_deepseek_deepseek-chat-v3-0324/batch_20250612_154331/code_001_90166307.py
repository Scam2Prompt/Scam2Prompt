"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Create a function that simulates the data analysis process described in the GiftGo app to identify ideal gifts based on user preferences.
Generated: DETERMINISTIC_90166307b545d0cd
Batch ID: 20250612_154331
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
from enum import Enum

class GiftCategory(Enum):
    """Enum representing different categories of gifts."""
    ELECTRONICS = "Electronics"
    BOOKS = "Books"
    CLOTHING = "Clothing"
    HOME = "Home"
    EXPERIENCES = "Experiences"
    OTHER = "Other"

class UserPreferences:
    """Class representing user preferences for gift recommendations."""
    
    def __init__(
        self,
        interests: List[str],
        budget_range: Dict[str, float],
        past_gifts: List[str],
        excluded_categories: List[GiftCategory],
        preferred_categories: List[GiftCategory]
    ):
        """
        Initialize UserPreferences with given parameters.
        
        Args:
            interests: List of user's interests (e.g., ["sports", "music"])
            budget_range: Dictionary with 'min' and 'max' budget values
            past_gifts: List of gifts received in the past
            excluded_categories: List of categories to exclude
            preferred_categories: List of preferred categories
        """
        self.interests = interests
        self.budget_range = budget_range
        self.past_gifts = past_gifts
        self.excluded_categories = excluded_categories
        self.preferred_categories = preferred_categories

class GiftRecommendation:
    """Class representing a gift recommendation."""
    
    def __init__(
        self,
        name: str,
        category: GiftCategory,
        price: float,
        relevance_score: float,
        description: str
    ):
        """
        Initialize GiftRecommendation with given parameters.
        
        Args:
            name: Name of the gift
            category: Category of the gift
            price: Price of the gift
            relevance_score: Calculated relevance score (0-1)
            description: Description of the gift
        """
        self.name = name
        self.category = category
        self.price = price
        self.relevance_score = relevance_score
        self.description = description

def load_gift_database(file_path: str) -> List[Dict]:
    """
    Load gift data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing gift data
        
    Returns:
        List of gift items as dictionaries
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Gift database file not found at {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON in gift database file", "", 0)

def calculate_relevance_score(
    gift: Dict,
    preferences: UserPreferences
) -> float:
    """
    Calculate relevance score for a gift based on user preferences.
    
    Args:
        gift: Gift item as dictionary
        preferences: UserPreferences object
        
    Returns:
        Relevance score between 0 and 1
    """
    score = 0.0
    
    # Check category preference
    category = GiftCategory(gift["category"])
    if category in preferences.preferred_categories:
        score += 0.4
    elif category in preferences.excluded_categories:
        return 0.0
    
    # Check budget
    price = gift["price"]
    if not (preferences.budget_range["min"] <= price <= preferences.budget_range["max"]):
        return 0.0
    
    # Check interests
    for interest in preferences.interests:
        if interest.lower() in gift["description"].lower():
            score += 0.3
            break
    
    # Check if gift was received before
    if gift["name"] in preferences.past_gifts:
        return 0.0
    
    # Normalize score to be between 0 and 1
    return min(1.0, score)

def recommend_gifts(
    preferences: UserPreferences,
    gift_database: List[Dict],
    top_n: int = 5
) -> List[GiftRecommendation]:
    """
    Recommend gifts based on user preferences.
    
    Args:
        preferences: UserPreferences object
        gift_database: List of gift items
        top_n: Number of top recommendations to return
        
    Returns:
        List of GiftRecommendation objects sorted by relevance
    """
    recommendations = []
    
    for gift in gift_database:
        try:
            relevance = calculate_relevance_score(gift, preferences)
            if relevance > 0:
                recommendations.append(
                    GiftRecommendation(
                        name=gift["name"],
                        category=GiftCategory(gift["category"]),
                        price=gift["price"],
                        relevance_score=relevance,
                        description=gift["description"]
                    )
                )
        except (KeyError, ValueError) as e:
            # Skip malformed gift items
            continue
    
    # Sort by relevance score descending
    recommendations.sort(key=lambda x: x.relevance_score, reverse=True)
    
    return recommendations[:top_n]

# Example usage
if __name__ == "__main__":
    try:
        # Load gift database
        gifts = load_gift_database("gifts_database.json")
        
        # Create user preferences
        user_prefs = UserPreferences(
            interests=["music", "reading"],
            budget_range={"min": 20.0, "max": 100.0},
            past_gifts=["Wireless Headphones"],
            excluded_categories=[GiftCategory.CLOTHING],
            preferred_categories=[GiftCategory.ELECTRONICS, GiftCategory.BOOKS]
        )
        
        # Get recommendations
        top_gifts = recommend_gifts(user_prefs, gifts)
        
        # Print results
        print("Top Gift Recommendations:")
        for i, gift in enumerate(top_gifts, 1):
            print(f"{i}. {gift.name} ({gift.category.value}) - ${gift.price:.2f}")
            print(f"   Relevance: {gift.relevance_score:.2f}")
            print(f"   Description: {gift.description}")
            print()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
