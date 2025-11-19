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
class GlossaryEntry:
    """
    A class to represent a glossary entry for trading terms.
    """

    def __init__(self, term: str, definition: str, example: str):
        """
        Initializes a new glossary entry.

        :param term: The trading term.
        :param definition: The definition of the term.
        :param example: An example of how the term is applied in trading.
        """
        self.term = term
        self.definition = definition
        self.example = example

    def __str__(self):
        """
        Returns a string representation of the glossary entry.
        """
        return f"{self.term}: {self.definition}\nExample: {self.example}"


class TradingGlossary:
    """
    A class to manage a glossary of trading terms.
    """

    def __init__(self):
        """
        Initializes the glossary with an empty list of entries.
        """
        self.entries = []

    def add_entry(self, entry: GlossaryEntry):
        """
        Adds a new entry to the glossary.

        :param entry: An instance of GlossaryEntry to be added.
        """
        if not isinstance(entry, GlossaryEntry):
            raise ValueError("entry must be an instance of GlossaryEntry")
        self.entries.append(entry)

    def get_entry(self, term: str) -> str:
        """
        Retrieves the definition and example of a term.

        :param term: The term to look up in the glossary.
        :return: The string representation of the glossary entry.
        :raises ValueError: If the term is not found in the glossary.
        """
        for entry in self.entries:
            if entry.term.lower() == term.lower():
                return str(entry)
        raise ValueError(f"Term '{term}' not found in the glossary.")

    def list_entries(self) -> str:
        """
        Lists all entries in the glossary.

        :return: A string representation of all glossary entries.
        """
        return "\n\n".join(str(entry) for entry in self.entries)


# Example usage
if __name__ == "__main__":
    glossary = TradingGlossary()

    # Adding glossary entries
    glossary.add_entry(GlossaryEntry(
        term="Margin Call",
        definition="A demand by a broker that an investor deposit additional money or securities to cover possible losses.",
        example="If the equity in your trading account falls below the required margin level, your broker may issue a margin call."
    ))

    glossary.add_entry(GlossaryEntry(
        term="Margin Level",
        definition="A percentage that indicates the amount of equity in a trading account relative to the margin used.",
        example="If your account equity is $10,000 and you have $1,000 in margin used, your margin level is 1000%."
    ))

    glossary.add_entry(GlossaryEntry(
        term="Stop Out Level",
        definition="The level at which a broker will automatically close open positions to prevent further losses.",
        example="If your stop out level is set at 50%, and your equity falls below this level, your positions will be closed."
    ))

    # Displaying glossary entries
    print(glossary.list_entries())

    # Example of retrieving a specific entry
    try:
        print(glossary.get_entry("Margin Call"))
    except ValueError as e:
        print(e)
```
