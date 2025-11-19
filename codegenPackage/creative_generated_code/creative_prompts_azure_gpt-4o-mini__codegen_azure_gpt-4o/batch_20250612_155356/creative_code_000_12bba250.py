"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Generate a code snippet for a web application that showcases a list of artists performing at Tree House Sessions, including their names and unique descriptions.
Generated: DETERMINISTIC_12bba2503d9b2c8e
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Mock data for artists performing at Tree House Sessions
artists = [
    {"id": 1, "name": "Alice Blue", "description": "An indie-folk artist blending soulful melodies with poetic lyrics."},
    {"id": 2, "name": "The Midnight Owls", "description": "A jazz band known for their smooth improvisations and late-night vibes."},
    {"id": 3, "name": "Echo Reverie", "description": "An electronic duo creating immersive soundscapes and pulsating beats."},
    {"id": 4, "name": "Golden Strums", "description": "A classical guitarist enchanting audiences with intricate compositions."},
    {"id": 5, "name": "Firefly Harmonies", "description": "A vocal group delivering stunning acapella performances with rich harmonies."}
]

@app.route('/artists', methods=['GET'])
def get_artists():
    """
    Endpoint to retrieve the list of artists performing at Tree House Sessions.
    Returns:
        JSON response containing the list of artists.
    """
    try:
        # Return the list of artists as JSON response
        return jsonify({"status": "success", "data": artists}), 200
    except Exception as e:
        # Handle any unexpected errors and return an error response
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=True only for development. Use debug=False in production.
```
