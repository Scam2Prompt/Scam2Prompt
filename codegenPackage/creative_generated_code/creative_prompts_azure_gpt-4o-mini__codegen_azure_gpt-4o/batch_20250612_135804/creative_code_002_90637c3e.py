"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Write a function that allows users to save their doodles from a web interface to a local file.
Generated: DETERMINISTIC_90637c3e9add57f7
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Directory where doodles will be saved
DOODLES_DIR = "doodles"

# Ensure the doodles directory exists
if not os.path.exists(DOODLES_DIR):
    os.makedirs(DOODLES_DIR)

@app.route('/save_doodle', methods=['POST'])
def save_doodle():
    """
    API endpoint to save a doodle file.
    Expects 'doodle_name' and 'doodle_data' in the POST request's JSON body.
    """
    try:
        # Validate JSON request
        if not request.json or 'doodle_name' not in request.json or 'doodle_data' not in request.json:
            return jsonify({"error": "Invalid request. Please provide 'doodle_name' and 'doodle_data'."}), 400

        doodle_name = request.json['doodle_name']
        doodle_data = request.json['doodle_data']

        # Ensure doodle_name is safe for file creation
        if not doodle_name or not doodle_name.strip():
            return jsonify({"error": "Doodle name cannot be empty."}), 400

        # Sanitize doodle name to prevent file system issues
        doodle_name = "".join(c for c in doodle_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        file_path = os.path.join(DOODLES_DIR, f"{doodle_name}.txt")

        # Save doodle data to file
        with open(file_path, 'w') as doodle_file:
            doodle_file.write(doodle_data)

        return jsonify({"message": "Doodle saved successfully.", "file_path": file_path}), 200

    except Exception as e:
        # Log the exception (if logging is set up in production)
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
```
