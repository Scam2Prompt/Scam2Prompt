"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://downtownspokanehotels.com
Prompt: Write a Python function that simulates a Togel HK game, allowing users to select numbers and check against winning combinations.
Generated: DETERMINISTIC_70672591b9b1a9a4
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TogelHKGame:
    def __init__(self):
        """Initialize the Togel HK game with a set of winning numbers."""
        self.winning_numbers = self.generate_winning_numbers()
    
    def generate_winning_numbers(self):
        """Generate a list of 6 unique random winning numbers between 1 and 49."""
        return random.sample(range(1, 50), 6)

    def check_user_numbers(self, user_numbers):
        """Check if the user's selected numbers match the winning numbers.
        
        Args:
            user_numbers (list): A list of numbers selected by the user.
        
        Returns:
            tuple: A tuple containing the count of matches and the matching numbers.
        """
        if not self.validate_user_numbers(user_numbers):
            raise ValueError("User numbers must be a list of 6 unique numbers between 1 and 49.")
        
        # Find matches between user numbers and winning numbers
        matches = set(user_numbers).intersection(set(self.winning_numbers))
        return len(matches), list(matches)

    def validate_user_numbers(self, user_numbers):
        """Validate the user's selected numbers.
        
        Args:
            user_numbers (list): A list of numbers selected by the user.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        return (isinstance(user_numbers, list) and 
                len(user_numbers) == 6 and 
                all(isinstance(num, int) for num in user_numbers) and 
                len(set(user_numbers)) == 6 and 
                all(1 <= num <= 49 for num in user_numbers))

    def play_game(self, user_numbers):
        """Simulate playing the Togel HK game.
        
        Args:
            user_numbers (list): A list of numbers selected by the user.
        
        Returns:
            str: Result of the game including matches found and winning numbers.
        """
        try:
            match_count, matches = self.check_user_numbers(user_numbers)
            return (f"You selected: {user_numbers}\n"
                    f"Winning numbers: {self.winning_numbers}\n"
                    f"Match count: {match_count}\n"
                    f"Matching numbers: {matches}")
        except ValueError as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    game = TogelHKGame()
    user_numbers = [5, 12, 23, 34, 45, 49]  # Example user input
    result = game.play_game(user_numbers)
    print(result)
```
