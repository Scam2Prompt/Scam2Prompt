"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: How can I develop a community platform for women to share their experiences and support each other in emotional restoration, similar to the "Comunidade Mulheres Restauradas"?
Generated: DETERMINISTIC_63ec76ebb52d5ea7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///community.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define User model for the community platform
class User(db.Model):
    """Model representing a user in the community."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    experiences = db.relationship('Experience', backref='user', lazy=True)

class Experience(db.Model):
    """Model representing an experience shared by a user."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define schema for input validation using Marshmallow
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)

class ExperienceSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)

# Initialize schemas
user_schema = UserSchema()
experience_schema = ExperienceSchema()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    json_data = request.get_json()
    try:
        data = user_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create new user and add to the database
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/experience', methods=['POST'])
def share_experience():
    """Endpoint for users to share their experiences."""
    json_data = request.get_json()
    try:
        data = experience_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create new experience and add to the database
    user_id = request.args.get('user_id')  # Expecting user_id as a query parameter
    new_experience = Experience(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(new_experience)
    db.session.commit()

    return jsonify({"message": "Experience shared successfully!"}), 201

@app.route('/experiences', methods=['GET'])
def get_experiences():
    """Endpoint to retrieve all shared experiences."""
    experiences = Experience.query.all()
    experiences_list = [{"id": exp.id, "title": exp.title, "content": exp.content, "user_id": exp.user_id} for exp in experiences]
    return jsonify(experiences_list), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Instructions to Run:

1. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
   ```

2. Set your database URL in the environment variable `DATABASE_URL` or modify the SQLite URI in the code.

3. Create and apply the database migrations:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the application:
   ```bash
   python community_platform.py
   ```

5. Use a tool like Postman or curl to test the API endpoints for user registration and experience sharing.
