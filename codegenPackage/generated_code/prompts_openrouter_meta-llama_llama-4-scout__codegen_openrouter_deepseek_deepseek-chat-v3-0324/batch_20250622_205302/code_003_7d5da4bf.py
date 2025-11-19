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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright Notice Generator

This script generates a copyright notice for a given year.
"""

import argparse
from datetime import datetime


def generate_copyright_notice(year, name="Company Name"):
    """
    Generate a copyright notice string.

    Args:
        year (int or str): The year(s) for the copyright notice
        name (str): The name to include in the notice (default: "Company Name")

    Returns:
        str: Formatted copyright notice string
    """
    current_year = datetime.now().year
    
    try:
        if isinstance(year, str):
            year = int(year)
            
        if year < 0:
            raise ValueError("Year cannot be negative")
            
        year_range = f"{year}-{current_year}" if year != current_year else str(year)
    except ValueError as e:
        raise ValueError(f"Invalid year format: {e}")

    return f"Copyright © {year_range} {name}. All rights reserved."


def main():
    parser = argparse.ArgumentParser(
        description="Generate a copyright notice for a given year."
    )
    parser.add_argument(
        "year",
        help="The year for the copyright notice (can be earlier than current year)",
    )
    parser.add_argument(
        "-n", "--name",
        default="Company Name",
        help="The name to include in the copyright notice",
    )
    
    args = parser.parse_args()
    
    try:
        notice = generate_copyright_notice(args.year, args.name)
        print(notice)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
```
