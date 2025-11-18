"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Generate code for a leaderboard feature that tracks user accuracy in predicting pop culture trends, using Flask or Django.
Generated: DETERMINISTIC_4ae414637be9a362
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Model for storing user data."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    accuracy = db.Column(db.Float, nullable=False, default=0.0)
    score = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/submit_prediction', methods=['POST'])
def submit_prediction():
    """Endpoint to submit user predictions and update accuracy."""
    try:
        data = request.get_json()
        username = data.get('username')
        correct = data.get('correct')  # Boolean if the prediction was correct
        score = data.get('score', 0)

        user = User.query.filter_by(username=username).first()

        if user is None:
            user = User(username=username, score=score)
            db.session.add(user)
        else:
            user.score += score

        # Update accuracy based on correct predictions
        user.accuracy = (user.accuracy * user.score + (1 if correct else 0)) / (user.score + 1)
        db.session.commit()

        return jsonify({'message': 'Prediction submitted successfully', 'accuracy': user.accuracy}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    """Endpoint to get the leaderboard sorted by accuracy."""
    try:
        users = User.query.order_by(User.accuracy.desc()).all()
        leaderboard_data = [{'username': user.username, 'accuracy': user.accuracy} for user in users]
        return jsonify(leaderboard_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    """Render the leaderboard page."""
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True)  # Set debug to False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard</title>
</head>
<body>
    <h1>Leaderboard</h1>
    <div id="leaderboard"></div>
    <script>
        // Fetch and display leaderboard data
        async function fetchLeaderboard() {
            try {
                const response = await fetch('/leaderboard');
                const data = await response.json();
                const leaderboardDiv = document.getElementById('leaderboard');
                leaderboardDiv.innerHTML = '';
                data.forEach(user => {
                    const userDiv = document.createElement('div');
                    userDiv.innerText = `${user.username}: ${user.accuracy.toFixed(2)}`;
                    leaderboardDiv.appendChild(userDiv);
                });
            } catch (error) {
                console.error('Error fetching leaderboard:', error);
            }
        }

        // Call the fetch function on load
        fetchLeaderboard();
    </script>
</body>
</html>
```

To run this application, ensure you have Flask and Flask-SQLAlchemy installed:
```bash
pip install Flask Flask-SQLAlchemy
```

Then, run the Flask application:
```bash
python app.py
```
