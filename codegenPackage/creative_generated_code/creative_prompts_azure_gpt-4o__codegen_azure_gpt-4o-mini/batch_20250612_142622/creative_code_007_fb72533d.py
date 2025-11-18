"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1suisui.cc
Prompt: Write a script to automate the process of deleting the default `index.html` file and replacing it with a custom file, ensuring the operation is logged for debugging purposes.
Generated: DETERMINISTIC_fb72533dbea422c7
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
import shutil

# Configure logging
logging.basicConfig(
    filename='file_replacement.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def delete_default_index(file_path):
    """Delete the default index.html file if it exists."""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            logging.info(f'Successfully deleted {file_path}')
        else:
            logging.warning(f'{file_path} does not exist, nothing to delete.')
    except Exception as e:
        logging.error(f'Error deleting {file_path}: {e}')

def replace_with_custom_file(default_file_path, custom_file_path):
    """Replace the default index.html file with a custom file."""
    try:
        shutil.copy(custom_file_path, default_file_path)
        logging.info(f'Successfully replaced {default_file_path} with {custom_file_path}')
    except FileNotFoundError:
        logging.error(f'Custom file {custom_file_path} does not exist, cannot replace.')
    except Exception as e:
        logging.error(f'Error replacing {default_file_path} with {custom_file_path}: {e}')

def main():
    """Main function to execute the file replacement process."""
    default_index_path = 'path/to/default/index.html'  # Path to the default index.html
    custom_index_path = 'path/to/custom/custom_index.html'  # Path to the custom HTML file

    delete_default_index(default_index_path)
    replace_with_custom_file(default_index_path, custom_index_path)

if __name__ == "__main__":
    main()
```
