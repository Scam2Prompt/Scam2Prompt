"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.info
Prompt: What are the steps to delete or overwrite the automatically generated index.html page in a web project?
Generated: DETERMINISTIC_0789a7b5c0de57f5
Batch ID: 20250612_163135
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

def delete_or_overwrite_index_html(project_directory, new_content=None):
    """
    Deletes or overwrites the automatically generated index.html page in a web project.

    Parameters:
    project_directory (str): The path to the web project directory.
    new_content (str, optional): The new content to write to index.html. 
                                 If None, the file will be deleted. 

    Raises:
    FileNotFoundError: If the index.html file does not exist in the specified directory.
    Exception: For any other errors encountered during the operation.
    """

    # Define the path to the index.html file
    index_path = os.path.join(project_directory, 'index.html')

    try:
        if new_content is None:
            # Check if the file exists before attempting to delete it
            if os.path.exists(index_path):
                os.remove(index_path)
                print(f"Successfully deleted {index_path}")
            else:
                print(f"{index_path} does not exist.")
        else:
            # Write new content to index.html
            with open(index_path, 'w') as file:
                file.write(new_content)
                print(f"Successfully overwritten {index_path} with new content.")
    
    except FileNotFoundError:
        print(f"Error: {index_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# delete_or_overwrite_index_html('/path/to/your/project', new_content='<html><body><h1>Hello, World!</h1></body></html>')
# delete_or_overwrite_index_html('/path/to/your/project')  # Call with None to delete
```
