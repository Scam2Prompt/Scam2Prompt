"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: "Develop a Flask API for managing Proof of Pitch-style startup competitions, including endpoints for submission, evaluation, and winner selection."
Generated: DETERMINISTIC_bc92ea22ad7fc419
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///competitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Submission model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    startup_name = db.Column(db.String(100), nullable=False)
    pitch_description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Submission {self.startup_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a startup pitch
@app.route('/submit', methods=['POST'])
def submit_pitch():
    data = request.get_json()
    if not data or 'startup_name' not in data or 'pitch_description' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_submission = Submission(
        startup_name=data['startup_name'],
        pitch_description=data['pitch_description']
    )

    try:
        db.session.add(new_submission)
        db.session.commit()
        return jsonify({'message': 'Submission successful', 'id': new_submission.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Submission failed, please try again'}), 500

# Endpoint to evaluate a submission
@app.route('/evaluate/<int:submission_id>', methods=['POST'])
def evaluate_submission(submission_id):
    data = request.get_json()
    if not data or 'score' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    submission = Submission.query.get(submission_id)
    if not submission:
        return jsonify({'error': 'Submission not found'}), 404

    submission.score = data['score']
    db.session.commit()
    return jsonify({'message': 'Evaluation updated successfully'}), 200

# Endpoint to select the winner based on highest score
@app.route('/winner', methods=['GET'])
def select_winner():
    submissions = Submission.query.all()
    if not submissions:
        return jsonify({'message': 'No submissions found'}), 404

    winner = max(submissions, key=lambda s: s.score if s.score is not None else -1)
    return jsonify({'winner': winner.startup_name, 'score': winner.score}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
