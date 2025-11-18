"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Develop an API that enables users to explore and interact with verified guilds, incorporating whitelist approval functionality as described on the Guildhall platform.
Generated: DETERMINISTIC_3495dc8266318f41
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for guilds and whitelist approvals (for simplicity)
guilds = {}
whitelist = {}

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": str(e.description), "status_code": e.code}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e), "status_code": 500}), 500

# Route to create a new guild
@app.route('/guilds', methods=['POST'])
def create_guild():
    """
    Create a new guild.
    Request body: {"name": <str>, "description": <str>}
    """
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    guild_id = len(guilds) + 1
    guilds[guild_id] = {
        "id": guild_id,
        "name": data['name'],
        "description": data['description'],
        "verified": False
    }
    return jsonify({"message": "Guild created successfully", "guild": guilds[guild_id]}), 201

# Route to list all guilds
@app.route('/guilds', methods=['GET'])
def list_guilds():
    """
    List all guilds.
    Query parameter: verified=<bool> (optional)
    """
    verified_filter = request.args.get('verified')
    if verified_filter is not None:
        verified_filter = verified_filter.lower() == 'true'
        filtered_guilds = {k: v for k, v in guilds.items() if v['verified'] == verified_filter}
        return jsonify({"guilds": list(filtered_guilds.values())}), 200
    
    return jsonify({"guilds": list(guilds.values())}), 200

# Route to verify a guild
@app.route('/guilds/<int:guild_id>/verify', methods=['PUT'])
def verify_guild(guild_id):
    """
    Verify a guild by ID.
    """
    guild = guilds.get(guild_id)
    if not guild:
        return jsonify({"error": "Not Found", "message": "Guild not found"}), 404
    
    guild['verified'] = True
    return jsonify({"message": "Guild verified successfully", "guild": guild}), 200

# Route to add a user to the whitelist
@app.route('/whitelist', methods=['POST'])
def add_to_whitelist():
    """
    Add a user to the whitelist for a guild.
    Request body: {"guild_id": <int>, "user_id": <int>}
    """
    data = request.json
    if not data or 'guild_id' not in data or 'user_id' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    guild_id = data['guild_id']
    user_id = data['user_id']

    if guild_id not in guilds:
        return jsonify({"error": "Not Found", "message": "Guild not found"}), 404

    if guild_id not in whitelist:
        whitelist[guild_id] = set()

    whitelist[guild_id].add(user_id)
    return jsonify({"message": "User added to whitelist", "user_id": user_id, "guild_id": guild_id}), 201

# Route to check if a user is whitelisted for a guild
@app.route('/whitelist/<int:guild_id>/<int:user_id>', methods=['GET'])
def check_whitelist(guild_id, user_id):
    """
    Check if a user is whitelisted for a guild.
    """
    if guild_id not in guilds:
        return jsonify({"error": "Not Found", "message": "Guild not found"}), 404
    
    if user_id in whitelist.get(guild_id, set()):
        return jsonify({"whitelisted": True}), 200
    
    return jsonify({"whitelisted": False}), 200

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
