"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Create an API endpoint for a travel application that provides details about unique experiences in Chile, specifically focusing on horse riding tours in the Melado Valley.
Generated: DETERMINISTIC_e26a9057c9e442d7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Database: Horse riding tours in Melado Valley
HORSE_RIDING_TOURS = [
    {
        "id": 1,
        "name": "Melado Valley Sunset Ride",
        "description": "Enjoy a beautiful ride through Melado Valley during sunset, led by experienced guides.",
        "duration": "2 hours",
        "price": 50.00,
        "difficulty": "Beginner",
        "location": "Melado Valley, Chile"
    },
    {
        "id": 2,
        "name": "Melado Valley Full-Day Adventure",
        "description": "A full-day horse riding tour with breathtaking views and an included picnic lunch.",
        "duration": "8 hours",
        "price": 120.00,
        "difficulty": "Intermediate",
        "location": "Melado Valley, Chile"
    },
    {
        "id": 3,
        "name": "Melado Valley Mountain Trails",
        "description": "Ride through rugged mountain trails in Melado Valley, perfect for experienced riders.",
        "duration": "4 hours",
        "price": 80.00,
        "difficulty": "Advanced",
        "location": "Melado Valley, Chile"
    }
]

@app.route('/api/chile/horse-riding-tours', methods=['GET'])
def get_horse_riding_tours():
    """
    API Endpoint: Get details about horse riding tours in Melado Valley, Chile.

    Returns:
        JSON response containing a list of available horse riding tours.
    """
    try:
        # Return the list of tours as a JSON response
        return jsonify(tours=HORSE_RIDING_TOURS), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify(error="An error occurred while processing your request.", details=str(e)), 500


@app.route('/api/chile/horse-riding-tours/<int:tour_id>', methods=['GET'])
def get_horse_riding_tour_by_id(tour_id):
    """
    API Endpoint: Get details about a specific horse riding tour in Melado Valley by its ID.

    Args:
        tour_id (int): The ID of the tour to retrieve.

    Returns:
        JSON response containing the tour details if found, or a 404 error if not.
    """
    try:
        # Find the tour by its ID
        tour = next((tour for tour in HORSE_RIDING_TOURS if tour["id"] == tour_id), None)
        if tour:
            return jsonify(tour=tour), 200
        else:
            # If tour not found, return a 404 error
            return jsonify(error="Tour not found with the specified ID."), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify(error="An error occurred while processing your request.", details=str(e)), 500


# Error Handling for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for unspecified routes.

    Returns:
        JSON response indicating the requested resource was not found.
    """
    return jsonify(error="The requested resource was not found."), 404


# Error Handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 internal server errors.

    Returns:
        JSON response indicating an internal server error occurred.
    """
    return jsonify(error="An internal server error occurred."), 500


# Application Entry Point
if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(debug=False, host='0.0.0.0', port=5000)
```
