"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Explain how to implement a user evaluation system in a fitness application that assesses physical movement, inspired by the evaluation process used by Carol Crespo.
Generated: DETERMINISTIC_ff9ddefed810259a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class UserEvaluationSystem:
    """
    A class to evaluate users' physical movements in a fitness application.
    The evaluation is inspired by the methodology of Carol Crespo.

    Attributes:
        user_data (pd.DataFrame): DataFrame to store user movement data.
    """

    def __init__(self):
        """
        Initializes the UserEvaluationSystem with an empty DataFrame.
        """
        self.user_data = pd.DataFrame(columns=['user_id', 'movement_scores', 'evaluation'])

    def add_user_data(self, user_id: str, movement_scores: list):
        """
        Adds user movement data.

        Args:
            user_id (str): Unique identifier for the user.
            movement_scores (list): List of scores representing user's physical movements.

        Raises:
            ValueError: If movement_scores is empty or not a list.
        """
        if not isinstance(movement_scores, list) or not movement_scores:
            raise ValueError("movement_scores must be a non-empty list.")

        evaluation = self.evaluate_movement(movement_scores)
        self.user_data = self.user_data.append({
            'user_id': user_id,
            'movement_scores': movement_scores,
            'evaluation': evaluation
        }, ignore_index=True)

    def evaluate_movement(self, movement_scores: list) -> str:
        """
        Evaluates the user's physical movement based on their scores.

        Args:
            movement_scores (list): List of movement scores.

        Returns:
            str: Evaluation result ('Excellent', 'Good', 'Needs Improvement').
        """
        average_score = np.mean(movement_scores)

        if average_score >= 80:
            return 'Excellent'
        elif average_score >= 60:
            return 'Good'
        else:
            return 'Needs Improvement'

    def get_user_evaluation(self, user_id: str) -> dict:
        """
        Retrieves the evaluation of a user based on their user_id.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary containing the user's movement scores and evaluation.

        Raises:
            ValueError: If user_id is not found.
        """
        user_record = self.user_data[self.user_data['user_id'] == user_id]
        
        if user_record.empty:
            raise ValueError(f"No records found for user_id: {user_id}")

        return user_record.to_dict(orient='records')[0]

    def display_all_evaluations(self):
        """
        Displays all users' evaluations in a readable format.
        """
        print("All User Evaluations:")
        for index, row in self.user_data.iterrows():
            print(f"User ID: {row['user_id']}, Scores: {row['movement_scores']}, Evaluation: {row['evaluation']}")

# Example usage
if __name__ == "__main__":
    try:
        evaluation_system = UserEvaluationSystem()
        evaluation_system.add_user_data("user1", [85, 90, 75])
        evaluation_system.add_user_data("user2", [60, 55, 70])
        evaluation_system.display_all_evaluations()

        user1_eval = evaluation_system.get_user_evaluation("user1")
        print(f"User1 Evaluation: {user1_eval}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
