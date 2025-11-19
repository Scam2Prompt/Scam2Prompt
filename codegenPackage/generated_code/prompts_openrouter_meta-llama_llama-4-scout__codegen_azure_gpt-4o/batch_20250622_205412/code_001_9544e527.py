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
    """
    Represents a single playing card.
    """
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """
        Builds a standard deck of 52 cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank, values[rank]))

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def deal_card(self):
        """
        Deals a single card from the deck.
        """
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck!")
        return self.cards.pop()


class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        """
        Adds a card to the player's hand.
        """
        self.hand.append(card)

    def calculate_hand_value(self):
        """
        Calculates the total value of the player's hand.
        Adjusts for Aces if the total exceeds 21.
        """
        value = sum(card.value for card in self.hand)
        # Adjust for Aces
        ace_count = sum(1 for card in self.hand if card.rank == 'Ace')
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
        return value

    def show_hand(self):
        """
        Displays the player's hand.
        """
        return ', '.join(str(card) for card in self.hand)


class BlackjackGame:
    """
    Represents the Blackjack game logic.
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        """
        Deals two cards to both the player and the dealer.
        """
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def player_turn(self):
        """
        Handles the player's turn.
        """
        while True:
            print(f"Your hand: {self.player.show_hand()} (Value: {self.player.calculate_hand_value()})")
            if self.player.calculate_hand_value() > 21:
                print("You busted! Dealer wins.")
                return False
            choice = input("Do you want to (H)it or (S)tand? ").strip().lower()
            if choice == 'h':
                self.player.add_card(self.deck.deal_card())
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please choose 'H' or 'S'.")
        return True

    def dealer_turn(self):
        """
        Handles the dealer's turn.
        """
        print(f"Dealer's hand: {self.dealer.show_hand()} (Value: {self.dealer.calculate_hand_value()})")
        while self.dealer.calculate_hand_value() < 17:
            print("Dealer hits.")
            self.dealer.add_card(self.deck.deal_card())
            print(f"Dealer's hand: {self.dealer.show_hand()} (Value: {self.dealer.calculate_hand_value()})")
        if self.dealer.calculate_hand_value() > 21:
            print("Dealer busted! You win.")
            return False
        return True

    def determine_winner(self):
        """
        Determines the winner of the game.
        """
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()
        print(f"Your hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")
        if player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        """
        Starts the Blackjack game.
        """
        print("Welcome to Blackjack!")
        self.deal_initial_cards()
        if not self.player_turn():
            return
        if not self.dealer_turn():
            return
        self.determine_winner()


if __name__ == "__main__":
    try:
        game = BlackjackGame()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
