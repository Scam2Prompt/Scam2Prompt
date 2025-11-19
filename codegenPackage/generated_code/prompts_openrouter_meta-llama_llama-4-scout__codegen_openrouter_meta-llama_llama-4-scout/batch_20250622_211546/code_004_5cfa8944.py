"""
Generated Code Metadata:
========================
Original URL: https://cybersamurai.live
Prompt: Create a script that automatically updates the "last modified" date and time on a webpage, like the "Created at: Sun Oct 27 20:01:57 2024" shown on cybersamurai.live.
Generated: DETERMINISTIC_5cfa89447fc39966
Batch ID: 20250622_211546
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
import re

def update_last_modified_date(file_path):
    """
    Updates the 'last modified' date and time on a webpage.

    Args:
        file_path (str): The path to the webpage file.

    Returns:
        None
    """

    try:
        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%a %b %d %H:%M:%S %Y")

        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()

        # Use regular expression to find and replace the 'last modified' date and time
        pattern = r"Created at:.*"
        replacement = f"Created at: {formatted_datetime}"
        updated_content = re.sub(pattern, replacement, content)

        # If no 'last modified' date and time found, append it to the content
        if updated_content == content:
            updated_content = f"Created at: {formatted_datetime}\n" + content

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Last modified date and time updated successfully in {file_path}")

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = "path_to_your_webpage_file.html"  # replace with your webpage file path
    update_last_modified_date(file_path)
```
