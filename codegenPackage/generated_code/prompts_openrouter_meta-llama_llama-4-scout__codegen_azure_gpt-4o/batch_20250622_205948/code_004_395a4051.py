"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: "Design a REST API for WPControl to manage WordPress themes and patterns remotely."
Generated: DETERMINISTIC_395a405187a9cb7b
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Mock data for themes and patterns
themes = [
    {"id": 1, "name": "Twenty Twenty-One", "status": "active"},
    {"id": 2, "name": "Twenty Twenty-Two", "status": "inactive"},
]

patterns = [
    {"id": 1, "name": "Hero Section", "status": "enabled"},
    {"id": 2, "name": "Footer Section", "status": "disabled"},
]

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to get all themes
@app.route('/api/themes', methods=['GET'])
def get_themes():
    return jsonify({"themes": themes}), 200

# Route to get a specific theme by ID
@app.route('/api/themes/<int:theme_id>', methods=['GET'])
def get_theme(theme_id):
    theme = next((t for t in themes if t["id"] == theme_id), None)
    if theme:
        return jsonify({"theme": theme}), 200
    return jsonify({"error": "Theme not found"}), 404

# Route to update a theme's status
@app.route('/api/themes/<int:theme_id>', methods=['PUT'])
def update_theme(theme_id):
    theme = next((t for t in themes if t["id"] == theme_id), None)
    if not theme:
        return jsonify({"error": "Theme not found"}), 404

    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400

    theme["status"] = data["status"]
    return jsonify({"message": "Theme updated successfully", "theme": theme}), 200

# Route to get all patterns
@app.route('/api/patterns', methods=['GET'])
def get_patterns():
    return jsonify({"patterns": patterns}), 200

# Route to get a specific pattern by ID
@app.route('/api/patterns/<int:pattern_id>', methods=['GET'])
def get_pattern(pattern_id):
    pattern = next((p for p in patterns if p["id"] == pattern_id), None)
    if pattern:
        return jsonify({"pattern": pattern}), 200
    return jsonify({"error": "Pattern not found"}), 404

# Route to update a pattern's status
@app.route('/api/patterns/<int:pattern_id>', methods=['PUT'])
def update_pattern(pattern_id):
    pattern = next((p for p in patterns if p["id"] == pattern_id), None)
    if not pattern:
        return jsonify({"error": "Pattern not found"}), 404

    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400

    pattern["status"] = data["status"]
    return jsonify({"message": "Pattern updated successfully", "pattern": pattern}), 200

# Route to add a new theme
@app.route('/api/themes', methods=['POST'])
def add_theme():
    data = request.get_json()
    if "name" not in data or "status" not in data:
        return jsonify({"error": "Missing 'name' or 'status' field"}), 400

    new_theme = {
        "id": len(themes) + 1,
        "name": data["name"],
        "status": data["status"]
    }
    themes.append(new_theme)
    return jsonify({"message": "Theme added successfully", "theme": new_theme}), 201

# Route to add a new pattern
@app.route('/api/patterns', methods=['POST'])
def add_pattern():
    data = request.get_json()
    if "name" not in data or "status" not in data:
        return jsonify({"error": "Missing 'name' or 'status' field"}), 400

    new_pattern = {
        "id": len(patterns) + 1,
        "name": data["name"],
        "status": data["status"]
    }
    patterns.append(new_pattern)
    return jsonify({"message": "Pattern added successfully", "pattern": new_pattern}), 201

# Route to delete a theme
@app.route('/api/themes/<int:theme_id>', methods=['DELETE'])
def delete_theme(theme_id):
    global themes
    theme = next((t for t in themes if t["id"] == theme_id), None)
    if not theme:
        return jsonify({"error": "Theme not found"}), 404

    themes = [t for t in themes if t["id"] != theme_id]
    return jsonify({"message": "Theme deleted successfully"}), 200

# Route to delete a pattern
@app.route('/api/patterns/<int:pattern_id>', methods=['DELETE'])
def delete_pattern(pattern_id):
    global patterns
    pattern = next((p for p in patterns if p["id"] == pattern_id), None)
    if not pattern:
        return jsonify({"error": "Pattern not found"}), 404

    patterns = [p for p in patterns if p["id"] != pattern_id]
    return jsonify({"message": "Pattern deleted successfully"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
