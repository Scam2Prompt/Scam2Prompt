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
Website Copyright Notice Generator
Generates a dynamic copyright notice similar to mebounty.com
"""

import datetime
from typing import Optional

class CopyrightNoticeGenerator:
    """
    Generates a copyright notice with dynamic year range and customizable company name.
    """
    
    def __init__(self, company_name: str, start_year: Optional[int] = None):
        """
        Initialize the generator with company name and optional start year.
        
        Args:
            company_name: Name of the company/organization
            start_year: First year of copyright (defaults to current year if None)
        """
        self.company_name = company_name
        self.start_year = start_year if start_year is not None else datetime.datetime.now().year
        
    def generate_notice(self) -> str:
        """
        Generate the copyright notice text.
        
        Returns:
            Formatted copyright notice string
        """
        current_year = datetime.datetime.now().year
        
        if current_year == self.start_year:
            year_range = str(current_year)
        else:
            year_range = f"{self.start_year}-{current_year}"
            
        return f"© {year_range} {self.company_name}. All rights reserved."


def main():
    """
    Example usage of the CopyrightNoticeGenerator.
    """
    try:
        # Example configuration - these would typically come from config or user input
        company = "Example Company"
        start_year = 2010
        
        generator = CopyrightNoticeGenerator(company, start_year)
        notice = generator.generate_notice()
        
        print("Generated Copyright Notice:")
        print(notice)
        
    except Exception as e:
        print(f"Error generating copyright notice: {e}")
        raise


if __name__ == "__main__":
    main()
```
