"""
Generated Code Metadata:
========================
Original URL: https://gala.red
Prompt: Generate a basic HTML page that displays a copyright notice for a given year and website, similar to what is seen on gala.red.
Generated: DETERMINISTIC_8293002315fc6a3b
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import date

def generate_copyright_notice(year=None, website=None):
    """
    Generate a basic HTML page that displays a copyright notice.

    Args:
        year (int): The year of the copyright notice. Defaults to the current year if not provided.
        website (str): The website name for the copyright notice.

    Returns:
        str: The HTML content for the copyright notice page.
    """

    # Use the current year if not provided
    if year is None:
        year = date.today().year

    # Check for required website name
    if website is None:
        raise ValueError("Website name is required")

    # Generate the HTML content
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Copyright Notice</title>
    </head>
    <body>
        <footer>
            <p>&copy; {year} {website}. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

    return html

def main():
    try:
        year = 2024  # Example year
        website = "Example Website"  # Example website
        html = generate_copyright_notice(year, website)
        print(html)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
