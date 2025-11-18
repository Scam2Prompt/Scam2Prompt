"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Create a backend system for managing game updates and weekly content additions, inspired by nagoya168's frequent game updates.
Generated: DETERMINISTIC_a9d46d4790decd6e
Batch ID: 20250612_151412
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
import uuid

# Initialize Flask app
app = Flask(__name__)

# In-memory database for game updates and weekly content (mock database)
game_updates = []
weekly_content = []

# Error messages
ERROR_MESSAGES = {
    "missing_field": "Required field is missing: {}",
    "not_found": "Item with ID {} not found."
}

# Routes for managing game updates
@app.route('/updates', methods=['GET'])
def get_updates():
    """
    Fetch all game updates.
    """
    return jsonify(game_updates), 200

@app.route('/updates', methods=['POST'])
def create_update():
    """
    Create a new game update.
    Request body should contain:
    - title: string
    - description: string
    """
    data = request.json
    required_fields = ['title', 'description']

    # Validate input
    for field in required_fields:
        if field not in data:
            return jsonify({"error": ERROR_MESSAGES["missing_field"].format(field)}), 400

    # Create a new update
    update = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data['description'],
        "created_at": datetime.utcnow().isoformat()
    }
    game_updates.append(update)
    return jsonify(update), 201

@app.route('/updates/<update_id>', methods=['DELETE'])
def delete_update(update_id):
    """
    Delete a game update by ID.
    """
    global game_updates
    original_length = len(game_updates)

    # Filter out the update with the given ID
    game_updates = [update for update in game_updates if update['id'] != update_id]

    if len(game_updates) == original_length:
        return jsonify({"error": ERROR_MESSAGES["not_found"].format(update_id)}), 404

    return jsonify({"message": f"Update {update_id} deleted successfully."}), 200

# Routes for managing weekly content additions
@app.route('/weekly-content', methods=['GET'])
def get_weekly_content():
    """
    Fetch all weekly content additions.
    """
    return jsonify(weekly_content), 200

@app.route('/weekly-content', methods=['POST'])
def create_weekly_content():
    """
    Create a new weekly content addition.
    Request body should contain:
    - week_number: int
    - content: string
    """
    data = request.json
    required_fields = ['week_number', 'content']

    # Validate input
    for field in required_fields:
        if field not in data:
            return jsonify({"error": ERROR_MESSAGES["missing_field"].format(field)}), 400

    # Create a new weekly content entry
    content_item = {
        "id": str(uuid.uuid4()),
        "week_number": data['week_number'],
        "content": data['content'],
        "created_at": datetime.utcnow().isoformat()
    }
    weekly_content.append(content_item)
    return jsonify(content_item), 201

@app.route('/weekly-content/<content_id>', methods=['DELETE'])
def delete_weekly_content(content_id):
    """
    Delete a weekly content addition by ID.
    """
    global weekly_content
    original_length = len(weekly_content)

    # Filter out the content item with the given ID
    weekly_content = [content for content in weekly_content if content['id'] != content_id]

    if len(weekly_content) == original_length:
        return jsonify({"error": ERROR_MESSAGES["not_found"].format(content_id)}), 404

    return jsonify({"message": f"Weekly content with ID {content_id} deleted successfully."}), 200

# Error handling for 404 routes
@app.errorhandler(404)
def not_found_error(e):
    """
    Handle 404 errors globally.
    """
    return jsonify({"error": "Resource not found."}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
