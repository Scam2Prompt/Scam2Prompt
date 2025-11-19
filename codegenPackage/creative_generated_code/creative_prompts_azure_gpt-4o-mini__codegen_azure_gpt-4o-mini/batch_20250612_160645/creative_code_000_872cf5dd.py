"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Generate a code snippet for a web application that calculates the cost of apartment renovation based on the provided pricing structure from Панам's services.
Generated: DETERMINISTIC_872cf5dd023fcf5d
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Pricing structure for renovation services per square meter
PRICING_STRUCTURE = {
    "kitchen": 150,
    "bathroom": 120,
    "living_room": 100,
    "bedroom": 90,
    "hallway": 80
}

@app.route('/calculate_renovation_cost', methods=['POST'])
def calculate_renovation_cost():
    """
    Calculate the cost of apartment renovation based on room types and their sizes.

    Expected JSON payload:
    {
        "renovation_details": [
            {"room_type": "kitchen", "size": 20},
            {"room_type": "bathroom", "size": 15},
            {"room_type": "living_room", "size": 30}
        ]
    }

    Returns a JSON response with the total cost of renovation.
    """
    try:
        data = request.get_json()
        renovation_details = data.get("renovation_details", [])
        
        total_cost = 0

        for detail in renovation_details:
            room_type = detail.get("room_type")
            size = detail.get("size", 0)

            if room_type not in PRICING_STRUCTURE:
                return jsonify({"error": f"Invalid room type: {room_type}"}), 400
            
            if size < 0:
                return jsonify({"error": "Size must be a non-negative value"}), 400
            
            cost_per_sqm = PRICING_STRUCTURE[room_type]
            total_cost += cost_per_sqm * size

        return jsonify({"total_cost": total_cost}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode for development
```
