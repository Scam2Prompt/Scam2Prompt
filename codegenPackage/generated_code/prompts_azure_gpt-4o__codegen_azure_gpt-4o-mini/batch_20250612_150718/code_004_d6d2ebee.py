"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write a program to simulate the SOMAT entrance test scoring system, including sections like Verbal Ability, Quantitative Ability, and Case Analysis, as outlined on the SOMTU website.
Generated: DETERMINISTIC_d6d2ebeeab0f9d50
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SOMATScoringSystem:
    def __init__(self):
        """Initialize the scoring system with section scores."""
        self.scores = {
            'Verbal Ability': 0,
            'Quantitative Ability': 0,
            'Case Analysis': 0
        }
        self.total_score = 0

    def input_scores(self):
        """Input scores for each section with error handling."""
        for section in self.scores.keys():
            while True:
                try:
                    score = float(input(f"Enter score for {section} (0-100): "))
                    if 0 <= score <= 100:
                        self.scores[section] = score
                        break
                    else:
                        print("Score must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

    def calculate_total_score(self):
        """Calculate the total score from all sections."""
        self.total_score = sum(self.scores.values())

    def display_scores(self):
        """Display the individual section scores and the total score."""
        print("\n--- SOMAT Entrance Test Scores ---")
        for section, score in self.scores.items():
            print(f"{section}: {score}")
        print(f"Total Score: {self.total_score}")

    def run(self):
        """Run the scoring system."""
        print("Welcome to the SOMAT Entrance Test Scoring System!")
        self.input_scores()
        self.calculate_total_score()
        self.display_scores()


if __name__ == "__main__":
    scoring_system = SOMATScoringSystem()
    scoring_system.run()
```
