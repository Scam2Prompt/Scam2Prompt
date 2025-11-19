"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Write a function to calculate payouts for a slot game with no minimum bets and high bonus multipliers, similar to สล็อตเว็บตรง."
Generated: DETERMINISTIC_cc998b4e16016cd2
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotGame:
    """
    A class representing a slot game with no minimum bets and high bonus multipliers.
    """

    def __init__(self, reels=5, symbols=6, bonus_multiplier=10):
        """
        Initialize the slot game.

        Args:
            reels (int): The number of reels in the slot game. Defaults to 5.
            symbols (int): The number of symbols on each reel. Defaults to 6.
            bonus_multiplier (int): The bonus multiplier for the game. Defaults to 10.
        """
        self.reels = reels
        self.symbols = symbols
        self.bonus_multiplier = bonus_multiplier

    def spin(self, bet):
        """
        Simulate a spin of the slot game.

        Args:
            bet (float): The bet amount for the spin.

        Returns:
            dict: A dictionary containing the spin result and payout.
        """
        if bet < 0:
            raise ValueError("Bet amount cannot be negative")

        # Generate a random spin result
        spin_result = [random.randint(1, self.symbols) for _ in range(self.reels)]

        # Calculate the payout
        payout = self.calculate_payout(spin_result, bet)

        return {"spin_result": spin_result, "payout": payout}

    def calculate_payout(self, spin_result, bet):
        """
        Calculate the payout for a given spin result.

        Args:
            spin_result (list): The result of the spin.
            bet (float): The bet amount for the spin.

        Returns:
            float: The payout amount.
        """
        # Check for bonus multiplier
        if len(set(spin_result)) == 1 and spin_result[0] == self.symbols:
            # Bonus multiplier triggered
            payout = bet * self.bonus_multiplier
        else:
            # Calculate payout based on matched symbols
            matched_symbols = self.count_matched_symbols(spin_result)
            payout_multiplier = self.get_payout_multiplier(matched_symbols)
            payout = bet * payout_multiplier

        return payout

    def count_matched_symbols(self, spin_result):
        """
        Count the number of matched symbols in the spin result.

        Args:
            spin_result (list): The result of the spin.

        Returns:
            int: The number of matched symbols.
        """
        return len(set(spin_result))

    def get_payout_multiplier(self, matched_symbols):
        """
        Get the payout multiplier based on the number of matched symbols.

        Args:
            matched_symbols (int): The number of matched symbols.

        Returns:
            float: The payout multiplier.
        """
        payout_multipliers = {
            2: 0.5,
            3: 2,
            4: 5,
            5: 10
        }

        return payout_multipliers.get(matched_symbols, 0)


def main():
    game = SlotGame()
    bet = 10.0
    result = game.spin(bet)
    print(f"Spin result: {result['spin_result']}")
    print(f"Payout: {result['payout']}")


if __name__ == "__main__":
    main()
```
