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
        """Initialize the scammer database as an empty dictionary."""
        self.scammers = {}

    def add_scammer(self, name, details):
        """
        Add a scammer to the database.

        Parameters:
        name (str): The name of the scammer.
        details (str): Details about the scammer.

        Raises:
        ValueError: If the scammer already exists in the database.
        """
        if name in self.scammers:
            raise ValueError(f"Scammer '{name}' already exists in the database.")
        self.scammers[name] = details
        print(f"Scammer '{name}' added successfully.")

    def check_scammer(self, name):
        """
        Check if a scammer exists in the database.

        Parameters:
        name (str): The name of the scammer.

        Returns:
        str: Details of the scammer if found, otherwise a not found message.
        """
        return self.scammers.get(name, f"Scammer '{name}' not found in the database.")

    def report_scammer(self, name):
        """
        Report a scammer by removing them from the database.

        Parameters:
        name (str): The name of the scammer.

        Raises:
        KeyError: If the scammer does not exist in the database.
        """
        if name not in self.scammers:
            raise KeyError(f"Scammer '{name}' cannot be reported because they do not exist.")
        del self.scammers[name]
        print(f"Scammer '{name}' reported and removed from the database.")

def main():
    """Main function to demonstrate the ScammerDatabase functionality."""
    db = ScammerDatabase()

    # Example usage
    try:
        db.add_scammer("John Doe", "Known for phishing scams.")
        print(db.check_scammer("John Doe"))
        db.report_scammer("John Doe")
        print(db.check_scammer("John Doe"))
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
