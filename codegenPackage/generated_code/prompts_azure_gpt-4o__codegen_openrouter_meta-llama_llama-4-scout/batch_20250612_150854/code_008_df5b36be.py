"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Generate an algorithm to rank investment education firms based on user preferences, budget constraints, and multilingual support, similar to Juros Xyro's matching system.
Generated: DETERMINISTIC_df5b36bee4411928
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from enum import Enum
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    PORTUGUESE = "pt"

class InvestmentEducationFirm:
    def __init__(self, id: int, name: str, languages: List[Language], min_budget: float, max_budget: float, rating: float):
        self.id = id
        self.name = name
        self.languages = languages
        self.min_budget = min_budget
        self.max_budget = max_budget
        self.rating = rating

class UserPreference:
    def __init__(self, budget: float, languages: List[Language], min_rating: float):
        self.budget = budget
        self.languages = languages
        self.min_rating = min_rating

def rank_investment_firms(firms: List[InvestmentEducationFirm], user_preference: UserPreference) -> List[Dict]:
    """
    Rank investment education firms based on user preferences, budget constraints, and multilingual support.

    Args:
    firms (List[InvestmentEducationFirm]): A list of investment education firms.
    user_preference (UserPreference): A user preference object.

    Returns:
    List[Dict]: A list of dictionaries containing the ranked firms and their scores.
    """
    ranked_firms = []

    for firm in firms:
        # Check if firm supports user's preferred languages
        language_score = len(set(firm.languages) & set(user_preference.languages))

        # Check if firm is within user's budget
        budget_score = 0
        if firm.min_budget <= user_preference.budget <= firm.max_budget:
            budget_score = 1

        # Calculate rating score
        rating_score = 0
        if firm.rating >= user_preference.min_rating:
            rating_score = 1

        # Calculate overall score
        score = language_score + budget_score + rating_score

        # Store firm and score in ranked_firms list
        ranked_firms.append({
            "firm": firm,
            "score": score,
            "language_score": language_score,
            "budget_score": budget_score,
            "rating_score": rating_score
        })

    # Sort ranked_firms list in descending order of score
    ranked_firms.sort(key=lambda x: x["score"], reverse=True)

    # Return ranked firms with scores
    return [{"id": firm["firm"].id, "name": firm["firm"].name, "score": firm["score"]} for firm in ranked_firms]

def main():
    try:
        # Create investment education firms
        firms = [
            InvestmentEducationFirm(1, "Firm A", [Language.ENGLISH, Language.SPANISH], 1000.0, 5000.0, 4.5),
            InvestmentEducationFirm(2, "Firm B", [Language.ENGLISH, Language.FRENCH], 500.0, 2000.0, 4.0),
            InvestmentEducationFirm(3, "Firm C", [Language.ENGLISH, Language.GERMAN], 2000.0, 10000.0, 4.8),
        ]

        # Create user preference
        user_preference = UserPreference(3000.0, [Language.ENGLISH, Language.SPANISH], 4.2)

        # Rank investment education firms
        ranked_firms = rank_investment_firms(firms, user_preference)

        # Print ranked firms
        logger.info("Ranked Firms:")
        for firm in ranked_firms:
            logger.info(f"ID: {firm['id']}, Name: {firm['name']}, Score: {firm['score']}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
