"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Generate code to simulate a blackjack game with an average RTP of 99%, incorporating strategies mentioned on Santa Claus Casino.
Generated: DETERMINISTIC_cb474a4f68a9753e
Batch ID: 20250612_151539
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
    """Represents a playing card with a rank and a suit."""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def value(self):
        """Returns the value of the card for Blackjack scoring."""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace can be 11 or 1, handled in hand value calculation
        else:
            return int(self.rank)

class Deck:
    """Represents a deck of cards."""
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal(self):
        """Deals one card from the deck."""
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()

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

class BlackjackGame:
    """Controls the flow of the Blackjack game."""
    
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        """Deals the initial two cards to both player and dealer."""
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def player_bust(self):
        """Checks if the player's hand exceeds 21."""
        return self.player_hand.value() > 21

    def dealer_bust(self):
        """Checks if the dealer's hand exceeds 21."""
        return self.dealer_hand.value() > 21

    def dealer_play(self):
        """Dealer plays by drawing cards until reaching 17 or higher."""
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

    def determine_winner(self):
        """Determines the winner based on the hands of the player and dealer."""
        if self.player_bust():
            return "Dealer wins! Player busts."
        if self.dealer_bust():
            return "Player wins! Dealer busts."
        
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()
        
        if player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"

    def play_game(self):
        """Main method to run the Blackjack game."""
        try:
            self.initial_deal()
            print(f"Player's hand: {[card.rank for card in self.player_hand.cards]}, Value: {self.player_hand.value()}")
            print(f"Dealer's hand: {[self.dealer_hand.cards[0].rank]}, Value: {self.dealer_hand.cards[0].value()} (one face down)")

            while True:
                action = input("Do you want to [hit] or [stand]? ").lower()
                if action == 'hit':
                    self.player_hand.add_card(self.deck.deal())
                    print(f"Player's hand: {[card.rank for card in self.player_hand.cards]}, Value: {self.player_hand.value()}")
                    if self.player_bust():
                        print(self.determine_winner())
                        return
                elif action == 'stand':
                    break
                else:
                    print("Invalid input. Please enter 'hit' or 'stand'.")

            self.dealer_play()
            print(f"Dealer's hand: {[card.rank for card in self.dealer_hand.cards]}, Value: {self.dealer_hand.value()}")
            print(self.determine_winner())

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()
```
