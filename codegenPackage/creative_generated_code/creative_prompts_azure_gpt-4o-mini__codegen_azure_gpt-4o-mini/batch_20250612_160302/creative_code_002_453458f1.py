"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viysrbyrrsvrirsinylfyudluyxkyrzxyrgvulyhgxryskftdryk.pages.dev
Prompt: Create a function that calculates potential winnings based on the RTP values for games available on BetFury, such as Plinko and Dice.
Generated: DETERMINISTIC_453458f1c23029fb
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Game:
    """Class representing a generic game with RTP (Return to Player) values."""
    
    def __init__(self, name: str, rtp: float):
        """
        Initializes a new game instance.
        
        Args:
            name (str): The name of the game.
            rtp (float): The RTP value of the game (as a percentage).
        
        Raises:
            ValueError: If rtp is not between 0 and 100.
        """
        if not (0 <= rtp <= 100):
            raise ValueError("RTP must be between 0 and 100.")
        
        self.name = name
        self.rtp = rtp / 100  # Convert RTP to decimal for calculations

    def calculate_winnings(self, bet_amount: float) -> float:
        """
        Calculates potential winnings based on the bet amount and the game's RTP.
        
        Args:
            bet_amount (float): The amount of money bet on the game.
        
        Returns:
            float: The potential winnings based on the RTP.
        
        Raises:
            ValueError: If bet_amount is negative.
        """
        if bet_amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        
        # Potential winnings calculation
        potential_winnings = bet_amount * self.rtp
        return potential_winnings


def main():
    """Main function to demonstrate the calculation of potential winnings."""
    try:
        # Example games with their respective RTP values
        games = [
            Game("Plinko", 97.0),
            Game("Dice", 98.0)
        ]

        # Define a bet amount
        bet_amount = 10.0  # Example bet amount

        # Calculate and display potential winnings for each game
        for game in games:
            winnings = game.calculate_winnings(bet_amount)
            print(f"Potential winnings for {game.name}: ${winnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
