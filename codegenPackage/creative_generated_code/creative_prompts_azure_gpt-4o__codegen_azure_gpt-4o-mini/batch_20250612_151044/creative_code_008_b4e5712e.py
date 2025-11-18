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
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for user bookmarks
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    listing_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f'<Bookmark {self.listing_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/bookmark', methods=['POST'])
def add_bookmark():
    """
    Endpoint to add a bookmark for a user.
    Expects JSON payload with 'listing_name'.
    """
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 403

    data = request.json
    listing_name = data.get('listing_name')

    if not listing_name:
        return jsonify({'message': 'Listing name is required'}), 400

    new_bookmark = Bookmark(user_id=session['user_id'], listing_name=listing_name)

    try:
        db.session.add(new_bookmark)
        db.session.commit()
        return jsonify({'message': 'Bookmark added successfully!', 'bookmark': listing_name}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Bookmark already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    """
    Endpoint to retrieve all bookmarks for the logged-in user.
    """
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 403

    bookmarks = Bookmark.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{'id': bookmark.id, 'listing_name': bookmark.listing_name} for bookmark in bookmarks]), 200

@app.route('/bookmark/<int:bookmark_id>', methods=['DELETE'])
def delete_bookmark(bookmark_id):
    """
    Endpoint to delete a specific bookmark by its ID.
    """
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 403

    bookmark = Bookmark.query.filter_by(id=bookmark_id, user_id=session['user_id']).first()

    if not bookmark:
        return jsonify({'message': 'Bookmark not found'}), 404

    db.session.delete(bookmark)
    db.session.commit()
    return jsonify({'message': 'Bookmark deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=False)
```
