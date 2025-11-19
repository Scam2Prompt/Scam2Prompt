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
import sys
from collections import deque
from enum import Enum

class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Rank(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def __str__(self):
        if not self.face_up:
            return "[X]"
        return f"[{self.rank.value}{self.suit.value}]"

    def __repr__(self):
        return self.__str__()

    def is_red(self):
        return self.suit in (Suit.HEARTS, Suit.DIAMONDS)

    def is_black(self):
        return not self.is_red()

class Foundation:
    def __init__(self, suit):
        self.suit = suit
        self.cards = []

    def can_accept(self, card):
        if card.suit != self.suit:
            return False
        
        if not self.cards:
            return card.rank == Rank.ACE
        
        last_card = self.cards[-1]
        try:
            return list(Rank).index(card.rank) == list(Rank).index(last_card.rank) + 1
        except ValueError:
            return False

    def add_card(self, card):
        if self.can_accept(card):
            self.cards.append(card)
            return True
        return False

    def __str__(self):
        if not self.cards:
            return f"[{self.suit.value}: ]"
        return f"[{self.suit.value}: {self.cards[-1].rank.value}]"

class TableauPile:
    def __init__(self):
        self.cards = []

    def can_accept(self, card):
        if not self.cards:
            return card.rank == Rank.KING
        
        last_card = self.cards[-1]
        if last_card.is_red() and card.is_black() or last_card.is_black() and card.is_red():
            try:
                return list(Rank).index(card.rank) == list(Rank).index(last_card.rank) - 1
            except ValueError:
                return False
        return False

    def add_card(self, card):
        if self.can_accept(card):
            self.cards.append(card)
            return True
        return False

    def add_sequence(self, cards):
        if not cards:
            return False
        
        if not self.cards and cards[0].rank != Rank.KING:
            return False
        
        if self.cards:
            last_card = self.cards[-1]
            if not ((last_card.is_red() and cards[0].is_black()) or 
                    (last_card.is_black() and cards[0].is_red())):
                return False
            
            try:
                if list(Rank).index(cards[0].rank) != list(Rank).index(last_card.rank) - 1:
                    return False
            except ValueError:
                return False

        for i in range(len(cards) - 1):
            current = cards[i]
            next_card = cards[i + 1]
            
            if (current.is_red() and next_card.is_red()) or (current.is_black() and next_card.is_black()):
                return False
            
            try:
                if list(Rank).index(current.rank) != list(Rank).index(next_card.rank) + 1:
                    return False
            except ValueError:
                return False

        self.cards.extend(cards)
        return True

    def get_sequence(self, index):
        if index < 0 or index >= len(self.cards) or not self.cards[index].face_up:
            return None
        return self.cards[index:]

    def remove_sequence(self, index):
        if index < 0 or index >= len(self.cards):
            return None
        removed = self.cards[index:]
        self.cards = self.cards[:index]
        return removed

    def flip_top_card(self):
        if self.cards and not self.cards[-1].face_up:
            self.cards[-1].face_up = True

    def __str__(self):
        return " ".join(str(card) for card in self.cards)

class Stock:
    def __init__(self, cards, draw_count=1):
        self.stock = deque(cards)
        self.waste = []
        self.draw_count = draw_count

    def draw(self):
        if not self.stock:
            if not self.waste:
                return False
            
            self.stock = deque(reversed(self.waste))
            self.waste = []
            return False

        drawn = []
        for _ in range(min(self.draw_count, len(self.stock))):
            card = self.stock.popleft()
            card.face_up = True
            drawn.append(card)
        
        self.waste.extend(drawn)
        return True

    def get_waste_top(self):
        if not self.waste:
            return None
        return self.waste[-1]

    def take_waste_top(self):
        if not self.waste:
            return None
        return self.waste.pop()

    def __str__(self):
        stock_str = f"Stock: {len(self.stock)} cards"
        waste_str = f"Waste: {' '.join(str(card) for card in self.waste[-3:])}" if self.waste else "Waste: empty"
        return f"{stock_str}\n{waste_str}"

class KlondikeGame:
    def __init__(self, draw_count=1):
        self.draw_count = draw_count
        self.foundations = {
            suit: Foundation(suit) for suit in Suit
        }
        self.tableau = [TableauPile() for _ in range(7)]
        self.stock = None
        self.initialize_game()

    def initialize_game(self):
        deck = [Card(suit, rank) for suit in Suit for rank in Rank]
        random.shuffle(deck)

        # Deal to tableau
        for i in range(7):
            for j in range(i, 7):
                card = deck.pop()
                if j == i:  # Last card in each column is face up
                    card.face_up = True
                self.tableau[j].cards.append(card)

        # Remaining cards go to stock
        self.stock = Stock(deck, self.draw_count)

    def display(self):
        print("\nFoundations:")
        for suit, foundation in self.foundations.items():
            print(foundation, end=" ")
        print("\n")

        print(self.stock)
        print()

        print("Tableau:")
        max_len = max(len(pile.cards) for pile in self.tableau)
        for i in range(max_len):
            for pile in self.tableau:
                if i < len(pile.cards):
                    print(f"{pile.cards[i]:<5}", end="")
                else:
                    print("     ", end="")
            print()

    def move_waste_to_foundation(self):
        card = self.stock.get_waste_top()
        if not card:
            print("No card in waste to move")
            return False

        foundation = self.foundations[card.suit]
        if foundation.can_accept(card):
            self.stock.take_waste_top()
            foundation.add_card(card)
            return True
        print("Cannot move that card to foundation")
        return False

    def move_tableau_to_foundation(self, pile_idx):
        if pile_idx < 0 or pile_idx >= len(self.tableau):
            print("Invalid pile index")
            return False

        pile = self.tableau[pile_idx]
        if not pile.cards:
            print("Pile is empty")
            return False

        card = pile.cards[-1]
        if not card.face_up:
            print("Card is not face up")
            return False

        foundation = self.foundations[card.suit]
        if foundation.can_accept(card):
            pile.cards.pop()
            foundation.add_card(card)
            if pile.cards and not pile.cards[-1].face_up:
                pile.cards[-1].face_up = True
            return True
        print("Cannot move that card to foundation")
        return False

    def move_waste_to_tableau(self, pile_idx):
        if pile_idx < 0 or pile_idx >= len(self.tableau):
            print("Invalid pile index")
            return False

        card = self.stock.get_waste_top()
        if not card:
            print("No card in waste to move")
            return False

        pile = self.tableau[pile_idx]
        if pile.add_card(card
