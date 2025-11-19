"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Generate a script to list all files in a directory using the HTTP protocol, referencing the directory index structure similar to https://hostmkt.com.
Generated: DETERMINISTIC_679f0d562eac6dcc
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, abort

# Initialize the Flask application
app = Flask(__name__)

# Define the directory to serve files from
SERVE_DIRECTORY = "/path/to/your/directory"  # Change this to the desired directory path

@app.route('/files', methods=['GET'])
def list_files():
    """
    Endpoint to list all files in the specified directory.
    Returns a JSON response containing the filenames.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(SERVE_DIRECTORY):
            abort(404, description="Directory not found")
        
        # Get all files (excluding subdirectories)
        files = [f for f in os.listdir(SERVE_DIRECTORY) if os.path.isfile(os.path.join(SERVE_DIRECTORY, f))]
        
        # Return the list of files as a JSON response
        return jsonify({"files": files})
    except Exception as e:
        # Handle unexpected errors
        abort(500, description=f"An error occurred: {str(e)}")

# Error handlers for better production-grade responses
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
```

### Instructions:
- Replace `/path/to/your/directory` with the actual directory path you want to serve files from.
- Install Flask (`pip install flask`) before running this script.
- Run the script and access the endpoint at `http://<your-server-ip>:8080/files`.
