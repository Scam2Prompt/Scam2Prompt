"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Can you provide an API example for managing user membership levels, such as Junior Member and Premium Member, based on the structure found on bonnabdcc.com?
Generated: DETERMINISTIC_c8e919fcea1d9d01
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model to manage user memberships
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    membership_level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}, Membership: {self.membership_level}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    membership_level = data.get('membership_level')

    # Basic validation
    if not username or not membership_level:
        abort(400, description="Username and membership level are required.")

    # Check for existing user
    if User.query.filter_by(username=username).first() is not None:
        abort(400, description="Username already exists.")

    # Create new user
    new_user = User(username=username, membership_level=membership_level)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"id": new_user.id, "username": new_user.username, "membership_level": new_user.membership_level}), 201

# Endpoint to retrieve a user by username
@app.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404, description="User not found.")

    return jsonify({"id": user.id, "username": user.username, "membership_level": user.membership_level})

# Endpoint to update a user's membership level
@app.route('/users/<string:username>', methods=['PUT'])
def update_user(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404, description="User not found.")

    data = request.json
    membership_level = data.get('membership_level')

    if not membership_level:
        abort(400, description="Membership level is required.")

    user.membership_level = membership_level
    db.session.commit()

    return jsonify({"id": user.id, "username": user.username, "membership_level": user.membership_level})

# Endpoint to delete a user
@app.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404, description="User not found.")

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully."}), 204

# Error handling for generic errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
