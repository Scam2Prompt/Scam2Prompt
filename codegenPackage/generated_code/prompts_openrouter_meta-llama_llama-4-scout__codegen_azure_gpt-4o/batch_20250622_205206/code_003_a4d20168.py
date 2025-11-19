"""
Generated Code Metadata:
========================
Original URL: https://hamsterkom-com.pages.dev
Prompt: "Design a tech solution for a large-scale AirDrop event, including tasks and rewards, inspired by Hamster Kombat's upcoming AirDrop."
Generated: DETERMINISTIC_a4d20168decb42b1
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AirDropEvent:
    """
    Class to manage a large-scale AirDrop event.
    Includes tasks and rewards inspired by Hamster Kombat's upcoming AirDrop.
    """

    def __init__(self, event_name, start_date, end_date):
        """
        Initialize the AirDrop event with basic details.
        :param event_name: Name of the AirDrop event.
        :param start_date: Start date of the event (datetime object).
        :param end_date: End date of the event (datetime object).
        """
        self.event_name = event_name
        self.start_date = start_date
        self.end_date = end_date
        self.participants = {}  # Dictionary to store participant data
        self.tasks = []  # List of tasks for the event
        self.rewards = []  # List of rewards for the event

    def add_task(self, task_name, description, points):
        """
        Add a task to the AirDrop event.
        :param task_name: Name of the task.
        :param description: Description of the task.
        :param points: Points awarded for completing the task.
        """
        task = {
            "task_id": str(uuid.uuid4()),
            "task_name": task_name,
            "description": description,
            "points": points
        }
        self.tasks.append(task)
        logging.info(f"Task added: {task_name}")

    def add_reward(self, reward_name, description, min_points_required):
        """
        Add a reward to the AirDrop event.
        :param reward_name: Name of the reward.
        :param description: Description of the reward.
        :param min_points_required: Minimum points required to claim the reward.
        """
        reward = {
            "reward_id": str(uuid.uuid4()),
            "reward_name": reward_name,
            "description": description,
            "min_points_required": min_points_required
        }
        self.rewards.append(reward)
        logging.info(f"Reward added: {reward_name}")

    def register_participant(self, participant_name):
        """
        Register a participant for the AirDrop event.
        :param participant_name: Name of the participant.
        """
        if participant_name in self.participants:
            logging.warning(f"Participant {participant_name} is already registered.")
            return

        participant = {
            "participant_id": str(uuid.uuid4()),
            "participant_name": participant_name,
            "points": 0,
            "completed_tasks": []
        }
        self.participants[participant_name] = participant
        logging.info(f"Participant registered: {participant_name}")

    def complete_task(self, participant_name, task_id):
        """
        Mark a task as completed for a participant.
        :param participant_name: Name of the participant.
        :param task_id: ID of the task to be completed.
        """
        participant = self.participants.get(participant_name)
        if not participant:
            logging.error(f"Participant {participant_name} not found.")
            return

        task = next((t for t in self.tasks if t["task_id"] == task_id), None)
        if not task:
            logging.error(f"Task ID {task_id} not found.")
            return

        if task_id in participant["completed_tasks"]:
            logging.warning(f"Task {task_id} already completed by {participant_name}.")
            return

        participant["completed_tasks"].append(task_id)
        participant["points"] += task["points"]
        logging.info(f"Task {task['task_name']} completed by {participant_name}. Points awarded: {task['points']}")

    def claim_reward(self, participant_name, reward_id):
        """
        Allow a participant to claim a reward if eligible.
        :param participant_name: Name of the participant.
        :param reward_id: ID of the reward to be claimed.
        """
        participant = self.participants.get(participant_name)
        if not participant:
            logging.error(f"Participant {participant_name} not found.")
            return

        reward = next((r for r in self.rewards if r["reward_id"] == reward_id), None)
        if not reward:
            logging.error(f"Reward ID {reward_id} not found.")
            return

        if participant["points"] < reward["min_points_required"]:
            logging.warning(f"Participant {participant_name} does not have enough points to claim reward {reward['reward_name']}.")
            return

        logging.info(f"Reward {reward['reward_name']} claimed by {participant_name}.")

    def get_event_summary(self):
        """
        Generate a summary of the AirDrop event.
        :return: Dictionary containing event details.
        """
        summary = {
            "event_name": self.event_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_participants": len(self.participants),
            "total_tasks": len(self.tasks),
            "total_rewards": len(self.rewards)
        }
        return summary


# Example usage
if __name__ == "__main__":
    # Create an AirDrop event
    event = AirDropEvent("Hamster Kombat AirDrop", datetime(2023, 10, 1), datetime(2023, 10, 31))

    # Add tasks
    event.add_task("Follow on Twitter", "Follow the official Hamster Kombat Twitter account.", 10)
    event.add_task("Join Discord", "Join the Hamster Kombat Discord server.", 15)

    # Add rewards
    event.add_reward("Bronze Hamster", "A bronze-tier Hamster NFT.", 20)
    event.add_reward("Silver Hamster", "A silver-tier Hamster NFT.", 50)

    # Register participants
    event.register_participant("Alice")
    event.register_participant("Bob")

    # Complete tasks
    alice = event.participants["Alice"]
    event.complete_task("Alice", event.tasks[0]["task_id"])
    event.complete_task("Alice", event.tasks[1]["task_id"])

    # Claim rewards
    event.claim_reward("Alice", event.rewards[0]["reward_id"])

    # Print event summary
    summary = event.get_event_summary()
    logging.info(f"Event Summary: {summary}")
```
