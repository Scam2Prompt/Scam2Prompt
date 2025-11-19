"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://you-trip.ru
Prompt: Generate a code snippet for a travel booking API that allows users to search for affordable tours to popular destinations like Egypt and Turkey, incorporating filters for ratings and reviews.
Generated: DETERMINISTIC_ea87c017fb64c120
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Mock data for tours
TOURS = [
    {"id": 1, "destination": "Egypt", "price": 500, "rating": 4.5, "reviews": 120},
    {"id": 2, "destination": "Turkey", "price": 400, "rating": 4.2, "reviews": 95},
    {"id": 3, "destination": "Egypt", "price": 600, "rating": 4.8, "reviews": 200},
    {"id": 4, "destination": "Turkey", "price": 450, "rating": 4.0, "reviews": 80},
]

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/search-tours', methods=['GET'])
def search_tours():
    """
    API endpoint for searching affordable tours to popular destinations.
    Allows filtering by rating and number of reviews.
    """
    try:
        # Extract query parameters
        destination = request.args.get('destination', '').capitalize()
        max_price = float(request.args.get('max_price', float('inf')))
        min_rating = float(request.args.get('min_rating', 0))
        min_reviews = int(request.args.get('min_reviews', 0))

        # Validate destination input
        if destination not in {"Egypt", "Turkey", ""}:
            return jsonify({"error": "Invalid destination. Choose 'Egypt' or 'Turkey'."}), 400

        # Filter tours based on query parameters
        filtered_tours = [
            tour for tour in TOURS
            if (destination == "" or tour['destination'] == destination) and
               tour['price'] <= max_price and
               tour['rating'] >= min_rating and
               tour['reviews'] >= min_reviews
        ]

        # Return results
        return jsonify({"tours": filtered_tours}), 200

    except ValueError as e:
        # Handle invalid data types in query parameters
        logging.error(f"ValueError: {e}")
        return jsonify({"error": "Invalid query parameter type."}), 400

    except Exception as e:
        # Catch unexpected errors
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An internal error occurred."}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
