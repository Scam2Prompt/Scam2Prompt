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
class SomatScoringSystem:
    """
    A class to simulate the SOMAT entrance test scoring system, which includes
    sections for Verbal Ability, Quantitative Ability, and Case Analysis.
    """

    def __init__(self):
        self.scores = {
            "Verbal Ability": 0,
            "Quantitative Ability": 0,
            "Case Analysis": 0
        }
        self.max_scores = {
            "Verbal Ability": 100,
            "Quantitative Ability": 100,
            "Case Analysis": 100
        }
    
    def input_score(self, section, score):
        """
        Input the score for a specific section.

        :param section: The section of the test (e.g., 'Verbal Ability').
        :param score: The score to input.
        :raises ValueError: If the section is invalid or the score is out of range.
        """
        if section not in self.scores:
            raise ValueError(f"Invalid section: {section}. Valid sections are: {list(self.scores.keys())}")

        if not (0 <= score <= self.max_scores[section]):
            raise ValueError(f"Score must be between 0 and {self.max_scores[section]} for {section}.")

        self.scores[section] = score

    def calculate_total_score(self):
        """
        Calculate the total score across all sections.

        :return: The total score.
        """
        return sum(self.scores.values())

    def calculate_percentage(self):
        """
        Calculate the percentage score across all sections.

        :return: The percentage score of the total.
        """
        total_max_score = sum(self.max_scores.values())
        total_score = self.calculate_total_score()
        percentage = (total_score / total_max_score) * 100
        return percentage
    
    def display_scores(self):
        """
        Display the scores for all sections and the total score.
        """
        print("SOMAT Entrance Test Scores:")
        for section, score in self.scores.items():
            print(f"{section}: {score}/{self.max_scores[section]}")
        print(f"Total Score: {self.calculate_total_score()}/{sum(self.max_scores.values())}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")

def main():
    """
    Main function to run the SOMAT scoring system simulation.
    """
    scoring_system = SomatScoringSystem()

    try:
        # Input scores for each section
        scoring_system.input_score("Verbal Ability", 85)
        scoring_system.input_score("Quantitative Ability", 90)
        scoring_system.input_score("Case Analysis", 75)

        # Display the scores
        scoring_system.display_scores()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
