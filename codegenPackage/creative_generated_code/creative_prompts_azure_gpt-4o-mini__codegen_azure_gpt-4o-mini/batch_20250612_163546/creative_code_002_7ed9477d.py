"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Create an API endpoint that allows law firms to receive live-transferred leads, similar to the services offered by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7ed9477d62da31a8
Batch ID: 20250612_163546
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Lead
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='new')

    def __repr__(self):
        return f'<Lead {self.name}>'


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/api/leads', methods=['POST'])
def receive_lead():
    """
    API endpoint to receive a live-transferred lead from law firms.
    Expects JSON payload with the lead's name, phone, and email.
    """
    try:
        # Retrieve JSON data from the request
        data = request.get_json()

        # Validate incoming data
        if not data or 'name' not in data or 'phone' not in data or 'email' not in data:
            return jsonify({'error': 'Invalid input. Must include name, phone, and email.'}), 400

        # Create a new lead instance
        new_lead = Lead(name=data['name'], phone=data['phone'], email=data['email'])

        # Add the new lead to the database
        db.session.add(new_lead)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Lead received successfully!', 'lead_id': new_lead.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Lead already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
