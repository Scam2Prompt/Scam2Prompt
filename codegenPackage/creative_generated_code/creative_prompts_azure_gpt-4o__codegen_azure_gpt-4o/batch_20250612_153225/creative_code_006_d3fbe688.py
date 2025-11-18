"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Develop a REST API that allows users to retrieve information about wine tasting seminars, including details like location, time, and sommelier information, as seen in the FestiVin Caraquet program.
Generated: DETERMINISTIC_d3fbe6886cd77419
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: REST API for retrieving wine tasting seminar details.

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing wine tasting seminars.
# In a production system, this would be replaced with a database.
seminar_data = [
    {
        "id": 1,
        "name": "Introduction to Wine Tasting",
        "location": "Caraquet Cultural Center",
        "time": "2023-11-15T18:00:00",
        "sommelier": "Jean Dupont"
    },
    {
        "id": 2,
        "name": "Pairing Wines with Cheese",
        "location": "La Maison du Vin",
        "time": "2023-11-16T19:00:00",
        "sommelier": "Marie Claire"
    },
    {
        "id": 3,
        "name": "Exploring Red Wines",
        "location": "Caraquet Community Hall",
        "time": "2023-11-17T18:30:00",
        "sommelier": "Émile Rousseau"
    }
]

@app.route("/seminars", methods=["GET"])
def get_seminars():
    """
    Endpoint to retrieve all wine tasting seminars.
    Returns:
        JSON response with the list of seminars.
    """
    return jsonify({"seminars": seminar_data}), 200

@app.route("/seminars/<int:seminar_id>", methods=["GET"])
def get_seminar_by_id(seminar_id):
    """
    Endpoint to retrieve information about a specific seminar by ID.
    Args:
        seminar_id (int): ID of the seminar to retrieve.
    Returns:
        JSON response with seminar details if found, or 404 error if not found.
    """
    seminar = next((s for s in seminar_data if s["id"] == seminar_id), None)
    if seminar:
        return jsonify({"seminar": seminar}), 200
    else:
        return jsonify({"error": "Seminar not found"}), 404

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    Args:
        e (HTTPException): The exception raised.
    Returns:
        JSON response with error details.
    """
    return jsonify({
        "error": e.name,
        "description": e.description
    }), e.code

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Global error handler for unexpected exceptions.
    Args:
        e (Exception): The exception raised.
    Returns:
        JSON response with a generic error message.
    """
    return jsonify({
        "error": "Internal Server Error",
        "description": "An unexpected error occurred. Please try again later."
    }), 500

if __name__ == "__main__":
    # Run the Flask application.
    # In production, use a WSGI server like Gunicorn or uWSGI instead.
    app.run(host="0.0.0.0", port=5000, debug=False)
```
