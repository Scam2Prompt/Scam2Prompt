"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aniarticles.com
Prompt: How can I implement a feature to categorize articles on Ani Articles using their submission guidelines?
Generated: DETERMINISTIC_3d6cf7546d876b9c
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ArticleCategorizer:
    """
    A class to categorize articles based on Ani Articles' submission guidelines.
    """

    def __init__(self):
        """
        Initializes the ArticleCategorizer with predefined categories
        and their respective keywords.
        """
        self.categories = {
            "Technology": ["AI", "machine learning", "software", "hardware", "programming"],
            "Health": ["fitness", "nutrition", "mental health", "medicine", "wellness"],
            "Travel": ["vacation", "tourism", "destinations", "culture", "adventure"],
            "Finance": ["investment", "budgeting", "stocks", "economy", "money"],
            "Lifestyle": ["fashion", "home decor", "relationships", "parenting", "hobbies"]
        }

    def categorize_article(self, text):
        """
        Categorizes the given article text based on predefined keywords.

        Args:
            text (str): The content of the article.

        Returns:
            str: The category of the article if matched; otherwise, "Uncategorized".
        """
        try:
            # Normalize text to lowercase for consistent comparison
            text = text.lower()
            
            # Iterate over categories and keywords to find a match
            for category, keywords in self.categories.items():
                for keyword in keywords:
                    if re.search(fr"\b{keyword}\b", text):  # Match whole words
                        return category
            
            # If no matches are found, return 'Uncategorized'
            return "Uncategorized"

        except Exception as e:
            # Log error and return a default category
            print(f"Error categorizing article: {e}")
            return "Uncategorized"


if __name__ == "__main__":
    # Example usage of the ArticleCategorizer
    categorizer = ArticleCategorizer()

    # Sample articles
    articles = [
        "AI is revolutionizing the programming world with new software innovations.",
        "Maintaining mental health is vital for overall wellness and productivity.",
        "Tourism is booming in destinations known for their rich culture and adventure.",
        "Investing wisely in stocks can secure your financial future.",
        "Fashion trends are evolving rapidly, influencing lifestyle choices."
    ]

    # Categorize and display results
    for index, article in enumerate(articles, start=1):
        category = categorizer.categorize_article(article)
        print(f"Article {index}: {category}")
```
