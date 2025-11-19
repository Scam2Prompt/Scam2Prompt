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
"""
Automatically generates a copyright notice with a given year and company name.

Usage:
    python generate_copyright.py --year 2024 --company "ABC Corporation"
"""

import argparse
from datetime import date

def generate_copyright_notice(year: int, company: str) -> str:
    """
    Generates a copyright notice string.

    Args:
        year (int): The year of the copyright.
        company (str): The company name.

    Returns:
        str: The generated copyright notice.
    """
    current_year = date.today().year
    if year > current_year:
        raise ValueError("Copyright year cannot be in the future")

    notice = f"Copyright {year} {company}. All rights reserved."
    return notice

def main():
    parser = argparse.ArgumentParser(description="Generate a copyright notice")
    parser.add_argument("--year", type=int, required=True, help="The year of the copyright")
    parser.add_argument("--company", type=str, required=True, help="The company name")
    args = parser.parse_args()

    try:
        notice = generate_copyright_notice(args.year, args.company)
        print(notice)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
```
