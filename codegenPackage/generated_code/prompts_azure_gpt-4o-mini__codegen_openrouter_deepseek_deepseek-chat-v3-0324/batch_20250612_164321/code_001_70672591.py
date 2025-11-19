"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: Write a Python function that simulates a Togel HK game, allowing users to select numbers and check against winning combinations.
Generated: DETERMINISTIC_70672591b9b1a9a4
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Tuple, Optional

class TogelHKGame:
    """
    A class to simulate a Togel HK (Hong Kong) lottery game.
    Players can select numbers and check against winning combinations.
    """
    
    def __init__(self):
        """Initialize the game with default settings."""
        self.winning_numbers: Optional[List[int]] = None
        self.prize_tiers = {
            '1st Prize': {'match': 6, 'payout': 5000000},
            '2nd Prize': {'match': 5, 'payout': 1000000},
            '3rd Prize': {'match': 4, 'payout': 500000},
            'Consolation': {'match': 3, 'payout': 50000}
        }
    
    def generate_winning_numbers(self) -> List[int]:
        """
        Generate 6 unique random winning numbers between 1 and 49.
        
        Returns:
            List[int]: List of 6 unique sorted numbers
        """
        self.winning_numbers = sorted(random.sample(range(1, 50), 6))
        return self.winning_numbers
    
    def check_numbers(self, user_numbers: List[int]) -> Tuple[bool, dict]:
        """
        Check user's numbers against winning numbers and determine prizes.
        
        Args:
            user_numbers (List[int]): List of 6 unique numbers between 1 and 49
            
        Returns:
            Tuple[bool, dict]: (True if any prize won, dictionary of prize results)
            
        Raises:
            ValueError: If input is invalid or winning numbers not generated
        """
        if not self.winning_numbers:
            raise ValueError("Winning numbers not generated yet. Call generate_winning_numbers() first.")
        
        if len(user_numbers) != 6 or len(set(user_numbers)) != 6:
            raise ValueError("Please provide 6 unique numbers.")
        
        if any(num < 1 or num > 49 for num in user_numbers):
            raise ValueError("All numbers must be between 1 and 49.")
        
        matched = len(set(user_numbers) & set(self.winning_numbers))
        results = {}
        won_any = False
        
        for prize, details in self.prize_tiers.items():
            if matched >= details['match']:
                results[prize] = {
                    'matched': matched,
                    'payout': details['payout']
                }
                won_any = True
        
        return (won_any, results)
    
    def play_round(self, user_numbers: List[int]) -> dict:
        """
        Complete game round: generate numbers and check results.
        
        Args:
            user_numbers (List[int]): List of 6 unique numbers between 1 and 49
            
        Returns:
            dict: Game results including winning numbers and prizes
        """
        self.generate_winning_numbers()
        won, prizes = self.check_numbers(user_numbers)
        
        return {
            'user_numbers': user_numbers,
            'winning_numbers': self.winning_numbers,
            'won_any': won,
            'prizes': prizes
        }


# Example usage
if __name__ == "__main__":
    try:
        game = TogelHKGame()
        
        # Simulate user input (in practice, this would come from user)
        user_picks = [5, 12, 23, 34, 41, 49]
        
        # Play a round
        results = game.play_round(user_picks)
        
        # Display results
        print(f"Your numbers: {results['user_numbers']}")
        print(f"Winning numbers: {results['winning_numbers']}")
        
        if results['won_any']:
            print("\nCongratulations! You won:")
            for prize, details in results['prizes'].items():
                print(f"- {prize}: Matched {details['matched']} numbers, Payout: ${details['payout']:,}")
        else:
            print("\nSorry, you didn't win any prizes this time.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
