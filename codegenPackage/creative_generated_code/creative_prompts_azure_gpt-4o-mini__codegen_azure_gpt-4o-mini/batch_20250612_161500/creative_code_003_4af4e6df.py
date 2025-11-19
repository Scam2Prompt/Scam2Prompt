"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalepullix.pages.dev
Prompt: Generate an API endpoint for user registration that mimics the Pullix account creation flow.
Generated: DETERMINISTIC_4af4e6df9b2032ac
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# User registration schema for input validation
class UserRegistrationSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, validate=lambda p: len(p) >= 6)

# User registration endpoint
@app.route('/api/register', methods=['POST'])
def register_user():
    try:
        # Validate the input data
        schema = UserRegistrationSchema()
        user_data = schema.load(request.json)

        # Check if the user already exists
        if User.query.filter((User.username == user_data['username']) | 
                              (User.email == user_data['email'])).first():
            return jsonify({"message": "Username or email already exists."}), 400
        
        # Create a new user
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=generate_password_hash(user_data['password'])
        )

        # Save the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201

    except ValidationError as ve:
        return jsonify({"message": "Validation error.", "errors": ve.messages}), 400
    except Exception as e:
        # Log the error or handle it as necessary
        return jsonify({"message": "An error occurred.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
