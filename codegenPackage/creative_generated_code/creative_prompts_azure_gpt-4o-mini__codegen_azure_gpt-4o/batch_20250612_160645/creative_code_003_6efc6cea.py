"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Provide an example of a backend setup for a corporate website that includes custom design and management features, as outlined on ra-don.com.
Generated: DETERMINISTIC_6efc6cea34b72f7a
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# backend_setup.py

"""
Backend setup for a corporate website with custom design and management features.
This script uses Flask as the web framework to implement the backend.
"""

from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import HTTPException
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database (Replace with real database implementation like SQLAlchemy or MongoDB)
mock_database = {
    "users": [],
    "designs": [],
    "content": []
}

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    logging.error(f"HTTP error occurred: {e.name} - {e.description}")
    return response

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    logging.error(f"Unexpected error occurred: {str(e)}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }), 500

# Route to render homepage
@app.route("/")
def home():
    """
    Endpoint to render the homepage.
    """
    logging.info("Homepage accessed.")
    return render_template("index.html")  # Template file should be in a 'templates' folder

# Route to manage user accounts
@app.route("/users", methods=["GET", "POST"])
def users():
    """
    Endpoint to handle user account management.
    - GET: Fetch all users.
    - POST: Add a new user.
    """
    if request.method == "GET":
        logging.info("Fetching all users.")
        return jsonify(mock_database["users"])
    elif request.method == "POST":
        try:
            new_user = request.json
            mock_database["users"].append(new_user)
            logging.info(f"New user added: {new_user}")
            return jsonify({"message": "User added successfully."}), 201
        except Exception as e:
            logging.error(f"Error adding new user: {str(e)}")
            return jsonify({"error": "Invalid data"}), 400

# Route to manage designs
@app.route("/designs", methods=["GET", "POST"])
def designs():
    """
    Endpoint to manage custom designs.
    - GET: Fetch all designs.
    - POST: Add a new design.
    """
    if request.method == "GET":
        logging.info("Fetching all designs.")
        return jsonify(mock_database["designs"])
    elif request.method == "POST":
        try:
            new_design = request.json
            mock_database["designs"].append(new_design)
            logging.info(f"New design added: {new_design}")
            return jsonify({"message": "Design added successfully."}), 201
        except Exception as e:
            logging.error(f"Error adding design: {str(e)}")
            return jsonify({"error": "Invalid data"}), 400

# Route to manage website content
@app.route("/content", methods=["GET", "POST"])
def content():
    """
    Endpoint to manage website content.
    - GET: Fetch all content.
    - POST: Add new content.
    """
    if request.method == "GET":
        logging.info("Fetching all content.")
        return jsonify(mock_database["content"])
    elif request.method == "POST":
        try:
            new_content = request.json
            mock_database["content"].append(new_content)
            logging.info(f"New content added: {new_content}")
            return jsonify({"message": "Content added successfully."}), 201
        except Exception as e:
            logging.error(f"Error adding content: {str(e)}")
            return jsonify({"error": "Invalid data"}), 400

# Run the application
if __name__ == "__main__":
    """
    Start the Flask application.
    """
    app.run(debug=True)
```
