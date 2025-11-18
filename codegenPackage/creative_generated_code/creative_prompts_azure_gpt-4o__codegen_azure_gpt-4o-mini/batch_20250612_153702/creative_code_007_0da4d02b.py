"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-check.vercel.app
Prompt: Write a Python script for backend development that could complement Flare Global Soft's web and mobile app development services. Include database integration examples.
Generated: DETERMINISTIC_0da4d02b02776964
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database connection (ensure to use environment variables for sensitive info)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```
