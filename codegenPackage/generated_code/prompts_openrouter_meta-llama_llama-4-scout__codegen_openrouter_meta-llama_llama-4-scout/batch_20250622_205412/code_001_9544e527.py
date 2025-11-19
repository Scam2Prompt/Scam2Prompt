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
    """Represents a standard playing card."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    """Represents a standard deck of 52 playing cards."""
    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Deals a single card from the deck."""
        return self.cards.pop()

class Hand:
    """Represents a player's hand of cards."""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def calculate_hand_value(self):
        """Calculates the total value of the hand."""
        value = 0
        aces = 0
        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            else:
                if card.value == 'Ace':
                    aces += 1
                    value += 11
                else:
                    value += 10

        # Adjust for Aces
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def __repr__(self):
        return f"Hand value: {self.calculate_hand_value()} with cards: {self.cards}"

class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        """Deals a card to the player."""
        self.hand.add_card(deck.deal())

    def stay(self):
        """Player chooses to stay."""
        pass

class Dealer(Player):
    """Represents the dealer in the game."""
    def play(self, deck):
        """Dealer's turn."""
        while self.hand.calculate_hand_value() < 17:
            self.hit(deck)

def play_game():
    deck = Deck()
    deck.shuffle()

    player = Player("Player")
    dealer = Dealer("Dealer")

    player.hit(deck)
    player.hit(deck)

    dealer.hit(deck)
    dealer.hit(deck)

    print(f"{player.name}'s hand: {player.hand}")
    print(f"{dealer.name}'s up card: {dealer.hand.cards[0]}")

    while True:
        action = input("Do you want to 'hit' or 'stay'? ")
        if action.lower() == 'hit':
            player.hit(deck)
            print(f"{player.name}'s hand: {player.hand}")
            if player.hand.calculate_hand_value() > 21:
                print(f"{player.name} busts! {dealer.name} wins!")
                return
        elif action.lower() == 'stay':
            player.stay()
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stay'.")

    dealer.play(deck)

    print(f"{player.name}'s hand: {player.hand}")
    print(f"{dealer.name}'s hand: {dealer.hand}")

    if dealer.hand.calculate_hand_value() > 21:
        print(f"{dealer.name} busts! {player.name} wins!")
    elif dealer.hand.calculate_hand_value() < player.hand.calculate_hand_value():
        print(f"{player.name} wins!")
    elif dealer.hand.calculate_hand_value() > player.hand.calculate_hand_value():
        print(f"{dealer.name} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
```
