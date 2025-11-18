"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Write code to simulate the backend logic of the GiftGo app, focusing on analyzing user data to find suitable gifts.
Generated: DETERMINISTIC_07269bd74e1648f1
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Simulate a database of available gifts
GIFTS_DATABASE = [
    {"id": 1, "name": "Wireless Headphones", "categories": ["electronics", "music"], "price": 99.99},
    {"id": 2, "name": "Art Set", "categories": ["art", "craft"], "price": 49.99},
    {"id": 3, "name": "Fitness Tracker", "categories": ["fitness", "electronics"], "price": 79.99},
    {"id": 4, "name": "Gourmet Chocolate Box", "categories": ["food", "luxury"], "price": 29.99},
    {"id": 5, "name": "Cookbook", "categories": ["food", "cooking"], "price": 19.99}
]

# Simulate user data
USER_DATA = [
    {"id": 101, "preferences": ["fitness", "electronics"], "budget": 100},
    {"id": 102, "preferences": ["art", "craft"], "budget": 50},
    {"id": 103, "preferences": ["food", "luxury"], "budget": 30},
    {"id": 104, "preferences": ["cooking"], "budget": 25}
]

def find_suitable_gifts(user_preferences: List[str], user_budget: float) -> List[Dict]:
    """
    Find suitable gifts based on user preferences and budget.

    Args:
        user_preferences (List[str]): Categories the user is interested in.
        user_budget (float): Maximum price the user is willing to pay.

    Returns:
        List[Dict]: List of gifts matching the user's preferences and budget.
    """
    suitable_gifts = []

    for gift in GIFTS_DATABASE:
        # Check if the gift matches any of the user's preferences and is within budget
        if set(user_preferences).intersection(gift["categories"]) and gift["price"] <= user_budget:
            suitable_gifts.append(gift)

    return suitable_gifts

def get_gift_recommendations() -> Dict[int, List[Dict]]:
    """
    Generate gift recommendations for all users.

    Returns:
        Dict[int, List[Dict]]: A dictionary where keys are user IDs and values are lists of recommended gifts.
    """
    recommendations = {}

    for user in USER_DATA:
        user_id = user["id"]
        preferences = user["preferences"]
        budget = user["budget"]

        # Find suitable gifts for each user
        recommendations[user_id] = find_suitable_gifts(preferences, budget)

    return recommendations

def main():
    """
    Main function to simulate the GiftGo app backend logic.
    """
    try:
        # Get gift recommendations for all users
        recommendations = get_gift_recommendations()

        # Output the recommendations in JSON format for clarity
        print(json.dumps(recommendations, indent=4))

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()
```
