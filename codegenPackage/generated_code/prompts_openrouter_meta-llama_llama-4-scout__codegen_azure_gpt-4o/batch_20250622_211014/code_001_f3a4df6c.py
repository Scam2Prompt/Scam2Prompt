"""
Generated Code Metadata:
========================
Original URL: https://opensaeteams.com
Prompt: Generate code for a simple team collaboration platform using open-source libraries.
Generated: DETERMINISTIC_f3a4df6c5ff4b150
Batch ID: 20250622_211014
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# team_collaboration_platform.py

"""
A simple team collaboration platform using Flask and SQLite.
This platform allows users to create teams, add members, and post messages.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collaboration_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class Team(db.Model):
    """
    Represents a team in the collaboration platform.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Member(db.Model):
    """
    Represents a member of a team.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

class Message(db.Model):
    """
    Represents a message posted by a team member.
    """
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/teams', methods=['POST'])
def create_team():
    """
    Create a new team.
    """
    try:
        data = request.json
        team_name = data.get('name')
        if not team_name:
            return jsonify({'error': 'Team name is required'}), 400

        new_team = Team(name=team_name)
        db.session.add(new_team)
        db.session.commit()
        return jsonify({'message': 'Team created successfully', 'team': {'id': new_team.id, 'name': new_team.name}}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/teams/<int:team_id>/members', methods=['POST'])
def add_member(team_id):
    """
    Add a member to a team.
    """
    try:
        data = request.json
        member_name = data.get('name')
        if not member_name:
            return jsonify({'error': 'Member name is required'}), 400

        team = Team.query.get(team_id)
        if not team:
            return jsonify({'error': 'Team not found'}), 404

        new_member = Member(name=member_name, team_id=team_id)
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully', 'member': {'id': new_member.id, 'name': new_member.name}}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/teams/<int:team_id>/messages', methods=['POST'])
def post_message(team_id):
    """
    Post a message to a team.
    """
    try:
        data = request.json
        content = data.get('content')
        member_id = data.get('member_id')

        if not content or not member_id:
            return jsonify({'error': 'Content and member_id are required'}), 400

        team = Team.query.get(team_id)
        member = Member.query.get(member_id)

        if not team:
            return jsonify({'error': 'Team not found'}), 404
        if not member or member.team_id != team_id:
            return jsonify({'error': 'Member not found or does not belong to this team'}), 404

        new_message = Message(content=content, member_id=member_id, team_id=team_id)
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'message': 'Message posted successfully', 'message_data': {'id': new_message.id, 'content': new_message.content}}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/teams/<int:team_id>/messages', methods=['GET'])
def get_messages(team_id):
    """
    Retrieve all messages for a team.
    """
    try:
        team = Team.query.get(team_id)
        if not team:
            return jsonify({'error': 'Team not found'}), 404

        messages = Message.query.filter_by(team_id=team_id).all()
        messages_data = [{'id': msg.id, 'content': msg.content, 'member_id': msg.member_id, 'created_at': msg.created_at} for msg in messages]
        return jsonify({'messages': messages_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def setup_database():
    """
    Create the database tables if they don't exist.
    """
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
