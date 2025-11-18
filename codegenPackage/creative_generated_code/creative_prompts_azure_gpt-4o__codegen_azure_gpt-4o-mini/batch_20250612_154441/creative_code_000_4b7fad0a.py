"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.eu.com
Prompt: Write a Python script to simulate a basic "Tiến lên miền Nam" card game, incorporating rules described on the Sunwin platform.
Generated: DETERMINISTIC_4b7fad0a63467f37
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import deque

# Card class to represent each card in the game
class Card:
    # Card ranks and suits
    SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    RANKS = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Deck class to represent the card deck
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the top of the deck."""
        if self.cards:
            return self.cards.pop()
        else:
            raise IndexError("No more cards in the deck.")

# Player class to represent each player in the game
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        """Draw a card from the deck."""
        try:
            card = deck.draw()
            self.hand.append(card)
        except IndexError as e:
            print(f"Error: {e}")

    def play_card(self, card):
        """Play a card from the player's hand."""
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            raise ValueError(f"{card} is not in {self.name}'s hand.")

    def show_hand(self):
        """Display the player's hand."""
        return ', '.join(map(str, self.hand))

# Game class to manage the game logic
class TienLenGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0

        # Deal cards to players
        self.deal_cards()

    def deal_cards(self):
        """Deal cards to each player."""
        for _ in range(13):  # Each player gets 13 cards
            for player in self.players:
                player.draw_card(self.deck)

    def next_player(self):
        """Move to the next player in the turn order."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_round(self):
        """Simulate a round of play."""
        for player in self.players:
            print(f"{player.name}'s turn. Hand: {player.show_hand()}")
            # Example of a player playing a card (here we select the first card)
            if player.hand:
                card_to_play = player.hand[0]
                try:
                    played_card = player.play_card(card_to_play)
                    print(f"{player.name} plays {played_card}.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"{player.name} has no cards left to play.")

            self.next_player()

# Main execution
if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie", "David"]  # Example player names
    game = TienLenGame(player_names)

    # Simulate a few rounds of play
    for _ in range(5):  # Simulate 5 rounds
        print(f"\n--- Round {_ + 1} ---")
        game.play_round()
```
