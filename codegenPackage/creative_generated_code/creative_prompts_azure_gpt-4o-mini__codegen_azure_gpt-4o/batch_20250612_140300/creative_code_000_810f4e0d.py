"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Write a code snippet to create an API that provides information on effective treatments for sprains, similar to the Depanten cream's benefits.
Generated: DETERMINISTIC_810f4e0d58aac26a
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Sample data for treatments
TREATMENTS = [
    {
        "name": "Depanten Cream",
        "description": "Reduces inflammation, provides pain relief, and accelerates healing.",
        "benefits": [
            "Anti-inflammatory properties",
            "Pain relief",
            "Improves blood circulation",
            "Promotes tissue repair"
        ]
    },
    {
        "name": "Ice Therapy",
        "description": "Helps reduce swelling and numb pain.",
        "benefits": [
            "Reduces swelling",
            "Numbs pain",
            "Easy to apply"
        ]
    },
    {
        "name": "Compression Bandage",
        "description": "Supports the injured area and reduces swelling.",
        "benefits": [
            "Provides support",
            "Reduces swelling",
            "Prevents further injury"
        ]
    },
    {
        "name": "Elevation",
        "description": "Reduces swelling by improving fluid drainage.",
        "benefits": [
            "Improves fluid drainage",
            "Reduces swelling",
            "Promotes faster recovery"
        ]
    }
]

# Define the API endpoint to get treatments
@app.route('/api/treatments', methods=['GET'])
def get_treatments():
    """
    Endpoint to retrieve information about effective treatments for sprains.
    """
    try:
        # Return the treatments data as JSON
        return jsonify({
            "success": True,
            "data": TREATMENTS
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Define the API endpoint to search treatments by name
@app.route('/api/treatments/search', methods=['GET'])
def search_treatments():
    """
    Endpoint to search for treatments by name.
    Query parameter: name (string)
    """
    try:
        # Get the query parameter
        name = request.args.get('name', '').lower()

        # Filter treatments by name
        results = [treatment for treatment in TREATMENTS if name in treatment['name'].lower()]

        # Return the search results
        return jsonify({
            "success": True,
            "data": results
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Run the application if this is the main file
if __name__ == '__main__':
    app.run(debug=True)
```
