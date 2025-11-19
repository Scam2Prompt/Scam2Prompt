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
"""
This script demonstrates the use of a Python library to manage copyright information on websites.
The library provides functionalities to dynamically set and update copyright statements.
"""

from datetime import datetime

class CopyrightManager:
    """
    A class to manage website copyright information dynamically.
    """
    
    def __init__(self, website_name: str, start_year: int):
        """
        Initializes the CopyrightManager.

        :param website_name: Name of the website.
        :param start_year: The year the website was launched.
        """
        self.website_name = website_name
        self.start_year = start_year
        self.current_year = datetime.now().year

    def get_copyright_statement(self) -> str:
        """
        Generates the copyright statement based on initialization values.

        :return: A dynamically updated copyright statement string.
        """
        if self.start_year < self.current_year:
            return f"© {self.start_year}-{self.current_year} {self.website_name}. All rights reserved."
        return f"© {self.current_year} {self.website_name}. All rights reserved."

    def update_start_year(self, start_year: int):
        """
        Updates the start year for the copyright statement.

        :param start_year: New start year to set.
        """
        if start_year > self.current_year:
            raise ValueError("Start year cannot be in the future.")
        self.start_year = start_year


# Example usage
if __name__ == "__main__":
    try:
        # Initialize copyright manager with website name and start year
        website_name = "starlknelt.website"
        start_year = 2020
        copyright_manager = CopyrightManager(website_name, start_year)

        # Generate and display the copyright statement
        print(copyright_manager.get_copyright_statement())

        # Update the start year if necessary
        new_start_year = 2018
        copyright_manager.update_start_year(new_start_year)
        print(copyright_manager.get_copyright_statement())

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
```
