"""
Generated Code Metadata:
========================
Original URL: https://www.androidwidget.com
Prompt: Design a system to enhance IoT security for smart devices, such as surveillance cameras and electric vehicles, using a combination of AI and blockchain technology, as discussed in the article on普及物联网开拓安全性需“表里兼修”.
Generated: DETERMINISTIC_413f1c1535ce1f84
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_security.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encryption and Decryption class
class Encryption:
    def __init__(self):
        self.key = generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """Encrypts the given data."""
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, token):
        """Decrypts the given token."""
        return self.cipher.decrypt(token.encode()).decode()

# Blockchain class to handle transactions
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, proof, previous_hash):
        """Creates a new block in the blockchain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """Returns the previous block in the chain."""
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """Simple proof of work algorithm."""
        new_proof = 1
        while not self.valid_proof(previous_proof, new_proof):
            new_proof += 1
        return new_proof

    @staticmethod
    def valid_proof(previous_proof, new_proof):
        """Validates the proof of work."""
        guess = f'{previous_proof}{new_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

# Database model for IoT devices
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100), unique=True, nullable=False)
    encrypted_data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Device {self.device_id}>"

# Initialize the database
db.create_all()

# Initialize blockchain
blockchain = Blockchain()
encryption = Encryption()

@app.route('/register_device', methods=['POST'])
def register_device():
    """Endpoint to register a new IoT device."""
    data = request.get_json()
    device_id = data.get('device_id')
    sensitive_data = data.get('sensitive_data')

    if not device_id or not sensitive_data:
        return jsonify({'error': 'Device ID and sensitive data are required.'}), 400

    encrypted_data = encryption.encrypt(sensitive_data)

    new_device = Device(device_id=device_id, encrypted_data=encrypted_data)
    db.session.add(new_device)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Device ID already exists.'}), 400

    # Create a new block in the blockchain
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = hashlib.sha256(json.dumps(previous_block, sort_keys=True).encode()).hexdigest()
    blockchain.create_block(proof, previous_hash)

    return jsonify({'message': 'Device registered successfully.', 'block_index': len(blockchain.chain)}), 201

@app.route('/get_device_data/<device_id>', methods=['GET'])
def get_device_data(device_id):
    """Endpoint to retrieve sensitive data for a specific device."""
    device = Device.query.filter_by(device_id=device_id).first()

    if not device:
        return jsonify({'error': 'Device not found.'}), 404

    decrypted_data = encryption.decrypt(device.encrypted_data)
    return jsonify({'device_id': device.device_id, 'sensitive_data': decrypted_data}), 200

if __name__ == '__main__':
    app.run(debug=False)
```
