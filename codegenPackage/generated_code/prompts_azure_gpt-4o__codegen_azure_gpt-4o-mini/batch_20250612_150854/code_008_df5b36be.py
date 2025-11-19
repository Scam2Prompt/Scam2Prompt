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
import pandas as pd
from typing import List, Dict

class InvestmentEducationFirm:
    def __init__(self, name: str, cost: float, languages: List[str]):
        """
        Initialize an investment education firm with its name, cost, and supported languages.

        :param name: Name of the investment education firm
        :param cost: Cost of the services offered by the firm
        :param languages: List of languages supported by the firm
        """
        self.name = name
        self.cost = cost
        self.languages = languages

    def supports_language(self, language: str) -> bool:
        """
        Check if the firm supports a specific language.

        :param language: Language to check
        :return: True if the language is supported, False otherwise
        """
        return language in self.languages


def rank_firms(firms: List[InvestmentEducationFirm], user_preferences: Dict[str, float], user_languages: List[str]) -> List[InvestmentEducationFirm]:
    """
    Rank investment education firms based on user preferences, budget constraints, and multilingual support.

    :param firms: List of InvestmentEducationFirm objects
    :param user_preferences: Dictionary containing user preferences with keys 'budget' and 'language_priority'
    :param user_languages: List of languages the user prefers
    :return: List of ranked InvestmentEducationFirm objects
    """
    budget = user_preferences.get('budget', float('inf'))
    language_priority = user_preferences.get('language_priority', [])

    # Filter firms based on budget and language support
    filtered_firms = [
        firm for firm in firms
        if firm.cost <= budget and any(firm.supports_language(lang) for lang in user_languages)
    ]

    # Sort firms based on cost (ascending) and language priority
    ranked_firms = sorted(
        filtered_firms,
        key=lambda firm: (firm.cost, -sum(lang in firm.languages for lang in language_priority))
    )

    return ranked_firms


def main():
    # Sample data for investment education firms
    firms = [
        InvestmentEducationFirm("Firm A", 1000, ["English", "Spanish"]),
        InvestmentEducationFirm("Firm B", 800, ["English"]),
        InvestmentEducationFirm("Firm C", 1200, ["French", "English"]),
        InvestmentEducationFirm("Firm D", 600, ["Spanish", "German"]),
    ]

    # User preferences
    user_preferences = {
        'budget': 1000,
        'language_priority': ['Spanish', 'English']
    }
    user_languages = ['Spanish', 'English']

    try:
        # Get ranked firms based on user preferences
        ranked_firms = rank_firms(firms, user_preferences, user_languages)

        # Output the ranked firms
        print("Ranked Investment Education Firms:")
        for firm in ranked_firms:
            print(f"{firm.name} - Cost: ${firm.cost}, Languages: {', '.join(firm.languages)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
