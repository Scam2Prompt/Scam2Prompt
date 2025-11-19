"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dam2020.de
Prompt: Create an API endpoint that provides information about leisure activities near Landgraaf, including details on the Skihalle and other attractions mentioned on the webpage.
Generated: DETERMINISTIC_6f80d300ae9299d0
Batch ID: 20250612_162504
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.pinkpop.nl": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.skihallelandgraaf.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.mondoverde.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)

# Sample data representing leisure activities in Landgraaf
LEISURE_ACTIVITIES = [
    {
        "name": "Skihalle Landgraaf",
        "description": "Indoor skiing facility with slopes for all levels.",
        "location": "Landgraaf, Netherlands",
        "website": "https://www.skihallelandgraaf.com"
    },
    {
        "name": "Mondo Verde",
        "description": "A beautiful theme park featuring gardens from around the world.",
        "location": "Landgraaf, Netherlands",
        "website": "https://www.mondoverde.com"
    },
    {
        "name": "Pinkpop Music Festival",
        "description": "Famous annual music festival with international artists.",
        "location": "Landgraaf, Netherlands",
        "website": "https://www.pinkpop.nl"
    }
]

@app.route('/api/leisure-activities', methods=['GET'])
def get_leisure_activities():
    """
    API endpoint to retrieve information about leisure activities near Landgraaf.
    Returns:
        JSON response containing a list of activities with their details.
    """
    try:
        # Check for optional query parameters (e.g., filtering by keyword)
        keyword = request.args.get('keyword', '').lower()
        
        if keyword:
            # Filter activities based on the keyword
            filtered_activities = [
                activity for activity in LEISURE_ACTIVITIES
                if keyword in activity['name'].lower() or keyword in activity['description'].lower()
            ]
            return jsonify({"activities": filtered_activities, "count": len(filtered_activities)}), 200
        
        # Return all activities if no filter is applied
        return jsonify({"activities": LEISURE_ACTIVITIES, "count": len(LEISURE_ACTIVITIES)}), 200

    except Exception as e:
        # Log the error and return a 500 response
        logging.error(f"Error occurred while fetching leisure activities: {str(e)}")
        return jsonify({"error": "An internal server error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
