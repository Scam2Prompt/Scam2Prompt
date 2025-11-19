"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdadw3qqd.pages.dev
Prompt: Provide a sample code for integrating the leaderboard feature from the Puffer Events Chapter 3 into a web application.
Generated: DETERMINISTIC_aa6270fdd088a964
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Leaderboard entries
class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the LeaderboardEntry to a dictionary format."""
        return {'id': self.id, 'username': self.username, 'score': self.score}

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the current leaderboard entries."""
    try:
        entries = LeaderboardEntry.query.order_by(LeaderboardEntry.score.desc()).all()
        return jsonify([entry.to_dict() for entry in entries]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/leaderboard', methods=['POST'])
def add_entry():
    """Add a new entry to the leaderboard."""
    data = request.json
    username = data.get('username')
    score = data.get('score')

    if not username or not isinstance(score, int):
        return jsonify({'error': 'Invalid input'}), 400

    new_entry = LeaderboardEntry(username=username, score=score)
    
    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(new_entry.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Ensure that you have Flask and Flask-SQLAlchemy installed in your environment. You can install these using the following command:

```bash
pip install Flask Flask-SQLAlchemy
```
