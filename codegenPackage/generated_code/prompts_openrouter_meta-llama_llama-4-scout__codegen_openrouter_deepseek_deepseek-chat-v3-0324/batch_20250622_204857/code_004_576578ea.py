"""
Generated Code Metadata:
========================
Original URL: https://pass-vee.com
Prompt: Create a glossary of key terms used in Changexcapital's educational resources, including definitions for terms like "Margin Call," "Margin Level," and "Stop Out Level," and provide examples of how they are applied in trading scenarios.
Generated: DETERMINISTIC_576578eafa2ad0e8
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingGlossary:
    """
    A glossary of key trading terms used in Changexcapital's educational resources.
    Each term includes a definition and an example application in trading scenarios.
    """

    def __init__(self):
        self.glossary = {
            "Margin Call": {
                "definition": "A broker's demand that an investor deposits additional money or securities "
                             "so that the margin account is brought up to the minimum maintenance margin.",
                "example": "If a trader's equity falls below the required margin level, the broker issues "
                          "a margin call requiring the trader to deposit more funds or close positions."
            },
            "Margin Level": {
                "definition": "The ratio of equity to margin, expressed as a percentage. It is used to "
                             "assess the account's health and risk level.",
                "example": "Margin Level = (Equity / Used Margin) * 100. A margin level of 100% means "
                          "equity equals used margin, indicating high risk."
            },
            "Stop Out Level": {
                "definition": "The predetermined level at which a broker automatically closes a trader's "
                             "positions to prevent further losses when margin level falls too low.",
                "example": "If a broker's stop out level is 20%, when the margin level reaches 20%, "
                          "positions are automatically closed starting with the most unprofitable ones."
            },
            "Leverage": {
                "definition": "The use of borrowed capital to increase the potential return of an investment.",
                "example": "With 1:100 leverage, a trader can control a $100,000 position with just $1,000."
            },
            "Spread": {
                "definition": "The difference between the bid (sell) price and the ask (buy) price of an asset.",
                "example": "If EUR/USD bid is 1.1000 and ask is 1.1002, the spread is 2 pips."
            },
            "Pip": {
                "definition": "The smallest price move that a given exchange rate can make based on market convention.",
                "example": "If EUR/USD moves from 1.1050 to 1.1051, it has moved 1 pip."
            },
            "Lot": {
                "definition": "A standardized quantity of a financial instrument being traded.",
                "example": "A standard lot is 100,000 units of the base currency in forex trading."
            }
        }

    def get_term(self, term: str) -> dict:
        """
        Retrieve the definition and example for a given trading term.

        Args:
            term (str): The trading term to look up.

        Returns:
            dict: Contains 'definition' and 'example' keys if term exists, None otherwise.

        Raises:
            ValueError: If the term is not found in the glossary.
        """
        if term not in self.glossary:
            raise ValueError(f"Term '{term}' not found in glossary.")
        return self.glossary[term]

    def list_terms(self) -> list:
        """
        List all available terms in the glossary.

        Returns:
            list: Alphabetically sorted list of all terms.
        """
        return sorted(self.glossary.keys())


# Example usage
if __name__ == "__main__":
    glossary = TradingGlossary()

    # List all terms
    print("Available terms:")
    for term in glossary.list_terms():
        print(f"- {term}")

    # Get details for a specific term
    try:
        term_info = glossary.get_term("Margin Call")
        print("\nMargin Call:")
        print(f"Definition: {term_info['definition']}")
        print(f"Example: {term_info['example']}")
    except ValueError as e:
        print(f"Error: {e}")
```
