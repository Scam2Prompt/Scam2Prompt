"""
Generated Code Metadata:
========================
Original URL: https://viysrbyrrsvrirsinylfyudluyxkyrzxyrgvulyhgxryskftdryk.pages.dev
Prompt: Create a function that calculates potential winnings based on the RTP values for games available on BetFury, such as Plinko and Dice.
Generated: DETERMINISTIC_453458f1c23029fb
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Game:
    def __init__(self, name: str, rtp: float):
        """
        Initializes a game with a name and RTP (Return to Player) value.

        :param name: The name of the game.
        :param rtp: The RTP value of the game as a percentage (0-100).
        """
        self.name = name
        self.rtp = rtp

    def calculate_winnings(self, bet_amount: float) -> float:
        """
        Calculates potential winnings based on the bet amount and the game's RTP.

        :param bet_amount: The amount of money bet on the game.
        :return: The potential winnings based on the RTP.
        :raises ValueError: If bet_amount is negative or RTP is not in the range of 0-100.
        """
        if bet_amount < 0:
            raise ValueError("Bet amount must be non-negative.")
        if not (0 <= self.rtp <= 100):
            raise ValueError("RTP must be between 0 and 100.")

        # Calculate potential winnings
        potential_winnings = bet_amount * (self.rtp / 100)
        return potential_winnings


def main():
    # Example games with their RTP values
    games = [
        Game("Plinko", 95.0),
        Game("Dice", 97.5)
    ]

    # Example bet amounts
    bet_amounts = [10.0, 50.0, 100.0]

    for game in games:
        print(f"Calculating potential winnings for {game.name}:")
        for bet in bet_amounts:
            try:
                winnings = game.calculate_winnings(bet)
                print(f"  Bet Amount: ${bet:.2f} -> Potential Winnings: ${winnings:.2f}")
            except ValueError as e:
                print(f"  Error: {e}")


if __name__ == "__main__":
    main()
```
