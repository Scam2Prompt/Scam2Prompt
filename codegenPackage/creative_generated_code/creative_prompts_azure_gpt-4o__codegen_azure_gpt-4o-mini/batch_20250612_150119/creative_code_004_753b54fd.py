"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Create a backend API endpoint to manage RPGF rounds and project submissions, ensuring compatibility with EasyRetroPGF.
Generated: DETERMINISTIC_753b54fd3d48c475
Batch ID: 20250612_150119
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rpgf.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for RPGF Rounds
class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    submissions = db.relationship('Submission', backref='round', lazy=True)

# Model for Submissions
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new RPGF round
@app.route('/api/rounds', methods=['POST'])
def create_round():
    data = request.json
    try:
        new_round = Round(title=data['title'], description=data.get('description'))
        db.session.add(new_round)
        db.session.commit()
        return jsonify({"message": "Round created", "round_id": new_round.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all RPGF rounds
@app.route('/api/rounds', methods=['GET'])
def get_rounds():
    rounds = Round.query.all()
    return jsonify([{"id": r.id, "title": r.title, "description": r.description} for r in rounds]), 200

# API endpoint to create a new submission for a specific round
@app.route('/api/rounds/<int:round_id>/submissions', methods=['POST'])
def create_submission(round_id):
    data = request.json
    try:
        new_submission = Submission(user=data['user'], content=data['content'], round_id=round_id)
        db.session.add(new_submission)
        db.session.commit()
        return jsonify({"message": "Submission created", "submission_id": new_submission.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all submissions for a specific round
@app.route('/api/rounds/<int:round_id>/submissions', methods=['GET'])
def get_submissions(round_id):
    submissions = Submission.query.filter_by(round_id=round_id).all()
    return jsonify([{"id": s.id, "user": s.user, "content": s.content} for s in submissions]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500 (internal server error)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
