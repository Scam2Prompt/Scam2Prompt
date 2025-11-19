"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adstar.network
Prompt: Write an API endpoint that logs user consent for data collection as outlined on adstar.network.
Generated: DETERMINISTIC_a407bcbebfe9e00f
Batch ID: 20250612_164152
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_consent.db'  # In-memory database for demonstration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for User Consent
class UserConsent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/consent', methods=['POST'])
def log_user_consent():
    """
    Endpoint to log user consent for data collection.

    Expected JSON payload:
    {
        "user_id": "unique_user_id",
        "consent_given": true/false
    }
    """
    try:
        # Parse JSON request body
        data = request.get_json()

        # Validate input data
        if not data or 'user_id' not in data or 'consent_given' not in data:
            return jsonify({"error": "Invalid input, 'user_id' and 'consent_given' are required."}), 400

        user_id = data['user_id']
        consent_given = data['consent_given']

        # Log the consent
        consent_record = UserConsent(user_id=user_id, consent_given=consent_given)
        db.session.add(consent_record)
        db.session.commit()

        logging.info(f"Consent logged for user_id: {user_id}, consent_given: {consent_given}")

        return jsonify({"message": "Consent logged successfully."}), 201

    except Exception as e:
        logging.error(f"Error logging consent: {str(e)}")
        return jsonify({"error": "An error occurred while logging consent."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
