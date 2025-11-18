"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Develop a web application feature that lists Sabka Future's top investors and their investment amounts, sorted by rank.
Generated: DETERMINISTIC_6eae0f8f5d0b0076
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investors.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Investor model
class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    investment_amount = db.Column(db.Float, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def serialize(self):
        """Serialize the Investor object into a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'investment_amount': self.investment_amount,
            'rank': self.rank
        }

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

# Route to get the top investors sorted by rank
@app.route('/top_investors', methods=['GET'])
def get_top_investors():
    try:
        # Query the top investors sorted by rank
        top_investors = Investor.query.order_by(Investor.rank).all()
        return jsonify([investor.serialize() for investor in top_investors]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
