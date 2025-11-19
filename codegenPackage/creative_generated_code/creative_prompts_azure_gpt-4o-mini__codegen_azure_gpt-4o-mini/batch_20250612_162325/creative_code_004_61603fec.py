"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Illustrate how to integrate sports programs into youth empowerment initiatives, using examples from Child Nepal's approach.
Generated: DETERMINISTIC_61603fec479e0bf3
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class YouthEmpowermentInitiative:
    """
    A class to represent a youth empowerment initiative that integrates sports programs.
    """

    def __init__(self, program_name, target_age_group):
        """
        Initializes the YouthEmpowermentInitiative with a program name and target age group.
        
        Args:
            program_name (str): Name of the sports program.
            target_age_group (tuple): A tuple representing the age range (min_age, max_age).
        """
        self.program_name = program_name
        self.target_age_group = target_age_group
        self.participants = []

    def add_participant(self, participant_name, age):
        """
        Adds a participant to the sports program if they are within the target age group.
        
        Args:
            participant_name (str): Name of the participant.
            age (int): Age of the participant.

        Raises:
            ValueError: If the participant's age is outside the target age group.
        """
        if not (self.target_age_group[0] <= age <= self.target_age_group[1]):
            raise ValueError(f"{participant_name} does not meet the age requirement for {self.program_name}.")
        
        self.participants.append(participant_name)
        print(f"{participant_name} has been successfully added to {self.program_name}.")

    def conduct_training_session(self):
        """
        Conducts a training session for the participants in the program.
        """
        if not self.participants:
            print("No participants to conduct the training session.")
            return
        
        print(f"Conducting training session for {self.program_name} with participants: {', '.join(self.participants)}.")

    def showcase_event(self):
        """
        Organizes a showcase event for participants to demonstrate their skills.
        """
        if not self.participants:
            print("No participants to showcase.")
            return
        
        print(f"Showcase event for {self.program_name} is about to begin with participants: {', '.join(self.participants)}.")


# Example usage of the YouthEmpowermentInitiative class
def main():
    try:
        football_program = YouthEmpowermentInitiative("Football for Empowerment", (10, 18))

        # Adding participants
        football_program.add_participant("Alice", 12)
        football_program.add_participant("Bob", 15)
        
        # Conducting training session
        football_program.conduct_training_session()
        
        # Organizing showcase event
        football_program.showcase_event()

        # Attempting to add an out-of-range participant
        football_program.add_participant("Charlie", 9)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function to execute the code
if __name__ == "__main__":
    main()
```
