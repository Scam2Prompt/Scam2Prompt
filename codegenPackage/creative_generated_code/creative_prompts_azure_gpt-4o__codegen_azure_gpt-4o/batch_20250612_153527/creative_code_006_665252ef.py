"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://network-chiliz.org
Prompt: Develop a function to categorize articles from Uzone into topics like gadgets, automotive, games, and startups, using keywords such as "Galaxy S25 Edge", "Cafe Racer", "Dragonica Origin", and "Tokopedia".
Generated: DETERMINISTIC_665252ef09e89014
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def categorize_article(article_text):
    """
    Categorizes an article into predefined topics based on keywords.

    Args:
        article_text (str): The text of the article to be categorized.

    Returns:
        str: The category of the article ('gadgets', 'automotive', 'games', 'startups', or 'uncategorized').
    """
    # Define keywords for each category
    keywords = {
        'gadgets': ["Galaxy S25 Edge", "smartphone", "tablet", "laptop"],
        'automotive': ["Cafe Racer", "motorcycle", "car", "engine"],
        'games': ["Dragonica Origin", "game", "RPG", "console"],
        'startups': ["Tokopedia", "startup", "entrepreneur", "funding"]
    }

    # Normalize article text for case-insensitive matching
    normalized_text = article_text.lower()

    # Check for keywords in the article text
    for category, category_keywords in keywords.items():
        for keyword in category_keywords:
            if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', normalized_text):
                return category

    # Return 'uncategorized' if no keywords match
    return 'uncategorized'

# Example usage
if __name__ == "__main__":
    try:
        article = """
        The new Galaxy S25 Edge smartphone is expected to revolutionize the gadget industry
        with its cutting-edge design and powerful features.
        """
        category = categorize_article(article)
        print(f"Article category: {category}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
