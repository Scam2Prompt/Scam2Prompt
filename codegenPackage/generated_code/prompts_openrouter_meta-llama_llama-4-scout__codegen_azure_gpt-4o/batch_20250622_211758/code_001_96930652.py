"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.eu.com
Prompt: Write a Python script to simulate a simple game of Xì Dách (Blackjack) as offered by Sunwin, including basic rules and betting mechanisms.
Generated: DETERMINISTIC_96930652c8dd83ba
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BlackjackGame:
    def __init__(self):
        # Initialize the deck, player balance, and other game variables
        self.deck = self.create_deck()
        self.player_balance = 1000  # Starting balance for the player
        self.bet_amount = 0
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """Create a standard 52-card deck."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

    def shuffle_deck(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)

    def deal_card(self):
        """Deal a card from the deck."""
        if not self.deck:
            raise ValueError("The deck is empty. Cannot deal more cards.")
        return self.deck.pop()

    def calculate_hand_value(self, hand):
        """Calculate the total value of a hand."""
        value = 0
        aces = 0
        for card in hand:
            if card['rank'] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card['rank'] == 'Ace':
                aces += 1
                value += 11  # Initially count Ace as 11
            else:
                value += int(card['rank'])

        # Adjust for Aces if value exceeds 21
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def place_bet(self):
        """Prompt the player to place a bet."""
        while True:
            try:
                bet = int(input(f"Your balance: ${self.player_balance}. Enter your bet: "))
                if bet <= 0 or bet > self.player_balance:
                    raise ValueError("Invalid bet amount.")
                self.bet_amount = bet
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def display_hand(self, hand, is_dealer=False):
        """Display the cards in a hand."""
        if is_dealer:
            print("Dealer's hand:")
        else:
            print("Your hand:")
        for card in hand:
            print(f"{card['rank']} of {card['suit']}")
        print(f"Total value: {self.calculate_hand_value(hand)}\n")

    def player_turn(self):
        """Handle the player's turn."""
        while True:
            self.display_hand(self.player_hand)
            if self.calculate_hand_value(self.player_hand) > 21:
                print("You busted!")
                return False
            choice = input("Do you want to (H)it or (S)tand? ").strip().lower()
            if choice == 'h':
                self.player_hand.append(self.deal_card())
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please enter 'H' or 'S'.")
        return True

    def dealer_turn(self):
        """Handle the dealer's turn."""
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
        self.display_hand(self.dealer_hand, is_dealer=True)

    def determine_winner(self):
        """Determine the winner of the game."""
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if player_value > 21:
            print("You lose! Dealer wins.")
            self.player_balance -= self.bet_amount
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            self.player_balance += self.bet_amount
        elif player_value < dealer_value:
            print("You lose! Dealer wins.")
            self.player_balance -= self.bet_amount
        else:
            print("It's a tie!")

    def play_round(self):
        """Play a single round of Blackjack."""
        # Reset hands and shuffle deck
        self.player_hand = []
        self.dealer_hand = []
        self.shuffle_deck()

        # Place bet
        self.place_bet()

        # Initial deal
        self.player_hand.append(self.deal_card())
        self.player_hand.append(self.deal_card())
        self.dealer_hand.append(self.deal_card())
        self.dealer_hand.append(self.deal_card())

        # Display initial hands
        self.display_hand(self.player_hand)
        print("Dealer's visible card:")
        print(f"{self.dealer_hand[0]['rank']} of {self.dealer_hand[0]['suit']}\n")

        # Player's turn
        if not self.player_turn():
            return

        # Dealer's turn
        self.dealer_turn()

        # Determine winner
        self.determine_winner()

    def start_game(self):
        """Start the Blackjack game."""
        print("Welcome to Xì Dách (Blackjack)!")
        while self.player_balance > 0:
            self.play_round()
            if self.player_balance <= 0:
                print("You are out of money! Game over.")
                break
            play_again = input("Do you want to play another round? (Y/N): ").strip().lower()
            if play_again != 'y':
                print("Thanks for playing! Goodbye.")
                break


if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()
```
