"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimplena.vercel.app
Prompt: Create a function to track leaderboard rankings for participants in the $PLENA Quest using data provided by Galxe and Plena Finance.
Generated: DETERMINISTIC_5e5934c05fb728c3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class Leaderboard:
    def __init__(self):
        """
        Initialize an empty leaderboard.
        The leaderboard will be a dictionary with participant addresses as keys 
        and their corresponding scores as values.
        """
        self.scores: Dict[str, float] = {}

    def update_score(self, participant: str, score: float) -> None:
        """
        Update the score of a participant.

        :param participant: The address of the participant.
        :param score: The score to add to the participant's current score.
        :raises ValueError: If the score is negative.
        """
        if score < 0:
            raise ValueError("Score cannot be negative.")
        
        if participant in self.scores:
            self.scores[participant] += score
        else:
            self.scores[participant] = score

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """
        Get the current leaderboard rankings sorted by score in descending order.

        :return: A list of dictionaries containing participant addresses and their scores.
        """
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        return [{"participant": participant, "score": score} for participant, score in sorted_scores]

    def reset_leaderboard(self) -> None:
        """
        Reset the leaderboard, removing all participants and their scores.
        """
        self.scores.clear()

def main():
    """
    Main function to demonstrate leaderboard functionality.
    Example usage for the leaderboard tracking participants in the $PLENA Quest.
    """
    leaderboard = Leaderboard()
    
    # Simulate updating scores
    try:
        leaderboard.update_score("0x123ABC", 50)
        leaderboard.update_score("0x456DEF", 75)
        leaderboard.update_score("0x123ABC", 25)  # Adding more score to the existing participant
        
        # Fetch and print the leaderboard
        print("Current Leaderboard:")
        for entry in leaderboard.get_leaderboard():
            print(entry)
        
        # Reset leaderboard
        leaderboard.reset_leaderboard()
        print("Leaderboard after reset:", leaderboard.get_leaderboard())
        
    except ValueError as e:
        print(f"Error updating score: {e}")

if __name__ == "__main__":
    main()
```
