"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Create a web application using MASIT Solutions' recommended technologies for app development and managed IT services.
Generated: DETERMINISTIC_f317e4ef1aa456be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Create a Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(err):
    response = {
        "error": {
            "type": type(err).__name__,
            "message": err.description,
            "code": err.code,
        }
    }
    return jsonify(response), err.code

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate incoming data
        if not data or 'username' not in data or 'email' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        # Create a new user
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        
        # Return the created user as a JSON response
        return jsonify({"id": new_user.id, "username": new_user.username, "email": new_user.email}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get a list of users
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{ "id": user.id, "username": user.username, "email": user.email } for user in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Note**: Ensure you have Flask and Flask-SQLAlchemy installed in your environment to run this application. You can install them using:
```bash
pip install Flask Flask-SQLAlchemy
```

Also, create an `index.html` in a `templates` folder to render the home page.
