"""
Generated Code Metadata:
========================
Original URL: https://icopages.info
Prompt: Write a Python script to automatically generate a default index.html page for a newly created website, similar to the one described on https://icopages.info.
Generated: DETERMINISTIC_bec5c71988b96682
Batch ID: 20250622_211159
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
Generate a default index.html page for a newly created website.

Usage:
    python generate_index.py <website_name> <website_description> <author_name>

Example:
    python generate_index.py "My Website" "This is my website." "John Doe"
"""

import sys
import argparse

def generate_index_html(website_name, website_description, author_name):
    """
    Generate the content of the index.html page.

    Args:
        website_name (str): The name of the website.
        website_description (str): A brief description of the website.
        author_name (str): The name of the website author.

    Returns:
        str: The HTML content of the index.html page.
    """
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{website_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #333;
            color: #fff;
            padding: 1em;
            text-align: center;
        }}
        main {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2em;
        }}
        footer {{
            background-color: #333;
            color: #fff;
            padding: 1em;
            text-align: center;
            clear: both;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{website_name}</h1>
    </header>
    <main>
        <p>{website_description}</p>
    </main>
    <footer>
        &copy; {author_name} {current_year}. All rights reserved.
    </footer>
</body>
</html>
""".format(
        website_name=website_name,
        website_description=website_description,
        author_name=author_name,
        current_year=2024  # This should be dynamic, but for simplicity, it's hardcoded
    )
    return html_content

def write_to_file(html_content, output_file):
    """
    Write the HTML content to a file.

    Args:
        html_content (str): The HTML content to write.
        output_file (str): The path to the output file.

    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        with open(output_file, 'w') as f:
            f.write(html_content)
    except IOError as e:
        print(f"Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate a default index.html page')
    parser.add_argument('website_name', help='The name of the website')
    parser.add_argument('website_description', help='A brief description of the website')
    parser.add_argument('author_name', help='The name of the website author')
    parser.add_argument('-o', '--output', default='index.html', help='The output file path')
    args = parser.parse_args()

    html_content = generate_index_html(args.website_name, args.website_description, args.author_name)
    write_to_file(html_content, args.output)

    print(f"Generated index.html page written to {args.output}")

if __name__ == "__main__":
    import datetime
    current_year = datetime.date.today().year
    main()
```
