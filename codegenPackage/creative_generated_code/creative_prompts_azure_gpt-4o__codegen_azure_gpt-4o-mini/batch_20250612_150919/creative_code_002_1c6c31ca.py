"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Generate a Python script to detect and delete the default `index.html` file in the root directory of a newly created website.
Generated: DETERMINISTIC_1c6c31caa7f12e5e
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def delete_default_index_html(root_directory):
    """
    Deletes the default 'index.html' file in the specified root directory if it exists.

    Args:
        root_directory (str): The path to the root directory of the website.

    Raises:
        FileNotFoundError: If the specified root directory does not exist.
        Exception: For any other errors that may occur during file deletion.
    """
    # Construct the path for the default index.html file
    index_file_path = os.path.join(root_directory, 'index.html')
    
    try:
        # Check if the root directory exists
        if not os.path.exists(root_directory):
            raise FileNotFoundError(f"The specified root directory '{root_directory}' does not exist.")

        # Check if the index.html file exists
        if os.path.isfile(index_file_path):
            # Delete the index.html file
            os.remove(index_file_path)
            print(f"Deleted: {index_file_path}")
        else:
            print(f"No default index.html file found in: {root_directory}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage: replace 'path/to/your/website' with the actual path
    website_root = 'path/to/your/website'
    delete_default_index_html(website_root)
```
