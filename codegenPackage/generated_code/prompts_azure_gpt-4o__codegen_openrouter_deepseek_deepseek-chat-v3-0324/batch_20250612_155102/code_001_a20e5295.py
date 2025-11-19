"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Create a Python function that automates the nomination process for categories such as "AISHwashers" and "Virtue Vampires," including fields for candidate examples and Discord usernames.
Generated: DETERMINISTIC_a20e529560bde604
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Nomination:
    """
    Represents a nomination entry with category, candidate examples, and Discord usernames.
    """
    def __init__(self, category: str, examples: List[str], discord_usernames: List[str]):
        self.category = category
        self.examples = examples
        self.discord_usernames = discord_usernames

    def to_dict(self) -> Dict:
        """Convert the Nomination object to a dictionary."""
        return {
            "category": self.category,
            "examples": self.examples,
            "discord_usernames": self.discord_usernames
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Nomination':
        """Create a Nomination object from a dictionary."""
        return cls(
            category=data["category"],
            examples=data["examples"],
            discord_usernames=data["discord_usernames"]
        )

class NominationManager:
    """
    Manages the nomination process including adding, removing, and saving nominations.
    """
    def __init__(self, filename: str = "nominations.json"):
        self.filename = filename
        self.nominations: List[Nomination] = []
        self.load_nominations()

    def add_nomination(self, category: str, examples: List[str], discord_usernames: List[str]) -> None:
        """Add a new nomination."""
        if not category or not examples or not discord_usernames:
            raise ValueError("Category, examples, and Discord usernames cannot be empty.")
        
        nomination = Nomination(category, examples, discord_usernames)
        self.nominations.append(nomination)
        self.save_nominations()

    def remove_nomination(self, category: str) -> bool:
        """Remove a nomination by category. Returns True if successful, False otherwise."""
        initial_length = len(self.nominations)
        self.nominations = [n for n in self.nominations if n.category != category]
        if len(self.nominations) < initial_length:
            self.save_nominations()
            return True
        return False

    def get_nominations(self) -> List[Nomination]:
        """Get all nominations."""
        return self.nominations

    def get_nomination_by_category(self, category: str) -> Optional[Nomination]:
        """Get a nomination by category. Returns None if not found."""
        for nomination in self.nominations:
            if nomination.category == category:
                return nomination
        return None

    def save_nominations(self) -> None:
        """Save nominations to a JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump([n.to_dict() for n in self.nominations], f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save nominations: {e}")

    def load_nominations(self) -> None:
        """Load nominations from a JSON file."""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.nominations = [Nomination.from_dict(item) for item in data]
        except FileNotFoundError:
            self.nominations = []
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data in {self.filename}: {e}")
        except IOError as e:
            raise IOError(f"Failed to load nominations: {e}")

def main():
    """Example usage of the NominationManager."""
    manager = NominationManager()

    # Add a nomination
    manager.add_nomination(
        category="AISHwashers",
        examples=["Example1", "Example2"],
        discord_usernames=["user1#1234", "user2#5678"]
    )

    # Get all nominations
    nominations = manager.get_nominations()
    for nom in nominations:
        print(f"Category: {nom.category}")
        print(f"Examples: {', '.join(nom.examples)}")
        print(f"Discord Usernames: {', '.join(nom.discord_usernames)}")
        print()

    # Remove a nomination
    if manager.remove_nomination("AISHwashers"):
        print("Nomination removed successfully.")
    else:
        print("Nomination not found.")

if __name__ == "__main__":
    main()
```
