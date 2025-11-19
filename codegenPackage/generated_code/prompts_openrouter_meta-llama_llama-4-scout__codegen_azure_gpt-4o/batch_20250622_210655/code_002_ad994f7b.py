"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Design a simple API to track and manage Styrofoam waste recycling, including endpoints for adding waste, processing it through a densifier, and calculating the economic benefits of recycling."
Generated: DETERMINISTIC_ad994f7b8d6d9aef
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store waste data
waste_data = {}

# Constants for economic calculations
DENSIFICATION_RATE = 0.9  # 90% reduction in volume
ECONOMIC_BENEFIT_PER_KG = 0.5  # $0.50 per kg of recycled Styrofoam

@app.route('/add_waste', methods=['POST'])
def add_waste():
    """
    Endpoint to add Styrofoam waste.
    Expects JSON payload with 'weight' (in kg) and 'description'.
    """
    try:
        data = request.json
        weight = data.get('weight')
        description = data.get('description')

        if weight is None or weight <= 0:
            return jsonify({"error": "Invalid weight provided"}), 400

        if not description:
            return jsonify({"error": "Description is required"}), 400

        waste_id = str(uuid.uuid4())
        waste_data[waste_id] = {
            "weight": weight,
            "description": description,
            "processed": False
        }

        return jsonify({"message": "Waste added successfully", "waste_id": waste_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process_waste/<waste_id>', methods=['POST'])
def process_waste(waste_id):
    """
    Endpoint to process Styrofoam waste through a densifier.
    Updates the waste entry to mark it as processed and reduces its volume.
    """
    try:
        waste_entry = waste_data.get(waste_id)

        if not waste_entry:
            return jsonify({"error": "Waste not found"}), 404

        if waste_entry['processed']:
            return jsonify({"error": "Waste has already been processed"}), 400

        original_weight = waste_entry['weight']
        processed_weight = original_weight * DENSIFICATION_RATE

        waste_entry['weight'] = processed_weight
        waste_entry['processed'] = True

        return jsonify({
            "message": "Waste processed successfully",
            "original_weight": original_weight,
            "processed_weight": processed_weight
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/calculate_benefits', methods=['GET'])
def calculate_benefits():
    """
    Endpoint to calculate the total economic benefits of recycling.
    Returns the total weight of processed waste and the corresponding economic benefit.
    """
    try:
        total_processed_weight = sum(
            entry['weight'] for entry in waste_data.values() if entry['processed']
        )
        total_benefit = total_processed_weight * ECONOMIC_BENEFIT_PER_KG

        return jsonify({
            "total_processed_weight": total_processed_weight,
            "total_economic_benefit": total_benefit
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
