"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: Write code to overwrite the default `index.html` file in the root directory of a newly created website with custom HTML content.
Generated: DETERMINISTIC_cda79d02888a99c3
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def create_website_with_custom_index(directory: str, custom_content: str) -> None:
    """
    Creates a new website directory and overwrites the default index.html file 
    with custom HTML content.

    Args:
        directory (str): The path to the new website directory.
        custom_content (str): The custom HTML content to be written to index.html.

    Raises:
        OSError: If the directory cannot be created.
        IOError: If the index.html file cannot be written.
    """
    try:
        # Create the website directory
        os.makedirs(directory, exist_ok=True)

        # Path for the index.html file
        index_file_path = os.path.join(directory, 'index.html')

        # Write custom content to index.html
        with open(index_file_path, 'w') as index_file:
            index_file.write(custom_content)

        print(f"Successfully created index.html in {directory}")

    except OSError as e:
        print(f"Error creating directory: {e}")
    
    except IOError as e:
        print(f"Error writing to index.html: {e}")

# Example usage
if __name__ == "__main__":
    custom_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Custom Website</title>
</head>
<body>
    <h1>Welcome to My Custom Website!</h1>
    <p>This is a sample index.html file with custom content.</p>
</body>
</html>"""

    # Specify the directory for the new website
    website_directory = './my_custom_website'

    # Create the website with custom index.html
    create_website_with_custom_index(website_directory, custom_html_content)
```
