"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westbengalrealestates.com
Prompt: Develop an API recommendation for integrating property reviews, specifically for projects like TATA Avenida and Sugam Serenity, in a real estate platform.
Generated: DETERMINISTIC_fb56e8d5298eda5b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mocked database of property reviews
property_reviews = {
    "TATA Avenida": [
        {
            "review_id": 1,
            "user": "John Doe",
            "rating": 5,
            "comment": "Fantastic property with great amenities and location!",
        },
        {
            "review_id": 2,
            "user": "Jane Smith",
            "rating": 4,
            "comment": "Good property, but slightly overpriced.",
        },
    ],
    "Sugam Serenity": [
        {
            "review_id": 3,
            "user": "Alice Brown",
            "rating": 4,
            "comment": "Spacious apartments and peaceful surroundings.",
        },
        {
            "review_id": 4,
            "user": "Bob White",
            "rating": 3,
            "comment": "Decent property but limited parking space.",
        },
    ],
}

@app.route("/reviews/<property_name>", methods=["GET"])
def get_reviews(property_name):
    """
    Endpoint to fetch reviews for a specific property.
    :param property_name: Name of the property (URL parameter)
    :return: JSON response with reviews for the property
    """
    try:
        # Check if property exists in the review database
        reviews = property_reviews.get(property_name)
        if not reviews:
            return jsonify({"error": f"No reviews found for property '{property_name}'"}), 404

        return jsonify({"property_name": property_name, "reviews": reviews}), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/reviews/<property_name>", methods=["POST"])
def add_review(property_name):
    """
    Endpoint to add a new review for a specific property.
    :param property_name: Name of the property (URL parameter)
    :return: JSON response with status of the operation
    """
    try:
        # Parse the request JSON
        review_data = request.json

        # Validate input data
        if not review_data or not all(key in review_data for key in ["user", "rating", "comment"]):
            return jsonify({"error": "Invalid input. 'user', 'rating', and 'comment' are required fields."}), 400

        # Add the new review to the property database
        new_review = {
            "review_id": len(property_reviews.get(property_name, [])) + 1,
            "user": review_data["user"],
            "rating": review_data["rating"],
            "comment": review_data["comment"],
        }

        if property_name not in property_reviews:
            property_reviews[property_name] = []

        property_reviews[property_name].append(new_review)

        return jsonify({"message": "Review added successfully", "review": new_review}), 201
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/reviews/<property_name>/<int:review_id>", methods=["DELETE"])
def delete_review(property_name, review_id):
    """
    Endpoint to delete a specific review for a property.
    :param property_name: Name of the property (URL parameter)
    :param review_id: ID of the review to be deleted
    :return: JSON response with status of the operation
    """
    try:
        # Check if property exists in the review database
        reviews = property_reviews.get(property_name)
        if not reviews:
            return jsonify({"error": f"No reviews found for property '{property_name}'"}), 404

        # Find and delete the review by ID
        review_to_delete = next((review for review in reviews if review["review_id"] == review_id), None)
        if not review_to_delete:
            return jsonify({"error": f"No review found with ID '{review_id}'"}), 404

        reviews.remove(review_to_delete)

        return jsonify({"message": "Review deleted successfully", "review": review_to_delete}), 200
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
