"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Develop a web application prototype for managing a hospital-based speech-language pathology service, including features for team supervision and sector structuring, inspired by Open Minds Instituto's consultancy offerings.
Generated: DETERMINISTIC_15125277477006fb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///speech_pathology.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    sector = db.relationship('Sector', backref=db.backref('teams', lazy=True))

    def __init__(self, name, sector_id):
        self.name = name
        self.sector_id = sector_id


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team = db.relationship('Team', backref=db.backref('patients', lazy=True))

    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id


# Routes
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'Logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/sectors', methods=['GET', 'POST'])
def sectors():
    try:
        if request.method == 'GET':
            sectors = Sector.query.all()
            return jsonify([{'id': s.id, 'name': s.name, 'description': s.description} for s in sectors]), 200
        elif request.method == 'POST':
            data = request.json
            sector = Sector(data['name'], data.get('description'))
            db.session.add(sector)
            db.session.commit()
            return jsonify({'message': 'Sector created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@app.route('/teams', methods=['GET', 'POST'])
def teams():
    try:
        if request.method == 'GET':
            teams = Team.query.all()
            return jsonify([{'id': t.id, 'name': t.name, 'sector_id': t.sector_id} for t in teams]), 200
        elif request.method == 'POST':
            data = request.json
            team = Team(data['name'], data['sector_id'])
            db.session.add(team)
            db.session.commit()
            return jsonify({'message': 'Team created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@app.route('/patients', methods=['GET', 'POST'])
def patients():
    try:
        if request.method == 'GET':
            patients = Patient.query.all()
            return jsonify([{'id': p.id, 'name': p.name, 'team_id': p.team_id} for p in patients]), 200
        elif request.method == 'POST':
            data = request.json
            patient = Patient(data['name'], data['team_id'])
            db.session.add(patient)
            db.session.commit()
            return jsonify({'message': 'Patient created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```python
# .env
DATABASE_URL=sqlite:///speech_pathology.db
```
