"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartlayer-network.pages.dev
Prompt: Develop a lottery system in Python that mimics the Tier 2 allocation system for $SLN tokens, ensuring fairness and inclusivity.
Generated: DETERMINISTIC_1be6b8f2d998f747
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import defaultdict

class LotterySystem:
    def __init__(self):
        # Initialize the lottery system with a participants list and a results dictionary
        self.participants = []
        self.results = defaultdict(int)

    def add_participant(self, participant_id):
        """
        Add a participant to the lottery.
        
        :param participant_id: Unique identifier for the participant
        """
        if participant_id in self.participants:
            raise ValueError("Participant already added.")
        self.participants.append(participant_id)

    def draw_winners(self, num_winners):
        """
        Randomly draw winners from the participants.
        
        :param num_winners: Number of winners to be drawn.
        :return: List of winner IDs.
        """
        if num_winners > len(self.participants):
            raise ValueError("Number of winners exceeds number of participants.")
        
        winners = random.sample(self.participants, num_winners)
        
        # Update results for each winner
        for winner in winners:
            self.results[winner] += 1
            
        return winners

    def get_results(self):
        """
        Get the results of the lottery.
        
        :return: A dictionary with participant IDs as keys and win counts as values.
        """
        return dict(self.results)

    def reset_lottery(self):
        """
        Reset the lottery, clearing participants and results.
        """
        self.participants.clear()
        self.results.clear()

if __name__ == "__main__":
    # Example usage of the LotterySystem
    lottery = LotterySystem()
    
    # Adding participants
    try:
        lottery.add_participant("user1")
        lottery.add_participant("user2")
        lottery.add_participant("user3")
    except ValueError as e:
        print(f"Error: {e}")

    # Drawing winners
    try:
        winners = lottery.draw_winners(2)
        print(f"Winners: {winners}")
    except ValueError as e:
        print(f"Error: {e}")

    # Displaying results
    print("Lottery Results:", lottery.get_results())

    # Resetting the lottery for the next round
    lottery.reset_lottery()
```
