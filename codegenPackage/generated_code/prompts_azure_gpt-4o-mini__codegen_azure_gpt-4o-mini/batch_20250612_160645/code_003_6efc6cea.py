"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Provide an example of a backend setup for a corporate website that includes custom design and management features, as outlined on ra-don.com.
Generated: DETERMINISTIC_6efc6cea34b72f7a
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model for managing users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for creating a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Define the route for retrieving all users
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define the route for updating a user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        user = User.query.get_or_404(user_id)
        user.username = data['username']
        user.email = data['email']
        db.session.commit()
        return jsonify({'message': 'User updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Define the route for deleting a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

### Requirements
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Create a `templates` directory and add an `index.html` file for the homepage.
- Set the `DATABASE_URL` environment variable for production use.
