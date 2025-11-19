"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Develop a RESTful API endpoint for managing customer reviews on jewelry products, inspired by the customer feedback section on Malkeenz's website.
Generated: DETERMINISTIC_ca935b833cab2504
Batch ID: 20250612_164257
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

# Mock database (in-memory storage)
reviews_db = []

# Error handling class for custom errors
class CustomError(HTTPException):
    def __init__(self, message, status_code):
        super().__init__()
        self.message = message
        self.code = status_code

# Helper function to find review by ID
def find_review(review_id):
    for review in reviews_db:
        if review['id'] == review_id:
            return review
    return None

@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    GET /reviews
    Fetch all reviews
    """
    return jsonify({'reviews': reviews_db}), 200

@app.route('/reviews', methods=['POST'])
def create_review():
    """
    POST /reviews
    Create a new review.
    Requires JSON payload with 'product_id', 'customer_name', 'review_text', and 'rating'.
    """
    try:
        data = request.get_json()
        if not data:
            raise CustomError("Invalid JSON payload.", 400)

        # Validate required fields
        required_fields = ['product_id', 'customer_name', 'review_text', 'rating']
        for field in required_fields:
            if field not in data:
                raise CustomError(f"'{field}' is required.", 400)

        # Validate rating
        rating = data['rating']
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise CustomError("Rating must be an integer between 1 and 5.", 400)

        # Create review object
        new_review = {
            'id': len(reviews_db) + 1,
            'product_id': data['product_id'],
            'customer_name': data['customer_name'],
            'review_text': data['review_text'],
            'rating': rating
        }

        # Save to mock database
        reviews_db.append(new_review)

        return jsonify({'message': 'Review created successfully.', 'review': new_review}), 201

    except CustomError as e:
        return jsonify({'error': e.message}), e.code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    PUT /reviews/<review_id>
    Update an existing review.
    Requires JSON payload with 'review_text' or 'rating'.
    """
    try:
        data = request.get_json()
        if not data:
            raise CustomError("Invalid JSON payload.", 400)

        # Find the review by ID
        review = find_review(review_id)
        if not review:
            raise CustomError("Review not found.", 404)

        # Update fields
        if 'review_text' in data:
            review['review_text'] = data['review_text']
        if 'rating' in data:
            rating = data['rating']
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise CustomError("Rating must be an integer between 1 and 5.", 400)
            review['rating'] = rating

        return jsonify({'message': 'Review updated successfully.', 'review': review}), 200

    except CustomError as e:
        return jsonify({'error': e.message}), e.code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    DELETE /reviews/<review_id>
    Delete an existing review by ID.
    """
    try:
        # Find the review by ID
        review = find_review(review_id)
        if not review:
            raise CustomError("Review not found.", 404)

        # Remove review from mock database
        reviews_db.remove(review)

        return jsonify({'message': 'Review deleted successfully.'}), 200

    except CustomError as e:
        return jsonify({'error': e.message}), e.code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def server_error(error):
    """
    Handle 500 errors
    """
    return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
