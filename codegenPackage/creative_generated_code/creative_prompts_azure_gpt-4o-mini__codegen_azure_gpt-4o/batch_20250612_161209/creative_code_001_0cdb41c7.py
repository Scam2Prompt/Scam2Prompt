"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waldoenruta.com
Prompt: Create an API that allows users to submit their own travel stories and experiences, similar to the journey shared by Waldo Correa in his epic bike trip through Chile.
Generated: DETERMINISTIC_0cdb41c7a4c5b47f
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for travel stories (to be replaced with a database in production)
travel_stories = []

# Helper function to validate incoming data
def validate_story(data):
    required_fields = ['title', 'author', 'content']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    return True, None

@app.route('/stories', methods=['POST'])
def create_story():
    """
    Endpoint to submit a new travel story.
    Expects JSON data with 'title', 'author', and 'content' keys.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate the incoming data
        is_valid, error = validate_story(data)
        if not is_valid:
            return jsonify({"error": error}), 400

        # Create the travel story object
        story = {
            "id": len(travel_stories) + 1,  # Auto-increment ID
            "title": data["title"],
            "author": data["author"],
            "content": data["content"],
            "created_at": datetime.utcnow().isoformat()
        }

        # Add the new story to the in-memory list
        travel_stories.append(story)

        # Return the created story and success response
        return jsonify({"message": "Story created successfully!", "story": story}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/stories', methods=['GET'])
def list_stories():
    """
    Endpoint to fetch all travel stories.
    Returns a JSON list of all submitted travel stories.
    """
    return jsonify({"stories": travel_stories}), 200

@app.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """
    Endpoint to fetch a specific travel story by its ID.
    """
    try:
        # Search for the story by ID
        story = next((s for s in travel_stories if s["id"] == story_id), None)

        if story is None:
            return jsonify({"error": "Story not found"}), 404

        # Return the requested story
        return jsonify({"story": story}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/stories/<int:story_id>', methods=['DELETE'])
def delete_story(story_id):
    """
    Endpoint to delete a specific travel story by its ID.
    """
    try:
        global travel_stories

        # Find the story by ID
        story = next((s for s in travel_stories if s["id"] == story_id), None)

        if story is None:
            return jsonify({"error": "Story not found"}), 404

        # Remove the story from the list
        travel_stories = [s for s in travel_stories if s["id"] != story_id]

        # Return a success response
        return jsonify({"message": "Story deleted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use debug mode for development, not suitable for production
    app.run(debug=True)
```
