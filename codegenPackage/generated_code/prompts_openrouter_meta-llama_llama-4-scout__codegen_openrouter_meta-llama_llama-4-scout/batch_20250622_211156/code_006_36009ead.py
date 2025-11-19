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
# Import required libraries
import datetime

class AwardNomination:
    def __init__(self, nominee_name, nominee_title, organization, 
                 activity_description, start_date, end_date, 
                 criteria_met):
        """
        Initialize an AwardNomination object.

        Args:
            nominee_name (str): Name of the nominee.
            nominee_title (str): Title of the nominee.
            organization (str): Organization of the nominee.
            activity_description (str): Description of the activity.
            start_date (str): Start date of the activity (YYYY-MM-DD).
            end_date (str): End date of the activity (YYYY-MM-DD).
            criteria_met (list): List of criteria met (e.g., 'I', 'II', 'III').
        """
        self.nominee_name = nominee_name
        self.nominee_title = nominee_title
        self.organization = organization
        self.activity_description = activity_description
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        self.criteria_met = criteria_met

    def validate_criteria(self):
        """
        Validate the criteria met.

        Raises:
            ValueError: If criteria met is not a list or contains invalid criteria.
        """
        valid_criteria = ['I', 'II', 'III', 'IV', 'V']
        if not isinstance(self.criteria_met, list):
            raise ValueError("Criteria met must be a list.")
        for criterion in self.criteria_met:
            if criterion not in valid_criteria:
                raise ValueError(f"Invalid criterion: {criterion}. Must be one of {valid_criteria}.")

    def generate_nomination(self):
        """
        Generate a sample award nomination.

        Returns:
            str: A sample award nomination.
        """
        try:
            self.validate_criteria()
        except ValueError as e:
            print(f"Error: {e}")
            return None

        nomination = f"""
        MINNESOTA STATEWIDE AWARD PROGRAM (MN SWAP)

        NOMINATION FOR ACTIVITY PROFESSIONAL AWARD

        Nominee Name: {self.nominee_name}
        Nominee Title: {self.nominee_title}
        Organization: {self.organization}

        Activity Description: {self.activity_description}
        Dates of Activity: {self.start_date} - {self.end_date}

        Criteria Met:
        """
        for criterion in self.criteria_met:
            nomination += f"\n- Criterion {criterion}: [Describe how the nominee met this criterion]"

        nomination += """
        
        I hereby nominate this individual for the MN SWAP Activity Professional Award.

        Nominee's Signature: _____________________________
        Date: _______________________________________

        Nominator's Name: [Your Name]
        Nominator's Title: [Your Title]
        Organization: [Your Organization]
        Date: _______________________________________
        """

        return nomination


def main():
    nominee_name = "Jane Doe"
    nominee_title = "Activity Professional"
    organization = "Example Organization"
    activity_description = "Implemented a new activity program for residents."
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    criteria_met = ['I', 'II', 'III']

    nomination = AwardNomination(nominee_name, nominee_title, organization, 
                                 activity_description, start_date, end_date, 
                                 criteria_met)

    print(nomination.generate_nomination())


if __name__ == "__main__":
    main()
```
