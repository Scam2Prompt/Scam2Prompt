"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Generate a Python script that simulates the gameplay of Klondike Flip-3 solitaire, including card movement rules and winning conditions.
Generated: DETERMINISTIC_1af5ec8576cc167a
Batch ID: 20250612_160526
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
from typing import List, Dict, Tuple, Optional

class Card:
    """Represents a playing card with a suit and rank."""
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def __str__(self) -> str:
        if not self.face_up:
            return "[X]"
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        return self.__str__()

    def color(self) -> str:
        """Returns the color of the card (red or black)."""
        return "red" if self.suit in ["♥", "♦"] else "black"

    def value(self) -> int:
        """Returns the numerical value of the card."""
        if self.rank == "A":
            return 1
        elif self.rank in ["J", "Q", "K"]:
            return 11 if self.rank == "J" else 12 if self.rank == "Q" else 13
        else:
            return int(self.rank)

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = []
        self.build()

    def build(self) -> None:
        """Builds a standard deck of 52 cards."""
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self) -> None:
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal(self) -> Optional[Card]:
        """Deals one card from the deck."""
        return self.cards.pop() if self.cards else None

class SolitaireGame:
    """Simulates Klondike Flip-3 solitaire gameplay."""
    def __init__(self):
        self.deck = Deck()
        self.waste_pile = []
        self.foundations = {"♠": [], "♥": [], "♦": [], "♣": []}
        self.tableau = [[] for _ in range(7)]
        self.stock = deque()
        self.setup_game()

    def setup_game(self) -> None:
        """Initializes the game by dealing cards to tableau and stock."""
        self.deck.shuffle()
        
        # Deal cards to tableau
        for i in range(7):
            for j in range(i, 7):
                card = self.deck.deal()
                if card:
                    card.face_up = (j == i)  # Only last card in each pile is face up
                    self.tableau[j].append(card)
        
        # Remaining cards go to stock
        while len(self.deck.cards) > 0:
            card = self.deck.deal()
            if card:
                self.stock.append(card)

    def draw_from_stock(self) -> None:
        """Draws 3 cards from stock to waste pile (Flip-3 rule)."""
        if not self.stock:
            # If stock is empty, recycle waste pile back to stock
            self.stock = deque(self.waste_pile[::-1])
            self.waste_pile = []
            for card in self.stock:
                card.face_up = False
        
        drawn_cards = []
        for _ in range(min(3, len(self.stock))):
            card = self.stock.popleft()
            card.face_up = True
            drawn_cards.append(card)
        
        self.waste_pile.extend(drawn_cards)

    def move_to_foundation(self, card: Card) -> bool:
        """Attempts to move a card to its foundation pile."""
        foundation = self.foundations[card.suit]
        
        if card.rank == "A":
            if not foundation:
                foundation.append(card)
                return True
        else:
            if foundation and foundation[-1].value() == card.value() - 1:
                foundation.append(card)
                return True
        return False

    def can_move_tableau(self, source_card: Card, target_card: Card) -> bool:
        """Checks if a card can be placed on another card in the tableau."""
        return (source_card.color() != target_card.color() and 
                source_card.value() == target_card.value() - 1)

    def move_within_tableau(self, source_pile: int, source_index: int, target_pile: int) -> bool:
        """Moves cards between tableau piles."""
        if (source_pile < 0 or source_pile >= 7 or 
            target_pile < 0 or target_pile >= 7 or 
            source_pile == target_pile):
            return False

        source = self.tableau[source_pile]
        target = self.tableau[target_pile]

        if not source or source_index < 0 or source_index >= len(source):
            return False

        moving_cards = source[source_index:]
        if not all(card.face_up for card in moving_cards):
            return False

        if not target:
            # Can only move a King to an empty pile
            if moving_cards[0].rank == "K":
                self.tableau[target_pile] = moving_cards
                self.tableau[source_pile] = source[:source_index]
                if source_index > 0 and not source[source_index-1].face_up:
                    source[source_index-1].face_up = True
                return True
        else:
            if self.can_move_tableau(moving_cards[0], target[-1]):
                self.tableau[target_pile].extend(moving_cards)
                self.tableau[source_pile] = source[:source_index]
                if source_index > 0 and not source[source_index-1].face_up:
                    source[source_index-1].face_up = True
                return True
        return False

    def move_waste_to_tableau(self, target_pile: int) -> bool:
        """Moves the top waste card to a tableau pile."""
        if not self.waste_pile or target_pile < 0 or target_pile >= 7:
            return False

        card = self.waste_pile[-1]
        target = self.tableau[target_pile]

        if not target:
            if card.rank == "K":
                self.tableau[target_pile].append(self.waste_pile.pop())
                return True
        else:
            if self.can_move_tableau(card, target[-1]):
                self.tableau[target_pile].append(self.waste_pile.pop())
                return True
        return False

    def move_waste_to_foundation(self) -> bool:
        """Moves the top waste card to its foundation."""
        if not self.waste_pile:
            return False

        card = self.waste_pile[-1]
        if self.move_to_foundation(card):
            self.waste_pile.pop()
            return True
        return False

    def move_tableau_to_foundation(self, pile: int) -> bool:
        """Moves the top tableau card to its foundation."""
        if pile < 0 or pile >= 7 or not self.tableau[pile]:
            return False

        card = self.tableau[pile][-1]
        if self.move_to_foundation(card):
            self.tableau[pile].pop()
            if self.tableau[pile] and not self.tableau[pile][-1].face_up:
                self.tableau[pile][-1].face_up = True
            return True
        return False

    def is_won(self) -> bool:
        """Checks if the game has been won."""
        return all(len(foundation) == 13 for foundation in self.foundations.values())

    def display(self) -> None:
        """Displays the current game state."""
        print("\n=== Solitaire Game ===")
        
        # Display stock and waste
        stock_count = len(self.stock)
        waste_top = self.waste_pile[-1] if self.waste_pile else None
        print(f"Stock: {stock_count} cards | Waste: {waste_top}")
        
        # Display foundations
        foundations = [f"{suit}: {foundation[-1] if foundation else '[]'}" 
                      for suit, foundation in self.foundations.items()]
        print("Foundations:", " | ".join(foundations))
        
        # Display tableau
        print("\nTableau:")
        max_height = max(len(pile) for pile in self.tableau)
        for i in range(max_height):
            row = []
            for pile in self.tableau:
                if i < len(pile):
                    row.append(str(pile[i]))
                else:
                    row.append("   ")
            print(" ".join(row))

    def play(self) -> None:
        """Main game loop."""
        print("Welcome to Klondike Solitaire (Flip-3
