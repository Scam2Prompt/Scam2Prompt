"""
Generated Code Metadata:
========================
Original URL: https://questsmisten.space
Prompt: Write a Python script to generate a copyright notice for a website, including the current year and a placeholder for the website name.
Generated: DETERMINISTIC_5a805920299d2c34
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
Generates a copyright notice for a website with current year and website name.
"""

import datetime
from typing import Optional

def generate_copyright_notice(website_name: str, start_year: Optional[int] = None) -> str:
    """
    Generates a copyright notice string.
    
    Args:
        website_name: Name of the website to include in the notice
        start_year: Optional start year for copyright range. If None, uses current year only.
    
    Returns:
        Formatted copyright notice string
    """
    current_year = datetime.datetime.now().year
    
    if start_year is not None and start_year != current_year:
        year_str = f"{start_year}-{current_year}"
    else:
        year_str = str(current_year)
    
    return f"© {year_str} {website_name}. All rights reserved."

if __name__ == "__main__":
    try:
        website = input("Enter website name: ").strip()
        if not website:
            raise ValueError("Website name cannot be empty")
            
        year_input = input("Enter start year (leave blank for current year only): ").strip()
        start_year = int(year_input) if year_input else None
        
        notice = generate_copyright_notice(website, start_year)
        print("\nGenerated Copyright Notice:")
        print(notice)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
