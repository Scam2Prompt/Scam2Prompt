"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessepollak-ebv.pages.dev
Prompt: Write a tutorial for building a photo-sharing application with blockchain integration, inspired by Jesse Pollak's interest in photography and engineering.
Generated: DETERMINISTIC_74dd0b49d88a6391
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# photo_sharing_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Ethereum settings
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
ACCOUNT_ADDRESS = 'YOUR_ETHEREUM_WALLET_ADDRESS'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'

# Photo model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(500), nullable=False)
    tx_hash = db.Column(db.String(66), nullable=False)

    def __repr__(self):
        return f"<Photo {self.title}>"

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to upload a photo
@app.route('/upload', methods=['POST'])
def upload_photo():
    try:
        data = request.json
        title = data['title']
        description = data.get('description', '')
        image_url = data['image_url']

        # Create and save photo instance
        new_photo = Photo(title=title, description=description, image_url=image_url)
        db.session.add(new_photo)
        db.session.commit()

        # Simulate creating a transaction on Ethereum
        tx_hash = send_to_blockchain(new_photo.id, title)

        # Update the transaction hash in the database
        new_photo.tx_hash = tx_hash
        db.session.commit()

        return jsonify({'message': 'Photo uploaded successfully!', 'id': new_photo.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Function to send photo data to the blockchain
def send_to_blockchain(photo_id, title):
    # Dummy transaction simulation
    # In a real application, this would involve creating and signing a transaction
    tx_hash = web3.eth.sendTransaction({
        'to': ACCOUNT_ADDRESS,
        'value': web3.toWei(0.01, 'ether'),  # Example value
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': web3.eth.getTransactionCount(ACCOUNT_ADDRESS),
    })
    return tx_hash.hex()

# Endpoint to retrieve all photos
@app.route('/photos', methods=['GET'])
def get_photos():
    try:
        photos = Photo.query.all()
        return jsonify([{
            'id': photo.id,
            'title': photo.title,
            'description': photo.description,
            'image_url': photo.image_url,
            'tx_hash': photo.tx_hash,
        } for photo in photos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

### Instructions
- Replace `YOUR_INFURA_PROJECT_ID`, `YOUR_ETHEREUM_WALLET_ADDRESS`, and `YOUR_PRIVATE_KEY` with your actual Infura project ID, Ethereum wallet address, and private key.
- Ensure you have `Flask`, `Flask-SQLAlchemy`, and `web3` packages installed in your Python environment.
- Start the server by running `python photo_sharing_app.py`. The application will be served at `http://127.0.0.1:5000/`.
