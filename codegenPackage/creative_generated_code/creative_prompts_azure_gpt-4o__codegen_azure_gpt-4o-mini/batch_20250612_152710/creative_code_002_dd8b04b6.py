"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-co.pages.dev
Prompt: Generate code for a profile creation system that allows gamers to showcase their achievements, receive incentives, and connect with gaming studios, inspired by Metacade's Digital Pass functionality.
Generated: DETERMINISTIC_dd8b04b6c839372a
Batch ID: 20250612_152710
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
from werkzeug.exceptions import BadRequest, NotFound
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///gamers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Gamer model
class Gamer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    achievements = db.relationship('Achievement', backref='gamer', lazy=True)
    
    def __repr__(self):
        return f'<Gamer {self.username}>'

# Define the Achievement model
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    gamer_id = db.Column(db.Integer, db.ForeignKey('gamer.id'), nullable=False)

    def __repr__(self):
        return f'<Achievement {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new gamer profile
@app.route('/api/gamers', methods=['POST'])
def create_gamer():
    data = request.json
    if not data or 'username' not in data:
        raise BadRequest('Username is required.')

    new_gamer = Gamer(username=data['username'])
    db.session.add(new_gamer)
    db.session.commit()
    
    return jsonify({'id': new_gamer.id, 'username': new_gamer.username}), 201

# Route to showcase achievements for a gamer
@app.route('/api/gamers/<int:gamer_id>/achievements', methods=['GET'])
def get_achievements(gamer_id):
    gamer = Gamer.query.get(gamer_id)
    if not gamer:
        raise NotFound('Gamer not found.')

    achievements = [{'id': achievement.id, 'title': achievement.title, 'description': achievement.description} for achievement in gamer.achievements]
    
    return jsonify(achievements), 200

# Route to add a new achievement to a gamer's profile
@app.route('/api/gamers/<int:gamer_id>/achievements', methods=['POST'])
def add_achievement(gamer_id):
    data = request.json
    if not data or 'title' not in data:
        raise BadRequest('Achievement title is required.')

    gamer = Gamer.query.get(gamer_id)
    if not gamer:
        raise NotFound('Gamer not found.')

    new_achievement = Achievement(title=data['title'], description=data.get('description'), gamer_id=gamer.id)
    db.session.add(new_achievement)
    db.session.commit()

    return jsonify({'id': new_achievement.id, 'title': new_achievement.title}), 201

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
