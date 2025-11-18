"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testinguuu444.pages.dev
Prompt: Write code to create a social sharing feature for a gaming platform, allowing users to share their leaderboard rankings and quest progress, inspired by the "Universe Game" socials section.
Generated: DETERMINISTIC_ade15f89ac441f1a
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    quest_progress = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'quest_progress': self.quest_progress
        }

# Model for Leaderboard
class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref='leaderboard_entries')

# Endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], quest_progress=data['quest_progress'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

# Endpoint to share leaderboard ranking
@app.route('/api/share/leaderboard', methods=['POST'])
def share_leaderboard():
    data = request.json
    user_id = data.get('user_id')
    score = data.get('score')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    leaderboard_entry = Leaderboard(user_id=user.id, score=score)
    db.session.add(leaderboard_entry)
    db.session.commit()

    return jsonify({
        'message': 'Leaderboard score shared successfully',
        'username': user.username,
        'score': score
    }), 201

# Endpoint to share quest progress
@app.route('/api/share/quest', methods=['POST'])
def share_quest():
    data = request.json
    user_id = data.get('user_id')
    quest_progress = data.get('quest_progress')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.quest_progress = quest_progress
    db.session.commit()

    return jsonify({
        'message': 'Quest progress shared successfully',
        'username': user.username,
        'quest_progress': quest_progress
    }), 200

# Function to initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
