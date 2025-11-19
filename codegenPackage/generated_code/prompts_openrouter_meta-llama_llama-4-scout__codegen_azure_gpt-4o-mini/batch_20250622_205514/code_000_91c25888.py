"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Write a Python script to implement the Klondike solitaire game, allowing users to flip through the Stock one or three at a time and move cards to Foundations.
Generated: DETERMINISTIC_91c25888db956501
Batch ID: 20250622_205514
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
    """Represents a single playing card."""
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        if suit not in self.SUITS or rank not in self.RANKS:
            raise ValueError("Invalid card suit or rank.")
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def is_red(self):
        return self.suit in ['Hearts', 'Diamonds']

    def is_black(self):
        return self.suit in ['Clubs', 'Spades']

class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self, count=1):
        """Draws a specified number of cards from the deck."""
        if count > len(self.cards):
            raise ValueError("Not enough cards in the deck.")
        drawn_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn_cards

class KlondikeSolitaire:
    """Represents the Klondike Solitaire game."""
    def __init__(self):
        self.stock = Deck()
        self.waste = []
        self.foundations = {suit: [] for suit in Card.SUITS}
        self.tableau = [[] for _ in range(7)]
        self.setup_tableau()

    def setup_tableau(self):
        """Sets up the tableau with cards from the stock."""
        for i in range(7):
            for j in range(i, 7):
                card = self.stock.draw()[0]
                self.tableau[j].append(card)
            self.tableau[i][-1] = self.tableau[i][-1]  # Last card face up

    def flip_stock(self, count=1):
        """Flips cards from the stock to the waste."""
        try:
            cards = self.stock.draw(count)
            self.waste.extend(cards)
        except ValueError as e:
            print(f"Error flipping stock: {e}")

    def move_to_foundation(self, card):
        """Moves a card to the appropriate foundation if valid."""
        if card.rank == 'A':
            self.foundations[card.suit].append(card)
        elif self.is_valid_foundation_move(card):
            self.foundations[card.suit].append(card)
        else:
            print(f"Cannot move {card} to foundation.")

    def is_valid_foundation_move(self, card):
        """Checks if a card can be moved to its foundation."""
        foundation = self.foundations[card.suit]
        if not foundation:
            return card.rank == 'A'
        return Card.RANKS.index(card.rank) == Card.RANKS.index(foundation[-1].rank) + 1

    def display(self):
        """Displays the current state of the game."""
        print("Foundations:")
        for suit, cards in self.foundations.items():
            print(f"{suit}: {', '.join(str(card) for card in cards) if cards else 'Empty'}")
        print("\nTableau:")
        for i, pile in enumerate(self.tableau):
            print(f"Pile {i + 1}: {', '.join(str(card) for card in pile)}")
        print("\nWaste:")
        print(f"{', '.join(str(card) for card in self.waste) if self.waste else 'Empty'}")
        print("\nStock:")
        print(f"{len(self.stock.cards)} cards remaining.")

def main():
    """Main function to run the Klondike Solitaire game."""
    game = KlondikeSolitaire()
    game.display()

    while True:
        action = input("Enter 'flip' to flip cards from stock, 'move' to move to foundation, or 'quit' to exit: ").strip().lower()
        if action == 'flip':
            count = int(input("Flip how many cards (1 or 3)? "))
            if count in [1, 3]:
                game.flip_stock(count)
                game.display()
            else:
                print("Invalid count. Please enter 1 or 3.")
        elif action == 'move':
            card_input = input("Enter the card to move (e.g., 'A of Hearts'): ")
            try:
                rank, _, suit = card_input.partition(' of ')
                card = Card(suit, rank)
                game.move_to_foundation(card)
                game.display()
            except ValueError as e:
                print(f"Error moving card: {e}")
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
```
