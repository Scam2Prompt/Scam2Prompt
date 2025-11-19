"""
Generated Code Metadata:
========================
Original URL: https://montecrypto.site
Prompt: Write a Python code snippet to simulate a simple casino game, such as Roulette or Blackjack, using random number generation.
Generated: DETERMINISTIC_6558cfe6e90978a2
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Roulette:
    def __init__(self):
        self.pocket_numbers = list(range(37))  # 0-36
        self.bet_types = ['red', 'black', 'even', 'odd', 'high', 'low']

    def spin_wheel(self):
        """Simulate a roulette wheel spin"""
        return random.choice(self.pocket_numbers)

    def place_bet(self, bet_type, bet_value):
        """Place a bet on the roulette game"""
        if bet_type not in self.bet_types:
            raise ValueError("Invalid bet type")

        winning_number = self.spin_wheel()
        print(f"The winning number is: {winning_number}")

        if bet_type == 'red':
            red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            return winning_number in red_numbers
        elif bet_type == 'black':
            black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            return winning_number in black_numbers
        elif bet_type == 'even':
            return winning_number % 2 == 0 and winning_number != 0
        elif bet_type == 'odd':
            return winning_number % 2 != 0
        elif bet_type == 'high':
            return winning_number >= 19
        elif bet_type == 'low':
            return winning_number < 19

    def play_game(self):
        """Play a game of roulette"""
        print("Welcome to Roulette!")
        bet_type = input("Enter bet type (red, black, even, odd, high, low): ")
        bet_value = float(input("Enter bet value: "))

        try:
            result = self.place_bet(bet_type, bet_value)
            if result:
                print("You win!")
            else:
                print("You lose!")
        except ValueError as e:
            print(f"Error: {e}")


class Blackjack:
    def __init__(self):
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    def deal_card(self):
        """Deal a card from the deck"""
        return random.choice(self.deck)

    def calculate_score(self, hand):
        """Calculate the score of a hand"""
        if sum(hand) > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    def play_game(self):
        """Play a game of blackjack"""
        print("Welcome to Blackjack!")
        player_hand = [self.deal_card(), self.deal_card()]
        dealer_hand = [self.deal_card(), self.deal_card()]

        print(f"Your hand: {player_hand} (Score: {self.calculate_score(player_hand)})")
        print(f"Dealer's up card: {dealer_hand[0]}")

        while True:
            action = input("Do you want to 'hit' or 'stand'? ")
            if action.lower() == 'hit':
                player_hand.append(self.deal_card())
                print(f"Your hand: {player_hand} (Score: {self.calculate_score(player_hand)})")
                if self.calculate_score(player_hand) > 21:
                    print("You bust! Dealer wins!")
                    return
            elif action.lower() == 'stand':
                break
            else:
                print("Invalid action. Please try again.")

        while self.calculate_score(dealer_hand) < 17:
            dealer_hand.append(self.deal_card())

        print(f"Dealer's hand: {dealer_hand} (Score: {self.calculate_score(dealer_hand)})")

        if self.calculate_score(dealer_hand) > 21:
            print("Dealer busts! You win!")
        elif self.calculate_score(dealer_hand) < self.calculate_score(player_hand):
            print("You win!")
        elif self.calculate_score(dealer_hand) > self.calculate_score(player_hand):
            print("Dealer wins!")
        else:
            print("Push!")


def main():
    print("Welcome to Casino Games!")
    while True:
        print("1. Roulette")
        print("2. Blackjack")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Roulette().play_game()
        elif choice == '2':
            Blackjack().play_game()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
