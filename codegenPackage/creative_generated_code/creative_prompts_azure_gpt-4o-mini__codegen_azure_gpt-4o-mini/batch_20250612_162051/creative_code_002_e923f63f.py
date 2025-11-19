"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Create a REST API endpoint that allows users to request a free estimate for cleaning services, incorporating features mentioned by Maria HouseKeepers, such as one-time and recurring cleaning options.
Generated: DETERMINISTIC_e923f63f4adaede0
Batch ID: 20250612_162051
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

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estimates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the cleaning service estimate
class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    cleaning_type = db.Column(db.String(50), nullable=False)  # One-time or Recurring
    details = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Estimate object to a dictionary for easy JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'cleaning_type': self.cleaning_type,
            'details': self.details
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/estimates', methods=['POST'])
def request_estimate():
    """
    API endpoint to create a new cleaning service estimate request.
    
    Request data should include 'name', 'email', 'phone', 'cleaning_type', and optional 'details'.
    Returns a JSON response with the created estimate or an error message.
    """
    try:
        data = request.get_json()

        # Validate the incoming data
        if not all(k in data for k in ('name', 'email', 'phone', 'cleaning_type')):
            return jsonify({'error': 'Missing required fields.'}), 400

        # Create a new Estimate object
        new_estimate = Estimate(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            cleaning_type=data['cleaning_type'],
            details=data.get('details', '')
        )

        # Add and commit the new estimate to the database
        db.session.add(new_estimate)
        db.session.commit()

        return jsonify(new_estimate.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error. Please check your data.'}), 500
    except Exception as e:
        # General error handling
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
