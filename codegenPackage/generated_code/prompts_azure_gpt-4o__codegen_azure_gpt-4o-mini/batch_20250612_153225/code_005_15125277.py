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
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_speech_pathology.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Team model
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    members = db.relationship('Member', backref='team', lazy=True)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

# Define the schema for validation
class TeamSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class MemberSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    team_id = fields.Int(required=True)

# Initialize schemas
team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# Route to create a new team
@app.route('/teams', methods=['POST'])
def create_team():
    try:
        # Validate and deserialize input
        team_data = team_schema.load(request.json)
        new_team = Team(name=team_data['name'])
        db.session.add(new_team)
        db.session.commit()
        return team_schema.jsonify(new_team), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all teams
@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return teams_schema.jsonify(teams), 200

# Route to add a member to a team
@app.route('/teams/<int:team_id>/members', methods=['POST'])
def add_member(team_id):
    try:
        # Validate and deserialize input
        member_data = member_schema.load(request.json)
        new_member = Member(name=member_data['name'], role=member_data['role'], team_id=team_id)
        db.session.add(new_member)
        db.session.commit()
        return member_schema.jsonify(new_member), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all members of a team
@app.route('/teams/<int:team_id>/members', methods=['GET'])
def get_members(team_id):
    members = Member.query.filter_by(team_id=team_id).all()
    return members_schema.jsonify(members), 200

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

### Instructions to Run the Application
1. Ensure you have Python installed on your machine.
2. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
   ```
3. Save the code in a file named `app.py`.
4. Run the application:
   ```bash
   python app.py
   ```
5. Use a tool like Postman or curl to interact with the API endpoints.
