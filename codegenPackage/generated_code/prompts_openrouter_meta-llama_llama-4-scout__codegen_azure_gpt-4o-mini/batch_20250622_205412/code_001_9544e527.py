"""
Generated Code Metadata:
========================
Original URL: https://travelobay.com
Prompt: Write a Python script to simulate a simple casino game, such as Blackjack, using object-oriented programming and random number generation.
Generated: DETERMINISTIC_9544e527b323fbb7
Batch ID: 20250622_205412
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
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        """Returns the value of the card for Blackjack."""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace can be 1 or 11, handled in hand evaluation
        else:
            return int(self.rank)

    def __str__(self):
        """Returns a string representation of the card."""
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of cards."""
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals a single card from the deck."""
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("No more cards in the deck.")


class Hand:
    """Represents a player's hand in Blackjack."""
    
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def value(self):
        """Calculates the total value of the hand."""
        total = sum(card.value() for card in self.cards)
        # Adjust for Aces
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        """Returns a string representation of the hand."""
        return ', '.join(str(card) for card in self.cards)


class BlackjackGame:
    """Represents a simple Blackjack game."""
    
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        """Starts the game by dealing initial cards."""
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
        self.show_hands()

    def show_hands(self):
        """Displays the current hands of the player and dealer."""
        print(f"Player's Hand: {self.player_hand} (Value: {self.player_hand.value()})")
        print(f"Dealer's Hand: {self.dealer_hand.cards[0]} and [Hidden]")

    def player_turn(self):
        """Handles the player's turn."""
        while True:
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                print(f"Player's Hand: {self.player_hand} (Value: {self.player_hand.value()})")
                if self.player_hand.value() > 21:
                    print("Player busts! Dealer wins.")
                    return False
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        """Handles the dealer's turn."""
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer's Hand: {self.dealer_hand} (Value: {self.dealer_hand.value()})")

    def determine_winner(self):
        """Determines the winner of the game."""
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()

        if dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        """Main method to play the game."""
        self.start_game()
        if self.player_turn():
            self.dealer_turn()
            self.determine_winner()


if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
```
