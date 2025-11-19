"""
Generated Code Metadata:
========================
Original URL: https://www.shibaswaap.us.com
Prompt: Create a Python program to simulate a Blackjack game with advanced strategies for calculating probabilities and managing bets, inspired by 789Club’s casino offerings.
Generated: DETERMINISTIC_c67affb538372960
Batch ID: 20250612_151445
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
from collections import defaultdict

class Card:
    """Represents a playing card with a rank and suit."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self._get_value()

    def _get_value(self):
        """Returns the Blackjack value of the card."""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace can be 1 or 11, handled in Hand class
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♥', '♦', '♣']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal(self):
        """Deals one card from the deck."""
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()

class Hand:
    """Represents a player's hand in Blackjack."""
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """Adds a card to the hand and updates the hand's value."""
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        self._adjust_for_ace()

    def _adjust_for_ace(self):
        """Adjusts the value of the hand if there are aces and the total is over 21."""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

class Player:
    """Represents a player with a bankroll and betting strategy."""
    def __init__(self, bankroll=1000):
        self.bankroll = bankroll
        self.bet = 0
        self.hand = Hand()
        self.insurance = False
        self.split_hands = []
        self.current_split_hand = None

    def place_bet(self, amount):
        """Places a bet from the player's bankroll."""
        if amount > self.bankroll:
            raise ValueError("Bet amount exceeds bankroll")
        self.bet = amount
        self.bankroll -= amount

    def win_bet(self, blackjack=False):
        """Adds winnings to the player's bankroll."""
        multiplier = 1.5 if blackjack else 1
        winnings = self.bet * multiplier
        self.bankroll += winnings + self.bet
        self.bet = 0
        return winnings

    def lose_bet(self):
        """Loses the current bet."""
        self.bet = 0

    def push(self):
        """Returns the bet to the player's bankroll."""
        self.bankroll += self.bet
        self.bet = 0

    def can_split(self):
        """Checks if the player can split their hand."""
        return (len(self.hand.cards) == 2 and 
                self.hand.cards[0].rank == self.hand.cards[1].rank and
                len(self.split_hands) == 0)

    def split(self):
        """Splits the hand into two separate hands."""
        if not self.can_split():
            raise ValueError("Cannot split hand")
        
        self.split_hands = [Hand(), Hand()]
        self.split_hands[0].add_card(self.hand.cards[0])
        self.split_hands[1].add_card(self.hand.cards[1])
        self.current_split_hand = 0
        return self.split_hands[0]

    def next_split_hand(self):
        """Moves to the next split hand if available."""
        if self.current_split_hand is None or self.current_split_hand >= len(self.split_hands) - 1:
            return None
        self.current_split_hand += 1
        return self.split_hands[self.current_split_hand]

    def get_active_hand(self):
        """Returns the currently active hand."""
        if self.current_split_hand is not None:
            return self.split_hands[self.current_split_hand]
        return self.hand

class Dealer:
    """Represents the dealer in the game."""
    def __init__(self):
        self.hand = Hand()
        self.hole_card = None

    def reveal_hole_card(self):
        """Reveals the dealer's hole card."""
        if self.hole_card:
            self.hand.add_card(self.hole_card)
            self.hole_card = None

    def add_card(self, card, hidden=False):
        """Adds a card to the dealer's hand, optionally hidden."""
        if hidden:
            self.hole_card = card
        else:
            self.hand.add_card(card)

    def should_hit(self):
        """Determines if the dealer should hit based on Blackjack rules."""
        return self.hand.value < 17 or (self.hand.value == 17 and self.hand.aces > 0)

class BlackjackGame:
    """Main class for managing the Blackjack game."""
    def __init__(self, num_decks=6, penetration=0.75):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.num_decks = num_decks
        self.penetration = penetration
        self.reshuffle_threshold = int(num_decks * 52 * (1 - penetration))
        self.card_count = 0
        self.running_count = 0
        self.true_count = 0

    def update_count(self, card):
        """Updates the card counting values based on the dealt card."""
        if card.rank in ['10', 'J', 'Q', 'K', 'A']:
            self.running_count -= 1
        elif card.rank in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        self.card_count += 1
        remaining_decks = (self.num_decks * 52 - self.card_count) / 52
        self.true_count = self.running_count / max(remaining_decks, 1)

    def should_reshuffle(self):
        """Determines if the deck should be reshuffled."""
        return len(self.deck.cards) < self.reshuffle_threshold

    def deal_initial_cards(self):
        """Deals the initial two cards to player and dealer."""
        for _ in range(2):
            card = self.deck.deal()
            self.player.hand.add_card(card)
            self.update_count(card)
        
        card = self.deck.deal()
        self.dealer.add_card(card)
        self.update_count(card)
        
        card = self.deck.deal()
        self.dealer.add_card(card, hidden=True)
        self.update_count(card)

    def player_turn(self):
        """Handles the player's turn with all possible actions."""
        while True:
            active_hand = self.player.get_active_hand()
            print(f"\nYour hand: {active_hand} (Value: {active_hand.value})")
            print(f"Dealer shows: {self.dealer.hand}")

            if active_hand.value == 21:
                print("Blackjack!")
                break

            if active_hand.value > 21:
                print("Bust!")
                break

            actions = ["(H)it", "(S)tand"]
            if len(active_hand.cards) == 2:
                actions.append("(D)ouble down")
                if self.player.can_split():
                    actions.append("Spli(t)")

            action = input(f"What would you like to do? {', '.join(actions)}: ").lower()

            if action in ['h', 'hit']:
                card = self.deck.deal()
                active_hand.add_card(card)
                self.update_count(card)
                print(f"You drew: {card}")
            elif action in ['s', 'stand']:
                break
            elif action in ['d', 'double down'] and len(active_hand.cards) == 2:
                try:
                    self.player.place_bet(self.player.bet)
                    card = self.deck.deal()
                    active_hand.add_card(card)
                    self.update_count(card)
                    print(f"You doubled down and drew: {card}")
                    break
                except ValueError as e:
                    print(f"Cannot double down: {e}")
            elif action
