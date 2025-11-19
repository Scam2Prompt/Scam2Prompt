"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Develop a web application feature that allows users to select influencers based on niche and engagement rate for their brand's promotional strategies.
Generated: DETERMINISTIC_233e907cd2a32914
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for the sake of simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///influencers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Influencer model
class Influencer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    niche = db.Column(db.String(50), nullable=False)
    engagement_rate = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Influencer object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'niche': self.niche,
            'engagement_rate': self.engagement_rate
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get influencers based on niche and engagement rate
@app.route('/influencers', methods=['GET'])
def get_influencers():
    try:
        # Get query parameters for niche and minimum engagement rate
        niche = request.args.get('niche', type=str)
        min_engagement_rate = request.args.get('min_engagement_rate', type=float)

        # Filter influencers based on the provided parameters
        query = Influencer.query

        if niche:
            query = query.filter_by(niche=niche)

        if min_engagement_rate is not None:
            query = query.filter(Influencer.engagement_rate >= min_engagement_rate)

        # Retrieve results
        influencers = query.all()

        # Return results in JSON format
        return jsonify([influencer.to_dict() for influencer in influencers]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle all other errors
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
