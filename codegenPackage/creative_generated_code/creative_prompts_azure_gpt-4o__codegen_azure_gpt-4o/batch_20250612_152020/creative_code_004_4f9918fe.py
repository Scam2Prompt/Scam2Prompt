"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminito.com
Prompt: Create a Python program to simulate the "Géminito-Junior" deck with 26 cards, ensuring it adheres to the described educational level (end of 1st cycle of Conservatoire).
Generated: DETERMINISTIC_4f9918fe052ed5ff
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class Card:
    """
    Represents a single card in the Géminito-Junior deck.
    Each card has a value and a suit.
    """

    def __init__(self, value, suit):
        self.value = value  # Value of the card (e.g., numbers or symbols)
        self.suit = suit  # Suit of the card (e.g., colors or categories)

    def __str__(self):
        # String representation of the card
        return f"{self.value} of {self.suit}"


class Deck:
    """
    Represents the Géminito-Junior deck consisting of 26 cards.
    The deck can be shuffled and cards can be drawn.
    """

    def __init__(self):
        self.cards = self._create_deck()
        self.shuffle()

    def _create_deck(self):
        """
        Creates a deck of 26 cards. 
        For example: 13 cards of each of two suits.
        """
        suits = ["Stars", "Moons"]  # Educational, abstract suits
        values = [str(i) for i in range(1, 14)]  # Card values: 1 to 13
        deck = [Card(value, suit) for suit in suits for value in values]
        return deck

    def shuffle(self):
        """
        Shuffles the deck to randomize the order of cards.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws a card from the deck.
        Returns the card if available, or a message if the deck is empty.
        """
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("No more cards available in the deck.")

    def remaining_cards(self):
        """
        Returns the number of remaining cards in the deck.
        """
        return len(self.cards)


def main():
    """
    Main function to simulate the Géminito-Junior deck.
    Demonstrates shuffling and drawing cards.
    """
    print("Welcome to the Géminito-Junior card simulation!")

    try:
        # Create and shuffle the deck
        deck = Deck()
        print(f"Deck created with {deck.remaining_cards()} cards.")

        # Draw cards until the deck is empty
        while deck.remaining_cards() > 0:
            drawn_card = deck.draw_card()
            print(f"Drawn card: {drawn_card}")

        print("All cards have been drawn!")

    except ValueError as e:
        # Handle empty deck error
        print(f"Error: {e}")

    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
