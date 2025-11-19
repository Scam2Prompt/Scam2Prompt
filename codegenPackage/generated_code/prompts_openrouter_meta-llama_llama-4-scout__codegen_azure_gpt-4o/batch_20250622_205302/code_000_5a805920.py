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

def generate_copyright_notice(website_name):
    """
    Generates a copyright notice for a website.

    Args:
        website_name (str): The name of the website.

    Returns:
        str: A formatted copyright notice.
    """
    try:
        # Get the current year
        current_year = datetime.datetime.now().year
        
        # Validate the website name
        if not website_name or not isinstance(website_name, str):
            raise ValueError("Invalid website name. It must be a non-empty string.")
        
        # Generate the copyright notice
        copyright_notice = f"© {current_year} {website_name}. All rights reserved."
        return copyright_notice
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error generating copyright notice: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace 'YourWebsiteName' with the actual name of your website
    website_name = "YourWebsiteName"
    print(generate_copyright_notice(website_name))
```
