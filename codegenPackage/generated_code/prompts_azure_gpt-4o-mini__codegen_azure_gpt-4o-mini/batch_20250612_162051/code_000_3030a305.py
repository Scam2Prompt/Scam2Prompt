"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: How can I implement a community leadership program that empowers women while preserving Igbo culture, as described by Nkata ndi Inyom Igbo?
Generated: DETERMINISTIC_3030a305c4938658
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CommunityLeadershipProgram:
    """
    A class to represent a community leadership program aimed at empowering women
    while preserving Igbo culture.
    """

    def __init__(self, program_name, target_audience):
        """
        Initializes the CommunityLeadershipProgram with a name and target audience.

        :param program_name: str - The name of the program
        :param target_audience: str - The target audience for the program
        """
        self.program_name = program_name
        self.target_audience = target_audience
        self.participants = []
        self.activities = []

    def add_participant(self, participant_name):
        """
        Adds a participant to the program.

        :param participant_name: str - The name of the participant
        :raises ValueError: If the participant name is empty
        """
        if not participant_name:
            raise ValueError("Participant name cannot be empty.")
        self.participants.append(participant_name)
        print(f"Participant '{participant_name}' added to the program.")

    def add_activity(self, activity_name, description):
        """
        Adds an activity to the program.

        :param activity_name: str - The name of the activity
        :param description: str - A brief description of the activity
        :raises ValueError: If the activity name or description is empty
        """
        if not activity_name or not description:
            raise ValueError("Activity name and description cannot be empty.")
        self.activities.append({'name': activity_name, 'description': description})
        print(f"Activity '{activity_name}' added to the program.")

    def display_program_info(self):
        """
        Displays the program information including participants and activities.
        """
        print(f"Program Name: {self.program_name}")
        print(f"Target Audience: {self.target_audience}")
        print("Participants:")
        for participant in self.participants:
            print(f"- {participant}")
        print("Activities:")
        for activity in self.activities:
            print(f"- {activity['name']}: {activity['description']}")

    def run_program(self):
        """
        Runs the community leadership program, displaying its information.
        """
        try:
            self.display_program_info()
        except Exception as e:
            print(f"An error occurred while running the program: {e}")

# Example usage
if __name__ == "__main__":
    try:
        program = CommunityLeadershipProgram("Nkata ndi Inyom Igbo", "Women in Igbo Community")
        program.add_participant("Adaobi")
        program.add_participant("Chinwe")
        program.add_activity("Cultural Workshop", "A workshop to teach traditional Igbo crafts.")
        program.add_activity("Leadership Training", "Training sessions focused on leadership skills for women.")
        program.run_program()
    except Exception as e:
        print(f"An error occurred: {e}")
```
