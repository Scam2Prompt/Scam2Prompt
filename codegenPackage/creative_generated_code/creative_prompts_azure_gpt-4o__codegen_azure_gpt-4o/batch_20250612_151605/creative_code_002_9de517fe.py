"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Create a basic server configuration script that includes a `/cgi-bin/` directory for executing CGI scripts.
Generated: DETERMINISTIC_9de517fea4af84e9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Python script using Flask to set up a basic server that includes a `/cgi-bin/` directory for executing CGI scripts:

```python
import os
import subprocess
from flask import Flask, request, Response

# Initialize Flask application
app = Flask(__name__)

# Set the path for CGI scripts
CGI_BIN_DIR = os.path.join(os.getcwd(), "cgi-bin")

# Ensure the `/cgi-bin/` directory exists
if not os.path.exists(CGI_BIN_DIR):
    os.makedirs(CGI_BIN_DIR)

@app.route('/cgi-bin/<path:script_name>', methods=['GET', 'POST'])
def execute_cgi(script_name):
    """
    Execute a CGI script residing in the `/cgi-bin/` directory.

    :param script_name: Name of the script to execute.
    :return: Output of the CGI script or an error message.
    """
    script_path = os.path.join(CGI_BIN_DIR, script_name)

    # Ensure the script exists and is executable
    if not os.path.isfile(script_path):
        return Response(f"Error: Script '{script_name}' not found.", status=404)
    if not os.access(script_path, os.X_OK):
        return Response(f"Error: Script '{script_name}' is not executable.", status=403)

    try:
        # Execute the CGI script and capture the output
        process = subprocess.Popen(
            script_path,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,  # Allow execution of scripts with proper shell environment
        )
        
        # Handle input for POST requests
        if request.method == 'POST':
            input_data = request.data
        else:
            input_data = None

        stdout, stderr = process.communicate(input=input_data)

        if process.returncode != 0:
            # Return error output if script execution failed
            return Response(f"Error executing script:\n{stderr.decode('utf-8')}", status=500)

        # Return the script output
        return Response(stdout.decode('utf-8'), status=200, content_type="text/plain")
    except Exception as e:
        # Handle unexpected errors
        return Response(f"Internal Server Error: {str(e)}", status=500)

@app.route('/')
def index():
    """
    Basic index route to verify the server is running.
    """
    return Response("Server is running. Use /cgi-bin/<script_name> to execute CGI scripts.", status=200)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080, debug=False)
```

### Notes:
- Place your CGI scripts inside the `cgi-bin` directory where this script is executed. Ensure they have proper executable permissions (`chmod +x script_name`).
- For security purposes, consider restricting access to CGI scripts and sanitizing user input if required.
- The `debug` mode is disabled in production for security reasons.
