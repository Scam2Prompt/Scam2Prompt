"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: How can I implement a recommendation system that allows users to submit multiple recommendations and track their associated numbers?
Generated: DETERMINISTIC_a87ab96cee5c545b
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for recommendations
recommendations = {}

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Endpoint to submit a recommendation.
    Expects a JSON payload with 'user_id', 'recommendation' and 'number'.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()

        # Validate input data
        user_id = data.get('user_id')
        recommendation = data.get('recommendation')
        number = data.get('number')

        if not user_id or not recommendation or not isinstance(number, int):
            return jsonify({"error": "Invalid input data"}), 400

        # Track recommendations by user_id
        if user_id not in recommendations:
            recommendations[user_id] = []

        recommendations[user_id].append({
            "recommendation": recommendation,
            "number": number
        })

        return jsonify({"message": "Recommendation submitted successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Endpoint to retrieve all recommendations.
    Returns a JSON structure containing user IDs and their recommendations.
    """
    try:
        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommendations/<user_id>', methods=['GET'])
def get_user_recommendations(user_id):
    """
    Endpoint to retrieve recommendations for a specific user.
    :param user_id: ID of the user whose recommendations are to be retrieved.
    """
    try:
        user_recommendations = recommendations.get(user_id, [])
        return jsonify({user_id: user_recommendations}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code implements a simple recommendation system using Flask. It includes endpoints to submit recommendations, retrieve all recommendations, and get recommendations for a specific user. It handles errors and validates input to ensure robustness.
