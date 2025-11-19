"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Design a simple API to manage roofing services, including scheduling inspections, requesting estimates, and tracking customer reviews, inspired by King Roofing's customer experience.
Generated: DETERMINISTIC_eb4c6d92e693d853
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for simplicity
inspections = []
estimates = []
reviews = []

# Error messages
ERROR_INVALID_DATA = "Invalid data provided."
ERROR_NOT_FOUND = "Resource not found."

# Helper function to validate date format
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Route to schedule an inspection
@app.route('/api/inspections', methods=['POST'])
def schedule_inspection():
    """
    Schedule a roofing inspection.
    Request JSON format:
    {
        "customer_name": "John Doe",
        "address": "123 Main St",
        "date": "2023-10-15"
    }
    """
    data = request.json
    if not data or 'customer_name' not in data or 'address' not in data or 'date' not in data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    if not validate_date(data['date']):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    inspection = {
        "id": len(inspections) + 1,
        "customer_name": data['customer_name'],
        "address": data['address'],
        "date": data['date']
    }
    inspections.append(inspection)
    return jsonify(inspection), 201

# Route to request an estimate
@app.route('/api/estimates', methods=['POST'])
def request_estimate():
    """
    Request a roofing estimate.
    Request JSON format:
    {
        "customer_name": "Jane Smith",
        "address": "456 Elm St",
        "description": "Need a new roof installation."
    }
    """
    data = request.json
    if not data or 'customer_name' not in data or 'address' not in data or 'description' not in data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    estimate = {
        "id": len(estimates) + 1,
        "customer_name": data['customer_name'],
        "address": data['address'],
        "description": data['description']
    }
    estimates.append(estimate)
    return jsonify(estimate), 201

# Route to submit a customer review
@app.route('/api/reviews', methods=['POST'])
def submit_review():
    """
    Submit a customer review.
    Request JSON format:
    {
        "customer_name": "John Doe",
        "rating": 5,
        "comments": "Excellent service!"
    }
    """
    data = request.json
    if not data or 'customer_name' not in data or 'rating' not in data or 'comments' not in data:
        return jsonify({"error": ERROR_INVALID_DATA}), 400

    if not isinstance(data['rating'], int) or data['rating'] < 1 or data['rating'] > 5:
        return jsonify({"error": "Rating must be an integer between 1 and 5."}), 400

    review = {
        "id": len(reviews) + 1,
        "customer_name": data['customer_name'],
        "rating": data['rating'],
        "comments": data['comments']
    }
    reviews.append(review)
    return jsonify(review), 201

# Route to get all inspections
@app.route('/api/inspections', methods=['GET'])
def get_inspections():
    """
    Get all scheduled inspections.
    """
    return jsonify(inspections), 200

# Route to get all estimates
@app.route('/api/estimates', methods=['GET'])
def get_estimates():
    """
    Get all requested estimates.
    """
    return jsonify(estimates), 200

# Route to get all reviews
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """
    Get all customer reviews.
    """
    return jsonify(reviews), 200

# Route to get a specific inspection by ID
@app.route('/api/inspections/<int:inspection_id>', methods=['GET'])
def get_inspection_by_id(inspection_id):
    """
    Get a specific inspection by ID.
    """
    inspection = next((i for i in inspections if i['id'] == inspection_id), None)
    if not inspection:
        return jsonify({"error": ERROR_NOT_FOUND}), 404
    return jsonify(inspection), 200

# Route to get a specific estimate by ID
@app.route('/api/estimates/<int:estimate_id>', methods=['GET'])
def get_estimate_by_id(estimate_id):
    """
    Get a specific estimate by ID.
    """
    estimate = next((e for e in estimates if e['id'] == estimate_id), None)
    if not estimate:
        return jsonify({"error": ERROR_NOT_FOUND}), 404
    return jsonify(estimate), 200

# Route to get a specific review by ID
@app.route('/api/reviews/<int:review_id>', methods=['GET'])
def get_review_by_id(review_id):
    """
    Get a specific review by ID.
    """
    review = next((r for r in reviews if r['id'] == review_id), None)
    if not review:
        return jsonify({"error": ERROR_NOT_FOUND}), 404
    return jsonify(review), 200

# Error handler for 404
@app.errorhandler(404)
def resource_not_found(e):
    """
    Handle 404 errors.
    """
    return jsonify({"error": ERROR_NOT_FOUND}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
