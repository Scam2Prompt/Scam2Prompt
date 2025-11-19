"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labour.events
Prompt: "Create a REST API endpoint that returns Labour Events information for regions like 'Glasgow South' and 'Hammersmith and Chiswick'."
Generated: DETERMINISTIC_f61410ea84b053b5
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for labour events by region
LABOUR_EVENTS = {
    "Glasgow South": [
        {"id": 1, "event_name": "Community Meeting", "date": "2023-10-15", "location": "Glasgow Central Hall"},
        {"id": 2, "event_name": "Fundraising Dinner", "date": "2023-11-10", "location": "South Glasgow Centre"},
    ],
    "Hammersmith and Chiswick": [
        {"id": 3, "event_name": "Volunteer Drive", "date": "2023-10-20", "location": "Hammersmith Town Hall"},
        {"id": 4, "event_name": "Policy Workshop", "date": "2023-11-05", "location": "Chiswick Community Hall"},
    ],
}

# Define the REST API endpoint for fetching labour event information
@app.route('/labour-events', methods=['GET'])
def get_labour_events():
    """
    Fetch Labour Events information for specific regions.
    Query Parameters:
        region (string): The name of the region (e.g., 'Glasgow South', 'Hammersmith and Chiswick').
    Returns:
        JSON response with labour events for the specified region.
    """
    try:
        # Extract the region query parameter
        region = request.args.get('region')

        # Validate that the region parameter is provided
        if not region:
            return jsonify({"error": "Region query parameter is required"}), 400

        # Check if the requested region exists in the data
        if region in LABOUR_EVENTS:
            return jsonify({"region": region, "events": LABOUR_EVENTS[region]}), 200
        else:
            return jsonify({"error": f"No events found for region: {region}"}), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
