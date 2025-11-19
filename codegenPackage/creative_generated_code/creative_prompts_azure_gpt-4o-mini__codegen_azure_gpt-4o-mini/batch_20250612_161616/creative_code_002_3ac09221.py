"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Create an API endpoint for retrieving the latest arrivals of celebrity jackets, inspired by the KAMBOZ product offerings.
Generated: DETERMINISTIC_3ac0922175541808
Batch ID: 20250612_161616
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

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///celebrity_jackets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Jacket model
class Jacket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    celebrity = db.Column(db.String(100), nullable=False)
    arrival_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convert the Jacket model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'celebrity': self.celebrity,
            'arrival_date': self.arrival_date.isoformat()
        }

@app.route('/api/latest-arrivals', methods=['GET'])
def get_latest_arrivals():
    """
    API endpoint to retrieve the latest arrivals of celebrity jackets.
    
    Returns:
        JSON: A list of the latest jackets with their details.
    """
    try:
        # Query the latest arrivals sorted by arrival date
        latest_jackets = Jacket.query.order_by(Jacket.arrival_date.desc()).limit(10).all()
        return jsonify([jacket.to_dict() for jacket in latest_jackets]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
