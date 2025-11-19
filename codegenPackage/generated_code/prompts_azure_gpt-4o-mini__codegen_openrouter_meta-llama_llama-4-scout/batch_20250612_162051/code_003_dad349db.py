"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Generate an API that connects women in Igbo communities for cultural preservation activities, reflecting the offerings of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_dad349dba7d3f035
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Igbo Cultural Preservation API**
=====================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-JWT-Extended 4.2+

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///igbo_cultural_preservation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({'msg': 'Please fill in all fields'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'msg': 'Email already exists'}), 400

        new_user = User(name, email, password, 'user')
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'msg': 'Please fill in all fields'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({'msg': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


@app.route('/events', methods=['GET'])
@jwt_required
def get_events():
    try:
        events = Event.query.all()
        output = []
        for event in events:
            event_data = {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}
            output.append(event_data)
        return jsonify({'events': output}), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


@app.route('/events', methods=['POST'])
@jwt_required
def create_event():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        title = data.get('title')
        description = data.get('description')
        date = data.get('date')

        if not title or not description or not date:
            return jsonify({'msg': 'Please fill in all fields'}), 400

        new_event = Event(title, description, date)
        db.session.add(new_event)
        db.session.commit()

        return jsonify({'msg': 'Event created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': str(e)}), 500


@app.route('/activities', methods=['GET'])
@jwt_required
def get_activities():
    try:
        activities = Activity.query.all()
        output = []
        for activity in activities:
            activity_data = {'id': activity.id, 'title': activity.title, 'description': activity.description}
            output.append(activity_data)
        return jsonify({'activities': output}), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
