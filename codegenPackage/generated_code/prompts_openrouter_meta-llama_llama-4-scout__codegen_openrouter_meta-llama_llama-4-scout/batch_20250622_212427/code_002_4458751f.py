"""
Generated Code Metadata:
========================
Original URL: https://peptok.site
Prompt: Write a Python script to automate the creation of a basic webpage with a copyright notice for a given year.
Generated: DETERMINISTIC_4458751ffd273da4
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to automate the creation of a basic webpage with a copyright notice.

Usage:
    python create_webpage.py <year> <output_file>

Args:
    year (int): The year for the copyright notice.
    output_file (str): The filename for the generated webpage.

Example:
    python create_webpage.py 2024 index.html
"""

import sys
import argparse

def create_webpage(year, output_file):
    """
    Creates a basic webpage with a copyright notice.

    Args:
        year (int): The year for the copyright notice.
        output_file (str): The filename for the generated webpage.

    Returns:
        None
    """
    try:
        # Check if year is a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")

        # Define the HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Webpage</title>
</head>
<body>
    <p>&copy; {year} All rights reserved.</p>
</body>
</html>
"""

        # Write the HTML content to the output file
        with open(output_file, 'w') as f:
            f.write(html_content)

        print(f"Webpage created successfully: {output_file}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Create a basic webpage with a copyright notice.")
    parser.add_argument("year", type=int, help="The year for the copyright notice.")
    parser.add_argument("output_file", type=str, help="The filename for the generated webpage.")
    args = parser.parse_args()

    create_webpage(args.year, args.output_file)

if __name__ == "__main__":
    main()
```
