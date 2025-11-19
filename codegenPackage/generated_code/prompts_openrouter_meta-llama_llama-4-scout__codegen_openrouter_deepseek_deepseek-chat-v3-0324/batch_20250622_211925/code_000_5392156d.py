"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: "Write a Python script to simulate a Togel HK game, considering the rules and betting options described on Holyslots88, including 2D, 3D, and 4D bets."
Generated: DETERMINISTIC_5392156d2daf0121
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple, Optional

class TogelHKSimulator:
    """
    A simulator for Togel HK (Hong Kong) game with various betting options.
    Supports 2D, 3D, and 4D bets as per Holyslots88 rules.
    """

    def __init__(self):
        self.winning_number: Optional[str] = None
        self.bet_types = {
            '2D': self._check_2d,
            '3D': self._check_3d,
            '4D': self._check_4d
        }

    def generate_winning_number(self) -> str:
        """
        Generates a random 4-digit winning number for the game.
        
        Returns:
            str: A 4-digit string representing the winning number.
        """
        self.winning_number = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return self.winning_number

    def place_bet(self, bet_type: str, bet_number: str, bet_amount: float) -> Tuple[bool, float]:
        """
        Places a bet and checks if it wins against the generated winning number.
        
        Args:
            bet_type (str): Type of bet ('2D', '3D', or '4D').
            bet_number (str): The number being bet on (2, 3, or 4 digits).
            bet_amount (float): The amount wagered.
            
        Returns:
            Tuple[bool, float]: A tuple indicating if the bet won and the payout amount.
            
        Raises:
            ValueError: If bet_type is invalid or bet_number length doesn't match bet_type.
        """
        if not self.winning_number:
            raise ValueError("Winning number not generated. Call generate_winning_number() first.")
        
        if bet_type not in self.bet_types:
            raise ValueError(f"Invalid bet type. Must be one of {list(self.bet_types.keys())}")
        
        expected_length = int(bet_type[0])
        if len(bet_number) != expected_length:
            raise ValueError(f"Bet number for {bet_type} must be {expected_length} digits long.")
        
        if not bet_number.isdigit():
            raise ValueError("Bet number must contain only digits.")
        
        check_func = self.bet_types[bet_type]
        is_winner = check_func(bet_number)
        
        payout = self._calculate_payout(bet_type, bet_amount, is_winner)
        return (is_winner, payout)

    def _check_2d(self, bet_number: str) -> bool:
        """Check if a 2D bet matches the last 2 digits of the winning number."""
        return bet_number == self.winning_number[-2:]

    def _check_3d(self, bet_number: str) -> bool:
        """Check if a 3D bet matches the last 3 digits of the winning number."""
        return bet_number == self.winning_number[-3:]

    def _check_4d(self, bet_number: str) -> bool:
        """Check if a 4D bet matches the entire winning number."""
        return bet_number == self.winning_number

    def _calculate_payout(self, bet_type: str, bet_amount: float, is_winner: bool) -> float:
        """
        Calculate the payout based on bet type and whether it won.
        
        Args:
            bet_type (str): Type of bet ('2D', '3D', or '4D').
            bet_amount (float): The amount wagered.
            is_winner (bool): Whether the bet won.
            
        Returns:
            float: The payout amount (0 if lost).
        """
        if not is_winner:
            return 0.0
        
        payout_rates = {
            '2D': 70,  # 70:1 payout for 2D
            '3D': 400,  # 400:1 payout for 3D
            '4D': 3000  # 3000:1 payout for 4D
        }
        
        return bet_amount * payout_rates[bet_type]

    def get_winning_number(self) -> str:
        """
        Returns the current winning number.
        
        Returns:
            str: The current winning number.
            
        Raises:
            ValueError: If winning number hasn't been generated.
        """
        if not self.winning_number:
            raise ValueError("Winning number not generated yet.")
        return self.winning_number


# Example usage
if __name__ == "__main__":
    try:
        simulator = TogelHKSimulator()
        winning_number = simulator.generate_winning_number()
        print(f"Winning number: {winning_number}")

        # Example bets
        bets = [
            ('2D', '45', 10),
            ('3D', '345', 5),
            ('4D', winning_number, 1)
        ]

        for bet_type, bet_number, bet_amount in bets:
            try:
                won, payout = simulator.place_bet(bet_type, bet_number, bet_amount)
                result = "WON" if won else "LOST"
                print(f"Bet: {bet_type} {bet_number} (${bet_amount}) - {result}. Payout: ${payout:.2f}")
            except ValueError as e:
                print(f"Error placing bet {bet_type} {bet_number}: {str(e)}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
