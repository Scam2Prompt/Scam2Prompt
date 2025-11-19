"""
Generated Code Metadata:
========================
Original URL: https://randomarts.netlify.app
Prompt: Create an API endpoint that allows users to check the status of their NFT minting process, inspired by the Randomarts minting model.
Generated: DETERMINISTIC_f570be18730e4130
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_minting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for NFT minting status
class NFTMintingStatus(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/minting_status/<string:user_id>', methods=['GET'])
def get_minting_status(user_id):
    """
    API endpoint to check the status of NFT minting for a given user.
    
    Args:
        user_id (str): The ID of the user whose minting status is being checked.
    
    Returns:
        JSON response containing the minting status or an error message.
    """
    try:
        # Query the database for the user's minting status
        status_record = NFTMintingStatus.query.filter_by(user_id=user_id).first()
        
        if status_record:
            return jsonify(status_record.to_dict()), 200
        else:
            return jsonify({'error': 'Minting status not found for this user.'}), 404

    except Exception as e:
        # Log the exception (in a real application, use a logging framework)
        print(f"Error retrieving minting status: {e}")
        return jsonify({'error': 'An error occurred while retrieving the minting status.'}), 500

@app.route('/api/minting_status', methods=['POST'])
def create_minting_status():
    """
    API endpoint to create a new NFT minting status entry.
    
    Returns:
        JSON response containing the created minting status.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        status = data.get('status')

        if not user_id or not status:
            return jsonify({'error': 'user_id and status are required.'}), 400

        # Create a new minting status record
        new_status = NFTMintingStatus(id=str(uuid.uuid4()), user_id=user_id, status=status)
        db.session.add(new_status)
        db.session.commit()

        return jsonify(new_status.to_dict()), 201

    except Exception as e:
        # Log the exception (in a real application, use a logging framework)
        print(f"Error creating minting status: {e}")
        return jsonify({'error': 'An error occurred while creating the minting status.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
