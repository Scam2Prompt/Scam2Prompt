"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Create an API recommendation for a mental health service that includes features for addiction intervention and personal growth coaching.
Generated: DETERMINISTIC_ea8fce4ca3dd245d
Batch ID: 20250612_135046
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

# Sample data for demonstration
mental_health_services = [
    {
        "id": 1,
        "name": "Addiction Intervention Service",
        "description": "Personalized programs to help overcome addiction.",
        "features": ["1-on-1 Counseling", "Group Support", "Online Resources"]
    },
    {
        "id": 2,
        "name": "Personal Growth Coaching",
        "description": "Guidance to unlock your potential and achieve personal goals.",
        "features": ["Life Planning", "Goal Setting", "Mindfulness Training"]
    }
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Get all mental health services.
    """
    return jsonify({"services": mental_health_services}), 200


@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    Get a specific mental health service by ID.
    """
    service = next((s for s in mental_health_services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200


@app.route('/api/recommendation', methods=['POST'])
def recommend_service():
    """
    Recommend a mental health service based on user preferences.
    Expected JSON payload: { "preferences": ["Addiction", "Growth"] }
    """
    try:
        data = request.get_json()
        preferences = data.get("preferences", [])
        if not preferences or not isinstance(preferences, list):
            return jsonify({"error": "Invalid preferences format"}), 400

        # Filter and recommend services based on preferences
        recommended_services = [
            service for service in mental_health_services
            if any(pref.lower() in service["description"].lower() for pref in preferences)
        ]

        if not recommended_services:
            return jsonify({"message": "No services match your preferences"}), 200

        return jsonify({"recommended_services": recommended_services}), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 internal server errors.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=True for development; use debug=False for production
```
