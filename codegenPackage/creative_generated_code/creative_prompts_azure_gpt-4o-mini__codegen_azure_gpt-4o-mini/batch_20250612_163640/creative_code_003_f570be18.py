"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://randomarts.netlify.app
Prompt: Create an API endpoint that allows users to check the status of their NFT minting process, inspired by the Randomarts minting model.
Generated: DETERMINISTIC_f570be18730e4130
Batch ID: 20250612_163640
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
from datetime import datetime
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_minting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFT minting status
class NFTMintingStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # e.g., 'pending', 'successful', 'failed'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/minting_status/<user_id>', methods=['GET'])
def check_minting_status(user_id):
    """
    API endpoint to check the NFT minting status for a given user.
    
    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        JSON response with the minting status or error message.
    """
    try:
        # Retrieve the minting status for the user
        minting_status = NFTMintingStatus.query.filter_by(user_id=user_id).first()
        
        if minting_status is None:
            return jsonify({'message': 'User not found or no minting process initiated.'}), 404
        
        return jsonify({
            'user_id': minting_status.user_id,
            'status': minting_status.status,
            'created_at': minting_status.created_at.isoformat()
        }), 200

    except Exception as e:
        # Log the error for debugging and return a server error response
        app.logger.error(f'Error checking minting status for user {user_id}: {e}')
        return jsonify({'message': 'Internal server error.'}), 500

@app.route('/api/initiate_minting', methods=['POST'])
def initiate_minting():
    """
    API endpoint to initiate the NFT minting process for a user.
    
    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        JSON response indicating the initiation of the minting process.
    """
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'message': 'user_id is required.'}), 400

    try:
        # Simulate the minting process with a random status
        status = random.choice(['pending', 'successful', 'failed'])
        new_minting_status = NFTMintingStatus(user_id=user_id, status=status)

        db.session.add(new_minting_status)
        db.session.commit()

        return jsonify({'message': 'Minting process initiated.', 'status': status}), 201

    except Exception as e:
        app.logger.error(f'Error initiating minting for user {user_id}: {e}')
        return jsonify({'message': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
