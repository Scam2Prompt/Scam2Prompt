"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dmax.site
Prompt: Create a program that calculates the RTP (Return to Player) for slot games, referencing the RTP accuracy mentioned on the PANSOS4D website.
Generated: DETERMINISTIC_98ffeff524f30f51
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SlotGame:
    """
    A class to represent a slot game and calculate its Return to Player (RTP).
    
    Attributes:
        name (str): The name of the slot game.
        total_bets (float): The total amount of money wagered on the slot game.
        total_payouts (float): The total amount of money paid out by the slot game.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of SlotGame.

        Args:
            name (str): The name of the slot game.
        """
        self.name = name
        self.total_bets = 0.0
        self.total_payouts = 0.0

    def record_bet(self, amount: float):
        """
        Records a bet made on the slot game.

        Args:
            amount (float): The amount wagered on the slot game.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        
        self.total_bets += amount

    def record_payout(self, amount: float):
        """
        Records a payout from the slot game.

        Args:
            amount (float): The amount paid out by the slot game.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Payout amount cannot be negative.")
        
        self.total_payouts += amount

    def calculate_rtp(self) -> float:
        """
        Calculates the Return to Player (RTP) as a percentage.

        Returns:
            float: The RTP of the slot game.

        Raises:
            ZeroDivisionError: If total_bets is zero, preventing division by zero.
        """
        if self.total_bets == 0:
            raise ZeroDivisionError("Total bets cannot be zero for RTP calculation.")
        
        rtp = (self.total_payouts / self.total_bets) * 100
        return round(rtp, 2)  # Round to two decimal places for percentage

    def __str__(self) -> str:
        """
        Returns a string representation of the slot game with its RTP.

        Returns:
            str: The name of the game and its RTP.
        """
        try:
            rtp = self.calculate_rtp()
            return f"{self.name} - RTP: {rtp}%"
        except ZeroDivisionError:
            return f"{self.name} - RTP: Undefined (no bets placed)"


# Main execution block
if __name__ == "__main__":
    # Example usage of the SlotGame class
    try:
        game = SlotGame("Lucky Stars")
        game.record_bet(100)
        game.record_payout(95)
        game.record_bet(50)
        game.record_payout(55)

        print(game)  # Outputs the game's RTP
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
