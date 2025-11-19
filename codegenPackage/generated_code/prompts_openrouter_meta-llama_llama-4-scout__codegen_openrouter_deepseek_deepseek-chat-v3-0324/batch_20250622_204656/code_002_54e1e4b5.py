"""
Generated Code Metadata:
========================
Original URL: https://opeansea.godaddysites.com
Prompt: Generate a simple copyright notice in Python that outputs the current year and a company name, similar to " 2023 Opean Sea" found on the website.
Generated: DETERMINISTIC_54e1e4b5ae2ca5e3
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_copyright_notice(company_name):
    """
    Generates a copyright notice with the current year and company name.
    
    Args:
        company_name (str): The name of the company to include in the notice.
    
    Returns:
        str: Formatted copyright notice string.
    """
    current_year = datetime.datetime.now().year
    return f"© {current_year} {company_name}"

# Example usage
if __name__ == "__main__":
    company = "Open Sea"
    notice = generate_copyright_notice(company)
    print(notice)
```
