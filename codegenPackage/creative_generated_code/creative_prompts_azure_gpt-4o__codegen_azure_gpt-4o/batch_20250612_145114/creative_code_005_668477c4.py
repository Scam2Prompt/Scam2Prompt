"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Suggest APIs or tools for managing a large database of online store offers and discounts, similar to Shoppiday's platform.
Generated: DETERMINISTIC_668477c4f40583f2
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script suggests APIs and tools for managing a large database of online store offers and discounts.
It utilizes Flask to create a RESTful API and MongoDB (via PyMongo) as the database.
For production environments, ensure to configure proper security settings like API authentication and database connection security.
"""

from flask import Flask, jsonify, request
from pymongo import MongoClient, errors

# Initialize Flask application
app = Flask(__name__)

# MongoDB connection details
DB_URI = "mongodb://localhost:27017"  # Change accordingly for production setup
DB_NAME = "store_offers"

# Connect to MongoDB
try:
    client = MongoClient(DB_URI)
    db = client[DB_NAME]
    offers_collection = db["offers"]
except errors.PyMongoError as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

# Utility function to validate offer data
def validate_offer_data(data):
    """
    Validate the offer data received in the request.
    Ensures required fields are present and well-formed.

    :param data: dict containing offer details
    :return: tuple (bool indicating validity, error message if invalid)
    """
    required_fields = ["store_name", "offer_description", "discount_percent", "expiry_date"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
        if not data[field]:
            return False, f"Field '{field}' cannot be empty."
    return True, None

# API route to list all offers
@app.route("/offers", methods=["GET"])
def list_offers():
    """
    List all store offers from the database.

    :return: JSON response containing all offers
    """
    try:
        offers = list(offers_collection.find({}, {"_id": 0}))  # Exclude MongoDB '_id' field from the response
        return jsonify({"success": True, "offers": offers}), 200
    except errors.PyMongoError as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500

# API route to add a new offer
@app.route("/offers", methods=["POST"])
def add_offer():
    """
    Add a new store offer to the database.

    :return: JSON response indicating success or failure
    """
    try:
        offer_data = request.json
        is_valid, error_message = validate_offer_data(offer_data)
        if not is_valid:
            return jsonify({"success": False, "message": error_message}), 400

        offers_collection.insert_one(offer_data)
        return jsonify({"success": True, "message": "Offer added successfully."}), 201
    except errors.PyMongoError as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500

# API route to delete an offer
@app.route("/offers", methods=["DELETE"])
def delete_offer():
    """
    Delete an offer from the database based on store name.

    :return: JSON response indicating success or failure
    """
    try:
        store_name = request.args.get("store_name")
        if not store_name:
            return jsonify({"success": False, "message": "Missing 'store_name' query parameter."}), 400

        result = offers_collection.delete_one({"store_name": store_name})
        if result.deleted_count > 0:
            return jsonify({"success": True, "message": "Offer deleted successfully."}), 200
        else:
            return jsonify({"success": False, "message": "No offer found for the specified store name."}), 404
    except errors.PyMongoError as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500

# API route to update an existing offer
@app.route("/offers", methods=["PUT"])
def update_offer():
    """
    Update an existing store offer in the database.

    :return: JSON response indicating success or failure
    """
    try:
        store_name = request.args.get("store_name")
        if not store_name:
            return jsonify({"success": False, "message": "Missing 'store_name' query parameter."}), 400

        update_data = request.json
        is_valid, error_message = validate_offer_data(update_data)
        if not is_valid:
            return jsonify({"success": False, "message": error_message}), 400

        result = offers_collection.update_one({"store_name": store_name}, {"$set": update_data})
        if result.matched_count > 0:
            return jsonify({"success": True, "message": "Offer updated successfully."}), 200
        else:
            return jsonify({"success": False, "message": "No offer found for the specified store name."}), 404
    except errors.PyMongoError as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500

# Main application entry point
if __name__ == "__main__":
    # Run the Flask application
    # For production, use a WSGI server like Gunicorn or uWSGI
    app.run(host="0.0.0.0", port=5000, debug=True)
```
