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
from collections import deque

class Card:
    """Represents a single playing card."""
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck."""
        if self.cards:
            return self.cards.pop()
        return None

class KlondikeSolitaire:
    """Implements the Klondike Solitaire game."""
    def __init__(self):
        self.stock = deque()  # Stock pile
        self.waste = deque()  # Waste pile
        self.foundations = {suit: [] for suit in Card.SUITS}  # Foundations
        self.tableau = [[] for _ in range(7)]  # Tableau columns
        self._initialize_game()

    def _initialize_game(self):
        """Sets up the initial game state."""
        deck = Deck()
        # Deal cards to tableau
        for i in range(7):
            for j in range(i + 1):
                card = deck.draw()
                if j == i:
                    self.tableau[i].append((card, True))  # Face-up card
                else:
                    self.tableau[i].append((card, False))  # Face-down card
        # Remaining cards go to stock
        self.stock.extend(deck.cards)

    def flip_stock(self, count=1):
        """Flips cards from the stock to the waste."""
        if not self.stock:
            # Reset stock from waste if stock is empty
            self.stock.extend(reversed(self.waste))
            self.waste.clear()
        for _ in range(count):
            if self.stock:
                self.waste.append(self.stock.pop())

    def move_to_foundation(self, tableau_index):
        """Moves a card from the tableau to the foundation."""
        if tableau_index < 0 or tableau_index >= len(self.tableau):
            print("Invalid tableau index.")
            return
        if not self.tableau[tableau_index]:
            print("No cards in the selected tableau column.")
            return
        card, face_up = self.tableau[tableau_index][-1]
        if not face_up:
            print("Cannot move a face-down card.")
            return
        foundation = self.foundations[card.suit]
        if (not foundation and card.rank == 'A') or \
           (foundation and Card.RANKS.index(card.rank) == Card.RANKS.index(foundation[-1].rank) + 1):
            foundation.append(card)
            self.tableau[tableau_index].pop()
            # Flip the next card in the tableau column if applicable
            if self.tableau[tableau_index]:
                self.tableau[tableau_index][-1] = (self.tableau[tableau_index][-1][0], True)
        else:
            print("Invalid move to foundation.")

    def display_game_state(self):
        """Displays the current state of the game."""
        print("\nStock:", len(self.stock), "cards")
        print("Waste:", [str(card) for card in self.waste])
        print("Foundations:")
        for suit, cards in self.foundations.items():
            print(f"  {suit}: {cards}")
        print("Tableau:")
        for i, column in enumerate(self.tableau):
            print(f"  Column {i + 1}: {[str(card) if face_up else 'Face-down' for card, face_up in column]}")

    def is_game_won(self):
        """Checks if the game is won."""
        return all(len(foundation) == 13 for foundation in self.foundations.values())

def main():
    """Main function to run the Klondike Solitaire game."""
    game = KlondikeSolitaire()
    while True:
        game.display_game_state()
        if game.is_game_won():
            print("Congratulations! You won the game!")
            break
        print("\nOptions:")
        print("1. Flip stock (1 card)")
        print("2. Flip stock (3 cards)")
        print("3. Move card to foundation")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            game.flip_stock(count=1)
        elif choice == '2':
            game.flip_stock(count=3)
        elif choice == '3':
            tableau_index = int(input("Enter tableau column index (1-7): ")) - 1
            game.move_to_foundation(tableau_index)
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
