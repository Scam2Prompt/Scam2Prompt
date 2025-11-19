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
from datetime import datetime

def generate_webpage(directory_path):
    """
    Generates a basic HTML webpage with a list of files in the given directory
    and a timestamp indicating when the page was generated.

    Args:
        directory_path (str): Path to the directory to list files from.

    Returns:
        str: The HTML content as a string.
    """
    try:
        # Validate the directory path
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # Get the list of files in the directory
        files = os.listdir(directory_path)

        # Generate the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Start building the HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin: 5px 0;
        }}
        .timestamp {{
            font-size: 0.9em;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <p class="timestamp">Generated on: {timestamp}</p>
    <ul>
"""
        # Add each file to the HTML list
        for file in files:
            html_content += f"        <li>{file}</li>\n"

        # Close the HTML tags
        html_content += """    </ul>
</body>
</html>
"""

        return html_content

    except Exception as e:
        # Handle any errors and return a meaningful message
        return f"<html><body><h1>Error</h1><p>{str(e)}</p></body></html>"


def save_webpage(html_content, output_path):
    """
    Saves the generated HTML content to a file.

    Args:
        html_content (str): The HTML content to save.
        output_path (str): Path to the output HTML file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Webpage successfully saved to {output_path}")
    except Exception as e:
        print(f"Failed to save webpage: {str(e)}")


if __name__ == "__main__":
    # Example usage
    directory_path = input("Enter the directory path: ").strip()
    output_path = input("Enter the output HTML file path: ").strip()

    # Generate the webpage content
    html_content = generate_webpage(directory_path)

    # Save the webpage to the specified file
    save_webpage(html_content, output_path)
```
