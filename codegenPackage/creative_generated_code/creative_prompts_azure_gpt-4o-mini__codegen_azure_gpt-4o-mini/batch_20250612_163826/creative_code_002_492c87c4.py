"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groupists.com
Prompt: How can I implement a CGI script to manage file listings in a directory structure as seen on groupists.com?
Generated: DETERMINISTIC_492c87c49d6d2c61
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

import os
import cgi
import cgitb
from urllib.parse import quote

# Enable CGI error reporting
cgitb.enable()

# Constants for the base directory
BASE_DIR = '/path/to/your/directory'  # Change to your directory path

def escape_html(text):
    """Escape HTML special characters in a string."""
    return (cgi.escape(text) if text else '')

def list_files(directory):
    """List files and directories in the specified directory."""
    try:
        # Get the list of files and directories
        items = os.listdir(directory)
        items.sort()  # Sort the items alphabetically
        return items
    except OSError as e:
        print(f"Error accessing directory: {e}")
        return []

def generate_file_listing(directory):
    """Generate HTML for the file listing in the specified directory."""
    items = list_files(directory)
    html = '<h1>File Listing</h1><ul>'
    
    for item in items:
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            html += f'<li><b>{escape_html(item)}</b> (Directory)</li>'
        else:
            encoded_item = quote(item)
            html += f'<li><a href="{encoded_item}">{escape_html(item)}</a></li>'
    
    html += '</ul>'
    return html

def main():
    """Main function to generate the CGI response for file listing."""
    # Set the content type for the response
    print("Content-Type: text/html")
    print()  # Important: print a blank line after the headers

    # Determine the current directory to list
    current_dir = BASE_DIR

    # Generate the HTML output
    output_html = generate_file_listing(current_dir)

    # Print the HTML output
    print(output_html)

if __name__ == "__main__":
    main()
```

**Note:** 
- Ensure to replace `'/path/to/your/directory'` with the actual directory path you want to list.
- Make sure that the web server has the necessary permissions to access the specified directory and execute the CGI script.
- This script should be placed in the appropriate CGI-bin directory of your web server and given executable permissions (e.g., `chmod +x script.py`).
