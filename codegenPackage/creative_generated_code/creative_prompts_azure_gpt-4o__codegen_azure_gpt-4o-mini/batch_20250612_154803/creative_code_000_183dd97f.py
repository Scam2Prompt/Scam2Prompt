"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Write code to simulate a slot machine game with high RTP settings, inspired by the games listed on Planet128, such as Gates of Olympus or Sweet Bonanza.
Generated: DETERMINISTIC_183dd97ff1cfc5e3
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    def __init__(self, reels, symbols, winning_combinations, max_bet, min_bet):
        """
        Initialize the SlotMachine with the given parameters.

        :param reels: Number of reels in the slot machine.
        :param symbols: List of symbols used in the slot machine.
        :param winning_combinations: Dictionary of winning combinations and their payouts.
        :param max_bet: Maximum bet allowed per spin.
        :param min_bet: Minimum bet allowed per spin.
        """
        self.reels = reels
        self.symbols = symbols
        self.winning_combinations = winning_combinations
        self.max_bet = max_bet
        self.min_bet = min_bet

    def spin(self, bet):
        """
        Simulate a spin of the slot machine.

        :param bet: Amount to bet on the spin.
        :return: A tuple consisting of the outcome and the winnings.
        """
        if not self.min_bet <= bet <= self.max_bet:
            raise ValueError(f"Bet must be between {self.min_bet} and {self.max_bet}.")

        # Generate the outcome of the spin
        outcome = [random.choice(self.symbols) for _ in range(self.reels)]
        winnings = self.calculate_winnings(outcome, bet)

        return outcome, winnings

    def calculate_winnings(self, outcome, bet):
        """
        Calculate winnings based on the outcome of the spin.

        :param outcome: Result of the spin (list of symbols).
        :param bet: Amount bet on the spin.
        :return: Winnings based on the outcome.
        """
        # Create a string representation of the outcome for pattern matching
        outcome_str = ''.join(outcome)

        # Check for winnings based on defined winning combinations
        for combo, payout in self.winning_combinations.items():
            if combo in outcome_str:
                return bet * payout  # Multiplying bet by payout ratio

        return 0  # No winnings if no combinations match

def main():
    # Define symbols and winning combinations
    symbols = ['🍒', '🍋', '🍊', '🔔', '💎', '🍀']
    winning_combinations = {
        '🍒🍒🍒': 10,
        '🍋🍋🍋': 20,
        '🍊🍊🍊': 30,
        '🔔🔔🔔': 50,
        '💎💎💎': 100,
        '🍀🍀🍀': 200
    }

    # Create a SlotMachine instance
    slot_machine = SlotMachine(reels=3, symbols=symbols, 
                               winning_combinations=winning_combinations,
                               max_bet=100, min_bet=1)

    # Simulating a game loop
    while True:
        try:
            # Get user's bet
            bet = int(input(f"Enter your bet ({slot_machine.min_bet}-{slot_machine.max_bet}): "))
            outcome, winnings = slot_machine.spin(bet)

            # Display the result
            print(f"Outcome: {' | '.join(outcome)}")
            if winnings > 0:
                print(f"You win: {winnings} coins!")
            else:
                print("No winnings this round.")

            # Ask to continue or exit
            continue_game = input("Do you want to play again? (y/n): ").strip().lower()
            if continue_game != 'y':
                print("Thank you for playing!")
                break

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
