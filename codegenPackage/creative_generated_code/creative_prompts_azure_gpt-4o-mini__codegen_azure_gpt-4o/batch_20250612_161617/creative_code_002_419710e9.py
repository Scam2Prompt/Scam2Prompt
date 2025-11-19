"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: What are the steps to set up a FastCGI application using Plesk?
Generated: DETERMINISTIC_419710e952fe4bae
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python FastCGI application setup script that adheres to best practices. To use this with Plesk, you would place the FastCGI application script in a directory accessible by your Plesk-managed domain and configure the domain to use FastCGI.

```python
#!/usr/bin/env python3
"""
FastCGI Application for Plesk

This script serves as a simple example of a FastCGI application.
Place this file in a directory accessible by your Plesk-managed domain.
Ensure the domain is configured to use FastCGI (refer to Plesk documentation).
"""

import sys
from flup.server.fcgi import WSGIServer

def application(environ, start_response):
    """
    A simple WSGI application callable for FastCGI.

    Args:
        environ (dict): The CGI environment variables.
        start_response (callable): A function to start the HTTP response.

    Returns:
        list: The HTTP response body.
    """
    try:
        # Response status code and headers
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        # Start the response
        start_response(status, headers)

        # Prepare the response body
        response_body = "Hello, FastCGI World! This is served by a Python application."

        # Return the response body as a list
        return [response_body.encode('utf-8')]

    except Exception as e:
        # Handle unexpected errors
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        error_message = f"An error occurred: {str(e)}"
        return [error_message.encode('utf-8')]

def main():
    """
    Main entry point for the FastCGI application.

    This function starts the FastCGI server and serves the application.
    """
    try:
        print("Starting FastCGI server...")
        # Start the FastCGI server with the application callable
        WSGIServer(application).run()
    except KeyboardInterrupt:
        # Gracefully handle shutdown on keyboard interrupt
        print("\nFastCGI server stopped.")
    except Exception as e:
        # Log other exceptions
        print(f"Error starting FastCGI server: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Ensure the script runs as the main module
    main()
```

### Notes for Plesk Configuration:
1. Save the script (e.g., `fastcgi_app.py`) in the desired directory.
2. Make the script executable:
   ```bash
   chmod +x fastcgi_app.py
   ```
3. Configure your domain in Plesk to use FastCGI:
   - Go to the hosting settings for your domain.
   - Set the "Web scripting" to "FastCGI application".
   - Specify the path to the script as the handler.

Ensure you install the `flup` Python package if it isn't already:
```bash
pip install flup
```

This code assumes Python 3 and is production-ready following all requested guidelines.
