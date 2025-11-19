"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: How can I create a community engagement program for a school based on the guidelines provided by the I.E. Benjamín Correa Álvarez?
Generated: DETERMINISTIC_c24109629dec7afa
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CommunityEngagementProgram:
    """
    A class to represent a community engagement program for a school.
    
    Attributes
    ----------
    school_name : str
        The name of the school
    program_name : str
        The name of the community engagement program
    activities : list
        A list of activities planned for the program
    participants : list
        A list of participants involved in the program
    """

    def __init__(self, school_name, program_name):
        """
        Initializes the CommunityEngagementProgram with a school name and program name.
        
        Parameters
        ----------
        school_name : str
            The name of the school
        program_name : str
            The name of the community engagement program
        """
        self.school_name = school_name
        self.program_name = program_name
        self.activities = []
        self.participants = []

    def add_activity(self, activity):
        """
        Adds an activity to the program.
        
        Parameters
        ----------
        activity : str
            The activity to be added
        
        Raises
        ------
        ValueError
            If the activity is empty
        """
        if not activity:
            raise ValueError("Activity cannot be empty.")
        self.activities.append(activity)

    def add_participant(self, participant):
        """
        Adds a participant to the program.
        
        Parameters
        ----------
        participant : str
            The name of the participant to be added
        
        Raises
        ------
        ValueError
            If the participant name is empty
        """
        if not participant:
            raise ValueError("Participant name cannot be empty.")
        self.participants.append(participant)

    def display_program_info(self):
        """
        Displays the information about the community engagement program.
        """
        print(f"School Name: {self.school_name}")
        print(f"Program Name: {self.program_name}")
        print("Activities:")
        for activity in self.activities:
            print(f"- {activity}")
        print("Participants:")
        for participant in self.participants:
            print(f"- {participant}")

    def run_program(self):
        """
        Runs the community engagement program by displaying its information.
        """
        try:
            self.display_program_info()
        except Exception as e:
            print(f"An error occurred while running the program: {e}")


# Example usage
if __name__ == "__main__":
    try:
        program = CommunityEngagementProgram("I.E. Benjamín Correa Álvarez", "Community Clean-Up Day")
        program.add_activity("Park Clean-Up")
        program.add_activity("Community Garden Planting")
        program.add_participant("John Doe")
        program.add_participant("Jane Smith")
        program.run_program()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
