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
    """Represents a card in the Géminito-Junior deck."""
    
    def __init__(self, name, value):
        """
        Initializes a Card object.

        Args:
            name (str): The name of the card.
            value (int): The value of the card.
        """
        self.name = name
        self.value = value

    def __repr__(self):
        """Returns a string representation of the card."""
        return f"{self.name}: {self.value}"


class Deck:
    """Represents the Géminito-Junior deck."""
    
    def __init__(self):
        """
        Initializes a Deck object with 26 cards.

        The deck consists of 13 pairs of cards with values from 1 to 13.
        """
        self.cards = []
        self.create_deck()

    def create_deck(self):
        """Creates the Géminito-Junior deck with 26 cards."""
        for i in range(1, 14):
            self.cards.append(Card(f"Card {i}", i))
            self.cards.append(Card(f"Card {i}", i))
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws a card from the deck.

        Returns:
            Card: The drawn card.

        Raises:
            ValueError: If the deck is empty.
        """
        if not self.cards:
            raise ValueError("The deck is empty.")
        return self.cards.pop()

    def __repr__(self):
        """Returns a string representation of the deck."""
        return f"Deck of {len(self.cards)} cards"


def main():
    try:
        deck = Deck()
        print("Géminito-Junior Deck Simulator")
        print("--------------------------------")
        print(deck)
        
        while True:
            user_input = input("Press 'd' to draw a card, 'q' to quit: ")
            if user_input.lower() == 'd':
                card = deck.draw_card()
                print(card)
                if not deck.cards:
                    print("The deck is empty.")
                    break
            elif user_input.lower() == 'q':
                break
            else:
                print("Invalid input. Please try again.")
                
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
