"""
Generated Code Metadata:
========================
Original URL: https://icopages.pw
Prompt: Write a Python script to auto-generate an index.html page for a newly created website, similar to the functionality described on https://icopages.pw.
Generated: DETERMINISTIC_6a103126dd59f2de
Batch ID: 20250622_211215
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
Auto-generate an index.html page for a newly created website.

This script creates a basic HTML5 template with responsive design,
meta tags, and a simple structure that can be customized later.

Usage:
    python generate_index.py [output_path]
"""

import os
import sys
from datetime import datetime

DEFAULT_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{site_title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
        }}
        header, footer {{
            text-align: center;
            padding: 20px 0;
        }}
        nav ul {{
            list-style-type: none;
            padding: 0;
        }}
        nav ul li {{
            display: inline;
            margin: 0 10px;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{site_title}</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Welcome to {site_title}</h2>
            <p>This is a placeholder page for your new website. Edit this file to add your own content.</p>
        </section>
    </main>

    <footer>
        <p>&copy; {year} {site_title}. All rights reserved.</p>
    </footer>
</body>
</html>
"""

def generate_index_html(output_path="index.html", site_title="My Website"):
    """
    Generate a basic index.html file with the given parameters.
    
    Args:
        output_path (str): Path to save the generated HTML file.
        site_title (str): Title of the website.
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Generate the HTML content
        html_content = DEFAULT_HTML_TEMPLATE.format(
            site_title=site_title,
            year=datetime.now().year
        )
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Successfully generated {output_path}")
        
    except OSError as e:
        print(f"Error creating file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Parse command line arguments
    output_path = "index.html"
    site_title = "My Website"
    
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    if len(sys.argv) > 2:
        site_title = " ".join(sys.argv[2:])
    
    generate_index_html(output_path, site_title)
```
