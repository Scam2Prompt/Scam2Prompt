"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Can you explain how to access and utilize the cgi-bin resources listed on refconegypt.net?
Generated: DETERMINISTIC_c0a255f64acb6b63
Batch ID: 20250612_160720
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

# Set the content-type header for HTTP response
print("Content-Type: text/html;charset=utf-8")
print()  # Blank line to end the headers

# Define a function to access CGI resources
def access_cgi_resources():
    # The directory where CGI scripts are located
    cgi_bin_dir = '/path/to/cgi-bin/'  # Update with actual path if necessary

    try:
        # List all files in the cgi-bin directory
        resources = os.listdir(cgi_bin_dir)

        # Filter out only executable files (CGI scripts)
        cgi_scripts = [f for f in resources if os.access(os.path.join(cgi_bin_dir, f), os.X_OK)]
        
        # Generate HTML output
        print("<html>")
        print("<head><title>CGI Resources</title></head>")
        print("<body>")
        print("<h1>Available CGI Scripts</h1>")
        
        if cgi_scripts:
            print("<ul>")
            for script in cgi_scripts:
                print(f"<li>{script}</li>")
            print("</ul>")
        else:
            print("<p>No CGI scripts found in the cgi-bin directory.</p>")
        
        print("</body>")
        print("</html>")

    except OSError as e:
        # Handle directory access errors
        print("<html>")
        print("<head><title>Error</title></head>")
        print("<body>")
        print(f"<h1>Error accessing CGI resources</h1>")
        print(f"<p>{str(e)}</p>")
        print("</body>")
        print("</html>")

# Run the function to access CGI resources
if __name__ == '__main__':
    access_cgi_resources()
```
