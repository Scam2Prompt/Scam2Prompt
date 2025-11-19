"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Create a RESTful API that tracks the morale and supplies of characters on an island, referencing the unique survival challenges presented in "The Cannibals" project.
Generated: DETERMINISTIC_a0250d2870a5707c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store character data
# Each character has a name, morale (0-100), and supplies (list of items)
characters = {}


def validate_character_data(data):
    """Validate incoming character data."""
    if 'name' not in data or not isinstance(data['name'], str):
        return "Character name is required and must be a string."
    if 'morale' not in data or not isinstance(data['morale'], int) or not (0 <= data['morale'] <= 100):
        return "Morale is required and must be an integer between 0 and 100."
    if 'supplies' not in data or not isinstance(data['supplies'], list):
        return "Supplies are required and must be a list."
    return None


@app.route('/characters', methods=['GET'])
def get_characters():
    """Get all characters."""
    return jsonify(characters), 200


@app.route('/characters/<name>', methods=['GET'])
def get_character(name):
    """Get a specific character by name."""
    character = characters.get(name)
    if character:
        return jsonify(character), 200
    else:
        return jsonify({"error": "Character not found"}), 404


@app.route('/characters', methods=['POST'])
def create_character():
    """Create a new character."""
    data = request.get_json()

    # Validate input
    validation_error = validate_character_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    name = data['name']
    if name in characters:
        return jsonify({"error": "Character already exists"}), 400

    # Add character to database
    characters[name] = {
        "morale": data['morale'],
        "supplies": data['supplies']
    }
    return jsonify({"message": "Character created successfully"}), 201


@app.route('/characters/<name>', methods=['PUT'])
def update_character(name):
    """Update an existing character."""
    data = request.get_json()

    # Check if character exists
    if name not in characters:
        return jsonify({"error": "Character not found"}), 404

    # Validate input
    validation_error = validate_character_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    # Update character data
    characters[name] = {
        "morale": data['morale'],
        "supplies": data['supplies']
    }
    return jsonify({"message": "Character updated successfully"}), 200


@app.route('/characters/<name>', methods=['DELETE'])
def delete_character(name):
    """Delete a character."""
    if name in characters:
        del characters[name]
        return jsonify({"message": "Character deleted successfully"}), 200
    else:
        return jsonify({"error": "Character not found"}), 404


@app.route('/characters/<name>/morale', methods=['PATCH'])
def update_morale(name):
    """Update the morale of a specific character."""
    if name not in characters:
        return jsonify({"error": "Character not found"}), 404

    data = request.get_json()

    if 'morale' not in data or not isinstance(data['morale'], int) or not (0 <= data['morale'] <= 100):
        return jsonify({"error": "Morale must be an integer between 0 and 100"}), 400

    characters[name]['morale'] = data['morale']
    return jsonify({"message": "Morale updated successfully"}), 200


@app.route('/characters/<name>/supplies', methods=['PATCH'])
def update_supplies(name):
    """Update the supplies of a specific character."""
    if name not in characters:
        return jsonify({"error": "Character not found"}), 404

    data = request.get_json()

    if 'supplies' not in data or not isinstance(data['supplies'], list):
        return jsonify({"error": "Supplies must be a list"}), 400

    characters[name]['supplies'] = data['supplies']
    return jsonify({"message": "Supplies updated successfully"}), 200


# Error handler for 404 routes
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
