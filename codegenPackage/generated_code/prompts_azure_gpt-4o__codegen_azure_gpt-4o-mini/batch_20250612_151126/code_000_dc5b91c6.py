"""
Generated Code Metadata:
========================
Original URL: https://elmensajero.e-kraken.net
Prompt: Write a Python script to interact with a CGI-bin directory on a server, using the structure described in the webpage.
Generated: DETERMINISTIC_dc5b91c6ab7051da
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import os
import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

# Set the content type to HTML
print("Content-Type: text/html")
print()  # End of headers

def list_cgi_bin_files(directory):
    """
    List all files in the specified CGI-bin directory.

    Args:
        directory (str): The path to the CGI-bin directory.

    Returns:
        list: A list of filenames in the directory.
    """
    try:
        # List all files in the directory
        files = os.listdir(directory)
        # Filter for files that are executable scripts
        cgi_files = [f for f in files if f.endswith('.py') or f.endswith('.pl')]
        return cgi_files
    except OSError as e:
        print(f"<h2>Error accessing directory: {e}</h2>")
        return []

def main():
    # Define the path to the CGI-bin directory
    cgi_bin_directory = '/path/to/cgi-bin'  # Update this path as necessary

    # List CGI files
    cgi_files = list_cgi_bin_files(cgi_bin_directory)

    # Generate HTML output
    print("<html>")
    print("<head><title>CGI-bin Directory Listing</title></head>")
    print("<body>")
    print("<h1>CGI-bin Directory Listing</h1>")
    
    if cgi_files:
        print("<ul>")
        for file in cgi_files:
            print(f"<li>{file}</li>")
        print("</ul>")
    else:
        print("<p>No CGI scripts found.</p>")
    
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
```

**Note:** Make sure to update the `cgi_bin_directory` variable with the correct path to your CGI-bin directory before running the script.
