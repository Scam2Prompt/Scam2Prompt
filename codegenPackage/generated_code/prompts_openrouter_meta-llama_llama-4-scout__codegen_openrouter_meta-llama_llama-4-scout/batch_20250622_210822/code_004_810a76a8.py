"""
Generated Code Metadata:
========================
Original URL: https://mebounty.com
Prompt: Write a Python script to automatically generate a copyright notice for a website, similar to the one on mebounty.com.
Generated: DETERMINISTIC_810a76a83f9e3790
Batch ID: 20250622_210822
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
Generate a copyright notice for a website.

This script generates a copyright notice similar to the one on mebounty.com.
It takes into account the current year and the provided company name.

Usage:
    python generate_copyright_notice.py --company_name "Company Name"

Author:
    [Your Name]
"""

import argparse
from datetime import date

def generate_copyright_notice(company_name: str) -> str:
    """
    Generate a copyright notice.

    Args:
        company_name (str): The name of the company.

    Returns:
        str: The generated copyright notice.
    """
    current_year = date.today().year
    notice = f"Copyright {current_year} {company_name}. All rights reserved."
    return notice

def main():
    parser = argparse.ArgumentParser(description="Generate a copyright notice.")
    parser.add_argument("--company_name", type=str, required=True, help="The name of the company.")
    args = parser.parse_args()

    try:
        company_name = args.company_name.strip()
        if not company_name:
            raise ValueError("Company name cannot be empty.")
        notice = generate_copyright_notice(company_name)
        print(notice)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
```
