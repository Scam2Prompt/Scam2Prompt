"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "How can I create an API endpoint that returns a directory listing like the one found at https://symbioticfi.world?"
Generated: DETERMINISTIC_2d65ea31a5765134
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, abort
import os

app = Flask(__name__)

# Define the directory to be listed
DIRECTORY_PATH = "/path/to/your/directory"

@app.route('/api/directory-listing', methods=['GET'])
def directory_listing():
    """
    API endpoint to return a directory listing in JSON format.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_PATH) or not os.path.isdir(DIRECTORY_PATH):
            abort(404, description="Directory not found")

        # Retrieve directory contents
        directory_contents = []
        for item in os.listdir(DIRECTORY_PATH):
            item_path = os.path.join(DIRECTORY_PATH, item)
            item_type = "file" if os.path.isfile(item_path) else "directory" if os.path.isdir(item_path) else "other"
            directory_contents.append({
                "name": item,
                "type": item_type,
                "size": os.path.getsize(item_path) if os.path.isfile(item_path) else None
            })

        # Return the directory listing as a JSON response
        return jsonify(directory_contents)

    except Exception as e:
        # Handle unexpected errors gracefully
        abort(500, description=str(e))


@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Not Found", "message": error.description}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal Server Error", "message": error.description}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=False, host="0.0.0.0", port=5000)
```

**Note:** Replace `/path/to/your/directory` with the actual path to the directory you want to list.
