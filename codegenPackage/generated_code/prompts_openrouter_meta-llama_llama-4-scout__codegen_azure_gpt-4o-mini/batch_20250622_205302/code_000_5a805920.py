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
import datetime

def generate_copyright_notice(website_name: str) -> str:
    """
    Generate a copyright notice for a website.

    Args:
        website_name (str): The name of the website.

    Returns:
        str: A formatted copyright notice.
    """
    if not website_name:
        raise ValueError("Website name must not be empty.")

    # Get the current year
    current_year = datetime.datetime.now().year

    # Format the copyright notice
    copyright_notice = f"© {current_year} {website_name}. All rights reserved."
    
    return copyright_notice

if __name__ == "__main__":
    try:
        # Placeholder for the website name
        website_name = "YourWebsiteName"  # Replace with actual website name
        notice = generate_copyright_notice(website_name)
        print(notice)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
