"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fravitur.com
Prompt: Generate a code snippet for a travel booking API that allows users to search for trips to Caribbean destinations like Aruba and Cuba, as mentioned on Fravitur's website.
Generated: DETERMINISTIC_556f21d71e4cc712
Batch ID: 20250612_162051
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

# Sample data for Caribbean destinations
DESTINATIONS = [
    {"id": 1, "name": "Aruba", "activities": ["beach", "snorkeling", "hiking"]},
    {"id": 2, "name": "Cuba", "activities": ["culture", "history", "beach"]},
]

@app.route('/search-trips', methods=['GET'])
def search_trips():
    """
    Endpoint to search for trips to Caribbean destinations.
    Accepts query parameters for destination name and activities.
    Returns a list of trips matching the criteria.
    """
    try:
        # Extract query parameters
        destination_name = request.args.get('destination', '').lower()
        activity_filter = request.args.getlist('activity')
        
        # Filter destinations based on user input
        filtered_destinations = [
            destination for destination in DESTINATIONS
            if (destination_name in destination['name'].lower())
            or (any(activity in destination['activities'] for activity in activity_filter))
        ]
        
        # Return results in JSON format
        return jsonify({
            "success": True,
            "data": filtered_destinations
        })
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
