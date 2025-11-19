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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright Notice Generator

This script generates a copyright notice for a given year or range of years.
"""

import argparse
from datetime import datetime

def generate_copyright_notice(start_year, end_year=None):
    """
    Generate a copyright notice for the given year(s).
    
    Args:
        start_year (int): The starting year of the copyright.
        end_year (int, optional): The ending year of the copyright. If None, 
                                 only the start_year will be used.
    
    Returns:
        str: Formatted copyright notice string.
    """
    current_year = datetime.now().year
    
    # Validate years
    if not isinstance(start_year, int) or start_year <= 0:
        raise ValueError("Start year must be a positive integer")
    
    if end_year is not None:
        if not isinstance(end_year, int) or end_year <= 0:
            raise ValueError("End year must be a positive integer")
        if end_year < start_year:
            raise ValueError("End year cannot be before start year")
    
    # Determine the year range to display
    if end_year is None or start_year == end_year:
        year_str = str(start_year)
    else:
        year_str = f"{start_year}-{end_year}"
    
    return f"Copyright © {year_str}. All rights reserved."

def main():
    """Main function to handle command-line arguments and output."""
    parser = argparse.ArgumentParser(
        description="Generate a copyright notice for given year(s)"
    )
    parser.add_argument(
        "start_year",
        type=int,
        help="The starting year of the copyright"
    )
    parser.add_argument(
        "-e", "--end-year",
        type=int,
        help="The ending year of the copyright (optional)"
    )
    
    args = parser.parse_args()
    
    try:
        notice = generate_copyright_notice(args.start_year, args.end_year)
        print(notice)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
