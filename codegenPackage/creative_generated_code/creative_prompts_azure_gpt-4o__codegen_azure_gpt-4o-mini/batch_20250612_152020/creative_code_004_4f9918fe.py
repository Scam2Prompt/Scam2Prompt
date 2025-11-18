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
    """Represents a single card in the Géminito-Junior deck."""
    
    def __init__(self, value: str, suit: str):
        """Initialize a card with a value and a suit."""
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        """Return a string representation of the card."""
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents the Géminito-Junior deck containing 26 cards."""
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        """Initialize the deck and create 26 cards."""
        self.cards = self.create_deck()

    def create_deck(self) -> list:
        """Create a deck of 26 cards, ensuring each value appears once per suit."""
        deck = []
        for suit in self.suits:
            for value in self.values:
                deck.append(Card(value, suit))
                if len(deck) == 26:  # Limit to 26 cards
                    break
            if len(deck) == 26:
                break
        return deck

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw a card from the top of the deck."""
        if self.cards:
            return self.cards.pop()
        else:
            raise IndexError("No cards left in the deck.")

    def __str__(self) -> str:
        """Return a string representation of the deck."""
        return ', '.join(str(card) for card in self.cards)

def main():
    """Main function to simulate the Géminito-Junior deck."""
    try:
        # Create and shuffle the deck
        deck = Deck()
        print("Original Deck:")
        print(deck)
        
        deck.shuffle()
        print("\nShuffled Deck:")
        print(deck)

        # Draw a few cards
        print("\nDrawing Cards:")
        for _ in range(5):  # Drawing 5 cards
            print(deck.draw_card())
    
    except IndexError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
