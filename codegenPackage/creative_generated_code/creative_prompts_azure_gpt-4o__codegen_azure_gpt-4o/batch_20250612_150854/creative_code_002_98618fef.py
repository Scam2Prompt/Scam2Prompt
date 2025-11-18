"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Create a function in Python that categorizes investment types (e.g., cryptocurrencies, forex, mutual funds) based on the descriptions provided by Immediate Peak.
Generated: DETERMINISTIC_98618fef221318aa
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for error handling and type hinting
from typing import List, Dict

def categorize_investments(descriptions: List[str]) -> Dict[str, List[str]]:
    """
    Categorizes investment types based on the descriptions provided.

    Args:
        descriptions (List[str]): A list of strings, where each string is a description of an investment.

    Returns:
        Dict[str, List[str]]: A dictionary where keys are investment categories and values are lists of descriptions
                              that belong to those categories.

    Raises:
        ValueError: If any description is empty or invalid.
    """
    # Define investment categories with associated keywords
    categories = {
        "Cryptocurrencies": ["bitcoin", "ethereum", "crypto", "blockchain", "digital currency"],
        "Forex": ["foreign exchange", "currency pairs", "forex", "FX trading"],
        "Mutual Funds": ["fund", "mutual", "portfolio", "equity fund", "investment fund"],
        "Stocks": ["stock", "shares", "equity", "NASDAQ", "NYSE"],
        "Bonds": ["bond", "fixed income", "treasury", "debt", "corporate bond"],
        "Real Estate": ["real estate", "property", "land", "housing market"],
        "Commodities": ["gold", "silver", "oil", "commodity", "raw material"]
    }

    # Initialize the result dictionary
    categorized_investments = {category: [] for category in categories}

    # Validate and process each description
    for description in descriptions:
        if not description or not isinstance(description, str):
            raise ValueError("Invalid description provided. Each description must be a non-empty string.")

        # Normalize the description to lowercase for keyword matching
        normalized_description = description.lower()

        # Flag to check if the description has been categorized
        categorized = False

        # Match the description to the appropriate category based on keywords
        for category, keywords in categories.items():
            if any(keyword in normalized_description for keyword in keywords):
                categorized_investments[category].append(description)
                categorized = True
                break  # Stop searching once a match is found

        # If no category matches, classify as "Uncategorized"
        if not categorized:
            if "Uncategorized" not in categorized_investments:
                categorized_investments["Uncategorized"] = []
            categorized_investments["Uncategorized"].append(description)

    return categorized_investments

# Example usage:
if __name__ == "__main__":
    investment_descriptions = [
        "Bitcoin and other digital currencies are gaining popularity.",
        "Investing in foreign exchange requires understanding currency pairs.",
        "Mutual funds provide a diversified portfolio for investors.",
        "Buying stocks in tech companies can be lucrative.",
        "Government bonds are considered low-risk investments.",
        "Real estate market is booming in urban areas.",
        "Gold is a traditional commodity investment.",
        "An unknown investment strategy."
    ]

    try:
        result = categorize_investments(investment_descriptions)
        for category, items in result.items():
            print(f"{category}:")
            for item in items:
                print(f"  - {item}")
    except ValueError as e:
        print(f"Error: {e}")
```
