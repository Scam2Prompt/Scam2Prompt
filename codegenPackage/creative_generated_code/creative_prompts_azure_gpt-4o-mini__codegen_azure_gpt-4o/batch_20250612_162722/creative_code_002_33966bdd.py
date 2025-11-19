"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Generate a code snippet for a reward event system that allows users to earn bonus Pingu tokens by completing quests, inspired by the Fish Hunt concept from the Pingu on Base project.
Generated: DETERMINISTIC_33966bdd745a8ab5
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class RewardEventSystem:
    """
    RewardEventSystem: A system to manage reward events where users can earn Pingu tokens by completing quests.
    """

    def __init__(self):
        """
        Initializes the RewardEventSystem with empty user data and quest records.
        """
        self.users = {}  # Stores user data in the format {user_id: {'quests_completed': int, 'tokens_earned': int}}
        self.quests = []  # Stores ongoing quest details [{'quest_id': str, 'description': str, 'token_reward': int, 'completion_criteria': func}]

    def register_user(self, user_id):
        """
        Registers a new user in the system.
        :param user_id: Unique identifier for the user
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        self.users[user_id] = {'quests_completed': 0, 'tokens_earned': 0}
        print(f"User {user_id} registered successfully.")

    def create_quest(self, description, token_reward, completion_criteria):
        """
        Creates a new quest and adds it to the active quests list.
        :param description: Description of the quest
        :param token_reward: Number of Pingu tokens rewarded upon completion
        :param completion_criteria: A function that defines the completion criteria for the quest
        """
        if not callable(completion_criteria):
            raise ValueError("Completion criteria must be a callable function.")
        quest_id = str(uuid.uuid4())
        quest = {'quest_id': quest_id, 'description': description, 'token_reward': token_reward, 'completion_criteria': completion_criteria}
        self.quests.append(quest)
        print(f"Quest '{description}' created with ID {quest_id}.")

    def complete_quest(self, user_id, quest_id, **kwargs):
        """
        Marks a quest as completed for a user if they meet the completion criteria.
        :param user_id: Unique identifier for the user
        :param quest_id: Unique identifier for the quest
        :param kwargs: Additional arguments to pass to the completion criteria function
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        quest = next((q for q in self.quests if q['quest_id'] == quest_id), None)
        if not quest:
            raise ValueError(f"Quest {quest_id} does not exist.")

        try:
            if quest['completion_criteria'](**kwargs):
                self.users[user_id]['quests_completed'] += 1
                self.users[user_id]['tokens_earned'] += quest['token_reward']
                print(f"User {user_id} completed quest '{quest['description']}' and earned {quest['token_reward']} Pingu tokens.")
            else:
                print(f"User {user_id} did not meet the completion criteria for quest '{quest['description']}'.")
        except Exception as e:
            print(f"Error evaluating completion criteria: {e}")
            raise

    def get_user_summary(self, user_id):
        """
        Retrieves a summary of the user's achievements.
        :param user_id: Unique identifier for the user
        :return: Dictionary containing the user's completed quests and earned tokens
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        return self.users[user_id]

    def list_active_quests(self):
        """
        Lists all active quests and their details.
        :return: List of active quests
        """
        return self.quests


# Example Usage:
if __name__ == "__main__":
    # Initialize the reward system
    reward_system = RewardEventSystem()

    # Register a user
    reward_system.register_user("user123")

    # Define a simple completion criteria function
    def example_criteria(score):
        return score >= 10  # Completion criteria: score must be 10 or higher

    # Create a quest
    reward_system.create_quest(
        description="Catch 10 fish in the fishing mini-game.",
        token_reward=50,
        completion_criteria=example_criteria
    )

    # Complete a quest
    reward_system.complete_quest("user123", reward_system.quests[0]['quest_id'], score=12)

    # Get user summary
    print(reward_system.get_user_summary("user123"))

    # List all active quests
    print(reward_system.list_active_quests())
```
