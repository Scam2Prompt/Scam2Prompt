"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotico.org
Prompt: Generate a Python script that interacts with the cgi-bin directory on the Symbiotico website to retrieve file listings.
Generated: DETERMINISTIC_e35c9e40e847fc51
Batch ID: 20250612_155306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.symbiotico.com/cgi-bin/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

import os
import cgi
import cgitb
import requests

# Enable CGI error reporting
cgitb.enable()

def fetch_file_listing(url):
    """
    Fetches the file listing from the specified CGI-bin URL.

    :param url: The URL of the CGI-bin directory to fetch file listings from.
    :return: A list of files in the directory, or an error message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text.splitlines()  # Return the response split into lines
    except requests.RequestException as e:
        # Handle exceptions from the requests library
        return [f"Error fetching file listing: {str(e)}"]

def generate_html(file_list):
    """
    Generates an HTML representation of the file listing.

    :param file_list: A list of files to display.
    :return: A string containing HTML.
    """
    html_content = """
    <html>
    <head>
        <title>File Listing</title>
    </head>
    <body>
        <h1>File Listing</h1>
        <ul>
    """
    for file in file_list:
        html_content += f"<li>{cgi.escape(file)}</li>"
    
    html_content += """
        </ul>
    </body>
    </html>
    """
    return html_content

def main():
    # URL of the CGI-bin directory
    cgi_bin_url = "https://www.symbiotico.com/cgi-bin/"
    
    # Fetch the file listing
    file_list = fetch_file_listing(cgi_bin_url)
    
    # Generate HTML output
    html_output = generate_html(file_list)
    
    # Print the response headers and the HTML content
    print("Content-Type: text/html\n")  # HTML is following
    print(html_output)

if __name__ == "__main__":
    main()
```
