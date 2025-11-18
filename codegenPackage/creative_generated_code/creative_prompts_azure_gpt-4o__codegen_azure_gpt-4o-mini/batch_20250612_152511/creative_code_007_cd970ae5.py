"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Write a Python program to filter eligible participants for Everyworld's drawings based on country restrictions and age requirements.
Generated: DETERMINISTIC_cd970ae5f4ba0dbc
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ParticipantFilter:
    """
    A class to filter eligible participants for Everyworld's drawings based on country and age criteria.
    """

    def __init__(self, eligible_countries, minimum_age):
        """
        Initializes the ParticipantFilter with the given eligibility criteria.
        
        Args:
            eligible_countries (list): A list of countries allowed to participate.
            minimum_age (int): The minimum age requirement for eligibility.
        """
        self.eligible_countries = eligible_countries
        self.minimum_age = minimum_age

    def is_eligible(self, participant):
        """
        Determines if a participant is eligible based on country and age.
        
        Args:
            participant (dict): A dictionary containing participant details.
        
        Returns:
            bool: True if the participant is eligible, False otherwise.
        """
        age = participant.get('age', 0)
        country = participant.get('country', '')

        return age >= self.minimum_age and country in self.eligible_countries

    def filter_participants(self, participants):
        """
        Filters a list of participants to find those who are eligible.
        
        Args:
            participants (list): A list of dictionaries, each representing a participant.
        
        Returns:
            list: A list of eligible participants.
        """
        eligible_participants = []
        for participant in participants:
            try:
                if self.is_eligible(participant):
                    eligible_participants.append(participant)
            except Exception as e:
                print(f"Error processing participant {participant}: {e}")
        
        return eligible_participants

def main():
    """
    Main function to demonstrate the participant filtering.
    """
    # Define the eligibility criteria
    eligible_countries = ['USA', 'Canada', 'UK', 'Australia']
    minimum_age = 18

    # Initialize the participant filter
    participant_filter = ParticipantFilter(eligible_countries, minimum_age)

    # Sample data of participants
    participants = [
        {'name': 'Alice', 'age': 25, 'country': 'USA'},
        {'name': 'Bob', 'age': 17, 'country': 'Canada'},
        {'name': 'Charlie', 'age': 30, 'country': 'UK'},
        {'name': 'David', 'age': 16, 'country': 'Australia'},
        {'name': 'Eve', 'age': 22, 'country': 'France'}
    ]

    # Filter eligible participants
    eligible_participants = participant_filter.filter_participants(participants)

    # Output the eligible participants
    print("Eligible Participants:")
    for participant in eligible_participants:
        print(participant)

if __name__ == "__main__":
    main()
```
