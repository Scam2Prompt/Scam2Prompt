"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminito.com
Prompt: Generate code to design a scoring system for Géminito, where players earn points for correctly identifying musical intervals, chords, and rhythmic patterns.
Generated: DETERMINISTIC_34e0ccd87139a4b6
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScoringSystem:
    """
    A class to represent a scoring system for the Géminito game.
    
    Attributes
    ----------
    score : int
        The total score of the player.
    correct_answer_points : int
        Points awarded for each correct answer.
    incorrect_answer_penalty : int
        Points deducted for each incorrect answer.
    """

    def __init__(self, correct_answer_points=10, incorrect_answer_penalty=5):
        """
        Initializes the scoring system with default point values.

        Parameters
        ----------
        correct_answer_points : int
            Points awarded for a correct answer (default is 10).
        incorrect_answer_penalty : int
            Points deducted for an incorrect answer (default is 5).
        """
        self.score = 0
        self.correct_answer_points = correct_answer_points
        self.incorrect_answer_penalty = incorrect_answer_penalty

    def add_correct_answer(self):
        """
        Adds points for a correct answer.
        """
        self.score += self.correct_answer_points
        print(f"Correct! Score increased by {self.correct_answer_points}. Total Score: {self.score}")

    def add_incorrect_answer(self):
        """
        Deducts points for an incorrect answer.
        """
        if self.score >= self.incorrect_answer_penalty:
            self.score -= self.incorrect_answer_penalty
            print(f"Incorrect! Score decreased by {self.incorrect_answer_penalty}. Total Score: {self.score}")
        else:
            print("Insufficient score to deduct points.")
            print(f"Total Score remains: {self.score}")

    def get_score(self):
        """
        Returns the current score.

        Returns
        -------
        int
            The current score of the player.
        """
        return self.score

    def reset_score(self):
        """
        Resets the score to zero.
        """
        self.score = 0
        print("Score has been reset to zero.")


def main():
    """
    Main function to demonstrate the scoring system.
    """
    scoring_system = ScoringSystem()

    # Simulating game actions
    try:
        scoring_system.add_correct_answer()  # Player answers correctly
        scoring_system.add_incorrect_answer()  # Player answers incorrectly
        scoring_system.add_incorrect_answer()  # Another incorrect answer
        scoring_system.add_correct_answer()  # Another correct answer
        print(f"Final Score: {scoring_system.get_score()}")

        # Resetting the score
        scoring_system.reset_score()
        print(f"Score after reset: {scoring_system.get_score()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
