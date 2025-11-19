"""
Generated Code Metadata:
========================
Original URL: https://retro-pgf.vercel.app
Prompt: What are the unique features of Retro PGF that enhance project management for RPGF rounds?
Generated: DETERMINISTIC_437a9c81a0845a4f
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RetroPGF:
    """
    A class to represent the Retro PGF project management tool for RPGF rounds.
    This class encapsulates the unique features that enhance project management.
    """

    def __init__(self):
        """
        Initializes the RetroPGF instance with default attributes.
        """
        self.rounds = []
        self.feedback = {}
        self.action_items = []

    def add_round(self, round_name):
        """
        Adds a new RPGF round to the project management tool.

        Parameters:
        round_name (str): The name of the RPGF round to be added.

        Raises:
        ValueError: If the round name is empty or already exists.
        """
        if not round_name:
            raise ValueError("Round name cannot be empty.")
        if round_name in self.rounds:
            raise ValueError(f"Round '{round_name}' already exists.")
        
        self.rounds.append(round_name)
        self.feedback[round_name] = []
        print(f"Round '{round_name}' added successfully.")

    def add_feedback(self, round_name, feedback_text):
        """
        Adds feedback to a specific RPGF round.

        Parameters:
        round_name (str): The name of the RPGF round.
        feedback_text (str): The feedback text to be added.

        Raises:
        ValueError: If the round name does not exist or feedback text is empty.
        """
        if round_name not in self.rounds:
            raise ValueError(f"Round '{round_name}' does not exist.")
        if not feedback_text:
            raise ValueError("Feedback text cannot be empty.")
        
        self.feedback[round_name].append(feedback_text)
        print(f"Feedback added to round '{round_name}'.")

    def add_action_item(self, item):
        """
        Adds an action item to the project management tool.

        Parameters:
        item (str): The action item to be added.

        Raises:
        ValueError: If the action item is empty.
        """
        if not item:
            raise ValueError("Action item cannot be empty.")
        
        self.action_items.append(item)
        print(f"Action item '{item}' added successfully.")

    def get_summary(self):
        """
        Returns a summary of all RPGF rounds, feedback, and action items.

        Returns:
        dict: A summary containing rounds, feedback, and action items.
        """
        return {
            "rounds": self.rounds,
            "feedback": self.feedback,
            "action_items": self.action_items
        }

    def display_summary(self):
        """
        Displays a summary of all RPGF rounds, feedback, and action items in a readable format.
        """
        summary = self.get_summary()
        print("RPGF Project Management Summary:")
        print("Rounds:")
        for round_name in summary["rounds"]:
            print(f" - {round_name}: {summary['feedback'][round_name]}")
        print("Action Items:")
        for item in summary["action_items"]:
            print(f" - {item}")

# Example usage
if __name__ == "__main__":
    try:
        retro_pgf = RetroPGF()
        retro_pgf.add_round("Round 1")
        retro_pgf.add_feedback("Round 1", "Great progress on the project.")
        retro_pgf.add_action_item("Follow up with the design team.")
        retro_pgf.display_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
