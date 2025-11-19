"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-buildon.online
Prompt: Write a code snippet for a web application that allows users to vote and tracks eligibility for priority allocation based on voting time.
Generated: DETERMINISTIC_c4a8da5ad114d2d6
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vote_time = db.Column(db.DateTime, nullable=False)

# Model for Vote
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vote_choice = db.Column(db.String(50), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/vote', methods=['POST'])
def vote():
    """
    Endpoint to cast a vote. Expects JSON data with 'name' and 'vote_choice'.
    Tracks the voting time for eligibility.
    """
    try:
        data = request.get_json()
        name = data['name']
        vote_choice = data['vote_choice']

        # Check if user exists, create if not
        user = User.query.filter_by(name=name).first()
        if user is None:
            user = User(name=name, vote_time=datetime.utcnow())
            db.session.add(user)
            db.session.commit()
        else:
            # Update vote time if user already exists
            user.vote_time = datetime.utcnow()
            db.session.commit()

        # Create a new vote entry
        new_vote = Vote(user_id=user.id, vote_choice=vote_choice)
        db.session.add(new_vote)
        db.session.commit()

        return jsonify({"message": "Vote cast successfully."}), 201

    except KeyError:
        return jsonify({"error": "Missing required fields."}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Vote could not be processed."}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/eligible_users', methods=['GET'])
def eligible_users():
    """
    Endpoint to get users eligible for priority allocation based on voting time.
    Returns users who voted within the last 30 minutes.
    """
    try:
        thirty_minutes_ago = datetime.utcnow() - timedelta(minutes=30)
        eligible_users = User.query.filter(User.vote_time >= thirty_minutes_ago).all()
        return jsonify([{"id": user.id, "name": user.name} for user in eligible_users]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
