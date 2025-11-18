"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-station-2.gitbook.io
Prompt: Generate code to implement a leaderboard system for a Web3 game, inspired by TON Station's "Storm the Leagues" Season 2 Finale event.
Generated: DETERMINISTIC_b22fe015bd5b8f7d
Batch ID: 20250612_153915
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model for the leaderboard
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new user or update score
@app.route('/api/leaderboard', methods=['POST'])
def add_or_update_user():
    data = request.get_json()
    username = data.get('username')
    score = data.get('score')

    if not username or not isinstance(score, int):
        return jsonify({'error': 'Invalid input'}), 400

    # Upsert user score
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            user.score = max(user.score, score)  # Update only if the new score is higher
        else:
            user = User(username=username, score=score)
            db.session.add(user)

        db.session.commit()
        return jsonify({'message': 'User score updated successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to fetch the leaderboard
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        users = User.query.order_by(User.score.desc()).limit(10).all()
        leaderboard = [{'username': user.username, 'score': user.score} for user in users]
        return jsonify(leaderboard), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=False)
```
