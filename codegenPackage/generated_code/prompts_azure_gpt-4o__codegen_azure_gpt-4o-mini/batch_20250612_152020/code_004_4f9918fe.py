"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Create a Python program to simulate the "Géminito-Junior" deck with 26 cards, ensuring it adheres to the described educational level (end of 1st cycle of Conservatoire).
Generated: DETERMINISTIC_4f9918fe052ed5ff
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Card:
    """Class representing a single card in the Géminito-Junior deck."""
    
    def __init__(self, name: str, value: int):
        """
        Initialize a card with a name and a value.

        Args:
            name (str): The name of the card.
            value (int): The value of the card.
        """
        self.name = name
        self.value = value

    def __repr__(self):
        """Return a string representation of the card."""
        return f"{self.name} (Value: {self.value})"


class Deck:
    """Class representing a deck of cards for the Géminito-Junior game."""
    
    def __init__(self):
        """Initialize the deck with 26 unique cards."""
        self.cards = self.create_deck()

    def create_deck(self) -> list:
        """Create a deck of 26 unique cards.

        Returns:
            list: A list of Card objects.
        """
        card_names = [
            "Do", "Re", "Mi", "Fa", "Sol", "La", "Si",
            "Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#",
            "Do♭", "Re♭", "Mi♭", "Fa♭", "Sol♭", "La♭",
            "C", "D", "E", "F", "G", "A", "B"
        ]
        # Ensure we only take 26 unique cards
        return [Card(name, index + 1) for index, name in enumerate(card_names)]

    def shuffle(self):
        """Shuffle the deck of cards in place."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw a card from the deck.

        Returns:
            Card: The drawn card.

        Raises:
            IndexError: If the deck is empty.
        """
        if not self.cards:
            raise IndexError("Cannot draw a card from an empty deck.")
        return self.cards.pop()

    def reset_deck(self):
        """Reset the deck to its original state and shuffle it."""
        self.cards = self.create_deck()
        self.shuffle()


def main():
    """Main function to simulate the card game."""
    try:
        deck = Deck()  # Create a new deck
        deck.shuffle()  # Shuffle the deck

        # Draw and display 5 cards from the deck
        for _ in range(5):
            card = deck.draw_card()
            print(f"Drew card: {card}")

    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
