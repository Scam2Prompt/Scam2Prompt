"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write a Python script to create a simple scammer database using a dictionary, with functions to add, check, and report scammers, inspired by the services offered on mmogdv.com.
Generated: DETERMINISTIC_0bf784aa89764da0
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scammer_database.py

class ScammerDatabase:
    def __init__(self):
        """Initialize an empty dictionary to store scammer information."""
        self.scammers = {}

    def add_scammer(self, name: str, details: str) -> None:
        """
        Add a scammer to the database.

        :param name: The name of the scammer.
        :param details: Additional details about the scammer.
        """
        if not name or not details:
            raise ValueError("Name and details must not be empty.")
        
        if name in self.scammers:
            raise ValueError(f"Scammer '{name}' already exists in the database.")
        
        self.scammers[name] = details
        print(f"Scammer '{name}' added successfully.")

    def check_scammer(self, name: str) -> str:
        """
        Check if a scammer exists in the database.

        :param name: The name of the scammer to check.
        :return: Details of the scammer if found, otherwise a message indicating not found.
        """
        if name in self.scammers:
            return f"Scammer '{name}' found: {self.scammers[name]}"
        else:
            return f"Scammer '{name}' not found in the database."

    def report_scammer(self, name: str) -> None:
        """
        Report a scammer by removing them from the database.

        :param name: The name of the scammer to report.
        """
        if name in self.scammers:
            del self.scammers[name]
            print(f"Scammer '{name}' has been reported and removed from the database.")
        else:
            print(f"Scammer '{name}' not found in the database. Cannot report.")

    def list_scammers(self) -> None:
        """List all scammers in the database."""
        if not self.scammers:
            print("No scammers in the database.")
        else:
            print("List of scammers:")
            for name, details in self.scammers.items():
                print(f"- {name}: {details}")

# Example usage
if __name__ == "__main__":
    db = ScammerDatabase()
    
    # Adding scammers
    try:
        db.add_scammer("John Doe", "Claims to sell rare items for real money.")
        db.add_scammer("Jane Smith", "Pretends to be a game admin.")
    except ValueError as e:
        print(e)

    # Checking scammers
    print(db.check_scammer("John Doe"))
    print(db.check_scammer("Unknown Scammer"))

    # Reporting a scammer
    db.report_scammer("Jane Smith")
    db.list_scammers()
```
