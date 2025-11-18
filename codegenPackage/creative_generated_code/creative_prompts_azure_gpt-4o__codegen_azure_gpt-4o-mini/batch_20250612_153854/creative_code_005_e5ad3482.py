"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write code to implement a consent management system for tracking user preferences, similar to the cookie management system described on Alghanim Capital's website.
Generated: DETERMINISTIC_e5ad3482851edf1f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consent_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserConsent(db.Model):
    """Model to store user consent preferences."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    consent_given = db.Column(db.Boolean, default=False)
    consent_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserConsent {self.user_id}: {self.consent_given}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/consent', methods=['POST'])
def set_consent():
    """Set the user's consent preference."""
    try:
        data = request.json
        user_id = data.get('user_id')
        consent_given = data.get('consent_given', False)

        if not user_id or not isinstance(consent_given, bool):
            return make_response(jsonify({"error": "Invalid input"}), 400)

        # Check if user consent already exists
        user_consent = UserConsent.query.filter_by(user_id=user_id).first()
        if user_consent:
            user_consent.consent_given = consent_given
            user_consent.consent_date = datetime.utcnow()
        else:
            user_consent = UserConsent(user_id=user_id, consent_given=consent_given)
            db.session.add(user_consent)

        db.session.commit()
        return jsonify({"message": "Consent preference updated successfully"}), 200

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/consent/<user_id>', methods=['GET'])
def get_consent(user_id):
    """Get the user's consent preference."""
    try:
        user_consent = UserConsent.query.filter_by(user_id=user_id).first()
        if user_consent:
            return jsonify({
                "user_id": user_consent.user_id,
                "consent_given": user_consent.consent_given,
                "consent_date": user_consent.consent_date.isoformat()
            }), 200
        else:
            return jsonify({"message": "No consent record found"}), 404

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

if __name__ == '__main__':
    app.run(debug=False)
```
