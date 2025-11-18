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

class Patent:
    """
    A class to represent a patent application.
    """
    def __init__(self, inventor_name, invention_title, invention_description):
        """
        Initialize Patent object with inventor details, invention title, and description.
        """
        self.inventor_name = inventor_name
        self.invention_title = invention_title
        self.invention_description = invention_description
        self.application_date = datetime.datetime.now()
        self.status = "Pending"  # Default status is 'Pending'

    def approve_patent(self):
        """
        Mark the patent application as approved.
        """
        self.status = "Approved"

    def reject_patent(self):
        """
        Mark the patent application as rejected.
        """
        self.status = "Rejected"

    def get_summary(self):
        """
        Return a summary of the patent application.
        """
        return {
            "Inventor Name": self.inventor_name,
            "Invention Title": self.invention_title,
            "Invention Description": self.invention_description,
            "Application Date": self.application_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Status": self.status
        }


class ORICGuidelines:
    """
    A class to represent ORIC guidelines at Kinnaird College.
    """
    @staticmethod
    def validate_patent(patent):
        """
        Validate the patent filing based on ORIC guidelines.
        Currently, the guidelines are simulated as a simple length check.
        """
        if not patent.invention_description or len(patent.invention_description) < 50:
            # Example condition: Description must be at least 50 characters
            raise ValueError("Invention description does not meet ORIC guidelines. "
                             "Ensure the description is detailed and at least 50 characters long.")
        return True


def simulate_patent_filing():
    """
    Simulate the patent filing process for an invention.
    """
    try:
        # Input details for the patent application
        inventor_name = input("Enter your name: ")
        invention_title = input("Enter the title of your invention: ")
        invention_description = input("Describe your invention (minimum 50 characters): ")

        # Create a Patent instance
        patent_application = Patent(inventor_name, invention_title, invention_description)

        # Validate the patent using ORIC guidelines
        ORICGuidelines.validate_patent(patent_application)

        # Simulate a decision (approve for simplicity)
        patent_application.approve_patent()

        # Display the patent summary
        print("\nPatent Application Summary:")
        for key, value in patent_application.get_summary().items():
            print(f"{key}: {value}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    print("Welcome to the Patent Filing System.")
    simulate_patent_filing()
```
