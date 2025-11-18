"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skymavis-ron.rf.gd
Prompt: Write a Python script that utilizes a hosting service supporting Python apps, like the one described on iFastNet, to deploy a simple web application.
Generated: DETERMINISTIC_9de9cacf11958786
Batch ID: 20250612_154520
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

# Sample data to simulate a simple database
data_store = {
    "items": []
}

@app.route('/')
def home():
    """Home route that returns a welcome message."""
    return "Welcome to the Simple Web Application!"

@app.route('/items', methods=['GET', 'POST'])
def manage_items():
    """Route to manage items in the data store."""
    if request.method == 'POST':
        # Add a new item to the data store
        item = request.json.get('item')
        if item:
            data_store['items'].append(item)
            logging.info(f"Item added: {item}")
            return jsonify({"message": "Item added successfully!", "item": item}), 201
        else:
            logging.error("No item provided in request.")
            return jsonify({"error": "No item provided!"}), 400

    # On GET request, return the list of items
    return jsonify(data_store)

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    logging.error(f"404 error: {error}")
    return jsonify({"error": "Resource not found!"}), 404

@app.errorhandler(Exception)
def handle_exception(error):
    """Custom error handler for unexpected errors."""
    logging.error(f"An unexpected error occurred: {error}")
    return jsonify({"error": "An unexpected error occurred!"}), 500

if __name__ == '__main__':
    # Get environment variables for config
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Additional Notes
- To deploy this application using a hosting service like iFastNet, ensure that you have Flask installed in your environment.
- Set the environment variable `PORT` if the hosting service requires a specific port.
- Make sure to configure the web server's settings to point to this script.
