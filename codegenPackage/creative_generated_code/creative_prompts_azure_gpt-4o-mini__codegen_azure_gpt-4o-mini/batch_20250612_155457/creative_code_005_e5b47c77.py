"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipmbway.pages.dev
Prompt: How can I develop an API endpoint to retrieve the latest proof of reserves for IPMB's gold-backed tokens?
Generated: DETERMINISTIC_e5b47c779e38fc11
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proof_of_reserves.db'
db = SQLAlchemy(app)

# Define the ProofOfReserves model
class ProofOfReserves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_amount = db.Column(db.Float, nullable=False)
    gold_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'token_amount': self.token_amount,
            'gold_amount': self.gold_amount,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/proof_of_reserves/latest', methods=['GET'])
def get_latest_proof_of_reserves():
    """API endpoint to retrieve the latest proof of reserves."""
    try:
        latest_proof = ProofOfReserves.query.order_by(ProofOfReserves.timestamp.desc()).first()
        if latest_proof is None:
            return jsonify({'error': 'No proof of reserves available'}), 404
        
        return jsonify(latest_proof.to_dict()), 200
    except Exception as e:
        # Log the exception (logging mechanism can be integrated here)
        return jsonify({'error': 'An error occurred while retrieving data', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development (set debug=False in production)
    app.run(debug=True)
```
