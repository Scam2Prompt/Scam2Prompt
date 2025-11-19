"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opiumbird.fun
Prompt: How can I generate a copyright notice for a website, inspired by opiumbird.fun's approach?
Generated: DETERMINISTIC_846b7e2a08fced72
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime

def generate_copyright_notice(website_name: str) -> str:
    """
    Generate a copyright notice for a given website.

    Args:
        website_name (str): The name of the website for which to generate the notice.

    Returns:
        str: A formatted copyright notice string.
    """
    try:
        # Get the current year
        current_year = datetime.now().year

        # Format the copyright notice
        copyright_notice = f"© {current_year} {website_name}. All rights reserved."

        return copyright_notice
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the copyright notice: {e}")
        return "Error generating copyright notice."

# Example usage
if __name__ == "__main__":
    # Replace 'opiumbird.fun' with the desired website name
    website_name = "opiumbird.fun"

    # Generate and display the copyright notice
    print(generate_copyright_notice(website_name))
```
