"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkub-claim-bitcoin-bonus.kesug.com
Prompt: Write Python code for a web application that utilizes a hosting service supporting Python apps and unlimited resources.
Generated: DETERMINISTIC_b86e03fdc281575e
Batch ID: 20250612_151414
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
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the database URI, assuming a PostgreSQL database for production
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for a simple resource, e.g., a User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user and store it in the database."""
    data = request.json
    username = data.get('username')
    email = data.get('email')

    # Basic validation
    if not username or not email:
        return jsonify({'error': 'Username and email are required.'}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'User already exists.'}), 409

    # Create and save the new user
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'User created successfully!'}), 201

# Route to get a user by username
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Retrieve a user by their username."""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found.'}), 404
    return jsonify({'username': user.username, 'email': user.email}), 200

# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions that occur during request processing."""
    return jsonify({'error': str(e)}), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the application on the host and port specified by environment variables or defaults
    app.run(host=os.getenv('HOST', '0.0.0.0'), port=int(os.getenv('PORT', 5000)))
```

To run this application, ensure you have the following environment variables set up:
- `DATABASE_URL`: The connection string for your PostgreSQL database.
- `HOST`: (Optional) The host address to run the app, default is `0.0.0.0`.
- `PORT`: (Optional) The port number to run the app, default is `5000`.

Make sure to install Flask and SQLAlchemy with:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate psycopg2
``` 

Remember to run database migrations using Flask-Migrate to set up the database schema.
