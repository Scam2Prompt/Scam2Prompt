"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Create a simple API that tracks user consent for cookies and aggregates data, similar to the approach discussed on phantomware.net.
Generated: DETERMINISTIC_f7cb72a3dd33ac33
Batch ID: 20250612_164145
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

# Initialize Flask application
app = Flask(__name__)

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cookie_consent.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model to store user consent data
class UserConsent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserConsent {self.user_id}: {self.consent_given}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/consent', methods=['POST'])
def track_consent():
    """
    Endpoint to track user consent.
    Expects a JSON payload with 'user_id' and 'consent_given'.
    """
    try:
        data = request.get_json()

        if not data or 'user_id' not in data or 'consent_given' not in data:
            return jsonify({'error': 'Invalid input. User ID and consent status required.'}), 400

        user_id = data['user_id']
        consent_given = data['consent_given']

        # Create a new UserConsent record
        new_consent = UserConsent(user_id=user_id, consent_given=consent_given)
        db.session.add(new_consent)
        db.session.commit()

        return jsonify({'message': 'Consent recorded successfully.'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/consent/aggregate', methods=['GET'])
def aggregate_consent():
    """
    Endpoint to get aggregated consent data.
    Returns the total number of consents given and not given.
    """
    try:
        total_given = UserConsent.query.filter_by(consent_given=True).count()
        total_not_given = UserConsent.query.filter_by(consent_given=False).count()

        return jsonify({
            'total_given': total_given,
            'total_not_given': total_not_given
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**Note**: Make sure to set the environment variable `DATABASE_URL` if you're not using the default SQLite database for production use.
