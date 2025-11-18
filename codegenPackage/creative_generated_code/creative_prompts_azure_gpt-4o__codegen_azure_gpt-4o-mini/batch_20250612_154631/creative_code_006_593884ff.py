"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Suggest tools or frameworks for building a community-driven voting platform for $DOG token holders, referencing the rewards voting system mentioned.
Generated: DETERMINISTIC_593884ffe70b5dbf
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# voting_platform.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Model for the voting options
class VotingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_name = db.Column(db.String(100), nullable=False)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<VotingOption {self.option_name}>'

# Model for tracking user votes
class UserVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('voting_option.id'), nullable=False)

    def __repr__(self):
        return f'<UserVote UserID: {self.user_id}, OptionID: {self.option_id}>'

# Endpoint to create a new voting option
@app.route('/options', methods=['POST'])
def create_option():
    data = request.get_json()
    new_option = VotingOption(option_name=data['option_name'])
    db.session.add(new_option)
    db.session.commit()
    return jsonify({'message': 'Voting option created!'}), 201

# Endpoint to vote on an option
@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    user_id = data['user_id']
    option_id = data['option_id']

    # Check if the user has already voted
    if UserVote.query.filter_by(user_id=user_id, option_id=option_id).first():
        return jsonify({'message': 'User has already voted for this option.'}), 400

    try:
        # Record the vote
        new_vote = UserVote(user_id=user_id, option_id=option_id)
        db.session.add(new_vote)
        
        # Increment the vote count for the option
        option = VotingOption.query.get(option_id)
        option.votes += 1

        db.session.commit()
        return jsonify({'message': 'Vote recorded successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Error recording vote.', 'error': str(e)}), 500

# Endpoint to get voting results
@app.route('/results', methods=['GET'])
def get_results():
    try:
        options = VotingOption.query.all()
        results = [{ 'option_name': option.option_name, 'votes': option.votes } for option in options]
        return jsonify(results), 200
    except SQLAlchemyError as e:
        return jsonify({'message': 'Error fetching results.', 'error': str(e)}), 500

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Dependencies:
- Flask
- Flask-SQLAlchemy

### To run the code:
1. Install the dependencies using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Run the script:
   ```bash
   python voting_platform.py
   ```
3. Use a tool like Postman or Curl to interact with the API endpoints for creating options, voting, and retrieving results.
