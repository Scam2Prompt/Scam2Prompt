"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Write a script to list files in a directory served by a LiteSpeed web server.
Generated: DETERMINISTIC_2c3958a958a42035
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, jsonify, request

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Flask application
app = Flask(__name__)

@app.route('/list-files', methods=['GET'])
def list_files():
    """
    Endpoint to list files in a specified directory.
    ---
    Query Parameters:
        - dir: The directory path relative to the server root. (optional)
    Returns:
        JSON response containing the list of files or an error message.
    """
    try:
        # Get the directory path from query parameters (default to current directory)
        directory = request.args.get('dir', '.')

        # Validate the directory path
        if not os.path.exists(directory):
            logging.error(f"Directory not found: {directory}")
            return jsonify({'error': f'Directory not found: {directory}'}), 404

        if not os.path.isdir(directory):
            logging.error(f"Path is not a directory: {directory}")
            return jsonify({'error': f'Path is not a directory: {directory}'}), 400

        # List files in the directory
        files = os.listdir(directory)
        logging.info(f"Successfully listed files in directory: {directory}")

        return jsonify({'files': files}), 200

    except Exception as e:
        # Handle unexpected errors
        logging.exception("An error occurred while listing files")
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on LiteSpeed-compatible WSGI server
    # Note: Flask can be served via LiteSpeed with WSGI configuration
    app.run(host='0.0.0.0', port=8080, debug=False)
```
