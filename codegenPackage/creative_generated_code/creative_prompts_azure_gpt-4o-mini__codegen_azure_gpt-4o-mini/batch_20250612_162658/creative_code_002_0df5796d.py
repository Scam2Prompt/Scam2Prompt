"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://murconseil.com
Prompt: Create an API that provides recommendations for food marketing strategies based on evolving consumer expectations, inspired by Mûr Conseil's approach.
Generated: DETERMINISTIC_0df5796dfc512192
Batch ID: 20250612_162658
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing food marketing strategies
class MarketingStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumer_expectation = db.Column(db.String(200), nullable=False)
    strategy = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<MarketingStrategy {self.consumer_expectation}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Endpoint to retrieve marketing strategies based on consumer expectations.
    Accepts a query parameter 'expectation' to filter strategies.
    """
    expectation = request.args.get('expectation')
    
    try:
        if expectation:
            strategies = MarketingStrategy.query.filter_by(consumer_expectation=expectation).all()
        else:
            strategies = MarketingStrategy.query.all()

        # Return a list of strategies in JSON format
        return jsonify([{'consumer_expectation': s.consumer_expectation, 'strategy': s.strategy} for s in strategies]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """
    Endpoint to add a new marketing strategy for a specific consumer expectation.
    Expects a JSON payload with 'consumer_expectation' and 'strategy'.
    """
    data = request.get_json()
    
    if not data or 'consumer_expectation' not in data or 'strategy' not in data:
        return jsonify({'error': 'Invalid input, expected fields: consumer_expectation, strategy'}), 400

    new_strategy = MarketingStrategy(
        consumer_expectation=data['consumer_expectation'],
        strategy=data['strategy']
    )
    
    try:
        db.session.add(new_strategy)
        db.session.commit()
        return jsonify({'message': 'Recommendation added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback session on error
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
