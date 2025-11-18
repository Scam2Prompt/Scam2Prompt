"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinfo.info
Prompt: Create a CGI script that generates an HTML page listing files in a directory, styled similarly to the "Index of /" format.
Generated: DETERMINISTIC_4df3b6fa753da22f
Batch ID: 20250612_154058
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

# Enable CGI error reporting
cgitb.enable()

# Set the directory to list
DIRECTORY = '.'  # Change this to the desired directory

def generate_file_listing(directory):
    """
    Generates an HTML page listing the files in the given directory.
    
    :param directory: The directory to list files from
    :return: HTML string containing file listing
    """
    try:
        # Get a list of files and directories in the specified directory
        items = os.listdir(directory)
        
        # Start building the HTML response
        html = "<html>\n"
        html += "<head><title>Index of {}</title></head>\n".format(directory)
        html += "<body>\n"
        html += "<h1>Index of {}</h1>\n".format(directory)
        html += "<hr>\n"
        html += "<ul>\n"

        for item in items:
            # Create a link for each item
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                html += '<li><a href="{}/">{}</a>/</li>\n'.format(item, item)
            else:
                html += '<li><a href="{}">{}</a></li>\n'.format(item, item)

        html += "</ul>\n"
        html += "<hr>\n"
        html += "</body>\n"
        html += "</html>\n"

        return html

    except Exception as e:
        return "<html><body><h1>Error</h1><p>{}</p></body></html>".format(e)

def main():
    """
    CGI main function to output the HTML file listing.
    """
    # Set the content type for the response
    print("Content-Type: text/html\n")
    
    # Generate the file listing HTML
    html_output = generate_file_listing(DIRECTORY)
    
    # Print the HTML output
    print(html_output)

if __name__ == '__main__':
    main()
```

Make sure to set the permissions of this script to be executable, and place it in your CGI-enabled directory on your web server. Also, adjust the `DIRECTORY` constant as needed to point to the directory you want to list files from.
