"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Write code for a pop-up event registration system for AKCB holders, prioritizing access for NFT owners while allowing limited spots for non-holders.
Generated: DETERMINISTIC_4b76472bfc7493be
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define database model for event registration
class EventRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), nullable=False, unique=True)  # Assuming Ethereum wallet addresses
    is_nft_holder = db.Column(db.Boolean, default=False)
    registration_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Registration {self.wallet_address}>"

# Define maximum spots for NFT holders and non-holders
MAX_NFT_HOLDER_SPOTS = 100
MAX_NON_HOLDER_SPOTS = 50

@app.route('/register', methods=['POST'])
def register():
    """
    Register a user for the pop-up event.
    Expects a JSON payload with wallet_address and is_nft_holder fields.
    """
    try:
        data = request.json
        wallet_address = data.get('wallet_address')
        is_nft_holder = data.get('is_nft_holder', False)

        # Validate input
        if not wallet_address or len(wallet_address) != 42:
            return jsonify({"error": "Invalid wallet address."}), 400

        # Check registration limits
        nft_holder_count = EventRegistration.query.filter_by(is_nft_holder=True).count()
        non_holder_count = EventRegistration.query.filter_by(is_nft_holder=False).count()

        if is_nft_holder:
            if nft_holder_count >= MAX_NFT_HOLDER_SPOTS:
                return jsonify({"error": "No more spots available for NFT holders."}), 403
        else:
            if non_holder_count >= MAX_NON_HOLDER_SPOTS:
                return jsonify({"error": "No more spots available for non-holders."}), 403

        # Create a new registration
        new_registration = EventRegistration(wallet_address=wallet_address, is_nft_holder=is_nft_holder)
        db.session.add(new_registration)
        db.session.commit()

        return jsonify({"message": "Registration successful!", "wallet_address": wallet_address}), 201

    except Exception as e:
        # Log the exception (could also log to a file or logging service)
        app.logger.error(f"Error during registration: {str(e)}")
        return jsonify({"error": "An error occurred during registration."}), 500

@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    Retrieve all event registrations.
    """
    try:
        registrations = EventRegistration.query.all()
        response = [{
            "wallet_address": reg.wallet_address,
            "is_nft_holder": reg.is_nft_holder,
            "registration_time": reg.registration_time.isoformat()
        } for reg in registrations]

        return jsonify(response), 200

    except Exception as e:
        app.logger.error(f"Error fetching registrations: {str(e)}")
        return jsonify({"error": "An error occurred while fetching registrations."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
