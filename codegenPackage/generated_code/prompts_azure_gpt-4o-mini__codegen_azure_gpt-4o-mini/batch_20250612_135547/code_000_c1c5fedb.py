"""
Generated Code Metadata:
========================
Original URL: https://suavv.com
Prompt: Generate a code snippet for a podcast application that features interviews with filmmakers like Kalia Love Jones, highlighting their impact on the industry.
Generated: DETERMINISTIC_c1c5fedb9ef4712a
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing podcasts
podcasts = [
    {
        "id": 1,
        "title": "Interview with Kalia Love Jones",
        "description": "A deep dive into the filmmaking journey of Kalia Love Jones and her impact on the industry.",
        "guest": "Kalia Love Jones",
        "date": "2023-10-01",
        "duration": "45:00"
    },
    {
        "id": 2,
        "title": "The Art of Filmmaking",
        "description": "Exploring the nuances of filmmaking with various industry experts.",
        "guest": "Various",
        "date": "2023-09-15",
        "duration": "60:00"
    }
]

@app.route('/podcasts', methods=['GET'])
def get_podcasts():
    """
    Retrieve the list of podcasts.
    Returns:
        JSON response containing the list of podcasts.
    """
    return jsonify(podcasts), 200

@app.route('/podcasts/<int:podcast_id>', methods=['GET'])
def get_podcast(podcast_id):
    """
    Retrieve a specific podcast by its ID.
    Args:
        podcast_id (int): The ID of the podcast to retrieve.
    Returns:
        JSON response containing the podcast details or an error message.
    """
    podcast = next((podcast for podcast in podcasts if podcast['id'] == podcast_id), None)
    if podcast is not None:
        return jsonify(podcast), 200
    else:
        return jsonify({"error": "Podcast not found"}), 404

@app.route('/podcasts', methods=['POST'])
def create_podcast():
    """
    Create a new podcast entry.
    Returns:
        JSON response containing the created podcast or an error message.
    """
    try:
        new_podcast = request.get_json()
        if not new_podcast or 'title' not in new_podcast or 'guest' not in new_podcast:
            return jsonify({"error": "Invalid podcast data"}), 400
        
        new_podcast['id'] = len(podcasts) + 1
        podcasts.append(new_podcast)
        return jsonify(new_podcast), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
