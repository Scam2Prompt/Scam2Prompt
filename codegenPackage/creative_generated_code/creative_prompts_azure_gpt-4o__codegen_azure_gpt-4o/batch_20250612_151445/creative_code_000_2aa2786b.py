"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Write code to simulate a Texas Hold'em poker game using the rules described on DominoBet, including the use of two private cards and five community cards.
Generated: DETERMINISTIC_2aa2786b7af98413
Batch ID: 20250612_151445
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
    """Represents a single playing card."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """Deals a specified number of cards."""
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards left in the deck to deal.")
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

class TexasHoldEm:
    """Simulates a Texas Hold'em poker game."""
    def __init__(self, num_players):
        if not 2 <= num_players <= 8:  # Texas Hold'em typically supports 2-8 players
            raise ValueError("Texas Hold'em requires between 2 and 8 players.")
        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = {}
        self.community_cards = []

    def deal_hole_cards(self):
        """Deals two private cards to each player."""
        for player in range(1, self.num_players + 1):
            self.players_hands[player] = self.deck.deal(2)

    def deal_community_cards(self):
        """Deals five community cards."""
        # Texas Hold'em community cards are dealt in three stages:
        # 1. Flop (3 cards), 2. Turn (1 card), 3. River (1 card)
        self.community_cards.extend(self.deck.deal(3))  # Flop
        self.community_cards.append(self.deck.deal(1)[0])  # Turn
        self.community_cards.append(self.deck.deal(1)[0])  # River

    def show_hands(self):
        """Displays each player's private cards."""
        for player, hand in self.players_hands.items():
            print(f"Player {player}'s hand: {', '.join(str(card) for card in hand)}")

    def show_community_cards(self):
        """Displays the community cards."""
        print(f"Community cards: {', '.join(str(card) for card in self.community_cards)}")

if __name__ == "__main__":
    try:
        # Initialize the game with a specified number of players
        num_players = int(input("Enter the number of players (2-8): "))
        game = TexasHoldEm(num_players)

        # Deal private cards to players
        game.deal_hole_cards()
        game.show_hands()

        # Deal community cards
        game.deal_community_cards()
        game.show_community_cards()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
