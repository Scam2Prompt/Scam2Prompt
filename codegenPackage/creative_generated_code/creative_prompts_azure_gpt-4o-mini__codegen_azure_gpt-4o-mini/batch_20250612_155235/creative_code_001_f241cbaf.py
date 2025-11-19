"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inovarerep.com.br
Prompt: What steps should I follow to change the content of a webpage hosted in the public_html directory?
Generated: DETERMINISTIC_f241cbafe083e1f3
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil

def update_webpage(file_name, new_content, public_html_dir='public_html'):
    """
    Update the content of a webpage in the specified directory.

    :param file_name: Name of the HTML file to be updated
    :param new_content: New content to be written to the HTML file
    :param public_html_dir: Directory where the HTML files are hosted (default is 'public_html')
    :raises ValueError: If the file_name does not end with '.html'
    :raises FileNotFoundError: If the specified HTML file does not exist
    :raises IOError: If there is an error writing to the file
    """

    # Validate the file name
    if not file_name.endswith('.html'):
        raise ValueError("The file name must end with '.html'.")

    # Construct the full path to the HTML file
    file_path = os.path.join(public_html_dir, file_name)

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_name}' does not exist in '{public_html_dir}'.")

    # Backup the existing file before updating
    backup_path = file_path + '.bak'
    shutil.copyfile(file_path, backup_path)

    try:
        # Write the new content to the HTML file
        with open(file_path, 'w') as html_file:
            html_file.write(new_content)
    except IOError as e:
        # Restore the backup if there was an error writing to the file
        shutil.copyfile(backup_path, file_path)
        raise IOError(f"Error writing to the file '{file_name}': {e}")
    finally:
        # Remove the backup file if everything went smoothly
        if os.path.exists(backup_path):
            os.remove(backup_path)

# Example usage
if __name__ == "__main__":
    try:
        update_webpage('index.html', '<html><body><h1>New Content!</h1></body></html>')
        print("Webpage updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
