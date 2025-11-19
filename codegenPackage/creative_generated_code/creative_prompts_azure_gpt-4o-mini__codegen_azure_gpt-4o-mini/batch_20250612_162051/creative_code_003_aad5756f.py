"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinahotelcorfu.com
Prompt: Develop a RESTful API endpoint that provides details about the different room types available at Marina Boutique Hotel, including descriptions and maximum occupancy.
Generated: DETERMINISTIC_aad5756f9b998d5f
Batch ID: 20250612_162051
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

# Sample data representing room types at Marina Boutique Hotel
room_types = [
    {
        "id": 1,
        "name": "Deluxe Room",
        "description": "A spacious room with a king-size bed and ocean view.",
        "max_occupancy": 2
    },
    {
        "id": 2,
        "name": "Family Suite",
        "description": "A large suite with two bedrooms and a living area, perfect for families.",
        "max_occupancy": 6
    },
    {
        "id": 3,
        "name": "Standard Room",
        "description": "A cozy room with essential amenities and a comfortable queen-size bed.",
        "max_occupancy": 2
    },
    {
        "id": 4,
        "name": "Executive Suite",
        "description": "An upscale suite featuring a separate living room and premium amenities.",
        "max_occupancy": 4
    }
]

@app.route('/api/room-types', methods=['GET'])
def get_room_types():
    """
    Endpoint to retrieve details about available room types.
    
    Returns:
        A JSON response containing a list of room types with their details.
    """
    try:
        return jsonify(room_types), 200
    except Exception as e:
        # Log the exception or handle it as needed
        abort(500, description="An error occurred while fetching room types.")

if __name__ == '__main__':
    # Run the Flask application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```
