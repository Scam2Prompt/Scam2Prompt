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
import sys

class BlackjackGame:
    """
    A class to simulate a Blackjack game with basic betting and probability strategies.
    """

    def __init__(self):
        # Deck of cards
        self.deck = self.generate_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.balance = 1000  # Starting balance for the player
        self.bet = 0

    def generate_deck(self):
        """
        Generate a standard deck of 52 cards.
        Returns:
            list: A shuffled deck of cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [{'value': value, 'suit': suit} for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        """
        Deal a card to the specified hand.
        Args:
            hand (list): The hand to which the card will be added.
        """
        if not self.deck:
            self.deck = self.generate_deck()  # Reshuffle if the deck is empty
        hand.append(self.deck.pop())

    def calculate_hand_value(self, hand):
        """
        Calculate the total value of a hand in Blackjack.
        Args:
            hand (list): The hand to calculate.
        Returns:
            int: The total value of the hand.
        """
        value = 0
        aces = 0
        for card in hand:
            if card['value'] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card['value'] == 'Ace':
                aces += 1
                value += 11  # Consider Ace initially as 11
            else:
                value += int(card['value'])

        # Adjust for Aces
        while value > 21 and aces > 0:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1

        return value

    def place_bet(self):
        """
        Place a bet for the current round. Includes basic error handling for input.
        """
        while True:
            try:
                self.bet = int(input(f"Your current balance is ${self.balance}. Enter your bet: "))
                if self.bet <= 0:
                    print("Bet must be greater than 0.")
                elif self.bet > self.balance:
                    print("You cannot bet more than your balance.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def display_hand(self, hand, name):
        """
        Display the cards in a hand.
        Args:
            hand (list): The hand to display.
            name (str): The name of the player (Player or Dealer).
        """
        hand_display = ', '.join([f"{card['value']} of {card['suit']}" for card in hand])
        print(f"{name}'s hand: {hand_display} (value: {self.calculate_hand_value(hand)})")

    def player_turn(self):
        """
        Handle the player's turn to hit or stand.
        Returns:
            str: The player's decision ('stand' if player chooses to end their turn).
        """
        while True:
            self.display_hand(self.player_hand, "Player")
            decision = input("Would you like to 'hit' or 'stand'? ").strip().lower()
            if decision == 'hit':
                self.deal_card(self.player_hand)
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("You busted!")
                    return 'stand'
            elif decision == 'stand':
                return 'stand'
            else:
                print("Invalid input. Please type 'hit' or 'stand'.")

    def dealer_turn(self):
        """
        Handle the dealer's turn based on basic dealer strategy.
        """
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

    def determine_winner(self):
        """
        Determine the winner of the round and update the player's balance.
        """
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("\n--- Final Hands ---")
        self.display_hand(self.player_hand, "Player")
        self.display_hand(self.dealer_hand, "Dealer")

        if player_value > 21:
            print("You busted! Dealer wins.")
            self.balance -= self.bet
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            self.balance += self.bet
        elif player_value < dealer_value:
            print("Dealer wins.")
            self.balance -= self.bet
        else:
            print("It's a tie! Your bet is returned.")

    def play_round(self):
        """
        Play a single round of Blackjack.
        """
        self.player_hand = []
        self.dealer_hand = []
        self.place_bet()

        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.dealer_hand)

        print("\n--- Starting Hands ---")
        self.display_hand(self.player_hand, "Player")
        self.display_hand([self.dealer_hand[0]], "Dealer")  # Show only one dealer card

        # Player's turn
        self.player_turn()

        # Dealer's turn
        self.dealer_turn()

        # Determine winner
        self.determine_winner()

    def start_game(self):
        """
        Start the Blackjack game loop.
        """
        print("Welcome to Blackjack!")
        while self.balance > 0:
            self.play_round()
            if self.balance <= 0:
                print("You are out of money! Game over.")
                break

            play_again = input("Would you like to play another round? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Your final balance is ${self.balance}.")
                break

if __name__ == "__main__":
    try:
        game = BlackjackGame()
        game.start_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
        sys.exit(0)
```
