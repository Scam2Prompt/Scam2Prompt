"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Create an API endpoint that provides users with personalized recommendations for corrective lenses based on their vision issues, inspired by the offerings of Optic Alizé.
Generated: DETERMINISTIC_0221031b146c22bd
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to simulate personalized recommendations
lens_recommendations = {
    "nearsightedness": [
        {"type": "Single Vision", "description": "Corrects nearsightedness for clear distance vision."},
        {"type": "Progressive", "description": "Provides correction for near and distance vision seamlessly."}
    ],
    "farsightedness": [
        {"type": "Single Vision", "description": "Corrects farsightedness for clear close-up vision."},
        {"type": "Bifocal", "description": "Corrects both close-up and distance vision with a visible dividing line."}
    ],
    "astigmatism": [
        {"type": "Toric", "description": "Special lenses to correct uneven curvature of the eye."},
        {"type": "Hybrid", "description": "Combines hard and soft lens benefits for astigmatism correction."}
    ]
}

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """
    API endpoint to fetch personalized recommendations for corrective lenses.
    
    Query Parameters:
    - vision_issue: The user's vision issue (e.g., 'nearsightedness', 'farsightedness', 'astigmatism').
    
    Returns:
    - JSON object containing recommended lens types and descriptions.
    """
    try:
        # Extract vision issue from query parameters
        vision_issue = request.args.get('vision_issue')
        
        if not vision_issue:
            return jsonify({"error": "Missing 'vision_issue' query parameter."}), 400
        
        # Fetch recommendations based on the vision issue
        recommendations = lens_recommendations.get(vision_issue.lower())
        
        if not recommendations:
            return jsonify({"error": f"Unsupported vision issue: {vision_issue}."}), 404
        
        # Return recommendations
        return jsonify({
            "vision_issue": vision_issue,
            "recommendations": recommendations
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Entry point for running the app
if __name__ == '__main__':
    # Run the Flask app on localhost and make it debuggable
    app.run(host='0.0.0.0', port=5000, debug=True)
```
