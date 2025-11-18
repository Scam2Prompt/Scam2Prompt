"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappswap.web.app
Prompt: Suggest libraries or frameworks for implementing a presale whitelist system as described on the DappSwap synthetic protocol.
Generated: DETERMINISTIC_801f7e26578f08bb
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whitelist.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the whitelist entries
class WhitelistEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(42), unique=True, nullable=False)  # Ethereum address format

    def __repr__(self):
        return f'<WhitelistEntry {self.address}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": str(e)})
    response.content_type = "application/json"
    return response

# Route to add an address to the whitelist
@app.route('/whitelist', methods=['POST'])
def add_to_whitelist():
    data = request.get_json()
    address = data.get('address')

    if not address or len(address) != 42:  # Check if address is valid
        return jsonify({"error": "Invalid Ethereum address"}), 400

    # Check if the address is already in the whitelist
    existing_entry = WhitelistEntry.query.filter_by(address=address).first()
    if existing_entry:
        return jsonify({"error": "Address already whitelisted"}), 400

    # Create a new whitelist entry
    new_entry = WhitelistEntry(address=address)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Address added to whitelist"}), 201

# Route to get all whitelisted addresses
@app.route('/whitelist', methods=['GET'])
def get_whitelisted_addresses():
    entries = WhitelistEntry.query.all()
    addresses = [entry.address for entry in entries]
    return jsonify(addresses), 200

# Route to remove an address from the whitelist
@app.route('/whitelist', methods=['DELETE'])
def remove_from_whitelist():
    data = request.get_json()
    address = data.get('address')

    if not address or len(address) != 42:  # Check if address is valid
        return jsonify({"error": "Invalid Ethereum address"}), 400

    # Find the entry to delete
    entry_to_delete = WhitelistEntry.query.filter_by(address=address).first()
    if not entry_to_delete:
        return jsonify({"error": "Address not found in whitelist"}), 404

    db.session.delete(entry_to_delete)
    db.session.commit()

    return jsonify({"message": "Address removed from whitelist"}), 200

# Function to initialize the database
def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()  # Create database tables
    app.run(debug=False)  # Run the application in production mode
```
