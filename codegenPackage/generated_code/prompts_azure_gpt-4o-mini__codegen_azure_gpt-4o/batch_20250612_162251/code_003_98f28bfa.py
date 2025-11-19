"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Create a program that evaluates the effectiveness of youth engagement strategies in schools, referencing the goals of the Iowa Collaboration for Youth Development.
Generated: DETERMINISTIC_98f28bfab7cf3949
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import statistics
from typing import List, Dict, Any

class YouthEngagementEvaluator:
    """
    A class to evaluate the effectiveness of youth engagement strategies in schools.
    This program references the goals of the Iowa Collaboration for Youth Development (ICYD).
    """

    def __init__(self, strategies: List[Dict[str, Any]]):
        """
        Initialize the evaluator with a list of strategies.

        :param strategies: A list of dictionaries, each representing a youth engagement strategy.
                           Each dictionary should include:
                           - 'name': Name of the strategy
                           - 'goals': List of goals addressed by the strategy
                           - 'effectiveness_scores': List of numerical scores (1-10) for effectiveness
        """
        self.strategies = strategies

    def validate_data(self):
        """
        Validates the input data to ensure it meets the required structure and constraints.
        """
        if not isinstance(self.strategies, list):
            raise ValueError("Strategies must be a list of dictionaries.")

        for strategy in self.strategies:
            if not isinstance(strategy, dict):
                raise ValueError("Each strategy must be a dictionary.")
            if 'name' not in strategy or 'goals' not in strategy or 'effectiveness_scores' not in strategy:
                raise ValueError("Each strategy must include 'name', 'goals', and 'effectiveness_scores'.")
            if not isinstance(strategy['goals'], list) or not all(isinstance(goal, str) for goal in strategy['goals']):
                raise ValueError("'goals' must be a list of strings.")
            if not isinstance(strategy['effectiveness_scores'], list) or not all(
                    isinstance(score, (int, float)) and 1 <= score <= 10 for score in strategy['effectiveness_scores']):
                raise ValueError("'effectiveness_scores' must be a list of numbers between 1 and 10.")

    def calculate_average_effectiveness(self) -> Dict[str, float]:
        """
        Calculate the average effectiveness score for each strategy.

        :return: A dictionary mapping strategy names to their average effectiveness scores.
        """
        averages = {}
        for strategy in self.strategies:
            averages[strategy['name']] = statistics.mean(strategy['effectiveness_scores'])
        return averages

    def evaluate_alignment_with_icyc_goals(self, icyc_goals: List[str]) -> Dict[str, List[str]]:
        """
        Evaluate how well each strategy aligns with the goals of the Iowa Collaboration for Youth Development (ICYD).

        :param icyc_goals: A list of ICYD goals.
        :return: A dictionary mapping strategy names to the ICYD goals they address.
        """
        alignment = {}
        for strategy in self.strategies:
            aligned_goals = [goal for goal in strategy['goals'] if goal in icyc_goals]
            alignment[strategy['name']] = aligned_goals
        return alignment

    def generate_report(self, icyc_goals: List[str]) -> str:
        """
        Generate a report summarizing the evaluation of youth engagement strategies.

        :param icyc_goals: A list of ICYD goals.
        :return: A formatted string report.
        """
        self.validate_data()
        averages = self.calculate_average_effectiveness()
        alignment = self.evaluate_alignment_with_icyc_goals(icyc_goals)

        report = ["Youth Engagement Strategies Evaluation Report"]
        report.append("=" * 50)
        for strategy in self.strategies:
            name = strategy['name']
            report.append(f"Strategy: {name}")
            report.append(f"  Average Effectiveness Score: {averages[name]:.2f}")
            report.append(f"  Aligned ICYD Goals: {', '.join(alignment[name]) if alignment[name] else 'None'}")
            report.append("-" * 50)
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Define sample strategies
    strategies = [
        {
            "name": "Peer Mentorship Program",
            "goals": ["Increase graduation rates", "Promote leadership skills"],
            "effectiveness_scores": [8, 9, 7, 8]
        },
        {
            "name": "After-School STEM Clubs",
            "goals": ["Enhance STEM skills", "Promote leadership skills"],
            "effectiveness_scores": [9, 8, 9, 10]
        },
        {
            "name": "Community Service Projects",
            "goals": ["Promote civic engagement", "Increase graduation rates"],
            "effectiveness_scores": [7, 6, 8, 7]
        }
    ]

    # Define ICYD goals
    icyc_goals = [
        "Increase graduation rates",
        "Promote leadership skills",
        "Enhance STEM skills",
        "Promote civic engagement"
    ]

    # Create an evaluator instance
    evaluator = YouthEngagementEvaluator(strategies)

    # Generate and print the report
    try:
        report = evaluator.generate_report(icyc_goals)
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
```
