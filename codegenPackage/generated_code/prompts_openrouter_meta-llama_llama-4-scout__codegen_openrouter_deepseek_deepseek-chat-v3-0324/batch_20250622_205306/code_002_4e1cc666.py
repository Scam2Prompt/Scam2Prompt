"""
Generated Code Metadata:
========================
Original URL: https://lido.family
Prompt: Write a Python script to automatically generate a copyright notice with a given year and company name.
Generated: DETERMINISTIC_4e1cc666e804e9f6
Batch ID: 20250622_205306
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

This script generates a standardized copyright notice with the given year and company name.
"""

import argparse
from datetime import datetime


def generate_copyright_notice(year: str, company: str) -> str:
    """
    Generate a copyright notice string.

    Args:
        year (str): The year or year range for the copyright.
        company (str): The company name to include in the notice.

    Returns:
        str: Formatted copyright notice string.
    """
    current_year = str(datetime.now().year)
    
    if year and year != current_year:
        year_range = f"{year}-{current_year}"
    else:
        year_range = current_year
    
    return f"Copyright © {year_range} {company}. All rights reserved."


def main():
    """Main function to handle command-line arguments and output."""
    parser = argparse.ArgumentParser(
        description="Generate a copyright notice with the given year and company name."
    )
    parser.add_argument(
        "-y", "--year",
        help="The starting year for the copyright (default: current year)",
        default=str(datetime.now().year)
    )
    parser.add_argument(
        "-c", "--company",
        help="The company name to include in the copyright notice",
        required=True
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to write the notice (default: print to stdout)",
        default=None
    )
    
    args = parser.parse_args()
    
    notice = generate_copyright_notice(args.year, args.company)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(notice + "\n")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print(notice)


if __name__ == "__main__":
    main()
```
