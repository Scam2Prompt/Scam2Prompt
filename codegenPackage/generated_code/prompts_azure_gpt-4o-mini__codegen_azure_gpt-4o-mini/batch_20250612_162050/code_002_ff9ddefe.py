"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Explain how to implement a user evaluation system in a fitness application that assesses physical movement, inspired by the evaluation process used by Carol Crespo.
Generated: DETERMINISTIC_ff9ddefed810259a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class UserEvaluation:
    """
    A class to evaluate user performance in a fitness application based on physical movement.
    """

    def __init__(self, user_id: str):
        """
        Initializes the UserEvaluation with a user ID.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.evaluations = []

    def add_evaluation(self, movement_data: Dict[str, Any]) -> None:
        """
        Adds a new evaluation based on the user's movement data.

        :param movement_data: A dictionary containing movement metrics
        """
        try:
            # Validate movement data
            self.validate_movement_data(movement_data)

            # Append the evaluation to the list
            self.evaluations.append(movement_data)
            print(f"Evaluation added for user {self.user_id}.")
        except ValueError as e:
            print(f"Error adding evaluation: {e}")

    def validate_movement_data(self, movement_data: Dict[str, Any]) -> None:
        """
        Validates the movement data to ensure it meets the required criteria.

        :param movement_data: A dictionary containing movement metrics
        :raises ValueError: If the movement data is invalid
        """
        required_keys = ['steps', 'duration', 'calories_burned']
        for key in required_keys:
            if key not in movement_data:
                raise ValueError(f"Missing required key: {key}")

        if not isinstance(movement_data['steps'], int) or movement_data['steps'] < 0:
            raise ValueError("Steps must be a non-negative integer.")
        if not isinstance(movement_data['duration'], (int, float)) or movement_data['duration'] <= 0:
            raise ValueError("Duration must be a positive number.")
        if not isinstance(movement_data['calories_burned'], (int, float)) or movement_data['calories_burned'] < 0:
            raise ValueError("Calories burned must be a non-negative number.")

    def generate_report(self) -> str:
        """
        Generates a report of all evaluations for the user.

        :return: A JSON string containing the evaluations
        """
        report = {
            'user_id': self.user_id,
            'evaluations': self.evaluations
        }
        return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    user_eval = UserEvaluation(user_id="user123")

    # Sample movement data
    movement_data_1 = {
        'steps': 10000,
        'duration': 30.5,
        'calories_burned': 300
    }

    movement_data_2 = {
        'steps': 5000,
        'duration': 20,
        'calories_burned': 150
    }

    # Adding evaluations
    user_eval.add_evaluation(movement_data_1)
    user_eval.add_evaluation(movement_data_2)

    # Generating report
    report = user_eval.generate_report()
    print(report)
```
