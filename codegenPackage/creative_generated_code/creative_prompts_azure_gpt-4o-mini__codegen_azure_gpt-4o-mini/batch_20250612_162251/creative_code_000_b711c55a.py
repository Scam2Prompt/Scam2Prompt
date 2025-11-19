"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: How can I implement community engagement programs for youth development in Iowa, based on the Iowa Collaboration for Youth Development's initiatives?
Generated: DETERMINISTIC_b711c55a330591b5
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_engagement.py

import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CommunityEngagementProgram:
    """
    A class to implement community engagement programs for youth development
    based on the Iowa Collaboration for Youth Development's initiatives.
    """

    def __init__(self, program_name, target_age_group):
        """
        Initialize the community engagement program.

        :param program_name: Name of the program
        :param target_age_group: The age group the program targets
        """
        self.program_name = program_name
        self.target_age_group = target_age_group
        self.participants = []

    def add_participant(self, participant_name):
        """
        Add a participant to the program.

        :param participant_name: Name of the participant
        """
        if not isinstance(participant_name, str) or not participant_name.strip():
            logging.error("Invalid participant name provided.")
            raise ValueError("Participant name must be a non-empty string.")
        
        self.participants.append(participant_name)
        logging.info(f"Participant {participant_name} added to program {self.program_name}.")

    def remove_participant(self, participant_name):
        """
        Remove a participant from the program.

        :param participant_name: Name of the participant to remove
        """
        try:
            self.participants.remove(participant_name)
            logging.info(f"Participant {participant_name} removed from program {self.program_name}.")
        except ValueError:
            logging.error(f"Participant {participant_name} not found in the program.")
            raise ValueError("Participant not found in the program.")

    def get_participant_list(self):
        """
        Retrieve the list of participants in the program.

        :return: List of participants
        """
        return self.participants

    def display_program_details(self):
        """
        Display program details including name, target age group, and participants.
        """
        logging.info(f"Program Name: {self.program_name}")
        logging.info(f"Target Age Group: {self.target_age_group}")
        logging.info(f"Participants: {', '.join(self.participants) if self.participants else 'No participants yet.'}")

def main():
    """
    Main function to demonstrate the functionality of the CommunityEngagementProgram class.
    """
    try:
        # Create a new community engagement program
        program = CommunityEngagementProgram("Iowa Youth Leadership Program", "13-18 years")

        # Add participants
        program.add_participant("John Doe")
        program.add_participant("Jane Smith")

        # Display program details
        program.display_program_details()

        # Remove a participant
        program.remove_participant("John Doe")

        # Display updated program details
        program.display_program_details()

    except Exception as e:
        logging.critical(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
