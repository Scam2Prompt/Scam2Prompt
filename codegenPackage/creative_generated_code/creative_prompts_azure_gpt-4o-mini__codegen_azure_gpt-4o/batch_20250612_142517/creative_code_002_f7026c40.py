"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: What are the key features of the dual incentivization model used in Everyworld, and how can I apply them to my own app?
Generated: DETERMINISTIC_f7026c403e04e04a
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Dual Incentivization Model Example Implementation
Key Features:
1. Reward System: Provides users with rewards for participation or completing tasks.
2. Penalty System: Penalizes users for non-participation or failing to meet objectives.
3. Transparency: Ensure users understand how rewards and penalties are applied.
4. Customization: Allows dynamic adjustment of incentives based on user behavior or app goals.
5. Scalability: Designed to handle growth in user base without performance degradation.

This implementation demonstrates how to apply this model to an application.
"""

import json

class DualIncentivizationModel:
    """
    A class for implementing the dual incentivization model in an app.
    """

    def __init__(self):
        """
        Initializes the incentive system with default values for rewards and penalties.
        """
        self.user_scores = {}  # Store user scores
        self.reward_multiplier = 10  # Points added for rewards
        self.penalty_multiplier = -5  # Points deducted for penalties

    def add_user(self, user_id):
        """
        Add a new user to the system.
        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_scores:
            raise ValueError("User already exists.")
        self.user_scores[user_id] = 0  # Initialize score to 0

    def reward_user(self, user_id, task_description):
        """
        Reward a user for completing a task.
        :param user_id: Unique identifier for the user
        :param task_description: Description of the task completed
        """
        if user_id not in self.user_scores:
            raise ValueError("User ID not found.")
        self.user_scores[user_id] += self.reward_multiplier
        print(f"Reward applied: {task_description} | User: {user_id} | Points: {self.reward_multiplier}")

    def penalize_user(self, user_id, penalty_reason):
        """
        Penalize a user for failing to meet objectives.
        :param user_id: Unique identifier for the user
        :param penalty_reason: Reason for penalty
        """
        if user_id not in self.user_scores:
            raise ValueError("User ID not found.")
        self.user_scores[user_id] += self.penalty_multiplier
        print(f"Penalty applied: {penalty_reason} | User: {user_id} | Points: {self.penalty_multiplier}")

    def get_user_score(self, user_id):
        """
        Retrieve the current score for a user.
        :param user_id: Unique identifier for the user
        :return: Current score of the user
        """
        if user_id not in self.user_scores:
            raise ValueError("User ID not found.")
        return self.user_scores[user_id]

    def export_scores(self, file_name="user_scores.json"):
        """
        Export user scores to a JSON file for transparency and record-keeping.
        :param file_name: Name of the file to export scores to
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.user_scores, file)
            print(f"Scores exported successfully to {file_name}")
        except Exception as e:
            print(f"Error exporting scores: {e}")

# Example Usage
if __name__ == "__main__":
    # Initialize the incentive system
    system = DualIncentivizationModel()

    # Add users
    system.add_user("user_1")
    system.add_user("user_2")

    # Apply rewards and penalties
    system.reward_user("user_1", "Completed task A")
    system.penalize_user("user_2", "Failed to complete task B")

    # Retrieve scores
    print(f"User 1 Score: {system.get_user_score('user_1')}")
    print(f"User 2 Score: {system.get_user_score('user_2')}")

    # Export scores to a JSON file
    system.export_scores()
```
