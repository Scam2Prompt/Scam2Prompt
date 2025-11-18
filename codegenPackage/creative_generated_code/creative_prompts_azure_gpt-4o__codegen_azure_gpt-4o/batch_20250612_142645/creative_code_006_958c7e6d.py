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
from flask import Flask, request, jsonify, abort
import os

# Initialize Flask application
app = Flask(__name__)

# Set a route to mimic the "cgi-bin" directory functionality
@app.route('/cgi-bin/<script_name>', methods=['GET', 'POST'])
def cgi_bin(script_name):
    """
    Mimic the behavior of a CGI script in a 'cgi-bin' directory.
    This endpoint accepts GET and POST requests and executes
    a specific "script" based on script_name.
    """
    # Define the directory where scripts are stored
    cgi_bin_path = './cgi-bin'

    # Construct the full script path
    script_path = os.path.join(cgi_bin_path, script_name)

    # Check if the script exists and is executable
    if not os.path.exists(script_path):
        abort(404, description="Script not found.")
    if not os.access(script_path, os.X_OK):
        abort(403, description="Script is not executable.")

    # Prepare environment variables for the script
    env = os.environ.copy()
    env['REQUEST_METHOD'] = request.method
    env['QUERY_STRING'] = request.query_string.decode('utf-8')
    env['CONTENT_TYPE'] = request.content_type or ''
    env['CONTENT_LENGTH'] = str(request.content_length or 0)
    env['REMOTE_ADDR'] = request.remote_addr or ''
    env['HTTP_USER_AGENT'] = request.headers.get('User-Agent', '')

    # Execute the script and capture its output
    try:
        import subprocess
        if request.method == 'POST':
            # Pass POST data to the script's stdin
            result = subprocess.run(
                script_path,
                input=request.data,
                text=True,
                capture_output=True,
                env=env
            )
        else:
            # GET request (no stdin input)
            result = subprocess.run(
                script_path,
                capture_output=True,
                text=True,
                env=env
            )
        
        # Return the script's output
        return result.stdout, result.returncode
    except Exception as e:
        # Catch and return any unexpected errors
        abort(500, description=f"Error executing script: {str(e)}")


# Error handlers for better feedback
@app.errorhandler(404)
def not_found_error(e):
    """Handle 404 Not Found errors."""
    return jsonify(error=str(e)), 404

@app.errorhandler(403)
def forbidden_error(e):
    """Handle 403 Forbidden errors."""
    return jsonify(error=str(e)), 403

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 Internal Server errors."""
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    # Ensure the 'cgi-bin' directory exists
    os.makedirs('./cgi-bin', exist_ok=True)

    # Run the Flask app on localhost, port 8000
    app.run(host='127.0.0.1', port=8000, debug=False)
```
