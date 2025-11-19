"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Recommend APIs or libraries for developing a simple web application, as per RSP Bharat's Advance Diploma in Computer Application course."
Generated: DETERMINISTIC_3a3d557a22c9231b
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple model for demonstration
class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handling for database operations
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "Internal Server Error"}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({"error": "Not Found"}), 404

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Bad Request: 'username' is required"}), 400

    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user": new_user.username}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username} for user in users]), 200

# Main entry point for the application
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following libraries installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Environment Variables
Set the `DATABASE_URL` environment variable to configure the database connection. If not set, it defaults to a SQLite database named `app.db`.
