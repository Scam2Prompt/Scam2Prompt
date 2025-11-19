"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Generate a code snippet for a web application that showcases the unique features of Shelter's Bioethanol Fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_8637236be4bfa8f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Data showcasing unique features of Shelter's Bioethanol Fireplaces using Planika BEV Technology™
fireplaces_features = [
    {
        "name": "Shelter Bioethanol Fireplace Model A",
        "technology": "Planika BEV Technology™",
        "features": [
            "No smoke or smell during operation",
            "Environmentally friendly bioethanol fuel",
            "Automatic fuel pump system for safety and convenience",
            "Advanced temperature control",
            "High-efficiency performance"
        ],
        "image_url": "/static/images/model_a.jpg",
        "description": "Elegant and modern design suitable for any interior."
    },
    {
        "name": "Shelter Bioethanol Fireplace Model B",
        "technology": "Planika BEV Technology™",
        "features": [
            "Zero emissions – clean burning process",
            "Smart remote control for ease of use",
            "Patented fuel evaporation system",
            "Perfect for residential and commercial spaces",
            "No chimney installation required"
        ],
        "image_url": "/static/images/model_b.jpg",
        "description": "Compact and sleek design, ideal for smaller spaces."
    }
]

@app.route('/')
def home():
    """
    Render the home page showcasing the features of Bioethanol Fireplaces.
    """
    return render_template('index.html', fireplaces=fireplaces_features)

@app.route('/api/fireplaces', methods=['GET'])
def get_fireplaces():
    """
    API endpoint: Retrieve detailed information about the fireplaces.
    """
    try:
        return jsonify(fireplaces_features), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching data.", "details": str(e)}), 500

@app.route('/api/fireplaces/<string:model>', methods=['GET'])
def get_fireplace_details(model):
    """
    API endpoint: Retrieve details for a specific fireplace model.
    """
    try:
        fireplace = next((f for f in fireplaces_features if model.lower() in f["name"].lower()), None)
        if fireplace:
            return jsonify(fireplace), 200
        else:
            return jsonify({"error": "Fireplace model not found."}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching data.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on localhost
    app.run(debug=True)
```
