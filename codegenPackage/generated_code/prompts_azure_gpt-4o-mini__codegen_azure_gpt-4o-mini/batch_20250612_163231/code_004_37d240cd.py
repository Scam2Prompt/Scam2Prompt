"""
Generated Code Metadata:
========================
Original URL: https://sparkfi.net
Prompt: Describe the process of earning rewards through the Spark Social Media Army and how to participate.
Generated: DETERMINISTIC_37d240cd17b809a1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SparkSocialMediaArmy:
    """
    A class to represent the Spark Social Media Army program for earning rewards.
    """

    def __init__(self):
        """
        Initializes the Spark Social Media Army with an empty list of participants.
        """
        self.participants = []

    def join_program(self, participant_name):
        """
        Allows a user to join the Spark Social Media Army program.

        Args:
            participant_name (str): The name of the participant.

        Raises:
            ValueError: If the participant name is empty or already exists.
        """
        if not participant_name:
            raise ValueError("Participant name cannot be empty.")
        if participant_name in self.participants:
            raise ValueError("Participant already exists.")

        self.participants.append(participant_name)
        print(f"{participant_name} has joined the Spark Social Media Army!")

    def earn_rewards(self, participant_name, activity):
        """
        Records an activity performed by a participant to earn rewards.

        Args:
            participant_name (str): The name of the participant.
            activity (str): The activity performed to earn rewards.

        Raises:
            ValueError: If the participant does not exist or activity is empty.
        """
        if participant_name not in self.participants:
            raise ValueError("Participant does not exist.")
        if not activity:
            raise ValueError("Activity cannot be empty.")

        # Here we would normally record the activity and calculate rewards.
        print(f"{participant_name} has earned rewards for: {activity}")

    def get_participants(self):
        """
        Returns the list of participants in the program.

        Returns:
            list: A list of participant names.
        """
        return self.participants


# Example usage
if __name__ == "__main__":
    try:
        spark_army = SparkSocialMediaArmy()
        spark_army.join_program("Alice")
        spark_army.join_program("Bob")
        spark_army.earn_rewards("Alice", "Shared a post")
        spark_army.earn_rewards("Bob", "Commented on a post")

        print("Current participants:", spark_army.get_participants())
    except ValueError as e:
        print(f"Error: {e}")
```
