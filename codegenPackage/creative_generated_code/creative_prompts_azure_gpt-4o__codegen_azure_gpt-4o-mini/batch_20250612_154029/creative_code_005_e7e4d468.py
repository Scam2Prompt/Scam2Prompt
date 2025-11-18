"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-ethereal.trade
Prompt: Create a RESTful API endpoint that fetches and displays the final voting round details, including the number of voters, total incentives, and rewards, as described on the Ethereal Vote webpage.
Generated: DETERMINISTIC_e7e4d46860e80db4
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'  # Update with your database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Voting model
class Voting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_voters = db.Column(db.Integer, nullable=False)
    total_incentives = db.Column(db.Float, nullable=False)
    rewards = db.Column(db.Float, nullable=False)

    def as_dict(self):
        """Convert model instance to dictionary."""
        return {
            'number_of_voters': self.number_of_voters,
            'total_incentives': self.total_incentives,
            'rewards': self.rewards
        }

# Create the database and tables (for the first run)
with app.app_context():
    db.create_all()

@app.route('/api/voting/final-round', methods=['GET'])
def get_final_voting_round():
    """Fetch the final voting round details."""
    try:
        # Fetch the latest voting details
        final_round = Voting.query.order_by(Voting.id.desc()).first()
        
        if final_round is None:
            return jsonify({"error": "No voting data found."}), 404
        
        return jsonify(final_round.as_dict()), 200

    except SQLAlchemyError as e:
        # Handle any database errors
        return jsonify({"error": "Database error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Turn off debug mode in production
```
