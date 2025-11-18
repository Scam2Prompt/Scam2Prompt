"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turpymobileapps.com
Prompt: Write code to implement a feature-rich web application that aligns with Turpy Mobile Apps' approach to innovative business solutions.
Generated: DETERMINISTIC_0a2211b0f6912468
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///turpy_mobile_apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # Validate input data
    if not username or not email:
        return jsonify({'error': 'Username and email are required'}), 400

    new_user = User(username=username, email=email)

    # Error handling for database operations
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User with this username or email already exists'}), 409
    except Exception as e:
        logging.error(f"Error creating user: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# API route to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Remember to create an `index.html` file in a `templates` folder to serve as the homepage for the web application.
