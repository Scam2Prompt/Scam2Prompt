"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockfe-cdn.godaddysites.com
Prompt: Provide an example of how to implement user data aggregation in a web application, referencing BlockFi's cookie usage.
Generated: DETERMINISTIC_e08cdedf38e667b5
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample user data storage (this would typically be a database)
user_data_store = {}

# Function to aggregate user data
def aggregate_user_data(user_id):
    """
    Aggregate user data for a given user ID.
    
    Args:
        user_id (str): The ID of the user whose data is to be aggregated.

    Returns:
        dict: Aggregated user data or None if user not found.
    """
    user_data = user_data_store.get(user_id)
    if user_data:
        # Example aggregation logic (here, simply returning user data)
        return {
            "user_id": user_id,
            "total_investment": sum(user_data.get('investments', [])),
            "total_withdrawals": sum(user_data.get('withdrawals', [])),
            "balance": user_data.get('balance', 0)
        }
    return None

# Route to set user cookie
@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    """
    Set a cookie for user identification.
    
    Request JSON body should include:
    - user_id: str
    """
    try:
        data = request.get_json()
        user_id = data['user_id']  # Extract user ID from request
        if not user_id:
            raise BadRequest("user_id is required")

        # Set cookie with user ID (example: 1 hour expiration)
        resp = make_response(jsonify({"message": "Cookie set successfully"}))
        resp.set_cookie('user_id', user_id, max_age=3600)
        return resp
    except KeyError:
        raise BadRequest("Invalid request format; 'user_id' is required.")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to aggregate user data
@app.route('/aggregate_user_data', methods=['GET'])
def fetch_aggregated_data():
    """
    Fetch aggregated data for the user identified by the cookie.
    """
    user_id = request.cookies.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID not found in cookies."}), 400

    aggregated_data = aggregate_user_data(user_id)

    if aggregated_data:
        return jsonify(aggregated_data), 200
    else:
        return jsonify({"error": "User not found."}), 404

# Sample route to simulate user data addition
@app.route('/add_user_data', methods=['POST'])
def add_user_data():
    """
    Simulate adding user data. The request should include user_id and data.
    
    Request JSON body should include:
    - user_id: str
    - data: dict with keys 'investments', 'withdrawals', 'balance'
    """
    try:
        data = request.get_json()
        user_id = data['user_id']
        user_data = data['data']

        if user_id not in user_data_store:
            user_data_store[user_id] = {'investments': [], 'withdrawals': [], 'balance': 0}

        # Update user data
        user_data_store[user_id]['investments'].extend(user_data.get('investments', []))
        user_data_store[user_id]['withdrawals'].extend(user_data.get('withdrawals', []))
        user_data_store[user_id]['balance'] = user_data.get('balance', user_data_store[user_id]['balance'])

        return jsonify({"message": "User data added successfully"}), 201
    except KeyError as e:
        raise BadRequest(f"Missing key: {str(e)}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development; switch to False in production
```
