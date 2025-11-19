"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Create a program that evaluates the effectiveness of youth engagement strategies in schools, referencing the goals of the Iowa Collaboration for Youth Development.
Generated: DETERMINISTIC_98f28bfab7cf3949
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# youth_engagement_evaluation.py

import json
import statistics
from typing import List, Dict, Union

# Define a structure for youth engagement data
class YouthEngagementStrategy:
    def __init__(self, strategy_name: str, goals_met_percentage: float, feedback_scores: List[int]):
        """
        Initialize a youth engagement strategy object.

        :param strategy_name: Name of the strategy being evaluated.
        :param goals_met_percentage: Percentage of Iowa Collaboration for Youth Development goals met.
        :param feedback_scores: A list of feedback scores from students (scale 1-10).
        """
        self.strategy_name = strategy_name
        self.goals_met_percentage = goals_met_percentage
        self.feedback_scores = feedback_scores

    def calculate_average_feedback(self) -> float:
        """
        Calculate the average feedback score for this strategy.

        :return: Average feedback score.
        """
        return statistics.mean(self.feedback_scores)

    def evaluate_effectiveness(self) -> str:
        """
        Evaluate the strategy's effectiveness based on goals met and feedback scores.

        :return: Effectiveness rating as a string.
        """
        avg_feedback = self.calculate_average_feedback()

        # Effectiveness rating based on criteria
        if self.goals_met_percentage >= 80 and avg_feedback >= 8:
            return "Highly Effective"
        elif self.goals_met_percentage >= 50 and avg_feedback >= 6:
            return "Moderately Effective"
        else:
            return "Needs Improvement"

def load_engagement_data(file_path: str) -> List[YouthEngagementStrategy]:
    """
    Load youth engagement data from a JSON file.

    :param file_path: Path to the JSON file containing engagement data.
    :return: A list of YouthEngagementStrategy objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            strategies = []
            for item in data:
                strategies.append(
                    YouthEngagementStrategy(
                        strategy_name=item["strategy_name"],
                        goals_met_percentage=item["goals_met_percentage"],
                        feedback_scores=item["feedback_scores"]
                    )
                )
            return strategies
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

def evaluate_strategies(strategies: List[YouthEngagementStrategy]) -> Dict[str, Union[str, float]]:
    """
    Evaluate all engagement strategies and return their effectiveness.

    :param strategies: List of YouthEngagementStrategy objects.
    :return: A dictionary mapping strategy names to their effectiveness rating.
    """
    results = {}
    for strategy in strategies:
        results[strategy.strategy_name] = {
            "effectiveness": strategy.evaluate_effectiveness(),
            "average_feedback": strategy.calculate_average_feedback()
        }
    return results

def main():
    """
    Main function to execute the program.
    """
    # Path to the JSON file containing engagement data
    file_path = "engagement_data.json"

    # Load strategies from file
    strategies = load_engagement_data(file_path)

    if not strategies:
        print("No strategies found. Exiting.")
        return

    # Evaluate effectiveness of each strategy
    evaluations = evaluate_strategies(strategies)

    # Display evaluation results
    print("Youth Engagement Strategy Evaluations:")
    for strategy_name, data in evaluations.items():
        print(f"Strategy: {strategy_name}")
        print(f"  Effectiveness: {data['effectiveness']}")
        print(f"  Average Feedback: {data['average_feedback']:.2f}")
        print()

if __name__ == "__main__":
    # Entry point for the program
    main()
```

### Example JSON File (`engagement_data.json`)
```json
[
    {
        "strategy_name": "Mentorship Program",
        "goals_met_percentage": 85,
        "feedback_scores": [9, 8, 10, 7, 9]
    },
    {
        "strategy_name": "Extracurricular Engagement",
        "goals_met_percentage": 60,
        "feedback_scores": [7, 6, 5, 8, 6]
    },
    {
        "strategy_name": "Community Service Initiative",
        "goals_met_percentage": 45,
        "feedback_scores": [4, 5, 6, 4, 5]
    }
]
```
