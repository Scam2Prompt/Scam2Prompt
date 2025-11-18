"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfl.org
Prompt: Develop a governance voting system for Lynex FI that allows community members to participate in decisions about new features or liquidity distribution.
Generated: DETERMINISTIC_d7ff2bec22c05b13
Batch ID: 20250612_150417
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///governance_voting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a voting option
class VotingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0)

# Database model for a user vote
class UserVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    voting_option_id = db.Column(db.Integer, db.ForeignKey('voting_option.id'), nullable=False)

# Schema for input validation
class VotingOptionSchema(Schema):
    feature = fields.Str(required=True)

class UserVoteSchema(Schema):
    user_id = fields.Str(required=True)
    voting_option_id = fields.Int(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/options', methods=['POST'])
def create_option():
    """
    Endpoint to create a new voting option.
    """
    schema = VotingOptionSchema()
    
    try:
        # Validate input data
        data = schema.load(request.json)
        new_option = VotingOption(feature=data['feature'])

        db.session.add(new_option)
        db.session.commit()
        
        return jsonify({"id": new_option.id, "feature": new_option.feature, "votes": new_option.votes}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Could not create the voting option."}), 500

@app.route('/vote', methods=['POST'])
def cast_vote():
    """
    Endpoint for a user to cast a vote for a specific option.
    """
    schema = UserVoteSchema()
    
    try:
        # Validate input data
        data = schema.load(request.json)
        user_vote = UserVote(user_id=data['user_id'], voting_option_id=data['voting_option_id'])

        # Check if the user has already voted
        if UserVote.query.filter_by(user_id=user_vote.user_id, voting_option_id=user_vote.voting_option_id).first():
            return jsonify({"error": "User has already voted for this option."}), 409

        db.session.add(user_vote)
        
        # Update the vote count
        option = VotingOption.query.get(user_vote.voting_option_id)
        if option:
            option.votes += 1
            db.session.commit()
            return jsonify({"message": "Vote cast successfully!", "votes": option.votes}), 200
        else:
            db.session.rollback()
            return jsonify({"error": "Voting option not found."}), 404
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Could not register the vote."}), 500

@app.route('/results', methods=['GET'])
def get_results():
    """
    Endpoint to retrieve the voting results.
    """
    options = VotingOption.query.all()
    results = [{"id": option.id, "feature": option.feature, "votes": option.votes} for option in options]
    
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
```
