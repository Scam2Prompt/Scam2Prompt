"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wasbroke.com
Prompt: Develop a simple web application that implements referral generation strategies based on Stacey Bront Randall’s Growth By Referrals course from Was Broke.
Generated: DETERMINISTIC_a32244b4a34b2dd8
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///referrals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Referral
class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_name = db.Column(db.String(100), nullable=False)
    referred_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Referral {self.referrer_name} referred {self.referred_name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to generate a new referral
@app.route('/referral', methods=['POST'])
def create_referral():
    try:
        data = request.json
        referrer_name = data.get('referrer_name')
        referred_name = data.get('referred_name')

        if not referrer_name or not referred_name:
            return jsonify({'error': 'Both referrer_name and referred_name are required.'}), 400

        new_referral = Referral(referrer_name=referrer_name, referred_name=referred_name)
        db.session.add(new_referral)
        db.session.commit()

        return jsonify({'message': 'Referral created successfully!', 'referral_id': new_referral.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all referrals
@app.route('/referrals', methods=['GET'])
def get_referrals():
    try:
        referrals = Referral.query.all()
        return jsonify([{'id': r.id, 'referrer_name': r.referrer_name, 'referred_name': r.referred_name, 'created_at': r.created_at} for r in referrals]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)
```

### Requirements
To run this application, ensure you have `Flask` and `Flask-SQLAlchemy` installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code above to a file named `app.py`.
2. In your terminal, navigate to the directory containing `app.py`.
3. Run the application using:

```bash
python app.py
```

### API Endpoints
- **POST /referral**: To create a new referral.
- **GET /referrals**: To fetch all referrals.

### Note
This is a basic implementation focusing on referral management. You may want to add additional features such as user authentication, advanced validation, and more robust error handling for production use.
