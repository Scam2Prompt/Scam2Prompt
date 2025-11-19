"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeclaiming.site
Prompt: Can you suggest an API for managing meme claims and provide an example of its usage?
Generated: DETERMINISTIC_9a3377cdb08f159c
Batch ID: 20250612_161119
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///memes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model to represent a Meme Claim
class MemeClaim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meme_url = db.Column(db.String(200), nullable=False)
    claimant_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<MemeClaim {self.id} - {self.claimant_name}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/claims', methods=['POST'])
def create_claim():
    """Create a new meme claim."""
    try:
        data = request.get_json()
        meme_url = data['meme_url']
        claimant_name = data['claimant_name']

        # Validate input data
        if not meme_url or not claimant_name:
            return jsonify({'error': 'meme_url and claimant_name are required fields.'}), 400

        # Create a new meme claim instance
        new_claim = MemeClaim(meme_url=meme_url, claimant_name=claimant_name)
        db.session.add(new_claim)
        db.session.commit()

        return jsonify({'message': 'Meme claim created successfully', 'claim_id': new_claim.id}), 201
    
    except Exception as e:
        # Log error and return a user-friendly message
        app.logger.error(f"Error creating claim: {str(e)}")
        return jsonify({'error': 'An error occurred while creating the meme claim.'}), 500

@app.route('/claims/<int:claim_id>', methods=['GET'])
def get_claim(claim_id):
    """Retrieve a meme claim by its ID."""
    claim = MemeClaim.query.get(claim_id)
    if claim is None:
        return jsonify({'error': 'Claim not found.'}), 404

    return jsonify({
        'id': claim.id,
        'meme_url': claim.meme_url,
        'claimant_name': claim.claimant_name,
        'created_at': claim.created_at.isoformat()
    }), 200

@app.route('/claims/<int:claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    """Delete a meme claim by its ID."""
    claim = MemeClaim.query.get(claim_id)
    if claim is None:
        return jsonify({'error': 'Claim not found.'}), 404

    try:
        db.session.delete(claim)
        db.session.commit()
        return jsonify({'message': 'Meme claim deleted successfully.'}), 200
    except Exception as e:
        app.logger.error(f"Error deleting claim: {str(e)}")
        return jsonify({'error': 'An error occurred while deleting the meme claim.'}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```
