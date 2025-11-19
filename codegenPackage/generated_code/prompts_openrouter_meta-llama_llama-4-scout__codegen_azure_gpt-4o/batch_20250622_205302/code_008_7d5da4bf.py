"""
Generated Code Metadata:
========================
Original URL: https://questsmisten.site
Prompt: Write a Python script to generate a copyright notice for a given year.
Generated: DETERMINISTIC_7d5da4bf4e0b3ca8
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to generate a copyright notice for a given year.
Author: [Your Name]
Date: [Today's Date]
"""

import sys

def generate_copyright_notice(year):
    """
    Generates a copyright notice for the given year.

    Args:
        year (int): The year for the copyright notice.

    Returns:
        str: A formatted copyright notice string.
    """
    return f"© {year} Your Company Name. All rights reserved."

def validate_year(year):
    """
    Validates the input year to ensure it is a positive integer.

    Args:
        year (str): The year input as a string.

    Returns:
        int: The validated year as an integer.

    Raises:
        ValueError: If the year is not a positive integer.
    """
    try:
        year_int = int(year)
        if year_int <= 0:
            raise ValueError("Year must be a positive integer.")
        return year_int
    except ValueError as e:
        raise ValueError(f"Invalid year input: {e}")

def main():
    """
    Main function to handle user input and generate the copyright notice.
    """
    try:
        # Prompt the user for the year
        year_input = input("Enter the year for the copyright notice: ").strip()
        
        # Validate the year
        year = validate_year(year_input)
        
        # Generate and display the copyright notice
        copyright_notice = generate_copyright_notice(year)
        print(copyright_notice)
    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
