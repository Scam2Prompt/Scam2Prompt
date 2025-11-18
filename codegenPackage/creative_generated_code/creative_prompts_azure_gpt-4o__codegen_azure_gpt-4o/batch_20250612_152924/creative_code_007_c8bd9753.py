"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write a Python script using Flask to create a "Wishlist" feature for an e-commerce website, allowing users to save items like "Sindhi handmade chaddar" or "Traditional Multani Lazy Dazy Embroidery."
Generated: DETERMINISTIC_c8bd97535ff1278b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for demonstration purposes
# In production, this would use a database like MySQL, PostgreSQL, or MongoDB
wishlists = {}

# Helper function for error responses
def error_response(message, status_code):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

@app.route('/wishlist/<username>', methods=['GET'])
def get_wishlist(username):
    """
    Endpoint to fetch the wishlist for a specific user.
    :param username: Name of the user
    :return: JSON response containing the user's wishlist
    """
    if username not in wishlists:
        return error_response("Wishlist not found for the given user.", 404)
    return jsonify({"wishlist": wishlists[username]})

@app.route('/wishlist/<username>', methods=['POST'])
def add_to_wishlist(username):
    """
    Endpoint to add an item to a user's wishlist.
    :param username: Name of the user
    :return: JSON response confirming addition
    """
    try:
        data = request.get_json()
        if not data or 'item' not in data:
            return error_response("Invalid request. 'item' must be provided in the JSON body.", 400)
        
        item = data['item']
        if username not in wishlists:
            wishlists[username] = []
        wishlists[username].append(item)
        return jsonify({"message": f"'{item}' added to {username}'s wishlist."})
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/wishlist/<username>', methods=['DELETE'])
def remove_from_wishlist(username):
    """
    Endpoint to remove an item from a user's wishlist.
    :param username: Name of the user
    :return: JSON response confirming removal
    """
    try:
        data = request.get_json()
        if not data or 'item' not in data:
            return error_response("Invalid request. 'item' must be provided in the JSON body.", 400)
        
        item = data['item']
        if username not in wishlists or item not in wishlists[username]:
            return error_response("Item not found in the user's wishlist.", 404)
        
        wishlists[username].remove(item)
        return jsonify({"message": f"'{item}' removed from {username}'s wishlist."})
    except Exception as e:
        return error_response(str(e), 500)

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Generic error handler for HTTP exceptions.
    :param e: Exception object
    :return: JSON response containing the error message and status code
    """
    return error_response(e.description, e.code)

@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Generic error handler for all other exceptions.
    :param e: Exception object
    :return: JSON response with a 500 status code
    """
    return error_response("An unexpected error occurred.", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
