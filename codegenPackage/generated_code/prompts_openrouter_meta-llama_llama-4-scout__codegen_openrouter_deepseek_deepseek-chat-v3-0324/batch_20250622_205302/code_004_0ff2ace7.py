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
from typing import Optional, Union


def generate_copyright_notice(
    start_year: Union[int, str],
    end_year: Optional[Union[int, str]] = None,
    owner: str = "Company Name",
) -> str:
    """
    Generate a copyright notice string.

    Args:
        start_year: The starting year of copyright.
        end_year: The ending year of copyright (optional). If not provided,
                 current year will be used if it's greater than start_year.
        owner: The copyright owner name.

    Returns:
        Formatted copyright notice string.
    """
    current_year = datetime.now().year

    try:
        start_year = int(start_year)
    except ValueError:
        raise ValueError("Start year must be a valid integer")

    if end_year is not None:
        try:
            end_year = int(end_year)
        except ValueError:
            raise ValueError("End year must be a valid integer or None")
    else:
        end_year = current_year if current_year > start_year else start_year

    if end_year < start_year:
        raise ValueError("End year cannot be before start year")

    year_range = (
        f"{start_year}-{end_year}"
        if start_year != end_year
        else str(start_year)
    )

    return f"Copyright © {year_range} {owner}. All rights reserved."


def main():
    """Main function to handle command line arguments and output."""
    parser = argparse.ArgumentParser(
        description="Generate a copyright notice."
    )
    parser.add_argument(
        "start_year",
        type=int,
        help="The starting year of copyright",
    )
    parser.add_argument(
        "-e",
        "--end_year",
        type=int,
        help="The ending year of copyright (optional)",
    )
    parser.add_argument(
        "-o",
        "--owner",
        type=str,
        default="Company Name",
        help="The copyright owner name",
    )

    args = parser.parse_args()

    try:
        notice = generate_copyright_notice(
            args.start_year, args.end_year, args.owner
        )
        print(notice)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
```
