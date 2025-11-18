"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owowiw.pages.dev
Prompt: Suggest tools or frameworks for building a secure registration system for digital artists, inspired by JRNY Gallery's three-step onboarding process.
Generated: DETERMINISTIC_e94e032e3e7fa469
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artists.db'  # Use a secure database
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define the Artist model
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Schema for input validation
class ArtistSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=lambda p: len(p) >= 6)

# Initialize the database (Create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Registration endpoint
@app.route('/register', methods=['POST'])
def register_artist():
    try:
        # Validate incoming data
        artist_schema = ArtistSchema()
        data = artist_schema.load(request.json)

        # Hash the password for security
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        # Create a new Artist instance
        new_artist = Artist(username=data['username'], email=data['email'], password=hashed_password)

        # Add the artist to the database
        db.session.add(new_artist)
        db.session.commit()

        # Create JWT token for the registered user
        access_token = create_access_token(identity=new_artist.username)
        return jsonify(message="Registration successful!", token=access_token), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle general exceptions
        return jsonify(message="An error occurred during registration.", error=str(e)), 500

# Login endpoint (for demonstration purposes)
@app.route('/login', methods=['POST'])
def login_artist():
    data = request.json
    artist = Artist.query.filter_by(email=data['email']).first()
    if artist and bcrypt.check_password_hash(artist.password, data['password']):
        access_token = create_access_token(identity=artist.username)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```
