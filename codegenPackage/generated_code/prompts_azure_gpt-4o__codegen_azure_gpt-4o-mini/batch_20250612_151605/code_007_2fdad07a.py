"""
Generated Code Metadata:
========================
Original URL: https://initia.org.in
Prompt: Write a CGI script in Python that outputs an HTML page listing the contents of a directory, including file names and last modified dates.
Generated: DETERMINISTIC_2fdad07abe37e581
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import os
import cgi
import datetime

# Set the content type to HTML
print("Content-Type: text/html")
print()  # End of headers

# Function to format the last modified date
def format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Function to generate the HTML page
def generate_html(directory):
    try:
        # List the contents of the directory
        files = os.listdir(directory)
    except OSError as e:
        # Handle errors in accessing the directory
        return f"<h1>Error accessing directory: {e}</h1>"

    # Start building the HTML content
    html_content = """
    <html>
    <head>
        <title>Directory Listing</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Directory Listing</h1>
        <table>
            <tr>
                <th>File Name</th>
                <th>Last Modified</th>
            </tr>
    """

    # Populate the table with file names and last modified dates
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        try:
            last_modified = format_date(os.path.getmtime(file_path))
            html_content += f"""
            <tr>
                <td>{cgi.escape(file_name)}</td>
                <td>{last_modified}</td>
            </tr>
            """
        except OSError as e:
            # Handle errors in getting file information
            html_content += f"""
            <tr>
                <td>{cgi.escape(file_name)}</td>
                <td>Error: {e}</td>
            </tr>
            """

    # Close the table and HTML tags
    html_content += """
        </table>
    </body>
    </html>
    """

    return html_content

# Get the current directory or use a specified one
directory = os.getcwd()  # Change this to a specific path if needed
html_output = generate_html(directory)

# Print the final HTML output
print(html_output)
```
