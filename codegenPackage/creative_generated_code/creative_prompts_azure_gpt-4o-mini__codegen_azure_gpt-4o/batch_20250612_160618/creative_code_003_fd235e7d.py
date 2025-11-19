"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Create an API that collects data on women's participation in clean energy initiatives, reflecting the outcomes of Sauti Kenya's Cohort 2 project.
Generated: DETERMINISTIC_fd235e7de072ee73
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
# Replace this with a proper database in production (e.g., PostgreSQL, MongoDB)
data_store = []

@app.route('/api/clean-energy-initiatives', methods=['POST'])
def add_participation_record():
    """
    Endpoint to collect data on women's participation in clean energy initiatives.
    This reflects outcomes of Sauti Kenya's Cohort 2 project.

    Expects JSON payload:
    {
        "name": "Jane Doe",
        "age": 35,
        "location": "Nairobi, Kenya",
        "initiative_name": "Solar Panel Training",
        "outcomes": "Trained in installation and maintenance of solar panels"
    }
    """
    try:
        # Parse and validate input
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        required_fields = ["name", "age", "location", "initiative_name", "outcomes"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Save record to in-memory database
        data_store.append(data)
        return jsonify({"message": "Participation record added successfully", "record": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/clean-energy-initiatives', methods=['GET'])
def get_participation_records():
    """
    Endpoint to retrieve all participation records.
    """
    try:
        return jsonify({"records": data_store}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions gracefully.
    """
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Handle unexpected exceptions gracefully.
    """
    return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```
