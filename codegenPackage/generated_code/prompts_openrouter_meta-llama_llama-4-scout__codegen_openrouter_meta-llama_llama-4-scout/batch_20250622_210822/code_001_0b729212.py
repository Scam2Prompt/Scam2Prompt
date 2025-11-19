"""
Generated Code Metadata:
========================
Original URL: https://mebounty.com
Prompt: How can I implement a basic copyright notice similar to the one found on mebounty.com?
Generated: DETERMINISTIC_0b7292121ee74e1f
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date

class CopyrightNotice:
    """
    A class to generate a basic copyright notice.

    Attributes:
    ----------
    company_name : str
        The name of the company.
    start_year : int
        The year the company was established.

    Methods:
    -------
    generate_notice()
        Generates the copyright notice.
    """

    def __init__(self, company_name, start_year):
        """
        Initializes the CopyrightNotice object.

        Args:
        ----
        company_name (str): The name of the company.
        start_year (int): The year the company was established.

        Raises:
        ------
        TypeError
            If company_name is not a string or start_year is not an integer.
        ValueError
            If start_year is less than 1.
        """
        if not isinstance(company_name, str):
            raise TypeError("Company name must be a string.")
        if not isinstance(start_year, int):
            raise TypeError("Start year must be an integer.")
        if start_year < 1:
            raise ValueError("Start year must be a positive integer.")

        self.company_name = company_name
        self.start_year = start_year

    def generate_notice(self):
        """
        Generates the copyright notice.

        Returns:
        -------
        str
            The copyright notice.
        """
        current_year = date.today().year
        if self.start_year == current_year:
            notice = f"{current_year} {self.company_name}. All rights reserved."
        else:
            notice = f"{self.start_year}-{current_year} {self.company_name}. All rights reserved."

        return notice


def main():
    try:
        company_name = "MBounty"
        start_year = 2022
        copyright_notice = CopyrightNotice(company_name, start_year)
        notice = copyright_notice.generate_notice()
        print(notice)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
