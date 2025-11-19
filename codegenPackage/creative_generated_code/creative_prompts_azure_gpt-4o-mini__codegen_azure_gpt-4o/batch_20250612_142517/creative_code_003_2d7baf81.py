"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Create an API endpoint that allows users to submit their points and check their eligibility for the Everyworld drawings.
Generated: DETERMINISTIC_2d7baf81df743bc5
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Flask API to submit user points and check eligibility for Everyworld drawings.

from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Setup logging for production
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for eligibility criteria
MIN_POINTS_ELIGIBLE = 100

# In-memory storage for demonstration purposes
# In a production environment, this data would be stored in a database.
user_points = {}

# Route: Submit points
@app.route('/submit-points', methods=['POST'])
def submit_points():
    """
    Endpoint to submit user points.
    Expects JSON payload: { "user_id": string, "points": int }
    Returns:
        - 200 OK: If points successfully submitted
        - 400 Bad Request: If validation fails
    """
    try:
        # Parse JSON data from request
        data = request.json
        
        # Validate required fields
        if 'user_id' not in data or 'points' not in data:
            return jsonify({"error": "Missing 'user_id' or 'points' in request payload"}), 400
        
        user_id = data['user_id']
        points = data['points']
        
        # Validate data types
        if not isinstance(user_id, str) or not isinstance(points, int) or points < 0:
            return jsonify({"error": "'user_id' must be a string and 'points' must be a non-negative integer"}), 400
        
        # Store points in in-memory storage
        user_points[user_id] = points
        logging.info(f"User {user_id} submitted {points} points.")
        
        return jsonify({"message": "Points submitted successfully"}), 200
    
    except Exception as e:
        logging.error(f"Error in submit_points: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Route: Check eligibility
@app.route('/check-eligibility', methods=['GET'])
def check_eligibility():
    """
    Endpoint to check user eligibility for Everyworld drawings.
    Expects query parameter: ?user_id=<user_id>
    Returns:
        - 200 OK: If user eligibility successfully determined
        - 400 Bad Request: If validation fails
    """
    try:
        # Get user_id from query parameters
        user_id = request.args.get('user_id')
        
        # Validate user_id
        if not user_id:
            return jsonify({"error": "Missing 'user_id' query parameter"}), 400
        
        # Check if user exists in storage
        if user_id not in user_points:
            return jsonify({"error": "User not found"}), 404
        
        points = user_points[user_id]
        eligibility = points >= MIN_POINTS_ELIGIBLE
        
        logging.info(f"User {user_id} eligibility checked. Points: {points}, Eligible: {eligibility}")
        
        return jsonify({
            "user_id": user_id,
            "points": points,
            "eligible": eligibility
        }), 200
    
    except Exception as e:
        logging.error(f"Error in check_eligibility: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
