"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Explain how to create a betting function for users to participate in meme battles using the $MK token.
Generated: DETERMINISTIC_986c4047c8e50c37
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MemeBattle:
    def __init__(self):
        # Initialize the meme battle with an empty list of participants and their bets
        self.participants = {}
        
    def add_participant(self, user_id, bet_amount):
        """
        Adds a participant to the meme battle with their bet amount.

        :param user_id: Unique identifier for the user
        :param bet_amount: Amount of $MK token the user is betting
        :raises ValueError: If the bet amount is negative or user already participated
        """
        if user_id in self.participants:
            raise ValueError("User already participated in the battle.")
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        self.participants[user_id] = bet_amount

    def determine_winner(self):
        """
        Randomly determines the winner of the meme battle among participants.

        :raises ValueError: If there are no participants
        :return: User ID of the winner
        """
        if not self.participants:
            raise ValueError("No participants in the battle.")
        
        # Randomly select a winner from the participants
        winner = random.choice(list(self.participants.keys()))
        return winner

    def distribute_prize(self):
        """
        Distributes the prize to the winner and resets the battle.

        :return: A dictionary containing the winner and the total prize amount
        """
        winner = self.determine_winner()
        total_prize = sum(self.participants.values())
        
        # Reset participants for the next battle
        self.participants.clear()
        
        return {
            "winner": winner,
            "total_prize": total_prize
        }


# Example usage
if __name__ == "__main__":
    battle = MemeBattle()
    
    try:
        battle.add_participant("user1", 10)
        battle.add_participant("user2", 15)
        battle.add_participant("user3", 20)
        
        prize_distribution = battle.distribute_prize()
        print(f"The winner is {prize_distribution['winner']} with a total prize of {prize_distribution['total_prize']} $MK tokens.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
