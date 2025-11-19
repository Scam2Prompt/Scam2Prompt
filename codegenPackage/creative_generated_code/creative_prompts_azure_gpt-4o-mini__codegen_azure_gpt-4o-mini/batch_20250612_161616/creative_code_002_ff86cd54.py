"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iedute.com
Prompt: "What are the essential elements to include in a website's copyright notice?"
Generated: DETERMINISTIC_ff86cd549fb82b21
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CopyrightNotice:
    """
    A class to generate a copyright notice for a website.
    """

    def __init__(self, owner: str, start_year: int, current_year: int = None):
        """
        Initializes the CopyrightNotice with the owner's name and the start year.

        :param owner: The name of the copyright owner (e.g., company or individual's name)
        :param start_year: The year the copyright began
        :param current_year: The current year (defaults to the current calendar year)
        """
        self.owner = owner
        self.start_year = start_year
        self.current_year = current_year if current_year else self._get_current_year()

        # Validate the input values
        if self.start_year < 0 or (self.current_year and self.current_year < self.start_year):
            raise ValueError("Start year must be a non-negative integer and not greater than the current year.")

    def _get_current_year(self) -> int:
        """
        Returns the current year.

        :return: The current year as an integer.
        """
        from datetime import datetime
        return datetime.now().year

    def generate_notice(self) -> str:
        """
        Generates a copyright notice string.

        :return: A formatted copyright notice.
        """
        if self.start_year == self.current_year:
            return f"© {self.current_year} {self.owner}. All rights reserved."
        else:
            return f"© {self.start_year} - {self.current_year} {self.owner}. All rights reserved."

# Example usage
if __name__ == "__main__":
    try:
        # Create a copyright notice instance
        notice = CopyrightNotice(owner="My Company", start_year=2020)
        
        # Generate and print the copyright notice
        print(notice.generate_notice())
    except ValueError as e:
        print(f"Error: {e}")
```
