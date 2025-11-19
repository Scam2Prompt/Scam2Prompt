"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Generate a detailed report template that mimics the 10-page evaluation report provided to participants in the Proof of Pitch competition.
Generated: DETERMINISTIC_28d5167cfabc30a0
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# evaluation_report_generator.py

from typing import Dict, List
from datetime import date

class EvaluationReport:
    def __init__(self, participant_name: str, project_name: str, evaluation_date: date):
        """
        Initialize the evaluation report with participant and project information.

        Args:
        - participant_name (str): Name of the participant.
        - project_name (str): Name of the project.
        - evaluation_date (date): Date of evaluation.
        """
        self.participant_name = participant_name
        self.project_name = project_name
        self.evaluation_date = evaluation_date
        self.criteria_scores = {}

    def add_criteria_score(self, criteria: str, score: int, max_score: int):
        """
        Add a score for a specific evaluation criteria.

        Args:
        - criteria (str): Name of the evaluation criteria.
        - score (int): Score achieved.
        - max_score (int): Maximum possible score.
        """
        self.criteria_scores[criteria] = {"score": score, "max_score": max_score}

    def calculate_total_score(self) -> float:
        """
        Calculate the total score achieved.

        Returns:
        - float: Total score achieved.
        """
        total_score = sum(score["score"] for score in self.criteria_scores.values())
        total_max_score = sum(score["max_score"] for score in self.criteria_scores.values())
        return (total_score / total_max_score) * 100 if total_max_score > 0 else 0

    def generate_report(self) -> str:
        """
        Generate the detailed evaluation report.

        Returns:
        - str: The detailed evaluation report.
        """
        report = f"# Evaluation Report for {self.participant_name} - {self.project_name}\n"
        report += f"## Evaluation Date: {self.evaluation_date}\n\n"

        report += "## Evaluation Criteria and Scores\n"
        report += "| Criteria | Score | Max Score |\n"
        report += "| --- | --- | --- |\n"
        for criteria, scores in self.criteria_scores.items():
            report += f"| {criteria} | {scores['score']} | {scores['max_score']} |\n"

        report += f"\n## Total Score: {self.calculate_total_score():.2f}%\n\n"

        report += "## Recommendations for Improvement\n"
        report += "### 1. Innovation and Originality\n"
        report += "* Provide specific feedback on innovation and originality.\n"
        report += "### 2. Technical Complexity and Feasibility\n"
        report += "* Provide specific feedback on technical complexity and feasibility.\n"
        report += "### 3. Presentation and Communication\n"
        report += "* Provide specific feedback on presentation and communication.\n"

        report += "\n## Conclusion\n"
        report += "* Provide an overall conclusion and feedback."

        return report


def main():
    try:
        participant_name = "John Doe"
        project_name = "Example Project"
        evaluation_date = date(2024, 9, 16)

        report = EvaluationReport(participant_name, project_name, evaluation_date)

        report.add_criteria_score("Innovation and Originality", 8, 10)
        report.add_criteria_score("Technical Complexity and Feasibility", 7, 10)
        report.add_criteria_score("Presentation and Communication", 9, 10)

        print(report.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
