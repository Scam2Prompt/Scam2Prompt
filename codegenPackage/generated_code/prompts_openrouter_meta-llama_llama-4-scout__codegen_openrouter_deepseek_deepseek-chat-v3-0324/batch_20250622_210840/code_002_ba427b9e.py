"""
Generated Code Metadata:
========================
Original URL: https://kubiccex.com
Prompt: "Generate a CGI-bin script to retrieve server information, including the web server software and port number."
Generated: DETERMINISTIC_ba427b9e02290d51
Batch ID: 20250622_210840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import cgi
import os
import sys

def get_server_info():
    """Retrieve and return server information as a dictionary."""
    server_info = {
        'server_software': os.environ.get('SERVER_SOFTWARE', 'UNKNOWN'),
        'server_port': os.environ.get('SERVER_PORT', 'UNKNOWN'),
        'server_name': os.environ.get('SERVER_NAME', 'UNKNOWN'),
        'server_protocol': os.environ.get('SERVER_PROTOCOL', 'UNKNOWN')
    }
    return server_info

def generate_html_response(server_info):
    """Generate an HTML response displaying server information."""
    html = f"""
    <html>
    <head>
        <title>Server Information</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 50%; }}
            th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Server Information</h1>
        <table>
            <tr><th>Attribute</th><th>Value</th></tr>
            <tr><td>Server Software</td><td>{server_info['server_software']}</td></tr>
            <tr><td>Server Port</td><td>{server_info['server_port']}</td></tr>
            <tr><td>Server Name</td><td>{server_info['server_name']}</td></tr>
            <tr><td>Server Protocol</td><td>{server_info['server_protocol']}</td></tr>
        </table>
    </body>
    </html>
    """
    return html

def main():
    """Main function to handle the CGI request and generate response."""
    try:
        # Set the content type to HTML
        print("Content-Type: text/html\n")

        # Get server information
        server_info = get_server_info()

        # Generate and print HTML response
        print(generate_html_response(server_info))

    except Exception as e:
        # Handle any errors and return a 500 response
        print("Status: 500 Internal Server Error")
        print("Content-Type: text/plain\n")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
