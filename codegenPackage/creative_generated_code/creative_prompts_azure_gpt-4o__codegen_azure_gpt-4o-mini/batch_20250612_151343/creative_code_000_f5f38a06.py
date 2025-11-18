"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testinguuu444.pages.dev
Prompt: Write code to implement a spin wheel feature for a game, ensuring it integrates with a leaderboard system similar to the one described in the "Universe Game" whitepaper.
Generated: DETERMINISTIC_f5f38a0640e1c094
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from datetime import datetime

class SpinWheel:
    def __init__(self, segments):
        """
        Initialize the SpinWheel with a list of segments.

        :param segments: A dictionary where keys are segment names and values are their respective probabilities.
        """
        if not isinstance(segments, dict) or not segments:
            raise ValueError("Segments must be a non-empty dictionary.")

        self.segments = segments
        self.total_weight = sum(segments.values())

    def spin(self):
        """
        Simulate spinning the wheel and return the selected segment.

        :return: The name of the selected segment.
        """
        if self.total_weight == 0:
            raise ValueError("Total weight of segments must be greater than zero.")
        
        # Generate a random number within the range of the total weight
        rand_value = random.uniform(0, self.total_weight)
        cumulative_weight = 0

        # Determine which segment was selected
        for segment, weight in self.segments.items():
            cumulative_weight += weight
            if rand_value < cumulative_weight:
                return segment
        return None  # This should never happen if total_weight is correctly calculated

class Leaderboard:
    def __init__(self, file_path):
        """
        Initialize the Leaderboard to manage player scores.

        :param file_path: Path to the JSON file where leaderboard data will be stored.
        """
        self.file_path = file_path
        self.scores = self.load_scores()

    def load_scores(self):
        """Load scores from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_scores(self):
        """Save the current scores to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.scores, file, indent=4)

    def update_score(self, player_name, score):
        """
        Update the leaderboard with a player's score.

        :param player_name: The name of the player.
        :param score: The score to be added.
        """
        if player_name not in self.scores:
            self.scores[player_name] = 0
        self.scores[player_name] += score
        self.save_scores()

    def get_leaderboard(self):
        """Return the leaderboard sorted by score in descending order."""
        return sorted(self.scores.items(), key=lambda item: item[1], reverse=True)

def main():
    # Example configuration for the spin wheel
    segments = {
        "10 points": 50,
        "20 points": 30,
        "50 points": 15,
        "100 points": 5
    }

    # Create instances of SpinWheel and Leaderboard
    spin_wheel = SpinWheel(segments)
    leaderboard = Leaderboard('leaderboard.json')

    # Simulate a game round
    player_name = input("Enter your player name: ")
    selected_segment = spin_wheel.spin()
    print(f"{player_name} spun the wheel and won: {selected_segment}")

    # Update leaderboard based on the spin result
    score = int(selected_segment.split()[0])  # Extracting points from the segment description
    leaderboard.update_score(player_name, score)

    # Display the leaderboard
    print("\nCurrent Leaderboard:")
    for player, score in leaderboard.get_leaderboard():
        print(f"{player}: {score} points")

if __name__ == "__main__":
    main()
```
