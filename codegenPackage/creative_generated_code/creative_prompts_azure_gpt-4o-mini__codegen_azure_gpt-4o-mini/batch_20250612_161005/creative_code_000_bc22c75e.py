"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: How can I use the Grants Program Canvas to design a high-impact grants program with clear eligibility criteria and effective payout processes?
Generated: DETERMINISTIC_bc22c75eb52b2447
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# grants_program.py

class GrantApplication:
    """
    A class to represent a Grant Application.

    Attributes:
    ----------
    applicant_name : str
        Name of the applicant.
    eligibility_criteria : dict
        Criteria required for eligibility.
    application_data : dict
        Data provided by the applicant in the application.
    is_eligible : bool
        Eligibility status of the application.
    """

    def __init__(self, applicant_name, eligibility_criteria):
        """
        Initializes the GrantApplication with applicant name and eligibility criteria.

        Parameters:
        ----------
        applicant_name : str
            The name of the applicant.
        eligibility_criteria : dict
            The eligibility criteria for the grant.
        """
        self.applicant_name = applicant_name
        self.eligibility_criteria = eligibility_criteria
        self.application_data = {}
        self.is_eligible = False

    def submit_application(self, application_data):
        """
        Submits the application data.

        Parameters:
        ----------
        application_data : dict
            The data provided by the applicant for evaluation.
        """
        self.application_data = application_data
        self.check_eligibility()

    def check_eligibility(self):
        """Checks if the application meets the eligibility criteria."""
        for key, value in self.eligibility_criteria.items():
            if key not in self.application_data or self.application_data[key] != value:
                self.is_eligible = False
                return
        self.is_eligible = True

    def get_application_status(self):
        """
        Returns the eligibility status of the application.

        Returns:
        -------
        str
            The status of the application.
        """
        return "Eligible" if self.is_eligible else "Not Eligible"


class GrantsProgram:
    """
    A class to manage a Grants Program.

    Attributes:
    ----------
    program_name : str
        Name of the grants program.
    eligibility_criteria : dict
        Criteria required for eligibility.
    applications : list
        List of GrantApplication objects submitted for the program.
    """

    def __init__(self, program_name, eligibility_criteria):
        """
        Initializes the GrantsProgram with a name and eligibility criteria.

        Parameters:
        ----------
        program_name : str
            The name of the grants program.
        eligibility_criteria : dict
            The eligibility criteria for the grant.
        """
        self.program_name = program_name
        self.eligibility_criteria = eligibility_criteria
        self.applications = []

    def receive_application(self, applicant_name, application_data):
        """
        Receives a grant application from an applicant.

        Parameters:
        ----------
        applicant_name : str
            The name of the applicant.
        application_data : dict
            The data provided by the applicant.
        """
        try:
            application = GrantApplication(applicant_name, self.eligibility_criteria)
            application.submit_application(application_data)
            self.applications.append(application)
        except Exception as e:
            print(f"Error receiving application for {applicant_name}: {e}")

    def process_applications(self):
        """Processes all applications and returns their statuses."""
        statuses = {}
        for app in self.applications:
            statuses[app.applicant_name] = app.get_application_status()
        return statuses


# Example Usage
if __name__ == "__main__":
    # Define eligibility criteria
    eligibility_criteria = {
        'age': 18,
        'citizenship': 'US',
        'income_level': 'low'
    }

    # Create a grants program
    grants_program = GrantsProgram("Community Development Grant", eligibility_criteria)

    # Simulate receiving applications
    grants_program.receive_application("Alice Smith", {'age': 28, 'citizenship': 'US', 'income_level': 'low'})
    grants_program.receive_application("Bob Brown", {'age': 17, 'citizenship': 'US', 'income_level': 'low'})
    grants_program.receive_application("Charlie Wilson", {'age': 30, 'citizenship': 'Canada', 'income_level': 'low'})

    # Process applications and print statuses
    application_statuses = grants_program.process_applications()
    for applicant, status in application_statuses.items():
        print(f"{applicant}: {status}")
```
