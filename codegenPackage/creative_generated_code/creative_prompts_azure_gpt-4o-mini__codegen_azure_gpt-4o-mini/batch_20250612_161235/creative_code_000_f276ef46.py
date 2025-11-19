"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Generate a Python script that simulates the grading system for the Fiji Mathematics Competition (FMC), categorizing scores into Prize, Distinction, Credit, Pass, and Participation.
Generated: DETERMINISTIC_f276ef46bf222f1a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GradingSystem:
    """
    A class to simulate the grading system for the Fiji Mathematics Competition (FMC).
    This class categorizes scores into Prize, Distinction, Credit, Pass, and Participation.
    """

    # Define the score thresholds for each category
    CATEGORY_THRESHOLDS = {
        'Prize': 90,
        'Distinction': 80,
        'Credit': 70,
        'Pass': 50,
        'Participation': 0
    }

    def __init__(self, score):
        """
        Initializes the GradingSystem with a given score.

        :param score: The score of the participant (int).
        """
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a non-negative integer.")
        self.score = score

    def get_grade(self):
        """
        Determines the grade category based on the score.

        :return: A string representing the grade category.
        """
        for category, threshold in self.CATEGORY_THRESHOLDS.items():
            if self.score >= threshold:
                return category
        return 'Invalid Score'  # This should never be reached due to input validation

def main():
    """
    Main function to run the grading system.
    It prompts the user for a score and outputs the corresponding grade category.
    """
    try:
        # Ask the user for the score
        score_input = input("Enter the score (0-100): ")
        score = int(score_input)

        # Create an instance of GradingSystem
        grading_system = GradingSystem(score)

        # Get and print the grade category
        grade = grading_system.get_grade()
        print(f"The grade category for the score {score} is: {grade}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid score.")

if __name__ == "__main__":
    main()
```
