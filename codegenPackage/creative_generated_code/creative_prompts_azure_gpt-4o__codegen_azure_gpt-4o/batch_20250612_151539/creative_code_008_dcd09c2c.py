"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write code to implement a voting system for rating online casinos, using the star-rating system described on Santa Claus Casino.
Generated: DETERMINISTIC_dcd09c2c39c73550
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for casino ratings
casino_ratings = {}

@app.route('/rate', methods=['POST'])
def rate_casino():
    """
    Endpoint to rate a casino.
    Expects JSON data with 'casino_name' and 'rating' keys.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data or 'casino_name' not in data or 'rating' not in data:
            raise BadRequest("Missing 'casino_name' or 'rating' in the request payload.")
        
        casino_name = data['casino_name']
        rating = data['rating']

        # Validate rating value
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise BadRequest("'rating' must be an integer between 1 and 5.")

        # Initialize or update casino ratings
        if casino_name not in casino_ratings:
            casino_ratings[casino_name] = {'total_rating': 0, 'num_ratings': 0}

        casino_ratings[casino_name]['total_rating'] += rating
        casino_ratings[casino_name]['num_ratings'] += 1

        # Calculate the average rating
        average_rating = casino_ratings[casino_name]['total_rating'] / casino_ratings[casino_name]['num_ratings']

        return jsonify({
            'message': f"Rating recorded for {casino_name}.",
            'average_rating': round(average_rating, 2),
            'total_ratings': casino_ratings[casino_name]['num_ratings']
        }), 200

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/ratings', methods=['GET'])
def get_all_ratings():
    """
    Endpoint to fetch all casinos with their average ratings.
    """
    try:
        if not casino_ratings:
            return jsonify({'message': 'No ratings available.'}), 200

        # Prepare response data
        response_data = {}
        for casino, data in casino_ratings.items():
            average_rating = data['total_rating'] / data['num_ratings']
            response_data[casino] = {
                'average_rating': round(average_rating, 2),
                'total_ratings': data['num_ratings']
            }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code implements a voting system for rating online casinos using a star-rating system (1-5). It includes endpoints to rate a casino and retrieve the casino ratings, while adhering to best practices and including proper error handling.
