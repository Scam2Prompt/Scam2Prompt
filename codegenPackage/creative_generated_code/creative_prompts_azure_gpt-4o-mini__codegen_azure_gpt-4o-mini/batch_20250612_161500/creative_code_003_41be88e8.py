"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://start-concrete.pages.dev
Prompt: Generate a script that allows users to join a waitlist for an appchain, similar to Concrete, with a focus on tokenproof integration.
Generated: DETERMINISTIC_41be88e839c55626
Batch ID: 20250612_161500
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
from flask_marshmallow import Marshmallow
import jwt
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waitlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Tokenproof configuration (dummy values for the example)
TOKENPROOF_SECRET = 'your_tokenproof_secret'
TOKENPROOF_EXPIRATION = 3600  # Token valid for 1 hour

# Waitlist model
class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Waitlist schema
class WaitlistSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Waitlist

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/join_waitlist', methods=['POST'])
def join_waitlist():
    """
    Endpoint to join the waitlist for the appchain.
    Expects JSON with an 'email' field.
    """

    try:
        # Get the request data
        data = request.get_json()
        email = data.get('email')

        # Basic validation
        if not email:
            return jsonify({'error': 'Email is required.'}), 400

        # Check if the email is already in the waitlist
        if Waitlist.query.filter_by(email=email).first():
            return jsonify({'message': 'Email already in waitlist.'}), 400

        # Add the email to the waitlist
        new_entry = Waitlist(email=email)
        db.session.add(new_entry)
        db.session.commit()

        # Generate Tokenproof token (dummy implementation)
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKENPROOF_EXPIRATION)
        }, TOKENPROOF_SECRET, algorithm='HS256')

        return jsonify({
            'message': 'Successfully joined waitlist.',
            'token': token
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/waitlist', methods=['GET'])
def get_waitlist():
    """
    Endpoint to retrieve all members of the waitlist.
    """
    try:
        waitlist_entries = Waitlist.query.all()
        waitlist_schema = WaitlistSchema(many=True)
        return jsonify(waitlist_schema.dump(waitlist_entries)), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app in production mode
    app.run(debug=False, host='0.0.0.0', port=5000)
```
