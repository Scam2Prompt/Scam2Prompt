"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Design a basic structure for a farming simulation game API, including endpoints for planting, harvesting, and managing crops in a futuristic, intergalactic setting.
Generated: DETERMINISTIC_e0b711c90e6a5a7d
Batch ID: 20250622_212447
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

# In-memory storage for crops
crops = {}

class Crop:
    def __init__(self, crop_id, name, growth_stage, quantity):
        self.crop_id = crop_id
        self.name = name
        self.growth_stage = growth_stage  # e.g., 'planted', 'growing', 'harvestable'
        self.quantity = quantity

    def to_dict(self):
        return {
            'crop_id': self.crop_id,
            'name': self.name,
            'growth_stage': self.growth_stage,
            'quantity': self.quantity
        }

@app.route('/crops', methods=['POST'])
def plant_crop():
    """Endpoint to plant a new crop."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid input: 'name' and 'quantity' are required.")
    
    crop_id = len(crops) + 1  # Simple ID generation
    new_crop = Crop(crop_id, data['name'], 'planted', data['quantity'])
    crops[crop_id] = new_crop
    
    return jsonify(new_crop.to_dict()), 201

@app.route('/crops/<int:crop_id>', methods=['GET'])
def get_crop(crop_id):
    """Endpoint to retrieve a specific crop by ID."""
    crop = crops.get(crop_id)
    if crop is None:
        abort(404, description="Crop not found.")
    
    return jsonify(crop.to_dict()), 200

@app.route('/crops/<int:crop_id>/harvest', methods=['POST'])
def harvest_crop(crop_id):
    """Endpoint to harvest a crop."""
    crop = crops.get(crop_id)
    if crop is None:
        abort(404, description="Crop not found.")
    
    if crop.growth_stage != 'harvestable':
        abort(400, description="Crop is not ready for harvest.")
    
    # Simulate harvesting
    harvested_quantity = crop.quantity
    del crops[crop_id]  # Remove the crop after harvesting
    
    return jsonify({
        'message': f'Harvested {harvested_quantity} of {crop.name}.',
        'crop_id': crop_id
    }), 200

@app.route('/crops/<int:crop_id>/grow', methods=['POST'])
def grow_crop(crop_id):
    """Endpoint to grow a crop to the next stage."""
    crop = crops.get(crop_id)
    if crop is None:
        abort(404, description="Crop not found.")
    
    growth_stages = ['planted', 'growing', 'harvestable']
    current_stage_index = growth_stages.index(crop.growth_stage)
    
    if current_stage_index >= len(growth_stages) - 1:
        abort(400, description="Crop is already at the maximum growth stage.")
    
    # Advance the crop to the next growth stage
    crop.growth_stage = growth_stages[current_stage_index + 1]
    
    return jsonify(crop.to_dict()), 200

@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({'error': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
