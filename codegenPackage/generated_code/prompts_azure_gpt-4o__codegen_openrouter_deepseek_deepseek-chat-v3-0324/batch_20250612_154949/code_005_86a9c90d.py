"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Develop a web application feature that allows teams to report their own scores using a shortcode, as described in Slo-Pitch Central's platform functionality.
Generated: DETERMINISTIC_86a9c90daf7335ad
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os
from datetime import datetime

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///scores.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    shortcode = db.Column(db.String(10), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class GameScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    opponent = db.Column(db.String(100), nullable=False)
    team_score = db.Column(db.Integer, nullable=False)
    opponent_score = db.Column(db.Integer, nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    verified = db.Column(db.Boolean, default=False)

    team = db.relationship('Team', backref=db.backref('scores', lazy=True))

# Helper functions
def validate_shortcode(shortcode):
    """Validate the shortcode format (3-10 alphanumeric chars)"""
    return re.match(r'^[a-zA-Z0-9]{3,10}$', shortcode) is not None

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/teams', methods=['POST'])
def create_team():
    """Create a new team with a shortcode"""
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('shortcode') or not data.get('password'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not validate_shortcode(data['shortcode']):
        return jsonify({'error': 'Invalid shortcode format'}), 400
    
    if Team.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'Team name already exists'}), 409
    
    if Team.query.filter_by(shortcode=data['shortcode']).first():
        return jsonify({'error': 'Shortcode already exists'}), 409
    
    team = Team(name=data['name'], shortcode=data['shortcode'])
    team.set_password(data['password'])
    
    try:
        db.session.add(team)
        db.session.commit()
        return jsonify({'message': 'Team created successfully', 'team_id': team.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/scores', methods=['POST'])
def report_score():
    """Report a game score using team shortcode"""
    data = request.get_json()
    
    if not data or not data.get('shortcode') or not data.get('password') or not data.get('opponent'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if 'team_score' not in data or 'opponent_score' not in data:
        return jsonify({'error': 'Missing score information'}), 400
    
    team = Team.query.filter_by(shortcode=data['shortcode']).first()
    if not team:
        return jsonify({'error': 'Invalid shortcode'}), 404
    
    if not team.check_password(data['password']):
        return jsonify({'error': 'Invalid password'}), 401
    
    try:
        score = GameScore(
            team_id=team.id,
            opponent=data['opponent'],
            team_score=int(data['team_score']),
            opponent_score=int(data['opponent_score'])
        )
        db.session.add(score)
        db.session.commit()
        return jsonify({'message': 'Score reported successfully', 'score_id': score.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/scores/<shortcode>', methods=['GET'])
def get_scores(shortcode):
    """Get all scores for a team using their shortcode"""
    team = Team.query.filter_by(shortcode=shortcode).first()
    if not team:
        return jsonify({'error': 'Invalid shortcode'}), 404
    
    scores = []
    for score in team.scores:
        scores.append({
            'id': score.id,
            'opponent': score.opponent,
            'team_score': score.team_score,
            'opponent_score': score.opponent_score,
            'reported_at': score.reported_at.isoformat(),
            'verified': score.verified
        })
    
    return jsonify({'team': team.name, 'scores': scores}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
