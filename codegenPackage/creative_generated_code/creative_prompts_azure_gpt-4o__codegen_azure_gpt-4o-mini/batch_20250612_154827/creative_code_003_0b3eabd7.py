"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Write code to automate the creation of a custom directory index page for LiteSpeed Web Server using Python.
Generated: DETERMINISTIC_0b3eabd744a30d6a
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

def generate_directory_index(directory_path, output_file):
    """
    Generate a custom directory index page for a specified directory.
    
    :param directory_path: Path to the directory for which to generate the index.
    :param output_file: Path to the output HTML file.
    """
    try:
        # Check if the specified directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Get the list of files and directories
        items = os.listdir(directory_path)

        # Start creating the HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {os.path.basename(directory_path)}</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        h1 {{ text-align: center; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 5px 0; }}
    </style>
</head>
<body>
    <h1>Index of {os.path.basename(directory_path)}</h1>
    <ul>"""

        # Populate the HTML with files and directories
        for item in items:
            item_path = os.path.join(directory_path, item)
            item_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
            html_content += f'\n        <li><a href="{item}">{item}</a> - Last Modified: {item_modified_time.strftime("%Y-%m-%d %H:%M:%S")}</li>'

        # Close the HTML tags
        html_content += """
    </ul>
</body>
</html>
"""
        # Write the HTML content to the output file
        with open(output_file, 'w') as file:
            file.write(html_content)

        print(f"Directory index created successfully: {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Example usage
    directory_to_index = "/path/to/your/directory"  # Change this to your target directory
    output_html_file = "index.html"  # Desired output HTML file name

    generate_directory_index(directory_to_index, output_html_file)
```

Make sure to replace `"/path/to/your/directory"` with the actual path of the directory you want to index. The code will generate an `index.html` file in the current working directory by default.
