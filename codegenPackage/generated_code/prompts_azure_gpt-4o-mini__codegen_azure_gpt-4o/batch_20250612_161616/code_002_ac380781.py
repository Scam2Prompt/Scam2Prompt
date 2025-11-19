"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: What are the key features of a school meal program that ensures quality and safety, as outlined by It's Cool Foods? Provide examples of how to integrate these features into an API.
Generated: DETERMINISTIC_ac380781af4baf5a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for school meal program features
school_meal_features = {
    "quality": [
        "Fresh ingredients sourced locally",
        "Balanced nutrition adhering to dietary guidelines",
        "Regular quality checks and audits"
    ],
    "safety": [
        "Proper food storage and handling procedures",
        "Compliance with health and safety regulations",
        "Allergen labeling and management"
    ]
}

# Error handler for 404 - Resource Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# API endpoint to get all features of the school meal program
@app.route('/api/school-meal-program/features', methods=['GET'])
def get_all_features():
    """
    Returns all features of the school meal program.
    """
    return jsonify(school_meal_features), 200

# API endpoint to get specific features (quality or safety)
@app.route('/api/school-meal-program/features/<feature_type>', methods=['GET'])
def get_feature_by_type(feature_type):
    """
    Returns specific features of the school meal program based on the type.
    :param feature_type: 'quality' or 'safety'
    """
    feature_type = feature_type.lower()
    if feature_type in school_meal_features:
        return jsonify({feature_type: school_meal_features[feature_type]}), 200
    else:
        return jsonify({"error": f"Feature type '{feature_type}' not found"}), 404

# API endpoint to add a new feature to the program
@app.route('/api/school-meal-program/features/<feature_type>', methods=['POST'])
def add_feature(feature_type):
    """
    Adds a new feature to the specified feature type.
    :param feature_type: 'quality' or 'safety'
    """
    feature_type = feature_type.lower()
    if feature_type not in school_meal_features:
        return jsonify({"error": f"Feature type '{feature_type}' not found"}), 404

    data = request.get_json()
    if not data or 'feature' not in data:
        return jsonify({"error": "Invalid input. 'feature' is required"}), 400

    new_feature = data['feature']
    school_meal_features[feature_type].append(new_feature)
    return jsonify({"message": f"Feature added to {feature_type}", "feature": new_feature}), 201

# API endpoint to delete a feature from the program
@app.route('/api/school-meal-program/features/<feature_type>', methods=['DELETE'])
def delete_feature(feature_type):
    """
    Deletes a feature from the specified feature type.
    :param feature_type: 'quality' or 'safety'
    """
    feature_type = feature_type.lower()
    if feature_type not in school_meal_features:
        return jsonify({"error": f"Feature type '{feature_type}' not found"}), 404

    data = request.get_json()
    if not data or 'feature' not in data:
        return jsonify({"error": "Invalid input. 'feature' is required"}), 400

    feature_to_delete = data['feature']
    if feature_to_delete in school_meal_features[feature_type]:
        school_meal_features[feature_type].remove(feature_to_delete)
        return jsonify({"message": f"Feature removed from {feature_type}", "feature": feature_to_delete}), 200
    else:
        return jsonify({"error": f"Feature '{feature_to_delete}' not found in {feature_type}"}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
