"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Can you provide a code snippet for creating a CGI script in Python?
Generated: DETERMINISTIC_1c3408d917b3496f
Batch ID: 20250612_160720
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://yourserver/cgi-bin/cgi_example.py?name=John&age=30`": {
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

# Import necessary modules
import os
import sys
import cgi
import cgitb

# Enable CGI traceback for debugging (useful during development)
# Should be disabled in production for security reasons.
cgitb.enable()

def main():
    try:
        # Set the content type to HTML
        print("Content-Type: text/html\n")

        # Parse CGI input
        form = cgi.FieldStorage()

        # Retrieve parameters (example: 'name' and 'age')
        name = form.getvalue("name", "Guest")  # Default to 'Guest' if not provided
        age = form.getvalue("age", "Unknown")  # Default to 'Unknown' if not provided

        # Construct the HTML response
        print("<html>")
        print("<head><title>CGI Script Example</title></head>")
        print("<body>")
        print(f"<h1>Welcome, {name}!</h1>")
        print(f"<p>Your age is: {age}</p>")
        print("</body>")
        print("</html>")
    except Exception as e:
        # Handle unexpected errors gracefully
        print("Content-Type: text/plain\n")
        print("An error occurred while processing your request.")
        print(f"Error details: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()
```

To run this script:
1. Save it as a `.py` file (e.g., `cgi_example.py`).
2. Place it in the `cgi-bin` directory of your web server.
3. Ensure the file is executable (`chmod +x cgi_example.py`).
4. Navigate to the script in a web browser and pass query parameters (e.g., `http://yourserver/cgi-bin/cgi_example.py?name=John&age=30`).
