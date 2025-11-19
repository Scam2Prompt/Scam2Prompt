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
import sys

class Card:
    """Represents a playing card with a suit and value."""
    
    def __init__(self, suit, value):
        """Initialize a card with suit and value."""
        self.suit = suit
        self.value = value
    
    def __str__(self):
        """Return string representation of the card."""
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents a deck of 52 playing cards."""
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self):
        """Initialize a full deck of cards."""
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        self.shuffle()
    
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)
    
    def deal(self):
        """Deal one card from the deck."""
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()

class Hand:
    """Represents a player's hand of cards."""
    
    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        """Add a card to the hand."""
        self.cards.append(card)
        self._update_value()
    
    def _update_value(self):
        """Calculate the value of the hand."""
        self.value = 0
        aces = 0
        
        for card in self.cards:
            if card.value in ['Jack', 'Queen', 'King']:
                self.value += 10
            elif card.value == 'Ace':
                self.value += 11
                aces += 1
            else:
                self.value += int(card.value)
        
        # Adjust for aces if value is over 21
        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1
    
    def __str__(self):
        """Return string representation of the hand."""
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    """Represents a game of Blackjack."""
    
    def __init__(self):
        """Initialize a new game with a deck and hands for player and dealer."""
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    
    def deal_initial_cards(self):
        """Deal initial two cards to player and dealer."""
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
    
    def player_hit(self):
        """Player draws another card."""
        self.player_hand.add_card(self.deck.deal())
        return self.player_hand.value <= 21
    
    def dealer_play(self):
        """Dealer plays according to standard rules."""
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())
    
    def determine_winner(self):
        """Determine the winner of the game."""
        player_value = self.player_hand.value
        dealer_value = self.dealer_hand.value
        
        if player_value > 21:
            return "Player busts! Dealer wins."
        elif dealer_value > 21:
            return "Dealer busts! Player wins."
        elif player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"
    
    def play(self):
        """Play a full round of Blackjack."""
        print("Welcome to Blackjack!\n")
        self.deal_initial_cards()
        
        print(f"Dealer shows: {self.dealer_hand.cards[0]}")
        print(f"Your hand: {self.player_hand} (Value: {self.player_hand.value})")
        
        # Player's turn
        while True:
            action = input("\nHit or stand? (h/s): ").lower()
            if action == 'h':
                if not self.player_hit():
                    print(f"\nYour hand: {self.player_hand} (Value: {self.player_hand.value})")
                    print("You busted!")
                    break
                print(f"\nYour hand: {self.player_hand} (Value: {self.player_hand.value})")
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        
        # Dealer's turn if player didn't bust
        if self.player_hand.value <= 21:
            print(f"\nDealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.value})")
            self.dealer_play()
            print(f"Dealer's final hand: {self.dealer_hand} (Value: {self.dealer_hand.value})")
        
        # Determine winner
        print(f"\n{self.determine_winner()}")

def main():
    """Main function to run the Blackjack game."""
    while True:
        game = BlackjackGame()
        game.play()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
```
