"""
Generated Code Metadata:
========================
Original URL: https://venus.farm
Prompt: Design a basic REST API for a farm management system inspired by venus.farm.
Generated: DETERMINISTIC_43da3418e96ce6ba
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database for simplicity
farms = []
crops = []

# Helper function to find a farm by ID
def find_farm(farm_id):
    return next((farm for farm in farms if farm['id'] == farm_id), None)

# Helper function to find a crop by ID
def find_crop(crop_id):
    return next((crop for crop in crops if crop['id'] == crop_id), None)

# Route: Get all farms
@app.route('/farms', methods=['GET'])
def get_farms():
    return jsonify(farms), 200

# Route: Create a new farm
@app.route('/farms', methods=['POST'])
def create_farm():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        abort(400, description="Invalid farm data. 'id' and 'name' are required.")
    if find_farm(data['id']):
        abort(400, description="Farm with this ID already exists.")
    farms.append(data)
    return jsonify(data), 201

# Route: Get a specific farm by ID
@app.route('/farms/<int:farm_id>', methods=['GET'])
def get_farm(farm_id):
    farm = find_farm(farm_id)
    if not farm:
        abort(404, description="Farm not found.")
    return jsonify(farm), 200

# Route: Delete a farm by ID
@app.route('/farms/<int:farm_id>', methods=['DELETE'])
def delete_farm(farm_id):
    farm = find_farm(farm_id)
    if not farm:
        abort(404, description="Farm not found.")
    farms.remove(farm)
    return jsonify({'message': 'Farm deleted successfully'}), 200

# Route: Get all crops
@app.route('/crops', methods=['GET'])
def get_crops():
    return jsonify(crops), 200

# Route: Create a new crop
@app.route('/crops', methods=['POST'])
def create_crop():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'farm_id' not in data:
        abort(400, description="Invalid crop data. 'id', 'name', and 'farm_id' are required.")
    if find_crop(data['id']):
        abort(400, description="Crop with this ID already exists.")
    if not find_farm(data['farm_id']):
        abort(400, description="Farm with this ID does not exist.")
    crops.append(data)
    return jsonify(data), 201

# Route: Get a specific crop by ID
@app.route('/crops/<int:crop_id>', methods=['GET'])
def get_crop(crop_id):
    crop = find_crop(crop_id)
    if not crop:
        abort(404, description="Crop not found.")
    return jsonify(crop), 200

# Route: Delete a crop by ID
@app.route('/crops/<int:crop_id>', methods=['DELETE'])
def delete_crop(crop_id):
    crop = find_crop(crop_id)
    if not crop:
        abort(404, description="Crop not found.")
    crops.remove(crop)
    return jsonify({'message': 'Crop deleted successfully'}), 200

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': error.description}), 400

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': error.description}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
