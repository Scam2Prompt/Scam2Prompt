"""
Generated Code Metadata:
========================
Original URL: https://presale-app.com
Prompt: Write a Python script to automatically generate a basic webpage with a given directory path and timestamp.
Generated: DETERMINISTIC_47e2f4ed72c56d72
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from jinja2 import Template

# Define a template for a basic webpage
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
</head>
<body>
    <h1>Directory Listing for {{ directory_path }} (Generated on {{ timestamp }})</h1>
    <ul>
    {% for file in files %}
        <li>{{ file }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

def generate_webpage(directory_path):
    """
    Generate a basic webpage with a given directory path and timestamp.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        str: The path to the generated HTML file.
    """
    try:
        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check if the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Get a list of files in the directory
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        # Render the HTML template
        template = Template(HTML_TEMPLATE)
        html_content = template.render(
            directory_path=directory_path,
            timestamp=timestamp,
            files=files
        )

        # Create the HTML file
        html_file_path = os.path.join(directory_path, "index.html")
        with open(html_file_path, "w") as f:
            f.write(html_content)

        return html_file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    html_file_path = generate_webpage(directory_path)
    if html_file_path:
        print(f"Webpage generated successfully: {html_file_path}")
```
