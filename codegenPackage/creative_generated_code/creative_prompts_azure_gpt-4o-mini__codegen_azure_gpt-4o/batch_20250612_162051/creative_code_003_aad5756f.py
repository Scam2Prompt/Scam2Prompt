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
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for room types
ROOM_TYPES = [
    {
        "id": 1,
        "name": "Standard Room",
        "description": "A comfortable room with a queen-sized bed and a private bathroom.",
        "max_occupancy": 2
    },
    {
        "id": 2,
        "name": "Deluxe Room",
        "description": "A spacious room with a king-sized bed, a private bathroom, and a balcony with stunning views.",
        "max_occupancy": 3
    },
    {
        "id": 3,
        "name": "Family Suite",
        "description": "An apartment-style suite with two bedrooms, a living room, and a full kitchen.",
        "max_occupancy": 6
    },
    {
        "id": 4,
        "name": "Presidential Suite",
        "description": "A luxurious suite with premium amenities, ocean views, and personalized services.",
        "max_occupancy": 4
    }
]

@app.route('/api/room-types', methods=['GET'])
def get_room_types():
    """
    RESTful endpoint to retrieve details about the different room types available at Marina Boutique Hotel.
    
    Returns:
        JSON response containing a list of room types with their descriptions and maximum occupancy.
    """
    try:
        # Return all room types in JSON format
        return jsonify({
            "success": True,
            "data": ROOM_TYPES
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "message": f"An error occurred while fetching room types: {str(e)}"
        }), 500


@app.route('/api/room-types/<int:room_id>', methods=['GET'])
def get_room_type_by_id(room_id):
    """
    RESTful endpoint to retrieve details about a specific room type by its ID.
    
    Args:
        room_id (int): ID of the room type.
    
    Returns:
        JSON response containing details of the specified room type or an error message if not found.
    """
    try:
        # Find the room type by ID
        room_type = next((room for room in ROOM_TYPES if room["id"] == room_id), None)
        
        if room_type is None:
            return jsonify({
                "success": False,
                "message": "Room type not found."
            }), 404
        
        return jsonify({
            "success": True,
            "data": room_type
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "message": f"An error occurred while fetching the room type: {str(e)}"
        }), 500


# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    
    Returns:
        JSON response indicating the requested resource was not found.
    """
    return jsonify({
        "success": False,
        "message": "Resource not found."
    }), 404


# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 internal server errors.
    
    Returns:
        JSON response indicating an internal server error occurred.
    """
    return jsonify({
        "success": False,
        "message": "Internal server error. Please try again later."
    }), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
