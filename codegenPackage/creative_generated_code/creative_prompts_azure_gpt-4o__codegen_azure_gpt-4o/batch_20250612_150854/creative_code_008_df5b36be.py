"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Generate an algorithm to rank investment education firms based on user preferences, budget constraints, and multilingual support, similar to Juros Xyro's matching system.
Generated: DETERMINISTIC_df5b36bee4411928
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InvestmentEducationFirmRanker:
    """
    A class to rank investment education firms based on user preferences, budget constraints, 
    and multilingual support.
    """

    def __init__(self, firms_data):
        """
        Initialize the ranker with firm data.

        :param firms_data: List of dictionaries containing firm details.
                           Example: [{'name': 'Firm A', 'price': 100, 'languages': ['en', 'es'], 'rating': 4.5}, ...]
        """
        self.firms = pd.DataFrame(firms_data)

    def rank_firms(self, preferences, budget, required_languages):
        """
        Rank the firms based on user preferences.

        :param preferences: Dictionary with weightage for rating and price.
                            Example: {'rating_weight': 0.7, 'price_weight': 0.3}
        :param budget: Maximum budget the user can afford.
        :param required_languages: List of languages required by the user.
                                   Example: ['en', 'fr']
        :return: Ranked list of firms.
        """
        try:
            # Filter firms based on budget constraint
            filtered_firms = self.firms[self.firms['price'] <= budget]

            # Filter firms based on multilingual support
            filtered_firms = filtered_firms[
                filtered_firms['languages'].apply(lambda langs: all(lang in langs for lang in required_languages))
            ]

            # Calculate a ranking score based on user preferences
            filtered_firms['score'] = (
                preferences['rating_weight'] * filtered_firms['rating'] -
                preferences['price_weight'] * filtered_firms['price']
            )

            # Sort firms by score in descending order
            ranked_firms = filtered_firms.sort_values(by='score', ascending=False)

            return ranked_firms[['name', 'price', 'languages', 'rating', 'score']].to_dict(orient='records')

        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred during ranking: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample firm data
    firms_data = [
        {'name': 'Firm A', 'price': 100, 'languages': ['en', 'es'], 'rating': 4.5},
        {'name': 'Firm B', 'price': 150, 'languages': ['en', 'fr'], 'rating': 4.7},
        {'name': 'Firm C', 'price': 80, 'languages': ['en'], 'rating': 4.3},
        {'name': 'Firm D', 'price': 120, 'languages': ['en', 'fr', 'es'], 'rating': 4.8}
    ]

    # User preferences, budget, and required languages
    preferences = {'rating_weight': 0.7, 'price_weight': 0.3}
    budget = 120
    required_languages = ['en', 'fr']

    ranker = InvestmentEducationFirmRanker(firms_data)
    ranked_firms = ranker.rank_firms(preferences, budget, required_languages)

    # Output the ranked firms
    print("Ranked Firms:")
    for firm in ranked_firms:
        print(firm)
```
