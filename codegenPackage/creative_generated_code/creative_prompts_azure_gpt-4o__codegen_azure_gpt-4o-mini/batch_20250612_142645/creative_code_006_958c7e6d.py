"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Write a Python Flask application that mimics the functionality of a CGI script typically stored in a "cgi-bin" directory.
Generated: DETERMINISTIC_958c7e6d298a3677
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/cgi-bin/<script_name>', methods=['GET', 'POST'])
def cgi_script(script_name):
    """
    Mimics the functionality of a CGI script.
    
    Args:
        script_name (str): The name of the CGI script to execute.
    
    Returns:
        Response: A JSON response containing the output of the script or an error message.
    """
    # Define the base directory for CGI scripts
    cgi_bin_path = os.path.join(os.getcwd(), 'cgi-bin')
    
    # Check if the script exists in the cgi-bin directory
    script_path = os.path.join(cgi_bin_path, script_name)
    
    if not os.path.isfile(script_path):
        logging.error(f"Script {script_name} not found.")
        return jsonify({"error": "Script not found."}), 404
    
    try:
        # Prepare environment variables for CGI script
        env = {
            'REQUEST_METHOD': request.method,
            'CONTENT_TYPE': request.content_type,
            'PATH_INFO': f'/cgi-bin/{script_name}',
            'QUERY_STRING': request.query_string.decode(),
        }

        # Capture the output of the script execution
        output = execute_script(script_path, env, request.data)

        # Return the output as JSON
        return jsonify({"output": output}), 200
    except Exception as e:
        logging.error(f"Error executing script {script_name}: {e}")
        return jsonify({"error": str(e)}), 500

def execute_script(script_path, env, data):
    """
    Executes the CGI script.
    
    Args:
        script_path (str): The path to the CGI script.
        env (dict): The environment variables for the script.
        data (bytes): The data to be sent to the script.
    
    Returns:
        str: The output of the script execution.
    """
    import subprocess

    # Prepare the command to execute the script
    process = subprocess.Popen(
        ['python3', script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        input=data,
        text=True
    )

    # Capture the output and error from the script
    output, error = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Script error: {error.strip()}")

    return output.strip()

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Place your CGI scripts in a directory named `cgi-bin` at the same level as this script.
- Ensure that your CGI scripts are executable and have the appropriate shebang line at the top (e.g., `#!/usr/bin/env python3`).
- This Flask application will mimic the behavior of a CGI script handler in a CGI environment.
