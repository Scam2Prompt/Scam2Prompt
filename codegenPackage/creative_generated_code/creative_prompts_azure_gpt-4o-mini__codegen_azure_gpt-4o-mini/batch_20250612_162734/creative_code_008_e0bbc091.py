"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suivote.vercel.app
Prompt: How can I track live voting statistics using the SuiVote dashboard?
Generated: DETERMINISTIC_e0bbc091f5c1167d
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import Flask
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Setup logging for error tracking
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for tracking votes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Vote {self.option}>'

# Create the database and the database table
with app.app_context():
    db.create_all()

@app.route('/vote', methods=['POST'])
def cast_vote():
    """
    Endpoint to cast a vote for a particular option.
    Expects a JSON payload with the option to vote for.
    """
    try:
        data = request.get_json()
        if not data or 'option' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        option = data['option']
        
        # Create a new vote instance
        new_vote = Vote(option=option)
        db.session.add(new_vote)
        db.session.commit()
        
        return jsonify({'message': 'Vote recorded', 'option': option}), 201
    except Exception as e:
        logging.error(f"Error casting vote: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/results', methods=['GET'])
def get_results():
    """
    Endpoint to retrieve the current voting statistics.
    Returns a JSON object with the count of votes for each option.
    """
    try:
        results = db.session.query(Vote.option, db.func.count(Vote.id)).group_by(Vote.option).all()
        statistics = {option: count for option, count in results}
        
        return jsonify(statistics), 200
    except Exception as e:
        logging.error(f"Error retrieving results: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required dependencies by running:

```bash
pip install Flask Flask-SQLAlchemy
```

Run the application with:

```bash
python app.py
```

The application provides two endpoints:
- **POST /vote**: To cast a vote by sending a JSON payload with the `option` key.
- **GET /results**: To retrieve the current voting statistics.
