"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a code snippet for a multipurpose CMS that integrates with a cooperative management system, similar to Nexelit.
Generated: DETERMINISTIC_d83b856b3545ca3f
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/users`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# multipurpose_cms.py

# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handling for database-related errors
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    response = {
        'error': str(error),
        'status_code': error.code
    }
    return jsonify(response), error.code

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_user = User(username=data['username'], email=data['email'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'user': new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

```bash
# requirements.txt
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
```

### Instructions to Run the Code:
1. Ensure you have Python installed on your machine.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python multipurpose_cms.py
   ```
5. Use a REST client (like Postman) to interact with the API at `http://127.0.0.1:5000/users`.
