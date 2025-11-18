"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Suggest an API for managing product reviews and ratings on an e-commerce platform, ensuring compatibility with categories like "Health & Beauty" and "Automotive."
Generated: DETERMINISTIC_507af7d40d49f7a7
Batch ID: 20250612_155102
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

# In-memory database simulation
reviews_db = []
categories = ["Health & Beauty", "Automotive"]

# Helper function to validate category
def validate_category(category):
    if category not in categories:
        raise ValueError(f"Invalid category. Supported categories: {categories}")

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).data
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 400

# Route: Get all reviews
@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    return jsonify(reviews_db), 200

# Route: Add a new review
@app.route("/api/reviews", methods=["POST"])
def add_review():
    try:
        data = request.json
        # Validate request data
        if not all(key in data for key in ("product_id", "user_id", "rating", "review", "category")):
            raise ValueError("Missing required fields: product_id, user_id, rating, review, category")
        validate_category(data["category"])
        if not (1 <= data["rating"] <= 5):
            raise ValueError("Rating must be between 1 and 5")

        # Create and add the review
        review = {
            "id": len(reviews_db) + 1,
            "product_id": data["product_id"],
            "user_id": data["user_id"],
            "rating": data["rating"],
            "review": data["review"],
            "category": data["category"]
        }
        reviews_db.append(review)
        return jsonify(review), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Update an existing review
@app.route("/api/reviews/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    try:
        data = request.json
        # Validate request data
        if not all(key in data for key in ("rating", "review", "category")):
            raise ValueError("Missing required fields: rating, review, category")
        if not (1 <= data["rating"] <= 5):
            raise ValueError("Rating must be between 1 and 5")
        validate_category(data["category"])

        # Find and update the review
        for review in reviews_db:
            if review["id"] == review_id:
                review["rating"] = data["rating"]
                review["review"] = data["review"]
                review["category"] = data["category"]
                return jsonify(review), 200
        return jsonify({"error": "Review not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Delete a review
@app.route("/api/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    try:
        # Find and delete the review
        for review in reviews_db:
            if review["id"] == review_id:
                reviews_db.remove(review)
                return jsonify({"message": "Review deleted successfully"}), 200
        return jsonify({"error": "Review not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```
