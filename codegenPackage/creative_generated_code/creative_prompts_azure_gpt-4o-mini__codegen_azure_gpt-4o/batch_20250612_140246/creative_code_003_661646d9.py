"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tinfun.pages.dev
Prompt: Create a sample API endpoint that retrieves information about the various characters in TinFun, such as their roles and attributes within the adventure.
Generated: DETERMINISTIC_661646d9e9508b86
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Sample data representing TinFun characters
characters = [
    {
        "id": 1,
        "name": "Arakon",
        "role": "Warrior",
        "attributes": {
            "strength": 85,
            "intelligence": 60,
            "agility": 70
        }
    },
    {
        "id": 2,
        "name": "Lurien",
        "role": "Mage",
        "attributes": {
            "strength": 40,
            "intelligence": 95,
            "agility": 50
        }
    },
    {
        "id": 3,
        "name": "Feyra",
        "role": "Archer",
        "attributes": {
            "strength": 65,
            "intelligence": 70,
            "agility": 90
        }
    }
]

@app.route('/api/characters', methods=['GET'])
def get_characters():
    """
    API endpoint to retrieve all TinFun characters.
    :return: JSON response containing character details.
    """
    try:
        # Return the list of characters as JSON
        return jsonify({"success": True, "data": characters}), 200
    except Exception as e:
        # Log the error and return a server error response
        app.logger.error(f"Error retrieving characters: {e}")
        return jsonify({"success": False, "message": "Internal server error"}), 500

@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    """
    API endpoint to retrieve a TinFun character by their ID.
    :param character_id: ID of the character to retrieve.
    :return: JSON response containing character details or error message.
    """
    try:
        # Find the character with the given ID
        character = next((char for char in characters if char["id"] == character_id), None)
        
        if character:
            # Return the character details as JSON
            return jsonify({"success": True, "data": character}), 200
        else:
            # Character not found, return a 404 response
            return jsonify({"success": False, "message": "Character not found"}), 404
    except Exception as e:
        # Log the error and return a server error response
        app.logger.error(f"Error retrieving character with ID {character_id}: {e}")
        return jsonify({"success": False, "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run(debug=True)
```
