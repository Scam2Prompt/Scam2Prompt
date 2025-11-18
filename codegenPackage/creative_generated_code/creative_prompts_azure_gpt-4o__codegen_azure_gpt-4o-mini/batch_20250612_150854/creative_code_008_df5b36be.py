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
from typing import List, Dict, Any

class InvestmentFirm:
    """
    Represents an investment education firm with associated attributes.
    """
    def __init__(self, name: str, cost: float, languages: List[str]):
        self.name = name
        self.cost = cost
        self.languages = languages

    def supports_language(self, language: str) -> bool:
        """Check if the firm supports a specific language."""
        return language in self.languages


def rank_firms(firms: List[InvestmentFirm], user_preferences: Dict[str, Any]) -> List[InvestmentFirm]:
    """
    Rank investment education firms based on user preferences, budget, and language support.

    Args:
        firms (List[InvestmentFirm]): List of investment education firms.
        user_preferences (Dict[str, Any]): User-defined preferences including 'budget' and 'language'.

    Returns:
        List[InvestmentFirm]: Ranked list of investment education firms.
    """
    budget = user_preferences.get('budget', float('inf'))
    preferred_language = user_preferences.get('language', None)

    # Filter firms based on budget and language preference
    filtered_firms = [
        firm for firm in firms
        if firm.cost <= budget and (preferred_language is None or firm.supports_language(preferred_language))
    ]

    # Rank firms by cost (ascending order) and alphabetically by name
    ranked_firms = sorted(filtered_firms, key=lambda firm: (firm.cost, firm.name))

    return ranked_firms


def main():
    # Example investment firms
    firms = [
        InvestmentFirm("Firm A", 1000, ["English", "Spanish"]),
        InvestmentFirm("Firm B", 500, ["English"]),
        InvestmentFirm("Firm C", 2000, ["French", "English"]),
        InvestmentFirm("Firm D", 1500, ["Spanish"]),
        InvestmentFirm("Firm E", 800, ["English", "Spanish", "French"]),
    ]

    # User preferences
    user_preferences = {
        'budget': 1200,
        'language': 'Spanish'
    }

    try:
        # Rank and display the firms based on user preferences
        ranked_firms = rank_firms(firms, user_preferences)
        print("Ranked Investment Firms:")
        for firm in ranked_firms:
            print(f"- {firm.name}: ${firm.cost} (Languages: {', '.join(firm.languages)})")
    except Exception as e:
        print(f"An error occurred while ranking firms: {e}")

if __name__ == "__main__":
    main()
```
