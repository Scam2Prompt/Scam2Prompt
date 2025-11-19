"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Generate a code snippet for a party planning application that includes features for organizing children's birthday parties, including customizable themes and entertainment options as described on Wonderplanet.ee.
Generated: DETERMINISTIC_1546cee2d70f63bf
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class PartyTheme:
    """Represents a customizable party theme."""
    def __init__(self, name: str, description: str, cost: float):
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self):
        return f"PartyTheme(name={self.name}, description={self.description}, cost={self.cost})"


class EntertainmentOption:
    """Represents an entertainment option for the party."""
    def __init__(self, name: str, duration: int, cost: float):
        self.name = name
        self.duration = duration  # in minutes
        self.cost = cost

    def __repr__(self):
        return f"EntertainmentOption(name={self.name}, duration={self.duration}, cost={self.cost})"


class BirthdayParty:
    """Represents a birthday party with themes and entertainment options."""
    def __init__(self, child_name: str, age: int):
        self.child_name = child_name
        self.age = age
        self.themes: List[PartyTheme] = []
        self.entertainments: List[EntertainmentOption] = []

    def add_theme(self, theme: PartyTheme):
        """Add a theme to the birthday party."""
        self.themes.append(theme)

    def add_entertainment(self, entertainment: EntertainmentOption):
        """Add an entertainment option to the birthday party."""
        self.entertainments.append(entertainment)

    def total_cost(self) -> float:
        """Calculate the total cost of the party."""
        theme_cost = sum(theme.cost for theme in self.themes)
        entertainment_cost = sum(ent.cost for ent in self.entertainments)
        return theme_cost + entertainment_cost

    def party_summary(self) -> Dict[str, Optional[List[str]]]:
        """Generate a summary of the birthday party."""
        return {
            "child_name": self.child_name,
            "age": self.age,
            "themes": [theme.name for theme in self.themes],
            "entertainments": [ent.name for ent in self.entertainments],
            "total_cost": self.total_cost()
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Create themes
        pirate_theme = PartyTheme("Pirate Adventure", "A thrilling pirate-themed party.", 150.00)
        fairy_theme = PartyTheme("Fairy Tale", "A magical fairy tale experience.", 200.00)

        # Create entertainment options
        clown_show = EntertainmentOption("Clown Show", 60, 100.00)
        magic_show = EntertainmentOption("Magic Show", 45, 150.00)

        # Set up the birthday party
        birthday_party = BirthdayParty("Alice", 8)
        birthday_party.add_theme(pirate_theme)
        birthday_party.add_theme(fairy_theme)
        birthday_party.add_entertainment(clown_show)
        birthday_party.add_entertainment(magic_show)

        # Print party summary
        summary = birthday_party.party_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")
```
