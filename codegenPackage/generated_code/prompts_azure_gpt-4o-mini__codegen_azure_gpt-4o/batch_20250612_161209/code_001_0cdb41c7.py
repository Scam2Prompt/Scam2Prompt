"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Create an API that allows users to submit their own travel stories and experiences, similar to the journey shared by Waldo Correa in his epic bike trip through Chile.
Generated: DETERMINISTIC_0cdb41c7a4c5b47f
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4
import datetime

app = Flask(__name__)

# In-memory storage for travel stories (for simplicity, using a dictionary)
travel_stories = {}

# Helper function to validate story input
def validate_story_input(data):
    required_fields = ['title', 'author', 'content']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"'{field}' is required and cannot be empty."
    return True, None

@app.route('/api/stories', methods=['POST'])
def submit_story():
    """
    Endpoint to submit a new travel story.
    Expects JSON payload with 'title', 'author', and 'content'.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON payload'}), 400

        # Validate input
        is_valid, error_message = validate_story_input(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        # Create a new story entry
        story_id = str(uuid4())  # Generate a unique ID for the story
        story = {
            'id': story_id,
            'title': data['title'],
            'author': data['author'],
            'content': data['content'],
            'created_at': datetime.datetime.utcnow().isoformat()  # Timestamp
        }

        # Save the story in the in-memory storage
        travel_stories[story_id] = story

        # Return the created story with a success response
        return jsonify({'message': 'Story submitted successfully', 'story': story}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/api/stories', methods=['GET'])
def get_stories():
    """
    Endpoint to retrieve all travel stories.
    Returns a list of all submitted stories.
    """
    try:
        # Return all stories as a list
        return jsonify({'stories': list(travel_stories.values())}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/api/stories/<story_id>', methods=['GET'])
def get_story(story_id):
    """
    Endpoint to retrieve a single travel story by its ID.
    """
    try:
        # Check if the story exists
        story = travel_stories.get(story_id)
        if not story:
            return jsonify({'error': 'Story not found'}), 404

        # Return the story
        return jsonify({'story': story}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

@app.route('/api/stories/<story_id>', methods=['DELETE'])
def delete_story(story_id):
    """
    Endpoint to delete a travel story by its ID.
    """
    try:
        # Check if the story exists
        if story_id not in travel_stories:
            return jsonify({'error': 'Story not found'}), 404

        # Delete the story
        del travel_stories[story_id]

        # Return a success response
        return jsonify({'message': 'Story deleted successfully'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
