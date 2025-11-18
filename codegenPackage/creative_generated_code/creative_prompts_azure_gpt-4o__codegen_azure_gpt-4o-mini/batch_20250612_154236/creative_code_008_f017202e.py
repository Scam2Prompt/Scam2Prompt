"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Design an API endpoint to fetch genuine aftermarket replacement parts for BPL appliances, including details like part type, availability, and pricing.
Generated: DETERMINISTIC_f017202eb40eab33
Batch ID: 20250612_154236
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model to represent aftermarket parts for BPL appliances
class ReplacementPart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_type = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Boolean, default=True)
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'part_type': self.part_type,
            'availability': self.availability,
            'price': self.price
        }

@app.route('/api/parts', methods=['GET'])
def get_parts():
    """API endpoint to fetch genuine aftermarket replacement parts."""
    try:
        # Fetch all parts from the database
        parts = ReplacementPart.query.all()
        # Serialize parts to dictionary format
        return jsonify([part.serialize() for part in parts]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=False)
```
