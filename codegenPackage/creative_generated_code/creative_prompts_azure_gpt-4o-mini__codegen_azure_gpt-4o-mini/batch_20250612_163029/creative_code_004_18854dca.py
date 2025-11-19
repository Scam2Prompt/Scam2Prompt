"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Design an API endpoint for Immediate Bitwave that retrieves a list of available investment education topics, including cryptocurrencies and risk management strategies.
Generated: DETERMINISTIC_18854dcafa6c8608
Batch ID: 20250612_163029
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

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_topics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Investment Education Topics
class InvestmentTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/investment-topics', methods=['GET'])
def get_investment_topics():
    """
    Retrieve a list of available investment education topics.
    Includes topics on cryptocurrencies and risk management strategies.
    """
    try:
        # Query all investment topics from the database
        topics = InvestmentTopic.query.all()
        # Convert topics to a list of dictionaries
        topics_list = [topic.to_dict() for topic in topics]
        
        # Return the list of topics as JSON response
        return jsonify(topics_list), 200

    except SQLAlchemyError as e:
        # Log the error and return a 500 Internal Server Error response
        app.logger.error(f"Database error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

Make sure to run `pip install Flask Flask-SQLAlchemy` to install the required dependencies before executing the code.
