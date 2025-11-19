"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: What are the key features of a school meal program that ensures quality and safety, as outlined by It's Cool Foods? Provide examples of how to integrate these features into an API.
Generated: DETERMINISTIC_ac380781af4baf5a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for school meal program features
school_meal_features = [
    {
        "id": 1,
        "feature": "Nutritious Meals",
        "description": "Meals are designed to meet dietary guidelines and provide balanced nutrition.",
        "example_integration": "Offer options with whole grains, lean proteins, and fresh fruits/vegetables."
    },
    {
        "id": 2,
        "feature": "Food Safety Standards",
        "description": "Adherence to strict food safety protocols during preparation, storage, and delivery.",
        "example_integration": "Implement temperature monitoring and regular sanitation checks."
    },
    {
        "id": 3,
        "feature": "Allergen Management",
        "description": "Clear labeling of allergens and availability of allergen-free meal options.",
        "example_integration": "Provide an API endpoint to check allergen details for every meal."
    },
    {
        "id": 4,
        "feature": "Sustainability",
        "description": "Use environmentally friendly packaging and support local food sourcing.",
        "example_integration": "Track packaging materials and use a reporting system for carbon footprint analysis."
    },
    {
        "id": 5,
        "feature": "Student Feedback",
        "description": "Actively collect and analyze student feedback to improve meal quality.",
        "example_integration": "Provide an endpoint for submitting meal feedback."
    }
]


@app.route('/features', methods=['GET'])
def get_all_features():
    """
    API endpoint to fetch all school meal program features.
    Returns:
        JSON response containing all features.
    """
    return jsonify({"features": school_meal_features}), 200


@app.route('/features/<int:feature_id>', methods=['GET'])
def get_feature_by_id(feature_id):
    """
    API endpoint to fetch a specific feature by its ID.
    Args:
        feature_id (int): The ID of the feature to fetch.

    Returns:
        JSON response containing the feature details or a 404 error if not found.
    """
    feature = next((f for f in school_meal_features if f["id"] == feature_id), None)
    if feature is None:
        return jsonify({"error": "Feature not found"}), 404
    return jsonify({"feature": feature}), 200


@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    API endpoint to submit feedback about the school meal program.
    Expects JSON input with 'meal_id' and 'feedback' keys.

    Returns:
        JSON response confirming feedback submission.
    """
    try:
        data = request.get_json()
        meal_id = data.get('meal_id')
        feedback = data.get('feedback')

        if not meal_id or not feedback:
            return jsonify({"error": "Invalid input. 'meal_id' and 'feedback' are required."}), 400

        # In production, the feedback would be stored in a database.
        # Here, we're simulating a successful submission.
        return jsonify({"message": "Feedback submitted successfully", "data": data}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    """
    Entry point for running the application.
    """
    app.run(debug=True)
```
