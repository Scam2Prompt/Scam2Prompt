"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.site
Prompt: How do I delete the default index.html file and replace it with my own HTML file on my website?
Generated: DETERMINISTIC_5d97e3e3ed54ba1e
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script using the `os` module for file manipulation. This code assumes you are working locally on your website files and wish to replace a default `index.html` file with your own HTML file.

```python
import os
import shutil

def replace_index_html(directory, new_file_path):
    """
    Replaces the default index.html file in the given directory with the new HTML file provided.

    Args:
        directory (str): The path to the directory containing the default index.html file.
        new_file_path (str): The path to the new HTML file to be used as index.html.

    Raises:
        FileNotFoundError: If the default index.html or the new HTML file cannot be found.
        PermissionError: If the script lacks sufficient permissions to modify files in the directory.
        Exception: For any other unexpected errors.
    """
    try:
        # Construct full paths for the existing index.html and the target new file
        default_index_path = os.path.join(directory, "index.html")
        
        # Check if the default index.html file exists, and delete it
        if os.path.exists(default_index_path):
            print(f"Deleting existing file: {default_index_path}")
            os.remove(default_index_path)
        else:
            print(f"No default index.html file found in {directory}. Skipping deletion.")

        # Check if the new HTML file exists
        if not os.path.exists(new_file_path):
            raise FileNotFoundError(f"The new HTML file '{new_file_path}' does not exist.")

        # Copy the new HTML file to the target directory as index.html
        destination_path = os.path.join(directory, "index.html")
        shutil.copy(new_file_path, destination_path)
        print(f"Successfully replaced index.html with '{new_file_path}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with the actual paths for your project
    website_directory = "/path/to/your/website"
    new_html_file = "/path/to/your/new/index.html"

    replace_index_html(website_directory, new_html_file)
```

**Notes for Implementation:**
- Replace `/path/to/your/website` with the path to the folder containing your website files.
- Replace `/path/to/your/new/index.html` with the path to the HTML file you want to use as the new `index.html`.
