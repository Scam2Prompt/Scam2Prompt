"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starlknelt.website
Prompt: Suggest a library for managing copyright information on websites, taking cues from starlknelt.website's copyright statement.
Generated: DETERMINISTIC_0b816bb485319d04
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# CopyrightManager.py

class CopyrightManager:
    """
    A class to manage copyright information for a website.
    It provides functionality to set, get, and display copyright statements.
    """

    def __init__(self, owner_name, year=None):
        """
        Initializes the CopyrightManager with the owner's name and the current year.
        
        Args:
            owner_name (str): The name of the copyright owner.
            year (int, optional): The copyright year. Defaults to the current year if not provided.
        """
        self.owner_name = owner_name
        self.year = year if year else self.get_current_year()
        self.validate_inputs()

    @staticmethod
    def get_current_year():
        """Returns the current year."""
        from datetime import datetime
        return datetime.now().year

    def validate_inputs(self):
        """Validates the input data to ensure it meets expected criteria."""
        if not isinstance(self.owner_name, str) or not self.owner_name.strip():
            raise ValueError("Owner name must be a non-empty string.")
        if not isinstance(self.year, int) or self.year < 0:
            raise ValueError("Year must be a non-negative integer.")

    def get_copyright_statement(self):
        """
        Constructs the copyright statement.
        
        Returns:
            str: A formatted string containing the copyright statement.
        """
        return f"© {self.year} {self.owner_name}. All rights reserved."

    def display_copyright(self):
        """Displays the copyright statement."""
        print(self.get_copyright_statement())


# Example usage
if __name__ == "__main__":
    try:
        copyright_manager = CopyrightManager("Your Name or Company", 2023)
        copyright_manager.display_copyright()
    except ValueError as e:
        print(f"Error: {e}")
```
