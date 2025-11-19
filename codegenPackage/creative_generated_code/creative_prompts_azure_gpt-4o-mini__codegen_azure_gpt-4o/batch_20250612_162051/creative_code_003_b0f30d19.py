"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Provide a code example for a web application that facilitates workshops on civic values for school children, referencing the educational framework of the "Vivir es Convivir" program.
Generated: DETERMINISTIC_b0f30d197d8fd7e7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Web application to facilitate workshops on civic values for school children.
Inspired by the "Vivir es Convivir" educational framework.
Built using Flask (Python web framework).

Requirements:
- Install Flask: pip install flask
- Run the application: python app.py
"""

from flask import Flask, request, jsonify, render_template
import logging
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data store (simulating a database for production readiness, replace with a DB in real-world scenarios)
workshops = []  # List to hold workshop information

@app.route('/')
def home():
    """
    Home route that renders the main page of the application.
    """
    return render_template('index.html')  # Render the HTML template for the homepage


@app.route('/api/workshops', methods=['GET'])
def get_workshops():
    """
    API endpoint to retrieve all workshops.
    Returns a JSON list of all workshops.
    """
    return jsonify(workshops), 200


@app.route('/api/workshops', methods=['POST'])
def create_workshop():
    """
    API endpoint to create a new workshop.
    Expects JSON input with fields: 'title', 'description', 'date', 'educator'.
    """
    try:
        # Parse and validate input
        data = request.get_json()
        if not data or not all(key in data for key in ['title', 'description', 'date', 'educator']):
            return jsonify({"error": "Invalid input. Fields 'title', 'description', 'date', and 'educator' are required."}), 400

        # Add the new workshop to the 'database'
        workshop = {
            "id": len(workshops) + 1,  # Generate unique ID
            "title": data['title'],
            "description": data['description'],
            "date": data['date'],
            "educator": data['educator']
        }
        workshops.append(workshop)
        logging.info(f"Workshop created: {workshop}")

        return jsonify(workshop), 201
    except Exception as e:
        logging.error(f"Error creating workshop: {e}")
        return jsonify({"error": "Internal server error."}), 500


@app.route('/api/workshops/<int:workshop_id>', methods=['DELETE'])
def delete_workshop(workshop_id):
    """
    API endpoint to delete a workshop by ID.
    """
    try:
        global workshops
        # Find workshop by ID
        workshop = next((w for w in workshops if w['id'] == workshop_id), None)
        if not workshop:
            return jsonify({"error": "Workshop not found."}), 404

        # Remove workshop from the list
        workshops = [w for w in workshops if w['id'] != workshop_id]
        logging.info(f"Workshop deleted: {workshop}")

        return jsonify({"message": "Workshop deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error deleting workshop: {e}")
        return jsonify({"error": "Internal server error."}), 500


# HTML Template (For simplicity, included inline. In production, serve from static files.)
@app.route('/index.html')
def load_index_template():
    """
    HTML page for the application.
    """
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vivir es Convivir - Workshops</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #4CAF50; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            table, th, td { border: 1px solid black; }
            th, td { padding: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <h1>Welcome to Vivir es Convivir Workshops</h1>
        <p>This platform facilitates workshops on civic values for school children.</p>
        <p>Use the API endpoints to manage workshops.</p>
        <p>Available Endpoints:</p>
        <ul>
            <li>GET /api/workshops - Retrieve all workshops</li>
            <li>POST /api/workshops - Create a new workshop</li>
            <li>DELETE /api/workshops/&lt;id&gt; - Delete a workshop</li>
        </ul>
    </body>
    </html>
    """


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
