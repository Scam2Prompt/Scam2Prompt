"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Suggest a library for implementing a wishlist feature on an e-commerce site specializing in replica wrestling belts, such as WWE Legacy Title Belts and AEW World Tag Team Championship Belts.
Generated: DETERMINISTIC_d082be918772887d
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Here is production-ready Python code using Flask and SQLAlchemy for implementing a wishlist feature. The chosen library is `Flask-SQLAlchemy` to manage the database, with all best practices applied.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Define the WishlistItem model
class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    belt_name = db.Column(db.String(120), nullable=False)
    belt_description = db.Column(db.String(250), nullable=True)
    user = db.relationship('User', backref=db.backref('wishlist_items', lazy=True))

    def __repr__(self):
        return f"<WishlistItem {self.belt_name}>"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add an item to a user's wishlist
@app.route('/wishlist/add', methods=['POST'])
def add_to_wishlist():
    try:
        data = request.json
        username = data.get('username')
        belt_name = data.get('belt_name')
        belt_description = data.get('belt_description')

        # Validate the input
        if not username or not belt_name:
            return jsonify({"error": "username and belt_name are required"}), 400

        # Get or create the user
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        # Add the wishlist item
        wishlist_item = WishlistItem(user_id=user.id, belt_name=belt_name, belt_description=belt_description)
        db.session.add(wishlist_item)
        db.session.commit()

        return jsonify({"message": "Item added to wishlist", "item": {"username": username, "belt_name": belt_name}}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to view a user's wishlist
@app.route('/wishlist/<username>', methods=['GET'])
def view_wishlist(username):
    try:
        user = User.query.filter_by(username=username).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        wishlist = [
            {"belt_name": item.belt_name, "belt_description": item.belt_description}
            for item in user.wishlist_items
        ]

        return jsonify({"username": username, "wishlist": wishlist}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to remove an item from a user's wishlist
@app.route('/wishlist/remove', methods=['POST'])
def remove_from_wishlist():
    try:
        data = request.json
        username = data.get('username')
        belt_name = data.get('belt_name')

        # Validate the input
        if not username or not belt_name:
            return jsonify({"error": "username and belt_name are required"}), 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        item = WishlistItem.query.filter_by(user_id=user.id, belt_name=belt_name).first()
        if not item:
            return jsonify({"error": "Item not found in wishlist"}), 404

        db.session.delete(item)
        db.session.commit()

        return jsonify({"message": "Item removed from wishlist"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Features:
- **Add to Wishlist**: `/wishlist/add` (POST)
- **View Wishlist**: `/wishlist/<username>` (GET)
- **Remove from Wishlist**: `/wishlist/remove` (POST)

### Notes:
- Ensure that `Flask` and `Flask-SQLAlchemy` are installed (`pip install flask flask-sqlalchemy`).
- Replace SQLite with your preferred database for production use.
- Add authentication for real-world usage if needed.
