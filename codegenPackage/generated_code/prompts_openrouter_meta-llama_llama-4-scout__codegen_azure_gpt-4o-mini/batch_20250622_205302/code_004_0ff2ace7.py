"""
Generated Code Metadata:
========================
Original URL: https://opiumbird.fun
Prompt: Write a Python script to generate a copyright notice for a given year, ensuring it covers a range of years if necessary.
Generated: DETERMINISTIC_0ff2ace76adb36e5
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_copyright_notice(start_year, end_year=None):
    """
    Generate a copyright notice for a given year or range of years.

    Parameters:
    start_year (int): The starting year for the copyright notice.
    end_year (int, optional): The ending year for the copyright notice. 
                               If None, the current year will be used.

    Returns:
    str: A formatted copyright notice.
    
    Raises:
    ValueError: If start_year is not a valid year or if end_year is less than start_year.
    """
    current_year = datetime.datetime.now().year

    # Validate start_year
    if not isinstance(start_year, int) or start_year < 0:
        raise ValueError("start_year must be a non-negative integer.")
    
    # Determine end_year
    if end_year is None:
        end_year = current_year
    elif not isinstance(end_year, int) or end_year < start_year:
        raise ValueError("end_year must be a non-negative integer and greater than or equal to start_year.")

    # Generate copyright notice
    if start_year == end_year:
        return f"© {start_year} Your Company Name. All rights reserved."
    else:
        return f"© {start_year} - {end_year} Your Company Name. All rights reserved."

if __name__ == "__main__":
    try:
        # Example usage
        start_year = 2020
        end_year = 2023  # You can set this to None to use the current year
        copyright_notice = generate_copyright_notice(start_year, end_year)
        print(copyright_notice)
    except ValueError as e:
        print(f"Error: {e}")
```
