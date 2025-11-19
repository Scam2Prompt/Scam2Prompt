"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: Can you provide an example of an API that could be used to manage user registrations for a contest, like the one detailed on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_f4bea9fd81372ffd
Batch ID: 20250612_162734
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contest.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Marshmallow schema for User validation
class UserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)

# Initialize user schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user for the contest."""
    try:
        # Validate and deserialize input data
        user_data = user_schema.load(request.json)
        
        # Create a new User instance
        new_user = User(username=user_data['username'], email=user_data['email'])
        
        # Add to the database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify(user_schema.dump(new_user)), 201  # Return the created user with status 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400  # Return validation errors with status 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User with this email or username already exists."}), 409  # Conflict error
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # General error handling

@app.route('/users', methods=['GET'])
def get_users():
    """Endpoint to retrieve all registered users."""
    try:
        users = User.query.all()  # Query all users
        return jsonify(users_schema.dump(users)), 200  # Return users with status 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # General error handling

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
```
