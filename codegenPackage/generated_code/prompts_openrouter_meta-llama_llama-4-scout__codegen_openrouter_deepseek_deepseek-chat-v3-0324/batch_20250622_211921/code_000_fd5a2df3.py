"""
Generated Code Metadata:
========================
Original URL: https://www.qatar2022.pro
Prompt: Write a Python code snippet to implement a simple lottery game simulator like Magetoto's togel game, considering the game's rules and payout structure.
Generated: DETERMINISTIC_fd5a2df36680c9ba
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class TogelGame:
    """
    A simple lottery game simulator similar to Magetoto's togel game.
    The game allows players to bet on 2-digit, 3-digit, or 4-digit numbers.
    Payouts are based on the type of bet and the accuracy of the prediction.
    """
    
    def __init__(self):
        """Initialize the game with default payout rates."""
        self.payout_rates = {
            '2d': {'exact': 70, 'permutation': 35},
            '3d': {'exact': 400, 'permutation': 200},
            '4d': {'exact': 3000, 'permutation': 1500}
        }
        self.winning_number = None
    
    def generate_winning_number(self, digits: int) -> str:
        """
        Generate a random winning number with the specified digits.
        
        Args:
            digits: The number of digits (2, 3, or 4).
            
        Returns:
            A string representing the winning number.
            
        Raises:
            ValueError: If digits is not 2, 3, or 4.
        """
        if digits not in (2, 3, 4):
            raise ValueError("Digits must be 2, 3, or 4.")
        
        self.winning_number = ''.join([str(random.randint(0, 9)) for _ in range(digits)])
        return self.winning_number
    
    def check_bet(self, bet_type: str, user_number: str) -> Tuple[bool, bool, int]:
        """
        Check if the user's bet matches the winning number.
        
        Args:
            bet_type: The type of bet ('2d', '3d', or '4d').
            user_number: The user's chosen number as a string.
            
        Returns:
            A tuple containing:
                - exact_match: True if the number matches exactly.
                - permutation_match: True if the number matches as a permutation.
                - payout: The payout amount based on the bet type and match.
                
        Raises:
            ValueError: If bet_type is invalid or user_number length doesn't match bet_type.
            RuntimeError: If winning number hasn't been generated.
        """
        if bet_type not in self.payout_rates:
            raise ValueError("Invalid bet type. Must be '2d', '3d', or '4d'.")
        
        if self.winning_number is None:
            raise RuntimeError("Winning number has not been generated.")
        
        expected_length = int(bet_type[0])
        if len(user_number) != expected_length:
            raise ValueError(f"User number must be {expected_length} digits for {bet_type} bet.")
        
        if not user_number.isdigit():
            raise ValueError("User number must contain only digits.")
        
        exact_match = user_number == self.winning_number
        permutation_match = (
            sorted(user_number) == sorted(self.winning_number) and
            not exact_match
        )
        
        payout = 0
        if exact_match:
            payout = self.payout_rates[bet_type]['exact']
        elif permutation_match:
            payout = self.payout_rates[bet_type]['permutation']
        
        return exact_match, permutation_match, payout
    
    def play_round(self, bet_type: str, user_number: str, bet_amount: float) -> Dict:
        """
        Simulate a single round of the game.
        
        Args:
            bet_type: The type of bet ('2d', '3d', or '4d').
            user_number: The user's chosen number as a string.
            bet_amount: The amount bet by the user.
            
        Returns:
            A dictionary containing:
                - winning_number: The generated winning number.
                - user_number: The user's chosen number.
                - exact_match: True if exact match.
                - permutation_match: True if permutation match.
                - payout: The total payout amount.
                - winnings: The net winnings (payout - bet_amount).
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")
        
        winning_number = self.generate_winning_number(int(bet_type[0]))
        exact_match, permutation_match, payout_multiplier = self.check_bet(bet_type, user_number)
        
        payout = bet_amount * payout_multiplier
        winnings = payout - bet_amount
        
        return {
            'winning_number': winning_number,
            'user_number': user_number,
            'exact_match': exact_match,
            'permutation_match': permutation_match,
            'payout': payout,
            'winnings': winnings
        }

# Example usage
if __name__ == "__main__":
    game = TogelGame()
    
    try:
        # Simulate a 2D bet
        result = game.play_round('2d', '12', 1.0)
        print(f"Winning Number: {result['winning_number']}")
        print(f"Your Number: {result['user_number']}")
        if result['exact_match']:
            print("Exact match! You win!")
        elif result['permutation_match']:
            print("Permutation match! You win!")
        else:
            print("No match. Better luck next time!")
        print(f"Payout: ${result['payout']:.2f}")
        print(f"Net Winnings: ${result['winnings']:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
```
