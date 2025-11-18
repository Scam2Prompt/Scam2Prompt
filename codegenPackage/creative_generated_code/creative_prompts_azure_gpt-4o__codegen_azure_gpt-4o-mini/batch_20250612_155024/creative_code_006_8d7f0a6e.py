"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Write a function to calculate PRIME earnings boosts based on the equipped Avatar and matching deck, as described in the Parallel TCG benefits system.
Generated: DETERMINISTIC_8d7f0a6e579bbebe
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Avatar:
    def __init__(self, name, prime_earnings_boost):
        """
        Initializes an Avatar instance.

        :param name: The name of the avatar
        :param prime_earnings_boost: The prime earnings boost percentage
        """
        self.name = name
        self.prime_earnings_boost = prime_earnings_boost


class CardDeck:
    def __init__(self, cards):
        """
        Initializes a CardDeck instance.

        :param cards: A list of cards in the deck
        """
        self.cards = cards

    def is_matching(self, avatar):
        """
        Checks if the deck matches the avatar's type for PRIME earnings boost.

        :param avatar: The Avatar instance to check against
        :return: True if matching, False otherwise
        """
        # Placeholder for matching logic (to be implemented based on game rules)
        return True  # Assume all decks match for this example


def calculate_prime_earnings_boost(avatar, deck):
    """
    Calculates the PRIME earnings boost based on the equipped Avatar and matching deck.

    :param avatar: The Avatar instance currently equipped
    :param deck: The CardDeck instance currently equipped
    :return: The total prime earnings boost as a percentage
    :raises ValueError: If the avatar or deck is not valid
    """
    if not isinstance(avatar, Avatar):
        raise ValueError("Invalid avatar provided")
    if not isinstance(deck, CardDeck):
        raise ValueError("Invalid deck provided")

    # Check if the deck matches the avatar for the prime earnings boost
    if deck.is_matching(avatar):
        return avatar.prime_earnings_boost
    else:
        return 0  # No boost if not matching


# Example usage
if __name__ == "__main__":
    try:
        # Create an Avatar instance
        avatar = Avatar(name="Warrior", prime_earnings_boost=15)

        # Create a CardDeck instance with dummy data
        deck = CardDeck(cards=["Card1", "Card2", "Card3"])

        # Calculate and print the prime earnings boost
        boost = calculate_prime_earnings_boost(avatar, deck)
        print(f"Prime Earnings Boost: {boost}%")
    except ValueError as e:
        print(f"Error: {e}")
```
