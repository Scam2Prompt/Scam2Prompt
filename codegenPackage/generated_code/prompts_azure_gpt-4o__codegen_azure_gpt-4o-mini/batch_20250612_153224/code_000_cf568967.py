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
import datetime

class PatentFilingError(Exception):
    """Custom exception for errors during the patent filing process."""
    pass

class Invention:
    """Class representing an invention to be patented."""
    
    def __init__(self, title, description, inventor_name):
        self.title = title
        self.description = description
        self.inventor_name = inventor_name
        self.filing_date = None
        self.patent_number = None

    def file_patent(self):
        """Simulate the patent filing process."""
        if not self.title or not self.description or not self.inventor_name:
            raise PatentFilingError("All fields must be filled out to file a patent.")
        
        # Simulate filing process
        self.filing_date = datetime.datetime.now()
        self.patent_number = self.generate_patent_number()
        return self.patent_number

    def generate_patent_number(self):
        """Generate a unique patent number."""
        return f"PAT-{int(datetime.datetime.now().timestamp())}"

    def __str__(self):
        """Return a string representation of the invention."""
        return f"Invention: {self.title}, Inventor: {self.inventor_name}, Patent Number: {self.patent_number}"

def main():
    """Main function to simulate the patent filing process."""
    try:
        # Example invention details
        title = "Innovative Widget"
        description = "A widget that improves efficiency."
        inventor_name = "Jane Doe"

        # Create an Invention instance
        invention = Invention(title, description, inventor_name)

        # File the patent
        patent_number = invention.file_patent()
        print(f"Patent filed successfully! Patent Number: {patent_number}")
        print(invention)

    except PatentFilingError as e:
        print(f"Error filing patent: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
