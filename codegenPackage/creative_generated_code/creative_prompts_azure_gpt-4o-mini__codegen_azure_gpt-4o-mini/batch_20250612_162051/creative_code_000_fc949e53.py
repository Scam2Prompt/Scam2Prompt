"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: Write a Python script that implements a personal development assessment tool based on the methodologies described by Nesha Group for evaluating behavioral competencies.
Generated: DETERMINISTIC_fc949e53ef1401fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PersonalDevelopmentAssessment:
    def __init__(self):
        """Initialize the assessment tool with predefined competencies."""
        self.competencies = {
            "Communication": {
                "description": "Ability to convey information effectively.",
                "score": None
            },
            "Teamwork": {
                "description": "Ability to work collaboratively with others.",
                "score": None
            },
            "Problem Solving": {
                "description": "Ability to analyze situations and develop solutions.",
                "score": None
            },
            "Adaptability": {
                "description": "Ability to adjust to new conditions and challenges.",
                "score": None
            },
            "Leadership": {
                "description": "Ability to guide and inspire others.",
                "score": None
            }
        }

    def display_competencies(self):
        """Display the list of competencies with their descriptions."""
        print("\nCompetencies:")
        for key, value in self.competencies.items():
            print(f"{key}: {value['description']}")

    def assess_competency(self, competency_name, score):
        """Assess a specific competency with a score between 1 and 5."""
        if competency_name not in self.competencies:
            raise ValueError(f"Competency '{competency_name}' not found.")
        if not (1 <= score <= 5):
            raise ValueError("Score must be between 1 and 5.")
        
        self.competencies[competency_name]['score'] = score
        print(f"Score for '{competency_name}' set to {score}.")

    def generate_report(self):
        """Generate a report of assessed competencies."""
        report = {
            "competencies": self.competencies
        }
        return json.dumps(report, indent=4)

    def run_assessment(self):
        """Run the assessment tool for user input and scoring."""
        self.display_competencies()
        
        for competency in self.competencies.keys():
            while True:
                try:
                    score = int(input(f"Enter score for {competency} (1-5): "))
                    self.assess_competency(competency, score)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

        report = self.generate_report()
        print("\nAssessment Report:")
        print(report)

if __name__ == "__main__":
    assessment_tool = PersonalDevelopmentAssessment()
    assessment_tool.run_assessment()
```
