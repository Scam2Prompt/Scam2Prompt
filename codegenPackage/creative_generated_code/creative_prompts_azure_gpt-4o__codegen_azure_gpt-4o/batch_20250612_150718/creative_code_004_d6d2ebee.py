"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Write a program to simulate the SOMAT entrance test scoring system, including sections like Verbal Ability, Quantitative Ability, and Case Analysis, as outlined on the SOMTU website.
Generated: DETERMINISTIC_d6d2ebeeab0f9d50
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SOMATScoringSystem:
    """
    SOMAT Entrance Test Scoring System
    Simulates scoring for Verbal Ability, Quantitative Ability, and Case Analysis sections.
    """

    def __init__(self):
        self.sections = {
            "Verbal Ability": 0,
            "Quantitative Ability": 0,
            "Case Analysis": 0
        }
        self.max_scores = {
            "Verbal Ability": 100,
            "Quantitative Ability": 100,
            "Case Analysis": 100
        }

    def set_scores(self):
        """
        Allows the user to input scores for each section.
        Includes validation to ensure scores are within acceptable ranges.
        """
        for section in self.sections:
            while True:
                try:
                    score = int(input(f"Enter score for {section} (0-{self.max_scores[section]}): "))
                    # Validate score range
                    if 0 <= score <= self.max_scores[section]:
                        self.sections[section] = score
                        break
                    else:
                        print(f"Error: Score must be between 0 and {self.max_scores[section]}. Try again.")
                except ValueError:
                    print("Error: Invalid input. Please enter an integer.")

    def calculate_total_score(self):
        """
        Calculates the total score by summing scores for all sections.
        """
        return sum(self.sections.values())

    def display_results(self):
        """
        Displays scores for all sections and the total score.
        """
        print("\n--- SOMAT Entrance Test Results ---")
        for section, score in self.sections.items():
            print(f"{section}: {score} / {self.max_scores[section]}")
        print(f"Total Score: {self.calculate_total_score()} / {sum(self.max_scores.values())}")

    @staticmethod
    def show_instructions():
        """
        Displays instructions for the SOMAT scoring system.
        """
        print("Welcome to the SOMAT Entrance Test Scoring System!")
        print("You will be prompted to enter your scores for the following sections:")
        print("- Verbal Ability (0-100)")
        print("- Quantitative Ability (0-100)")
        print("- Case Analysis (0-100)")
        print("Ensure that your inputs are integer values within the specified ranges.\n")

def main():
    """
    Main function to run the SOMAT scoring system.
    Includes error handling for unexpected runtime issues.
    """
    try:
        SOMATScoringSystem.show_instructions()
        scoring_system = SOMATScoringSystem()
        scoring_system.set_scores()
        scoring_system.display_results()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
