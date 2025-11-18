"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Generate code to create a "Request a Book" feature for an e-commerce site, where users can submit requests for unavailable books, similar to the feature on medebooks.shop.
Generated: DETERMINISTIC_dc90408708e278b8
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the BookRequest model
class BookRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Define the schema for validating incoming requests
class BookRequestSchema(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)
    email = fields.Email(required=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to handle book requests
@app.route('/request-book', methods=['POST'])
def request_book():
    # Validate the incoming JSON data
    schema = BookRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new book request
    book_request = BookRequest(
        title=data['title'],
        author=data['author'],
        email=data['email']
    )

    # Save the request to the database
    try:
        db.session.add(book_request)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error saving book request: {e}")
        db.session.rollback()
        return jsonify({"error": "Could not save the book request"}), 500

    # Return a success response
    return jsonify({"message": "Book request submitted successfully!"}), 201

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unexpected error: {e}")
    return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
