"""
Generated Code Metadata:
========================
Original URL: https://baamgift.info
Prompt: Generate a list of gift card categories and their corresponding descriptions for an e-commerce platform, including Google Play, PlayStation, and Xbox gift cards.
Generated: DETERMINISTIC_ac2b5ef4d585b3fe
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gift_card_categories.py
# Defines a list of gift card categories and their descriptions for an e-commerce platform

from typing import List, Dict

def get_gift_card_categories() -> List[Dict[str, str]]:
    """
    Returns a list of gift card categories with their descriptions.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary contains
                             'category' and 'description' keys.
    """
    categories = [
        {
            "category": "Google Play",
            "description": "Redeemable for apps, games, movies, books, and more on Google Play."
        },
        {
            "category": "PlayStation",
            "description": "Use to purchase games, add-ons, subscriptions, and more on PlayStation Store."
        },
        {
            "category": "Xbox",
            "description": "Redeemable for games, movies, TV shows, and subscriptions on Microsoft Store."
        },
        {
            "category": "Amazon",
            "description": "Shop millions of products across various categories on Amazon."
        },
        {
            "category": "Apple",
            "description": "Use for apps, games, music, movies, books, and more on Apple services."
        },
        {
            "category": "Steam",
            "description": "Purchase games, software, and other digital content on Steam."
        },
        {
            "category": "Netflix",
            "description": "Redeem for Netflix subscription to watch TV shows and movies."
        },
        {
            "category": "Spotify",
            "description": "Use for Spotify Premium subscriptions to enjoy ad-free music."
        },
        {
            "category": "Uber",
            "description": "Redeem for rides or Uber Eats orders on the Uber platform."
        },
        {
            "category": "Airbnb",
            "description": "Use towards stays at unique homes and experiences worldwide."
        }
    ]
    
    return categories


if __name__ == "__main__":
    # Example usage
    gift_cards = get_gift_card_categories()
    for card in gift_cards:
        print(f"{card['category']}: {card['description']}")
```
