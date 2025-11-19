"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkasluxury.com
Prompt: Generate a code snippet for a travel booking API that allows users to customize their itineraries for tours in Peru, similar to the personalized experiences offered by Inkas Luxury.
Generated: DETERMINISTIC_d02c8518d6584ab9
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

# Sample data to simulate available tours
TOURS = [
    {"id": 1, "name": "Machu Picchu Guided Tour", "duration": "1 day", "price": 250},
    {"id": 2, "name": "Sacred Valley Adventure", "duration": "2 days", "price": 400},
    {"id": 3, "name": "Cusco City Exploration", "duration": "1 day", "price": 150},
    {"id": 4, "name": "Lake Titicaca Journey", "duration": "3 days", "price": 600},
]

@app.route('/api/tours', methods=['GET'])
def list_tours():
    """
    Endpoint to list all available tours.
    Returns:
        JSON response with the list of available tours.
    """
    return jsonify({"tours": TOURS}), 200

@app.route('/api/itinerary', methods=['POST'])
def create_itinerary():
    """
    Endpoint to create a customized itinerary.
    Request body should include tour IDs and user preferences.
    Returns:
        JSON response with the created itinerary details or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'selected_tours' not in data:
            return jsonify({"error": "Invalid request. Please provide 'selected_tours'."}), 400

        selected_tour_ids = data['selected_tours']
        preferences = data.get('preferences', {})

        # Fetch the selected tours
        selected_tours = [tour for tour in TOURS if tour['id'] in selected_tour_ids]

        if not selected_tours:
            return jsonify({"error": "No valid tours found for the provided ids."}), 404

        # Calculate total duration and price
        total_price = sum(tour['price'] for tour in selected_tours)
        total_duration = f"{len(selected_tours)} days"  # Simplified duration calculation

        # Create itinerary response
        itinerary = {
            "selected_tours": selected_tours,
            "total_price": total_price,
            "total_duration": total_duration,
            "preferences": preferences
        }

        return jsonify({"itinerary": itinerary}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for internal server issues.
    """
    return jsonify({"error": "Internal server error."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
