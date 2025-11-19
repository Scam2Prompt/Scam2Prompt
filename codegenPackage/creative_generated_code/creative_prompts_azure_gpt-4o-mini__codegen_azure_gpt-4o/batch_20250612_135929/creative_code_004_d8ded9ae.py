"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wasbroke.com
Prompt: Suggest an API that can help aspiring authors promote their books effectively, as outlined in the Best Seller Writing Program review on Was Broke.
Generated: DETERMINISTIC_d8ded9ae547da9b4
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a simple Flask-based API for aspiring authors
to promote their books effectively. The API provides endpoints to:
1. Add a new book along with promotional details.
2. Retrieve all books for promotional purposes.
3. Update promotional details for a specific book.
4. Delete a book from the promotional list.

The API adheres to best practices for Python and Flask development.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store book details (for demonstration purposes)
books = {}

@app.route("/books", methods=["GET"])
def get_books():
    """
    Retrieves all books with their promotional details.
    """
    return jsonify({"success": True, "data": books}), 200

@app.route("/books", methods=["POST"])
def add_book():
    """
    Adds a new book with promotional details.
    Expects JSON payload with 'id', 'title', 'author', and 'promotion_details'.
    """
    try:
        data = request.json
        book_id = data.get("id")
        title = data.get("title")
        author = data.get("author")
        promotion_details = data.get("promotion_details")

        if not all([book_id, title, author, promotion_details]):
            return jsonify({"success": False, "message": "Missing required fields"}), 400

        if book_id in books:
            return jsonify({"success": False, "message": "Book ID already exists"}), 409

        books[book_id] = {
            "title": title,
            "author": author,
            "promotion_details": promotion_details
        }
        return jsonify({"success": True, "message": "Book added successfully"}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    """
    Updates the promotional details for an existing book.
    Expects JSON payload with 'promotion_details'.
    """
    try:
        if book_id not in books:
            return jsonify({"success": False, "message": "Book not found"}), 404

        data = request.json
        promotion_details = data.get("promotion_details")

        if not promotion_details:
            return jsonify({"success": False, "message": "Missing promotional details"}), 400

        books[book_id]["promotion_details"] = promotion_details
        return jsonify({"success": True, "message": "Promotion details updated successfully"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    """
    Deletes a book from the promotional list.
    """
    try:
        if book_id not in books:
            return jsonify({"success": False, "message": "Book not found"}), 404

        del books[book_id]
        return jsonify({"success": True, "message": "Book deleted successfully"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
