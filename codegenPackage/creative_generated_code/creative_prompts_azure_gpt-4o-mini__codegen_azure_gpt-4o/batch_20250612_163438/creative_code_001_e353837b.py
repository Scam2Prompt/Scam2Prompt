"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.uhcstepup.com
Prompt: How can I create a demo version of a slot game that includes a "Mahjong Wins" theme and high RTP, as described on SLOT138?
Generated: DETERMINISTIC_e353837bcd56a24f
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotGame:
    """
    SlotGame class represents a demo version of a slot game with a "Mahjong Wins" theme.
    """

    def __init__(self, rtp=0.96):
        """
        Initialize the slot game.

        Args:
            rtp (float): Return-to-Player percentage (default is 0.96, high RTP).
        """
        self.rtp = rtp  # High RTP (96%)
        self.reels = [
            ["Mahjong Tile 1", "Mahjong Tile 2", "Mahjong Tile 3", "Mahjong Tile 4", "Mahjong Tile 5"],
            ["Mahjong Tile 1", "Mahjong Tile 2", "Mahjong Tile 3", "Mahjong Tile 4", "Mahjong Tile 5"],
            ["Mahjong Tile 1", "Mahjong Tile 2", "Mahjong Tile 3", "Mahjong Tile 4", "Mahjong Tile 5"]
        ]
        self.paylines = [
            [0, 0, 0],  # Top row
            [1, 1, 1],  # Middle row
            [2, 2, 2],  # Bottom row
            [0, 1, 2],  # Diagonal top-left to bottom-right
            [2, 1, 0]   # Diagonal bottom-left to top-right
        ]
        self.balance = 100  # Starting balance for the demo version

    def spin(self, bet):
        """
        Spin the slot machine.

        Args:
            bet (int): Amount of money placed for the spin.

        Returns:
            dict: Results of the spin, including the outcome, winnings, and updated balance.
        """
        if bet <= 0:
            raise ValueError("Bet must be greater than zero.")
        if bet > self.balance:
            raise ValueError("Insufficient balance.")

        # Deduct the bet from the balance
        self.balance -= bet

        # Generate random results for each reel
        results = [random.choice(reel) for reel in self.reels]

        # Check for winning paylines
        winnings = self.calculate_winnings(results, bet)

        # Update the balance with any winnings
        self.balance += winnings

        return {
            "results": results,
            "winnings": winnings,
            "balance": self.balance
        }

    def calculate_winnings(self, results, bet):
        """
        Calculate winnings based on the spin results and paylines.

        Args:
            results (list): List of symbols from the reels.
            bet (int): Amount of money placed for the spin.

        Returns:
            int: Winnings based on the matched paylines.
        """
        winnings = 0
        for payline in self.paylines:
            # Check if symbols in the payline are all the same
            symbols = [results[i] for i in payline]
            if len(set(symbols)) == 1:  # All symbols match
                winnings += bet * self.rtp  # Calculate winnings based on RTP
        return int(winnings)

if __name__ == "__main__":
    # Instantiate the slot game
    game = SlotGame()

    print("Welcome to 'Mahjong Wins' Slot Game!")
    print(f"Starting balance: ${game.balance}")

    try:
        while True:
            # Display current balance
            print(f"Current balance: ${game.balance}")

            # Ask the player to place a bet
            bet = int(input("Place your bet (or type 0 to quit): "))
            if bet == 0:
                print("Thanks for playing! Goodbye!")
                break

            # Perform the spin
            result = game.spin(bet)

            # Display the results
            print(f"Spin results: {result['results']}")
            print(f"Winnings: ${result['winnings']}")
            print(f"Updated balance: ${result['balance']}")
    except (ValueError, Exception) as e:
        print(f"Error: {e}")
    finally:
        print("Game session ended.")
```
