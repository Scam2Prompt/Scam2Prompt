"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Create a Python program to simulate a Blackjack game with advanced strategies for calculating probabilities and managing bets, inspired by 789Club’s casino offerings.
Generated: DETERMINISTIC_c67affb538372960
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
    
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit, rank):
        if suit not in self.SUITS or rank not in self.RANKS:
            raise ValueError("Invalid card suit or rank.")
        self.suit = suit
        self.rank = rank

    def value(self):
        """Returns the value of the card for Blackjack."""
        if self.rank in ('Jack', 'Queen', 'King'):
            return 10
        elif self.rank == 'Ace':
            return 11  # Ace can also be 1, handled in hand value calculation
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of cards."""

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck."""
        if not self.cards:
            raise ValueError("No cards left in the deck.")
        return self.cards.pop()


class Hand:
    """Represents a player's or dealer's hand in Blackjack."""
    
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def value(self):
        """Calculates the total value of the hand, treating Aces as 1 or 11 as appropriate."""
        total = sum(card.value() for card in self.cards)
        aces_count = sum(1 for card in self.cards if card.rank == 'Ace')

        # Adjust for Aces
        while total > 21 and aces_count:
            total -= 10
            aces_count -= 1
        
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class BlackjackGame:
    """Simulates a game of Blackjack."""

    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_balance = 1000  # Starting balance
        self.bet_amount = 0

    def place_bet(self, amount):
        """Places a bet for the player."""
        if amount <= 0 or amount > self.player_balance:
            raise ValueError("Invalid bet amount.")
        self.bet_amount = amount

    def deal_cards(self):
        """Deals two initial cards to both player and dealer."""
        for _ in range(2):
            self.player_hand.add_card(self.deck.draw())
            self.dealer_hand.add_card(self.deck.draw())

    def check_winner(self):
        """Determines the winner of the game."""
        player_total = self.player_hand.value()
        dealer_total = self.dealer_hand.value()

        if player_total > 21:
            return "Dealer wins! Player busts."
        elif dealer_total > 21:
            return "Player wins! Dealer busts."
        elif player_total == dealer_total:
            return "It's a tie!"
        elif player_total > dealer_total:
            return f"Player wins! (Player: {player_total}, Dealer: {dealer_total})"
        else:
            return f"Dealer wins! (Player: {player_total}, Dealer: {dealer_total})"

    def play_round(self):
        """Plays a single round of Blackjack."""
        while True:
            bet_amount = input(f"Place your bet (Current balance: ${self.player_balance}): ")
            try:
                self.place_bet(int(bet_amount))
                break
            except ValueError as e:
                print(f"Error: {e}")

        self.deal_cards()
        print(f"Player Hand: {self.player_hand}")
        print(f"Dealer shows: {self.dealer_hand.cards[0]}")

        # Player's turn
        while self.player_hand.value() < 21:
            action = input("Choose action: (h)it or (s)tand: ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.draw())
                print(f"Player Hand: {self.player_hand}")
            elif action == 's':
                break
            else:
                print("Invalid action. Please choose 'h' or 's'.")

        # Dealer's turn
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.draw())

        # Determine winner
        result = self.check_winner()
        print(result)

        # Update balance based on outcome
        if "wins!" in result:
            self.player_balance += self.bet_amount
        else:
            self.player_balance -= self.bet_amount

    def play_game(self):
        """Starts the game loop."""
        while self.player_balance > 0:
            self.play_round()
            continue_game = input("Do you want to play another round? (y/n): ").lower()
            if continue_game != 'y':
                break

        print("Game over! Final balance:", self.player_balance)


if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()
```
