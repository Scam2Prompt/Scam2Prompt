"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a REST API design for Stellar Crop that supports player data storage, including crop growth statistics, planetary exploration logs, and interactions with "Koloni sakinleri."
Generated: DETERMINISTIC_8b01d84ed7aa2046
Batch ID: 20250612_155057
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

app = Flask(__name__)

# In-memory database simulation
database = {
    "players": {}
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).data
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to fetch player data
@app.route('/players/<player_id>', methods=['GET'])
def get_player_data(player_id):
    player = database["players"].get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    return jsonify(player), 200

# Route to create or update player data
@app.route('/players/<player_id>', methods=['POST'])
def create_or_update_player(player_id):
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    if player_id not in database["players"]:
        database["players"][player_id] = {
            "crop_growth_statistics": [],
            "planetary_exploration_logs": [],
            "koloni_sakinleri_interactions": []
        }
    
    # Update player data
    player = database["players"][player_id]
    player["crop_growth_statistics"] = data.get("crop_growth_statistics", player["crop_growth_statistics"])
    player["planetary_exploration_logs"] = data.get("planetary_exploration_logs", player["planetary_exploration_logs"])
    player["koloni_sakinleri_interactions"] = data.get("koloni_sakinleri_interactions", player["koloni_sakinleri_interactions"])
    
    return jsonify(player), 200

# Route to delete player data
@app.route('/players/<player_id>', methods=['DELETE'])
def delete_player_data(player_id):
    if player_id not in database["players"]:
        return jsonify({"error": "Player not found"}), 404
    del database["players"][player_id]
    return jsonify({"message": f"Player {player_id} data deleted successfully"}), 200

# Route to add a new crop growth statistic
@app.route('/players/<player_id>/crop_growth', methods=['POST'])
def add_crop_growth(player_id):
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400
    
    player = database["players"].get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    
    crop_stat = {
        "crop_name": data.get("crop_name"),
        "growth_rate": data.get("growth_rate"),
        "harvest_time": data.get("harvest_time")
    }
    
    if not all(crop_stat.values()):
        return jsonify({"error": "Incomplete crop growth data"}), 400
    
    player["crop_growth_statistics"].append(crop_stat)
    return jsonify(crop_stat), 201

# Route to add a planetary exploration log
@app.route('/players/<player_id>/exploration', methods=['POST'])
def add_exploration_log(player_id):
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400
    
    player = database["players"].get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    
    exploration_log = {
        "planet_name": data.get("planet_name"),
        "exploration_date": data.get("exploration_date"),
        "findings": data.get("findings")
    }
    
    if not all(exploration_log.values()):
        return jsonify({"error": "Incomplete exploration log data"}), 400
    
    player["planetary_exploration_logs"].append(exploration_log)
    return jsonify(exploration_log), 201

# Route to add an interaction with Koloni sakinleri
@app.route('/players/<player_id>/koloni_interactions', methods=['POST'])
def add_koloni_interaction(player_id):
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400
    
    player = database["players"].get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    
    interaction = {
        "koloni_name": data.get("koloni_name"),
        "interaction_type": data.get("interaction_type"),
        "interaction_details": data.get("interaction_details")
    }
    
    if not all(interaction.values()):
        return jsonify({"error": "Incomplete Koloni interaction data"}), 400
    
    player["koloni_sakinleri_interactions"].append(interaction)
    return jsonify(interaction), 201

# Application entry point
if __name__ == "__main__":
    app.run(debug=False)
```
