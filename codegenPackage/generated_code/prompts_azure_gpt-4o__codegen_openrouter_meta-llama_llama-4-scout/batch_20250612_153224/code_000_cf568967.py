"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write Python code to simulate a patent filing process for an invention, incorporating the guidelines provided by ORIC at Kinnaird College.
Generated: DETERMINISTIC_cf5689678d428076
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patent_filing_process.py

from datetime import datetime
from enum import Enum

class PatentStatus(Enum):
    """Enum representing the status of a patent."""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class Inventor:
    """Class representing an inventor."""
    def __init__(self, name, email, phone):
        """
        Initialize an Inventor object.

        Args:
            name (str): Name of the inventor.
            email (str): Email address of the inventor.
            phone (str): Phone number of the inventor.
        """
        self.name = name
        self.email = email
        self.phone = phone

class Patent:
    """Class representing a patent."""
    def __init__(self, title, description, inventor):
        """
        Initialize a Patent object.

        Args:
            title (str): Title of the patent.
            description (str): Description of the patent.
            inventor (Inventor): Inventor of the patent.
        """
        self.title = title
        self.description = description
        self.inventor = inventor
        self.status = PatentStatus.PENDING
        self.filing_date = None

    def file_patent(self):
        """File the patent and update the filing date."""
        try:
            self.filing_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Patent '{self.title}' filed successfully on {self.filing_date}.")
        except Exception as e:
            print(f"Error filing patent: {str(e)}")

    def update_status(self, status):
        """
        Update the status of the patent.

        Args:
            status (PatentStatus): New status of the patent.
        """
        if isinstance(status, PatentStatus):
            self.status = status
            print(f"Patent '{self.title}' status updated to {self.status.value}.")
        else:
            print("Invalid patent status.")

def main():
    # Create an inventor
    inventor = Inventor("John Doe", "john.doe@example.com", "1234567890")

    # Create a patent
    patent = Patent("Invention Title", "Invention description.", inventor)

    # File the patent
    patent.file_patent()

    # Update the patent status
    patent.update_status(PatentStatus.APPROVED)

    # Print patent details
    print("\nPatent Details:")
    print(f"Title: {patent.title}")
    print(f"Description: {patent.description}")
    print(f"Inventor: {patent.inventor.name}")
    print(f"Status: {patent.status.value}")
    print(f"Filing Date: {patent.filing_date}")

if __name__ == "__main__":
    main()
```
