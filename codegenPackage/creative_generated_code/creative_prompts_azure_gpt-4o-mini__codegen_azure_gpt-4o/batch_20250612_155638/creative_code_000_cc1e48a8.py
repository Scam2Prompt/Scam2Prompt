"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Generate a Python script that simulates betting on online slots, incorporating features from the "how do progressive slot machines work" section on walletguard.pro.
Generated: DETERMINISTIC_cc1e48a87d86bf0e
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class ProgressiveSlotMachine:
    """
    A class to simulate a progressive slot machine.
    """

    def __init__(self, base_jackpot=1000, jackpot_growth_rate=0.01):
        """
        Initializes the slot machine with a base jackpot and growth rate.

        Args:
            base_jackpot (float): Initial jackpot amount.
            jackpot_growth_rate (float): Percentage of the bet that contributes to the jackpot.
        """
        self.base_jackpot = base_jackpot
        self.current_jackpot = base_jackpot
        self.jackpot_growth_rate = jackpot_growth_rate
        self.reel_symbols = ["Cherry", "7", "Bar", "Bell", "Diamond", "Heart"]  # Example symbols

    def spin(self, bet):
        """
        Simulates a spin of the slot machine.

        Args:
            bet (float): Amount wagered by the player.

        Returns:
            dict: Result of the spin, including symbols, outcome, and jackpot amount.
        """
        if bet <= 0:
            raise ValueError("Bet must be greater than 0.")

        # Increment jackpot based on bet
        self.current_jackpot += bet * self.jackpot_growth_rate

        # Randomly generate symbols on three reels
        reels = [random.choice(self.reel_symbols) for _ in range(3)]

        # Determine if player wins the jackpot (e.g., all symbols match)
        if len(set(reels)) == 1:  # All symbols match
            jackpot_won = self.current_jackpot
            self.current_jackpot = self.base_jackpot  # Reset jackpot
            return {
                "reels": reels,
                "outcome": "Jackpot Won!",
                "jackpot_won": jackpot_won,
                "current_jackpot": self.current_jackpot,
            }

        # Determine smaller payouts (e.g., two symbols match)
        elif len(set(reels)) == 2:  # Two symbols match
            payout = bet * 2  # Example payout multiplier
            return {
                "reels": reels,
                "outcome": "Small Win!",
                "payout": payout,
                "current_jackpot": self.current_jackpot,
            }

        # No win
        else:
            return {
                "reels": reels,
                "outcome": "No Win",
                "current_jackpot": self.current_jackpot,
            }


def main():
    """
    Main function to simulate betting on the slot machine.
    """
    print("Welcome to the Progressive Slot Machine!")
    print("Each spin contributes to the growing jackpot.")

    # Initialize slot machine
    slot_machine = ProgressiveSlotMachine(base_jackpot=1000, jackpot_growth_rate=0.01)

    while True:
        try:
            # Get user input for bet amount
            bet = float(input("Enter your bet amount (or type '0' to exit): "))
            if bet == 0:
                print("Thank you for playing!")
                break

            # Spin the slot machine
            result = slot_machine.spin(bet)

            # Display results
            print("\nSpin Result:")
            print(f"Reels: {result['reels']}")
            print(f"Outcome: {result['outcome']}")

            if "jackpot_won" in result:
                print(f"You won the jackpot of ${result['jackpot_won']:.2f}!")
            elif "payout" in result:
                print(f"You won ${result['payout']:.2f}!")
            else:
                print("Better luck next time!")

            print(f"Current Jackpot: ${result['current_jackpot']:.2f}\n")

        except ValueError as e:
            # Handle invalid input
            print(f"Error: {e}. Please enter a valid number.")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
