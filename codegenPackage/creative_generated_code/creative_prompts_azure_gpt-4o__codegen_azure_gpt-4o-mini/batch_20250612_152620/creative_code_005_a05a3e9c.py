"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Provide an example of a REST API endpoint for retrieving staking statistics for $SCOTTY tokens, including total staked tokens, rewards per ETH block, and annual return percentages.
Generated: DETERMINISTIC_a05a3e9ce9de5843
Batch ID: 20250612_152620
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (you can change this to any other database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scotty_staking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy DB
db = SQLAlchemy(app)

# Define a model for StakingStatistics
class StakingStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_staked_tokens = db.Column(db.Float, nullable=False)
    rewards_per_eth_block = db.Column(db.Float, nullable=False)
    annual_return_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'total_staked_tokens': self.total_staked_tokens,
            'rewards_per_eth_block': self.rewards_per_eth_block,
            'annual_return_percentage': self.annual_return_percentage
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/staking_stats', methods=['GET'])
def get_staking_statistics():
    """Retrieve staking statistics for $SCOTTY tokens."""
    try:
        # Query the staking statistics from the database
        stats = StakingStatistics.query.first()

        # Check if statistics are found
        if not stats:
            return jsonify({"error": "No staking statistics found."}), 404

        # Return the statistics in JSON format
        return jsonify(stats.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Note:
- Ensure that the `Flask` and `Flask-SQLAlchemy` libraries are installed in your environment. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- You can add entries to the `StakingStatistics` table manually for testing purposes using the SQLAlchemy ORM or a database management tool.
