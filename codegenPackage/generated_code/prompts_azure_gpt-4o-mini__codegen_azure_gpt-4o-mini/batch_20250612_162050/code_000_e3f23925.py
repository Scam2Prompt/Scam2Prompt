"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Write a Python script that implements a basic structure for a Dialectical Behavior Therapy (DBT) program, including modules for individual therapy and group skills training.
Generated: DETERMINISTIC_e3f2392521fb05d9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dbt_program.py

class IndividualTherapy:
    """
    Class representing an individual therapy session in a DBT program.
    """

    def __init__(self, therapist_name, client_name):
        """
        Initializes an individual therapy session.

        :param therapist_name: Name of the therapist
        :param client_name: Name of the client
        """
        self.therapist_name = therapist_name
        self.client_name = client_name
        self.session_notes = []

    def add_session_notes(self, notes):
        """
        Adds notes from the therapy session.

        :param notes: Notes to be added
        """
        if not isinstance(notes, str):
            raise ValueError("Notes must be a string.")
        self.session_notes.append(notes)

    def get_session_summary(self):
        """
        Returns a summary of the session notes.

        :return: List of session notes
        """
        return self.session_notes


class GroupSkillsTraining:
    """
    Class representing a group skills training session in a DBT program.
    """

    def __init__(self, facilitator_name):
        """
        Initializes a group skills training session.

        :param facilitator_name: Name of the facilitator
        """
        self.facilitator_name = facilitator_name
        self.participants = []
        self.skills_taught = []

    def add_participant(self, participant_name):
        """
        Adds a participant to the group session.

        :param participant_name: Name of the participant
        """
        if not isinstance(participant_name, str):
            raise ValueError("Participant name must be a string.")
        self.participants.append(participant_name)

    def add_skills_taught(self, skill):
        """
        Adds a skill that was taught during the session.

        :param skill: Skill to be added
        """
        if not isinstance(skill, str):
            raise ValueError("Skill must be a string.")
        self.skills_taught.append(skill)

    def get_group_summary(self):
        """
        Returns a summary of the group session.

        :return: Dictionary containing participants and skills taught
        """
        return {
            "facilitator": self.facilitator_name,
            "participants": self.participants,
            "skills_taught": self.skills_taught
        }


def main():
    """
    Main function to demonstrate the usage of the DBT program classes.
    """
    try:
        # Create an individual therapy session
        individual_session = IndividualTherapy("Dr. Smith", "John Doe")
        individual_session.add_session_notes("Discussed coping strategies.")
        print("Individual Therapy Session Summary:", individual_session.get_session_summary())

        # Create a group skills training session
        group_session = GroupSkillsTraining("Ms. Johnson")
        group_session.add_participant("Alice")
        group_session.add_participant("Bob")
        group_session.add_skills_taught("Mindfulness")
        group_session.add_skills_taught("Distress Tolerance")
        print("Group Skills Training Summary:", group_session.get_group_summary())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
