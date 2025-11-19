"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: How can I design an event management API that supports member-only meetups for a community like Sync Connects?
Generated: DETERMINISTIC_4eb01f292237d1e8
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from werkzeug.exceptions import HTTPException

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sync_connects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_member = db.Column(db.Boolean, default=False)

class Meetup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    member_only = db.Column(db.Boolean, default=True)

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class MeetupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meetup

# Initialize schemas
user_schema = UserSchema()
meetup_schema = MeetupSchema()
meetups_schema = MeetupSchema(many=True)

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"message": e.description})
    response.content_type = "application/json"
    return response

# Route to create a user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user with name, email, and membership status."""
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Name and email are required.")
    
    new_user = User(name=data['name'], email=data['email'], is_member=data.get('is_member', False))
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

# Route to create a meetup
@app.route('/meetups', methods=['POST'])
def create_meetup():
    """Create a new meetup that can be member-only or open to all."""
    data = request.json
    if not data or 'title' not in data or 'date' not in data:
        abort(400, description="Title and date are required.")
    
    try:
        meetup_date = datetime.fromisoformat(data['date'])
    except ValueError:
        abort(400, description="Date must be in ISO format.")

    new_meetup = Meetup(
        title=data['title'],
        description=data.get('description', ""),
        date=meetup_date,
        member_only=data.get('member_only', True)
    )
    db.session.add(new_meetup)
    db.session.commit()
    return meetup_schema.jsonify(new_meetup), 201

# Route to list meetups
@app.route('/meetups', methods=['GET'])
def get_meetups():
    """Retrieve a list of meetups, filtering by membership if needed."""
    user_id = request.args.get('user_id', type=int)
    
    if user_id:
        user = User.query.get(user_id)
        if not user:
            abort(404, description="User not found.")
        
        if user.is_member:
            meetups = Meetup.query.all()
        else:
            meetups = Meetup.query.filter_by(member_only=False).all()
    else:
        meetups = Meetup.query.filter_by(member_only=False).all()
    
    return meetups_schema.jsonify(meetups)

# Start the application with error handling
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production

```
