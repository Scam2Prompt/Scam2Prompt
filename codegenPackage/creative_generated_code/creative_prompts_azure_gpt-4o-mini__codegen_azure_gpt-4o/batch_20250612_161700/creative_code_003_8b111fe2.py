"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoastalroofing.com
Prompt: Develop a RESTful API endpoint for submitting customer reviews for Coastal Roofing & Waterproofing's roofing services.
Generated: DETERMINISTIC_8b111fe2817f8c4c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# A mock database to store reviews (In production, use a real database)
reviews = []

@app.route('/api/reviews', methods=['POST'])
def submit_review():
    """
    Endpoint for submitting customer reviews.
    Accepts a JSON payload with the following fields:
    - customer_name: str, required
    - rating: int, required, must be between 1 and 5
    - review: str, optional
    - contact_email: str, optional
    Returns:
    - JSON response with success message or error details.
    """
    try:
        # Parse JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        customer_name = data.get("customer_name")
        rating = data.get("rating")
        
        if not customer_name or not rating:
            return jsonify({"error": "Fields 'customer_name' and 'rating' are required"}), 400

        # Validate rating (must be between 1 and 5)
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"error": "Rating must be an integer between 1 and 5"}), 400

        # Optional fields
        review = data.get("review", "")
        contact_email = data.get("contact_email", "")

        # Construct review object
        review_entry = {
            "customer_name": customer_name,
            "rating": rating,
            "review": review,
            "contact_email": contact_email,
            "submitted_at": datetime.now().isoformat()
        }

        # Add the review to the mock database
        reviews.append(review_entry)

        # Return success response
        return jsonify({"message": "Review submitted successfully", "review": review_entry}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the Flask application (debug mode should be off in production)
if __name__ == "__main__":
    app.run(debug=True)
```
