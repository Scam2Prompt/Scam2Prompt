"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Create a REST API in Flask to serve data about "Social Impact Heroes," including their categories, featured stories, and latest interviews.
Generated: DETERMINISTIC_7d7220ee12b93de8
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data for Social Impact Heroes
social_impact_heroes = [
    {
        "id": 1,
        "name": "Jane Doe",
        "category": "Environmental Activism",
        "featured_story": "Leading the charge against plastic pollution",
        "latest_interview": "Discussing innovative solutions for clean oceans",
    },
    {
        "id": 2,
        "name": "John Smith",
        "category": "Human Rights Advocacy",
        "featured_story": "Fighting for equal opportunities worldwide",
        "latest_interview": "Exploring challenges in the fight for justice",
    },
]

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health status of the API.
    """
    return jsonify({"status": "OK"}), 200

# Get all Social Impact Heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    """
    Endpoint to fetch all Social Impact Heroes.
    """
    return jsonify({"heroes": social_impact_heroes}), 200

# Get a specific Social Impact Hero by ID
@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero_by_id(hero_id):
    """
    Endpoint to fetch a specific Social Impact Hero by their ID.
    """
    hero = next((hero for hero in social_impact_heroes if hero["id"] == hero_id), None)
    if hero is None:
        abort(404, description=f"Hero with ID {hero_id} not found")
    return jsonify(hero), 200

# Add a new Social Impact Hero
@app.route('/heroes', methods=['POST'])
def add_hero():
    """
    Endpoint to add a new Social Impact Hero.
    """
    if not request.json or not all(k in request.json for k in ("name", "category", "featured_story", "latest_interview")):
        abort(400, description="Invalid data provided")
    
    new_hero = {
        "id": len(social_impact_heroes) + 1,
        "name": request.json["name"],
        "category": request.json["category"],
        "featured_story": request.json["featured_story"],
        "latest_interview": request.json["latest_interview"],
    }
    social_impact_heroes.append(new_hero)
    return jsonify(new_hero), 201

# Update an existing Social Impact Hero by ID
@app.route('/heroes/<int:hero_id>', methods=['PUT'])
def update_hero(hero_id):
    """
    Endpoint to update a specific Social Impact Hero's details.
    """
    hero = next((hero for hero in social_impact_heroes if hero["id"] == hero_id), None)
    if hero is None:
        abort(404, description=f"Hero with ID {hero_id} not found")
    
    if not request.json:
        abort(400, description="Invalid data provided")

    hero.update({
        "name": request.json.get("name", hero["name"]),
        "category": request.json.get("category", hero["category"]),
        "featured_story": request.json.get("featured_story", hero["featured_story"]),
        "latest_interview": request.json.get("latest_interview", hero["latest_interview"]),
    })
    return jsonify(hero), 200

# Delete a Social Impact Hero by ID
@app.route('/heroes/<int:hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    """
    Endpoint to delete a specific Social Impact Hero.
    """
    hero = next((hero for hero in social_impact_heroes if hero["id"] == hero_id), None)
    if hero is None:
        abort(404, description=f"Hero with ID {hero_id} not found")
    
    social_impact_heroes.remove(hero)
    return jsonify({"message": f"Hero with ID {hero_id} deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 Not Found.
    """
    return jsonify({"error": "Not Found", "message": error.description}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request_error(error):
    """
    Custom error handler for 400 Bad Request.
    """
    return jsonify({"error": "Bad Request", "message": error.description}), 400

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
