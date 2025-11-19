"""
Generated Code Metadata:
========================
Original URL: https://clhaingpt.org
Prompt: Write a function that dynamically adjusts the difficulty level of a game based on user performance, similar to the AI adaptive features mentioned for Rusiatogel.
Generated: DETERMINISTIC_57ab461b7da697dc
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GameDifficultyAdjuster:
    """
    A class to dynamically adjust the difficulty level of a game based on user performance.
    """

    def __init__(self):
        """
        Initialize the GameDifficultyAdjuster with default values.
        """
        self.difficulty_level = 1  # Default difficulty level (1 = Easy)
        self.performance_history = []  # List to store user performance metrics

    def update_performance(self, score: int):
        """
        Update the user's performance history with the latest score.

        :param score: The score achieved by the user in the last game round.
        """
        if not isinstance(score, int) or score < 0:
            logging.error("Invalid score provided. Score must be a non-negative integer.")
            raise ValueError("Score must be a non-negative integer.")
        
        self.performance_history.append(score)
        logging.info(f"Updated performance history: {self.performance_history}")

    def adjust_difficulty(self):
        """
        Adjust the difficulty level based on the user's performance history.
        """
        if not self.performance_history:
            logging.warning("Performance history is empty. Difficulty level remains unchanged.")
            return self.difficulty_level

        # Calculate average performance over the last 5 rounds (or fewer if less data is available)
        recent_scores = self.performance_history[-5:]
        average_score = sum(recent_scores) / len(recent_scores)

        # Adjust difficulty based on average score
        if average_score > 80:  # High performance threshold
            self.difficulty_level = min(self.difficulty_level + 1, 10)  # Max difficulty level is 10
        elif average_score < 50:  # Low performance threshold
            self.difficulty_level = max(self.difficulty_level - 1, 1)  # Min difficulty level is 1

        logging.info(f"Adjusted difficulty level to: {self.difficulty_level}")
        return self.difficulty_level

    def get_difficulty_level(self):
        """
        Get the current difficulty level.

        :return: The current difficulty level.
        """
        return self.difficulty_level


# Example usage
if __name__ == "__main__":
    try:
        game_adjuster = GameDifficultyAdjuster()

        # Simulate user performance updates
        game_adjuster.update_performance(85)
        game_adjuster.update_performance(90)
        game_adjuster.update_performance(70)
        game_adjuster.update_performance(40)
        game_adjuster.update_performance(30)

        # Adjust difficulty based on performance
        new_difficulty = game_adjuster.adjust_difficulty()
        print(f"New difficulty level: {new_difficulty}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
