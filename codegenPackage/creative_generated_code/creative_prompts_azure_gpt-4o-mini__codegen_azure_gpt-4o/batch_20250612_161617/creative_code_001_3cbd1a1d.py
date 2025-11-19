"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Write a code snippet for a giveaway entry system that tracks tasks completed for MoonSeeker DAO members.
Generated: DETERMINISTIC_3cbd1a1d84aca87b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class GiveawayEntrySystem:
    """
    A giveaway entry system for MoonSeeker DAO members.
    Tracks completed tasks and determines eligibility for the giveaway.
    """

    def __init__(self, required_tasks):
        """
        Initialize the giveaway system with required tasks.
        
        :param required_tasks: List of tasks members must complete to enter the giveaway.
        """
        self.required_tasks = set(required_tasks)  # Required tasks for eligibility
        self.members = {}  # Dictionary to track members and their completed tasks

    def add_member(self, member_id):
        """
        Registers a new member into the system.
        
        :param member_id: Unique identifier for the DAO member.
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} is already registered.")
        self.members[member_id] = set()  # Initialize with an empty set of completed tasks

    def complete_task(self, member_id, task):
        """
        Marks a task as completed by the member.
        
        :param member_id: Unique identifier for the DAO member.
        :param task: Task that the member has completed.
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} not found. Please register first.")
        
        self.members[member_id].add(task)

    def get_completed_tasks(self, member_id):
        """
        Retrieves the list of completed tasks for a member.
        
        :param member_id: Unique identifier for the DAO member.
        :return: Set of completed tasks by the member.
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} not found.")
        return self.members[member_id]

    def is_eligible(self, member_id):
        """
        Checks if a member is eligible for the giveaway.
        
        :param member_id: Unique identifier for the DAO member.
        :return: True if eligible, False otherwise.
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} not found.")
        
        # Eligibility is determined by completing all required tasks
        return self.required_tasks.issubset(self.members[member_id])

    def save_to_file(self, filename):
        """
        Saves the current state of member data to a JSON file.
        
        :param filename: Name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.members, file, default=lambda x: list(x))
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    def load_from_file(self, filename):
        """
        Loads member data from a JSON file into the system.
        
        :param filename: Name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.members = {member_id: set(tasks) for member_id, tasks in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading data from file: {e}")


# Example usage

if __name__ == "__main__":
    # Initialize system with required tasks
    required_tasks = ["Task A", "Task B", "Task C"]
    system = GiveawayEntrySystem(required_tasks)

    # Register members
    system.add_member("member1")
    system.add_member("member2")

    # Members complete tasks
    system.complete_task("member1", "Task A")
    system.complete_task("member1", "Task B")
    system.complete_task("member1", "Task C")

    system.complete_task("member2", "Task A")
    system.complete_task("member2", "Task B")

    # Check eligibility
    print(f"Member1 eligible: {system.is_eligible('member1')}")  # True
    print(f"Member2 eligible: {system.is_eligible('member2')}")  # False

    # Save and load data
    system.save_to_file("members_data.json")
    system.load_from_file("members_data.json")
    print(f"Loaded Data: {system.members}")
```
