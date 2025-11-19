"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Write a Python script to help evaluate the technical fluency of founders of crypto projects, considering factors such as design and functionality.
Generated: DETERMINISTIC_bee5d42624637373
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FounderEvaluator:
    """
    A class to evaluate the technical fluency of founders of crypto projects.
    """

    def __init__(self):
        """
        Initializes the evaluator with predefined criteria.
        """
        self.criteria = {
            "design": {
                "description": "Ability to design scalable and secure systems.",
                "weight": 0.4  # 40% weight
            },
            "functionality": {
                "description": "Ability to implement functional and efficient code.",
                "weight": 0.4  # 40% weight
            },
            "innovation": {
                "description": "Ability to propose innovative solutions.",
                "weight": 0.2  # 20% weight
            }
        }

    def evaluate_founder(self, scores: Dict[str, float]) -> float:
        """
        Evaluates a founder based on their scores in different criteria.

        Args:
            scores (Dict[str, float]): A dictionary containing scores for each criterion.

        Returns:
            float: The final evaluation score (0 to 100).
        """
        try:
            # Validate input scores
            for criterion in self.criteria:
                if criterion not in scores:
                    raise ValueError(f"Missing score for criterion: {criterion}")
                if not (0 <= scores[criterion] <= 100):
                    raise ValueError(f"Score for {criterion} must be between 0 and 100.")

            # Calculate weighted score
            final_score = 0.0
            for criterion, details in self.criteria.items():
                final_score += scores[criterion] * details["weight"]

            return final_score

        except Exception as e:
            logging.error(f"Error during evaluation: {e}")
            raise

    def evaluate_multiple_founders(self, founders_scores: List[Dict[str, float]]) -> List[float]:
        """
        Evaluates multiple founders based on their scores.

        Args:
            founders_scores (List[Dict[str, float]]): A list of dictionaries containing scores for each founder.

        Returns:
            List[float]: A list of final evaluation scores for each founder.
        """
        try:
            results = []
            for scores in founders_scores:
                results.append(self.evaluate_founder(scores))
            return results

        except Exception as e:
            logging.error(f"Error during multiple evaluations: {e}")
            raise


def main():
    """
    Main function to demonstrate the evaluation process.
    """
    evaluator = FounderEvaluator()

    # Example input: scores for founders
    founders_scores = [
        {"design": 85, "functionality": 90, "innovation": 75},
        {"design": 70, "functionality": 80, "innovation": 60},
        {"design": 95, "functionality": 85, "innovation": 90}
    ]

    try:
        # Evaluate multiple founders
        results = evaluator.evaluate_multiple_founders(founders_scores)

        # Output results
        for i, score in enumerate(results):
            logging.info(f"Founder {i + 1} Final Score: {score:.2f}")

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
