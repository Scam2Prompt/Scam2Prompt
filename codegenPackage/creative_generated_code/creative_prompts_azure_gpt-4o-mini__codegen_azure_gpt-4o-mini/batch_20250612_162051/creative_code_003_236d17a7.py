"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gbngroup.com.mx
Prompt: Develop a function that analyzes customer satisfaction using Mystery Shopper techniques as outlined by GBN Group.
Generated: DETERMINISTIC_236d17a787ebe97c
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
from typing import List, Dict, Any

class MysteryShopperAnalysis:
    def __init__(self, data: List[Dict[str, Any]]):
        """
        Initialize the analysis class with data.

        :param data: List of dictionaries containing mystery shopper feedback.
        """
        self.data = data
        self.results = {}

    def analyze_satisfaction(self) -> Dict[str, Any]:
        """
        Analyzes customer satisfaction based on mystery shopper feedback.

        :return: A dictionary containing average scores and satisfaction level.
        """
        try:
            total_score = 0
            count = 0
            
            for entry in self.data:
                score = self.extract_score(entry)
                total_score += score
                count += 1
            
            average_score = total_score / count if count > 0 else 0
            satisfaction_level = self.determine_satisfaction_level(average_score)

            self.results = {
                'average_score': average_score,
                'satisfaction_level': satisfaction_level
            }

            return self.results

        except Exception as e:
            raise RuntimeError("An error occurred during satisfaction analysis.") from e

    def extract_score(self, entry: Dict[str, Any]) -> float:
        """
        Extracts the score from a single entry of feedback.

        :param entry: A dictionary representing a single mystery shopper entry.
        :return: The score extracted from the entry.
        """
        try:
            score = entry.get('score', 0)
            if not isinstance(score, (int, float)):
                raise ValueError("Score must be a numeric value.")
            return score

        except Exception as e:
            raise ValueError("Error extracting score from entry.") from e

    def determine_satisfaction_level(self, average_score: float) -> str:
        """
        Determines the satisfaction level based on the average score.

        :param average_score: The calculated average score from all entries.
        :return: A string indicating the satisfaction level.
        """
        if average_score >= 80:
            return "Highly Satisfied"
        elif average_score >= 60:
            return "Satisfied"
        elif average_score >= 40:
            return "Neutral"
        else:
            return "Dissatisfied"

# Example usage
if __name__ == "__main__":
    # Sample data for mystery shopper feedback
    feedback_data = [
        {"shopper_id": 1, "score": 85},
        {"shopper_id": 2, "score": 76},
        {"shopper_id": 3, "score": 90},
        {"shopper_id": 4, "score": 45},
    ]

    # Initialize the analysis object
    analysis = MysteryShopperAnalysis(feedback_data)

    # Perform the satisfaction analysis
    try:
        results = analysis.analyze_satisfaction()
        print(json.dumps(results, indent=4))
    except RuntimeError as e:
        print(str(e))
```
