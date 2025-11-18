"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Provide a step-by-step guide for integrating internship opportunities into a brokerage training program, referencing Kigali Institute's focus on internships for career advancement.
Generated: DETERMINISTIC_0748acbd0b90fc30
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BrokerageTrainingProgram:
    """
    Class representing a brokerage training program integrating internship opportunities.
    """

    def __init__(self, institute_name):
        """
        Initialize the brokerage training program with the specified institute name.

        :param institute_name: Name of the institute offering the training program.
        """
        self.institute_name = institute_name
        self.internship_opportunities = []

    def add_internship_opportunity(self, internship):
        """
        Add an internship opportunity to the program.

        :param internship: A dictionary containing details about the internship.
        :raises ValueError: If the internship does not contain the required fields.
        """
        required_fields = ['title', 'company', 'duration', 'description', 'salary']

        for field in required_fields:
            if field not in internship:
                raise ValueError(f"Internship must include '{field}'")

        self.internship_opportunities.append(internship)

    def list_internships(self):
        """
        List all internship opportunities available in the program.

        :return: A list of internships available.
        """
        return self.internship_opportunities

    def apply_to_internship(self, internship_title, applicant_info):
        """
        Apply for an internship opportunity.

        :param internship_title: The title of the internship to apply for.
        :param applicant_info: A dictionary containing applicant's information.
        :raises ValueError: If the internship is not found or applicant info is missing.
        """
        if not any(internship['title'] == internship_title for internship in self.internship_opportunities):
            raise ValueError(f"Internship '{internship_title}' not found.")

        if not isinstance(applicant_info, dict) or not applicant_info.get('name'):
            raise ValueError("Applicant info must be a dictionary with at least a 'name' field.")

        # Logic to submit application (mock-up)
        print(f"Application submitted for {internship_title} by {applicant_info['name']}.")

    def __str__(self):
        """
        String representation of the training program.

        :return: Formatted string of the training program details.
        """
        return f"Brokerage Training Program at {self.institute_name} with {len(self.internship_opportunities)} internship(s) available."


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the training program with the Kigali Institute's focus on internships
        program = BrokerageTrainingProgram("Kigali Institute")

        # Add internship opportunities
        internship1 = {
            'title': 'Finance Intern',
            'company': 'ABC Brokerage',
            'duration': '3 months',
            'description': 'Internship at a leading brokerage firm.',
            'salary': 5000
        }
        program.add_internship_opportunity(internship1)

        # Apply for an internship
        applicant_info = {'name': 'John Doe', 'email': 'johndoe@example.com'}
        program.apply_to_internship('Finance Intern', applicant_info)

        # List internship opportunities
        print(program.list_internships())
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
