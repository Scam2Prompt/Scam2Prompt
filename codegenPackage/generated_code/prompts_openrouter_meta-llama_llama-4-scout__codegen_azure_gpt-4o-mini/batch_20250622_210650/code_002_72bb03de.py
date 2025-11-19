"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: "Design a community program based on Premchand's vision of building with purpose and leading with heart."
Generated: DETERMINISTIC_72bb03de8c7fb282
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CommunityProgram:
    """
    A class to represent a community program based on Premchand's vision of building with purpose and leading with heart.
    """

    def __init__(self, name, purpose):
        """
        Initializes the CommunityProgram with a name and purpose.

        Args:
            name (str): The name of the community program.
            purpose (str): The purpose of the community program.
        """
        self.name = name
        self.purpose = purpose
        self.members = []
        self.activities = []

    def add_member(self, member_name):
        """
        Adds a member to the community program.

        Args:
            member_name (str): The name of the member to be added.
        """
        if member_name not in self.members:
            self.members.append(member_name)
            print(f"Member '{member_name}' added to the program.")
        else:
            print(f"Member '{member_name}' is already in the program.")

    def remove_member(self, member_name):
        """
        Removes a member from the community program.

        Args:
            member_name (str): The name of the member to be removed.
        """
        try:
            self.members.remove(member_name)
            print(f"Member '{member_name}' removed from the program.")
        except ValueError:
            print(f"Member '{member_name}' not found in the program.")

    def add_activity(self, activity):
        """
        Adds an activity to the community program.

        Args:
            activity (str): The activity to be added.
        """
        self.activities.append(activity)
        print(f"Activity '{activity}' added to the program.")

    def list_members(self):
        """
        Lists all members of the community program.
        """
        print("Members of the program:")
        for member in self.members:
            print(f"- {member}")

    def list_activities(self):
        """
        Lists all activities of the community program.
        """
        print("Activities of the program:")
        for activity in self.activities:
            print(f"- {activity}")

    def execute_activity(self, activity):
        """
        Executes a specified activity if it exists in the program.

        Args:
            activity (str): The activity to be executed.
        """
        if activity in self.activities:
            print(f"Executing activity: {activity}")
            # Here you can add the logic for what happens during the activity
        else:
            print(f"Activity '{activity}' not found in the program.")

# Example usage
if __name__ == "__main__":
    # Create a community program
    program = CommunityProgram("Heart of the Community", "To foster unity and support among members.")

    # Add members
    program.add_member("Alice")
    program.add_member("Bob")

    # List members
    program.list_members()

    # Add activities
    program.add_activity("Community Clean-up")
    program.add_activity("Food Drive")

    # List activities
    program.list_activities()

    # Execute an activity
    program.execute_activity("Community Clean-up")

    # Remove a member
    program.remove_member("Alice")
    program.list_members()
```
