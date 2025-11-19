"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dam2020.de
Prompt: Create an API endpoint that provides information about leisure activities near Landgraaf, including details on the Skihalle and other attractions mentioned on the webpage.
Generated: DETERMINISTIC_6f80d300ae9299d0
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data for leisure activities near Landgraaf
leisure_activities = [
    {
        "name": "Skihalle",
        "type": "Skiing",
        "description": "Indoor skiing facility with various slopes and amenities.",
        "location": "Landgraaf",
        "rating": 4.5
    },
    {
        "name": "Thermae 2000",
        "type": "Spa",
        "description": "Wellness resort with thermal baths and wellness treatments.",
        "location": "Landgraaf",
        "rating": 4.7
    },
    {
        "name": "SnowWorld",
        "type": "Skiing",
        "description": "Indoor snow sports park with skiing and snowboarding.",
        "location": "Landgraaf",
        "rating": 4.3
    },
    {
        "name": "Couven Museum",
        "type": "Museum",
        "description": "Museum showcasing the history and culture of the region.",
        "location": "Aachen",
        "rating": 4.2
    }
]

@app.route('/api/leisure-activities', methods=['GET'])
def get_leisure_activities():
    """
    API endpoint to get leisure activities near Landgraaf.

    Returns:
        JSON response containing a list of leisure activities.
    """
    try:
        # Filter activities based on the location
        location = request.args.get('location', default='Landgraaf', type=str)
        activities_filtered = [activity for activity in leisure_activities if activity["location"] == location]

        if not activities_filtered:
            return jsonify({"message": "No leisure activities found in the specified location."}), 404

        return jsonify(activities_filtered), 200

    except Exception as e:
        # Return a 500 error in case of any unexpected exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
