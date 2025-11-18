"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Provide code to integrate a "Bookmark" feature into a directory website, allowing users to save listings like "Ταπετσαρίες Αυτοκινήτων Νεκτάριος Βαμβούνης" for later reference.
Generated: DETERMINISTIC_b4e5712ef5c140f0
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'  # Using SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a secure, random key in production

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """
    User model representing a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Bookmark(db.Model):
    """
    Bookmark model representing a saved listing by a user.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    listing_name = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', backref=db.backref('bookmarks', lazy=True))

# Routes
@app.route('/bookmark', methods=['POST'])
def add_bookmark():
    """
    Endpoint to add a new bookmark for a user.
    """
    try:
        # Extract data from request
        user_id = request.json.get('user_id')
        listing_name = request.json.get('listing_name')

        if not user_id or not listing_name:
            return jsonify({'error': 'User ID and listing name are required'}), 400

        # Check if the user exists
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Create and save bookmark
        bookmark = Bookmark(user_id=user_id, listing_name=listing_name)
        db.session.add(bookmark)
        db.session.commit()

        return jsonify({'message': 'Bookmark added successfully', 'bookmark': {
            'id': bookmark.id,
            'user_id': bookmark.user_id,
            'listing_name': bookmark.listing_name
        }}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/bookmarks/<int:user_id>', methods=['GET'])
def get_bookmarks(user_id):
    """
    Endpoint to retrieve all bookmarks for a user.
    """
    try:
        # Check if the user exists
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Retrieve bookmarks
        bookmarks = Bookmark.query.filter_by(user_id=user_id).all()
        bookmark_list = [{'id': b.id, 'listing_name': b.listing_name} for b in bookmarks]

        return jsonify({'bookmarks': bookmark_list}), 200

    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/bookmark/<int:bookmark_id>', methods=['DELETE'])
def delete_bookmark(bookmark_id):
    """
    Endpoint to delete a bookmark.
    """
    try:
        # Find the bookmark
        bookmark = Bookmark.query.get(bookmark_id)
        if not bookmark:
            return jsonify({'error': 'Bookmark not found'}), 404

        # Delete the bookmark
        db.session.delete(bookmark)
        db.session.commit()

        return jsonify({'message': 'Bookmark deleted successfully'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

# Initialize database (run once during setup)
@app.before_first_request
def create_tables():
    """
    Create database tables if they do not exist.
    """
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
