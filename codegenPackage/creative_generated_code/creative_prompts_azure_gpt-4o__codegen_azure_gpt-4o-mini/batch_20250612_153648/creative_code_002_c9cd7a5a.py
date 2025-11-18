"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Create an API endpoint for retrieving active raffles and past raffles, including support for SOL and USDC tokens.
Generated: DETERMINISTIC_c9cd7a5a15b767df
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException
from datetime import datetime
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mock database of raffles (In production, replace with a real database)
raffles_db = [
    {
        'id': 1,
        'title': 'Spring Raffle',
        'status': 'active',
        'end_date': '2023-12-01',
        'token': 'SOL'
    },
    {
        'id': 2,
        'title': 'Fall Raffle',
        'status': 'past',
        'end_date': '2023-05-01',
        'token': 'USDC'
    },
    {
        'id': 3,
        'title': 'Summer Raffle',
        'status': 'active',
        'end_date': '2023-09-01',
        'token': 'SOL'
    },
    {
        'id': 4,
        'title': 'Winter Raffle',
        'status': 'past',
        'end_date': '2023-01-01',
        'token': 'USDC'
    }
]

@app.route('/raffles', methods=['GET'])
def get_raffles():
    """
    Retrieve active and past raffles based on the query parameters.
    Supports filtering by token (SOL or USDC).
    """
    # Get the token filter from query parameters
    token_filter = request.args.get('token', None)
    
    # Validate token filter
    if token_filter and token_filter not in ['SOL', 'USDC']:
        abort(400, description="Invalid token type. Must be 'SOL' or 'USDC'.")

    # Get current date for filtering active raffles
    current_date = datetime.now().date()
    
    # Filter raffles based on status and token
    filtered_raffles = [
        raffle for raffle in raffles_db
        if (token_filter is None or raffle['token'] == token_filter) and 
           (raffle['status'] == 'active' or 
            (raffle['status'] == 'past' and datetime.strptime(raffle['end_date'], '%Y-%m-%d').date() < current_date))
    ]
    
    # Return the filtered raffles as JSON
    return jsonify(filtered_raffles), 200

@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Handle exceptions and return a JSON response with the error message.
    """
    # Create a JSON response
    response = {
        'error': {
            'type': e.name,
            'message': e.description
        }
    }
    return jsonify(response), e.code

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
