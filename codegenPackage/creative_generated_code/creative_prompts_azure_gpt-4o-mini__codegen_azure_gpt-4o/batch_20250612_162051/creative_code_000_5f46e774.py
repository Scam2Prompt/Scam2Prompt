"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: How can I implement a wishlist feature in my e-commerce application similar to the one on Alwan's website?
Generated: DETERMINISTIC_5f46e774b50fab63
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: wishlist.py

# Import necessary modules
from flask import Flask, request, jsonify, session
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Secret key for session management (in production, use a secure key)
app.secret_key = 'your_secret_key_here'

# Initialize wishlist in session if not already present
@app.before_request
def initialize_wishlist():
    if 'wishlist' not in session:
        session['wishlist'] = []

# Route to view all items in the wishlist
@app.route('/wishlist', methods=['GET'])
def view_wishlist():
    """Return the current wishlist."""
    return jsonify({
        'status': 'success',
        'wishlist': session.get('wishlist', [])
    })

# Route to add an item to the wishlist
@app.route('/wishlist/add', methods=['POST'])
def add_to_wishlist():
    """
    Add an item to the wishlist.
    Request Body:
        {
            "item_id": str,
            "item_name": str
        }
    """
    try:
        # Parse request data
        data = request.get_json()
        item_id = data.get('item_id')
        item_name = data.get('item_name')

        # Validate input
        if not item_id or not item_name:
            raise BadRequest('Missing item_id or item_name.')

        # Check if the item already exists in the wishlist
        wishlist = session['wishlist']
        for item in wishlist:
            if item['item_id'] == item_id:
                return jsonify({'status': 'error', 'message': 'Item already in wishlist.'}), 400

        # Add the item to the wishlist
        new_item = {'item_id': item_id, 'item_name': item_name}
        wishlist.append(new_item)
        session['wishlist'] = wishlist
        
        return jsonify({'status': 'success', 'message': 'Item added to wishlist.', 'wishlist': wishlist})

    except BadRequest as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred while adding item to wishlist.'}), 500

# Route to remove an item from the wishlist
@app.route('/wishlist/remove', methods=['POST'])
def remove_from_wishlist():
    """
    Remove an item from the wishlist.
    Request Body:
        {
            "item_id": str
        }
    """
    try:
        # Parse request data
        data = request.get_json()
        item_id = data.get('item_id')

        # Validate input
        if not item_id:
            raise BadRequest('Missing item_id.')

        # Remove the item from the wishlist
        wishlist = session['wishlist']
        wishlist = [item for item in wishlist if item['item_id'] != item_id]
        session['wishlist'] = wishlist
        
        return jsonify({'status': 'success', 'message': 'Item removed from wishlist.', 'wishlist': wishlist})

    except BadRequest as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred while removing item from wishlist.'}), 500

# Route to clear the wishlist
@app.route('/wishlist/clear', methods=['POST'])
def clear_wishlist():
    """Clear the entire wishlist."""
    try:
        session['wishlist'] = []
        return jsonify({'status': 'success', 'message': 'Wishlist cleared.'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred while clearing the wishlist.'}), 500

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
