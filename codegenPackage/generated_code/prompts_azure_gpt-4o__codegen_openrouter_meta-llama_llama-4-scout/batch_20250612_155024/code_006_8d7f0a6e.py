"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Write a function to calculate PRIME earnings boosts based on the equipped Avatar and matching deck, as described in the Parallel TCG benefits system.
Generated: DETERMINISTIC_8d7f0a6e579bbebe
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class Avatar:
    """Represents an Avatar in the Parallel TCG."""
    
    def __init__(self, name: str, prime_earnings_boosts: Dict[str, float]):
        """
        Initializes an Avatar.

        Args:
        - name (str): The name of the Avatar.
        - prime_earnings_boosts (Dict[str, float]): A dictionary of PRIME earnings boosts.
        """
        self.name = name
        self.prime_earnings_boosts = prime_earnings_boosts


class Deck:
    """Represents a Deck in the Parallel TCG."""
    
    def __init__(self, name: str, card_types: List[str]):
        """
        Initializes a Deck.

        Args:
        - name (str): The name of the Deck.
        - card_types (List[str]): A list of card types in the Deck.
        """
        self.name = name
        self.card_types = card_types


def calculate_prime_earnings_boosts(avatar: Avatar, deck: Deck) -> float:
    """
    Calculates the PRIME earnings boosts based on the equipped Avatar and matching deck.

    Args:
    - avatar (Avatar): The equipped Avatar.
    - deck (Deck): The matching Deck.

    Returns:
    - float: The total PRIME earnings boost.

    Raises:
    - ValueError: If the Avatar or Deck is not provided.
    """
    if not avatar:
        raise ValueError("Avatar is required")
    if not deck:
        raise ValueError("Deck is required")

    total_boost = 0.0
    for card_type in deck.card_types:
        if card_type in avatar.prime_earnings_boosts:
            total_boost += avatar.prime_earnings_boosts[card_type]

    return total_boost


def main():
    # Example usage:
    avatar = Avatar(
        "Example Avatar",
        {
            "Creature": 0.1,
            "Spell": 0.05,
            "Enchant": 0.2
        }
    )

    deck = Deck(
        "Example Deck",
        ["Creature", "Spell", "Enchant"]
    )

    try:
        boost = calculate_prime_earnings_boosts(avatar, deck)
        print(f"PRIME earnings boost: {boost:.2%}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
