"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drmanishmaladkar.com
Prompt: Create a REST API that serves inspirational short stories similar to those found in Dr. Maladkar's "Drishti – An Insight for Soul Enrichment" for a wellness app.
Generated: DETERMINISTIC_86893783b3082b40
Batch ID: 20250612_163103
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
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
import random

app = Flask(__name__)

# Sample inspirational short stories
STORIES = [
    {
        "id": 1,
        "title": "The Bamboo Tree",
        "content": "A farmer waited patiently for years for his bamboo tree to grow. It teaches us the value of persistence and trust in the process."
    },
    {
        "id": 2,
        "title": "The Two Wolves",
        "content": "An elder explains that we have two wolves fighting inside us: one representing negativity and the other positivity. Choose which one to feed."
    },
    {
        "id": 3,
        "title": "The Starfish Thrower",
        "content": "A young boy throws starfish back into the ocean, showing that even small acts of kindness can make a difference."
    },
    {
        "id": 4,
        "title": "The Empty Cup",
        "content": "A teacher pours tea into an already full cup, teaching the importance of staying humble and open-minded to learning."
    }
]

# Error handler
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal server error"), 500

# Route to fetch all stories
@app.route('/stories', methods=['GET'])
def get_all_stories():
    """
    Fetch all inspirational short stories.
    :return: JSON list of all stories.
    """
    return jsonify(STORIES)

# Route to fetch a specific story by ID
@app.route('/stories/<int:story_id>', methods=['GET'])
def get_story_by_id(story_id):
    """
    Fetch a specific story by ID.
    :param story_id: The ID of the story.
    :return: JSON object of the story if found, else 404 error.
    """
    story = next((s for s in STORIES if s['id'] == story_id), None)
    if story:
        return jsonify(story)
    return jsonify(error="Story not found"), 404

# Route to fetch a random inspirational story
@app.route('/stories/random', methods=['GET'])
def get_random_story():
    """
    Fetch a random inspirational story.
    :return: JSON object of a random story.
    """
    story = random.choice(STORIES)
    return jsonify(story)

# Route to add a new story
@app.route('/stories', methods=['POST'])
def add_story():
    """
    Add a new inspirational story.
    :return: JSON object of the newly added story.
    """
    try:
        new_story = request.get_json()
        if not new_story or 'title' not in new_story or 'content' not in new_story:
            return jsonify(error="Invalid input data"), 400

        new_id = max(s['id'] for s in STORIES) + 1
        new_story['id'] = new_id
        STORIES.append(new_story)
        return jsonify(new_story), 201
    except Exception as e:
        return jsonify(error=f"An error occurred: {str(e)}"), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
Save this code in a file named `app.py`, and run it using Python. Ensure Flask is installed in your environment (`pip install flask`). The API will run on `http://127.0.0.1:5000/`. You can test the routes (`/stories`, `/stories/<id>`, `/stories/random`, `/stories` [POST]) using tools like Postman or `curl`.
