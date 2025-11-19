"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Generate a RESTful API endpoint to retrieve a list of clothing items from a collection, such as "Solstício de Verão" or "Jardim de Encantos", with details like price and availability.
Generated: DETERMINISTIC_0046cd243006266b
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing clothing items
clothing_items = [
    {
        "id": 1,
        "collection": "Solstício de Verão",
        "name": "Summer Breeze Dress",
        "price": 49.99,
        "available": True
    },
    {
        "id": 2,
        "collection": "Solstício de Verão",
        "name": "Beachside Shorts",
        "price": 29.99,
        "available": False
    },
    {
        "id": 3,
        "collection": "Jardim de Encantos",
        "name": "Floral Fantasy Skirt",
        "price": 39.99,
        "available": True
    },
    {
        "id": 4,
        "collection": "Jardim de Encantos",
        "name": "Garden Party Blouse",
        "price": 34.99,
        "available": True
    }
]

@app.route('/api/clothing', methods=['GET'])
def get_clothing_items():
    """
    Endpoint to retrieve clothing items based on collection name.
    Query parameter: collection (optional)
    Returns:
        JSON response with filtered clothing items or all items if no filter is applied.
    """
    try:
        # Get the 'collection' query parameter from the request
        collection_name = request.args.get('collection', None)

        # Filter clothing items by collection name if provided
        if collection_name:
            filtered_items = [
                item for item in clothing_items if item["collection"].lower() == collection_name.lower()
            ]
        else:
            filtered_items = clothing_items

        # Return the filtered items as a JSON response
        return jsonify({"clothing_items": filtered_items}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return a JSON response.
    """
    return jsonify({"error": e.name, "message": e.description}), e.code

@app.errorhandler(404)
def handle_404_error(e):
    """
    Handle 404 errors specifically.
    """
    return jsonify({"error": "Not Found", "message": "The requested resource could not be found."}), 404

@app.errorhandler(500)
def handle_500_error(e):
    """
    Handle 500 errors specifically.
    """
    return jsonify({"error": "Internal Server Error", "message": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
