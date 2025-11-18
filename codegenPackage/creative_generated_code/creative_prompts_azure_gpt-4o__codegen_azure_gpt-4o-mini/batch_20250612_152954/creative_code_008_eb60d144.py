"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vantardxyz.web.app
Prompt: Develop an API to submit pitches to the "Tard Tank" feature on the Vantard website, allowing basement developers to propose new meme coin ideas.
Generated: DETERMINISTIC_eb60d144bc2688cd
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from datetime import datetime
import json
import os

app = Flask(__name__)

# In-memory storage for pitches (for production, consider using a database)
pitches = []

class Pitch:
    def __init__(self, name, description, developer):
        self.name = name
        self.description = description
        self.developer = developer
        self.submission_time = datetime.utcnow()

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'developer': self.developer,
            'submission_time': self.submission_time.isoformat()
        }

@app.route('/api/pitches', methods=['POST'])
def submit_pitch():
    """
    Endpoint to submit a new pitch to the Tard Tank.
    Expects JSON payload with 'name', 'description', and 'developer'.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()

        # Validate input data
        if not data or 'name' not in data or 'description' not in data or 'developer' not in data:
            raise BadRequest("Missing required fields: name, description, developer")

        # Create a new pitch and store it
        new_pitch = Pitch(
            name=data['name'],
            description=data['description'],
            developer=data['developer']
        )
        pitches.append(new_pitch)

        # Return success response with the pitch data
        return jsonify(new_pitch.to_dict()), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400

    except Exception as e:
        # Log unexpected errors for debugging
        app.logger.error(f'Unexpected error: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/pitches', methods=['GET'])
def get_pitches():
    """
    Endpoint to retrieve all submitted pitches.
    Returns a JSON array of pitches.
    """
    return jsonify([pitch.to_dict() for pitch in pitches]), 200

if __name__ == '__main__':
    # Ensure the server runs in production mode
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
```

This code provides a simple Flask API for submitting and retrieving pitches for a meme coin idea. It uses in-memory storage for demonstration purposes, but for production use, a persistent database (like PostgreSQL, MongoDB, etc.) should be implemented. The API includes proper error handling, input validation, and relevant HTTP status codes.
