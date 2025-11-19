"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Generate a Python script that simulates the grading system for the Fiji Mathematics Competition (FMC), categorizing scores into Prize, Distinction, Credit, Pass, and Participation.
Generated: DETERMINISTIC_f276ef46bf222f1a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fmc_grading.py

class FMCGradingSystem:
    """
    A class to represent the grading system for the Fiji Mathematics Competition (FMC).
    """

    # Define score thresholds for each category
    GRADING_CATEGORIES = {
        "Prize": 90,
        "Distinction": 80,
        "Credit": 70,
        "Pass": 50,
        "Participation": 0
    }

    def __init__(self, score):
        """
        Initializes the grading system with a given score.

        :param score: The score obtained by the participant (should be between 0 and 100).
        """
        self.score = score
        self.validate_score()

    def validate_score(self):
        """
        Validates the score to ensure it is within the acceptable range.

        :raises ValueError: If the score is not between 0 and 100.
        """
        if not (0 <= self.score <= 100):
            raise ValueError("Score must be between 0 and 100.")

    def get_grade(self):
        """
        Determines the grade category based on the score.

        :return: The grade category as a string.
        """
        for category, threshold in self.GRADING_CATEGORIES.items():
            if self.score >= threshold:
                return category
        return "Invalid Score"

def main():
    """
    Main function to run the grading system.
    """
    try:
        # Input score from the user
        score_input = input("Enter the score (0-100): ")
        score = int(score_input)

        # Create an instance of the grading system
        grading_system = FMCGradingSystem(score)

        # Get and print the grade
        grade = grading_system.get_grade()
        print(f"The grade for a score of {score} is: {grade}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
