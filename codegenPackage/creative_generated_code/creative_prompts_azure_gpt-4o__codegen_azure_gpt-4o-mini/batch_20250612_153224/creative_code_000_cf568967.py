"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write Python code to simulate a patent filing process for an invention, incorporating the guidelines provided by ORIC at Kinnaird College.
Generated: DETERMINISTIC_cf5689678d428076
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PatentApplicationError(Exception):
    """Custom exception for patent application errors."""
    pass

class PatentFiling:
    def __init__(self, inventor_name, invention_title, invention_description):
        """
        Initializes the PatentFiling instance.

        :param inventor_name: Name of the inventor
        :param invention_title: Title of the invention
        :param invention_description: Description of the invention
        """
        self.inventor_name = inventor_name
        self.invention_title = invention_title
        self.invention_description = invention_description
        self.filing_date = None
        self.application_number = None
        self.status = "Draft"

    def validate(self):
        """
        Validates the application details.

        :raises PatentApplicationError: If any of the required fields are empty
        """
        if not self.inventor_name or not self.invention_title or not self.invention_description:
            raise PatentApplicationError("All fields must be filled out.")

    def file_application(self):
        """
        Simulates the filing of a patent application.
        
        This method will validate the application, assign a filing date and an application number
        and change the status to "Filed".
        """
        try:
            self.validate()
            self.filing_date = datetime.datetime.now()
            self.application_number = self.generate_application_number()
            self.status = "Filed"
            print(f"Patent application filed successfully with application number: {self.application_number}")
            print(f"Filing date: {self.filing_date.strftime('%Y-%m-%d %H:%M:%S')}")
        except PatentApplicationError as e:
            print(f"Error filing patent application: {e}")

    def generate_application_number(self):
        """
        Generates a unique application number.

        :return: A unique application number as a string
        """
        return f"PAT-{int(datetime.datetime.now().timestamp())}"

    def get_application_status(self):
        """
        Retrieves the current status of the application.

        :return: Current status of the patent application
        """
        return self.status

# Example usage
if __name__ == "__main__":
    # Sample data for patent filing
    inventor = "Alice Doe"
    title = "Self-Cleaning Water Bottle"
    description = "A water bottle that cleans itself using UV light."

    # Create a PatentFiling instance
    patent_filing = PatentFiling(inventor, title, description)

    # File the patent application
    patent_filing.file_application()

    # Print the current status
    print(f"Current application status: {patent_filing.get_application_status()}")
```
