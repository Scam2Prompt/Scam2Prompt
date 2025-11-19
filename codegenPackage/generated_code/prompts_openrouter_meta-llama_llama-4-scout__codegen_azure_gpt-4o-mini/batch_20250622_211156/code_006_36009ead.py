"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a sample award nomination for an activity professional in Minnesota, using the criteria outlined by MN SWAP.
Generated: DETERMINISTIC_36009ead5b0f3449
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class AwardNomination:
    """
    A class to represent an award nomination for an activity professional.
    """

    def __init__(self, nominee_name, nominee_position, nominee_organization, 
                 nominator_name, nominator_contact, achievements, criteria):
        """
        Initializes the AwardNomination with the provided details.

        :param nominee_name: Name of the nominee
        :param nominee_position: Position of the nominee
        :param nominee_organization: Organization of the nominee
        :param nominator_name: Name of the nominator
        :param nominator_contact: Contact information of the nominator
        :param achievements: List of achievements of the nominee
        :param criteria: Criteria met by the nominee
        """
        self.nominee_name = nominee_name
        self.nominee_position = nominee_position
        self.nominee_organization = nominee_organization
        self.nominator_name = nominator_name
        self.nominator_contact = nominator_contact
        self.achievements = achievements
        self.criteria = criteria
        self.nomination_date = datetime.now().strftime("%Y-%m-%d")

    def validate_nomination(self):
        """
        Validates the nomination details.

        :raises ValueError: If any required field is missing or invalid
        """
        if not all([self.nominee_name, self.nominee_position, self.nominee_organization,
                    self.nominator_name, self.nominator_contact, self.achievements, self.criteria]):
            raise ValueError("All fields must be filled out.")

    def to_json(self):
        """
        Converts the nomination details to a JSON format.

        :return: JSON string of the nomination details
        """
        return json.dumps(self.__dict__, indent=4)

def main():
    """
    Main function to create and display an award nomination.
    """
    try:
        # Sample data for the nomination
        nominee_name = "Jane Doe"
        nominee_position = "Activity Director"
        nominee_organization = "Sunshine Senior Living"
        nominator_name = "John Smith"
        nominator_contact = "john.smith@example.com"
        achievements = [
            "Implemented a new wellness program that increased resident participation by 40%.",
            "Organized monthly community events that fostered intergenerational relationships."
        ]
        criteria = [
            "Demonstrates exceptional leadership in activity programming.",
            "Fosters a positive and inclusive environment for all residents."
        ]

        # Create an instance of AwardNomination
        nomination = AwardNomination(nominee_name, nominee_position, nominee_organization,
                                      nominator_name, nominator_contact, achievements, criteria)

        # Validate the nomination
        nomination.validate_nomination()

        # Output the nomination in JSON format
        print("Award Nomination:")
        print(nomination.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
