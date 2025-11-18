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
from typing import List, Dict

def categorize_articles(articles: List[str]) -> Dict[str, List[str]]:
    """
    Categorizes a list of articles into predefined topics based on keywords.

    Args:
        articles (List[str]): A list of article titles or contents to categorize.

    Returns:
        Dict[str, List[str]]: A dictionary where keys are topic names and values are lists of articles
                               that belong to those topics.
    
    Raises:
        ValueError: If articles is not a list of strings.
    """
    
    if not isinstance(articles, list) or not all(isinstance(article, str) for article in articles):
        raise ValueError("Input must be a list of strings")

    # Define the keywords for each category
    categories = {
        "gadgets": ["Galaxy S25 Edge"],
        "automotive": ["Cafe Racer"],
        "games": ["Dragonica Origin"],
        "startups": ["Tokopedia"]
    }

    # Initialize a dictionary to hold categorized articles
    categorized_articles = {category: [] for category in categories}

    # Iterate over each article to categorize it
    for article in articles:
        found_category = False
        for category, keywords in categories.items():
            if any(re.search(r'\b' + re.escape(keyword) + r'\b', article, re.IGNORECASE) for keyword in keywords):
                categorized_articles[category].append(article)
                found_category = True
                break  # Stop checking other categories once one is found
        
        # If no category matches, you can choose to handle it differently if needed
        if not found_category:
            categorized_articles.setdefault("uncategorized", []).append(article)

    return categorized_articles

# Example usage
if __name__ == "__main__":
    articles = [
        "Latest features of Galaxy S25 Edge",
        "The rise of Cafe Racer culture",
        "Dragonica Origin: A new era in gaming",
        "Innovations by Tokopedia in the e-commerce space",
        "An article about cooking"
    ]

    try:
        categorized = categorize_articles(articles)
        print(categorized)
    except ValueError as e:
        print(f"Error: {e}")
```
