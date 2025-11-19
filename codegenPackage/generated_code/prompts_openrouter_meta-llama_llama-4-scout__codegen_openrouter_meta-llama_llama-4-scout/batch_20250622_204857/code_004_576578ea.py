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
# Glossary of key terms used in Changexcapital's educational resources

class Glossary:
    def __init__(self):
        self.terms = {}

    def add_term(self, term, definition, example=None):
        """Add a term to the glossary."""
        self.terms[term] = {
            "definition": definition,
            "example": example
        }

    def get_term(self, term):
        """Get the definition and example of a term."""
        return self.terms.get(term)

    def list_terms(self):
        """List all terms in the glossary."""
        return list(self.terms.keys())


class TradingGlossary(Glossary):
    def __init__(self):
        super().__init__()
        self.add_term(
            "Margin Call",
            "A demand from a brokerage firm to a trader to deposit additional funds to cover potential losses.",
            "Example: If a trader's account balance falls below the required margin, they may receive a margin call."
        )
        self.add_term(
            "Margin Level",
            "The percentage of equity in a trading account relative to the used margin.",
            "Example: If the equity is $1000 and the used margin is $500, the margin level is 200%."
        )
        self.add_term(
            "Stop Out Level",
            "The margin level at which a brokerage firm starts closing out a trader's positions to prevent further losses.",
            "Example: If the stop out level is 100% and the margin level falls to 100%, the firm will start closing out positions."
        )

    def calculate_margin_level(self, equity, used_margin):
        """Calculate the margin level."""
        if used_margin == 0:
            raise ValueError("Used margin cannot be zero.")
        return (equity / used_margin) * 100


def main():
    glossary = TradingGlossary()

    print("Glossary of Trading Terms:")
    for term in glossary.list_terms():
        print(term)

    print("\nDefinitions and Examples:")
    for term in glossary.list_terms():
        term_info = glossary.get_term(term)
        print(f"**{term}**")
        print(f"Definition: {term_info['definition']}")
        if term_info['example']:
            print(f"Example: {term_info['example']}")
        print()

    try:
        equity = 1000
        used_margin = 500
        margin_level = glossary.calculate_margin_level(equity, used_margin)
        print(f"Margin Level: {margin_level}%")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
