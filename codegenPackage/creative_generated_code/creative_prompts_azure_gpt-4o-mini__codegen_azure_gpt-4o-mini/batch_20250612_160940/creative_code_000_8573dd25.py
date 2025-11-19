"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travaux.fr.fo
Prompt: Generate a code snippet for a web application that allows users to request estimates for home renovation projects like painting, roofing, or electrical work.
Generated: DETERMINISTIC_8573dd25ba1d9927
Batch ID: 20250612_160940
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///renovation_estimates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Estimate model
class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Estimate {self.id} - {self.project_type}>'

# Create the database and the Estimate table
with app.app_context():
    db.create_all()

# Route to request an estimate
@app.route('/request_estimate', methods=['POST'])
def request_estimate():
    try:
        # Get data from the request
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'project_type']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Create a new Estimate instance
        new_estimate = Estimate(
            name=data['name'],
            email=data['email'],
            project_type=data['project_type'],
            description=data.get('description')  # Optional field
        )
        
        # Add the new estimate to the database
        db.session.add(new_estimate)
        db.session.commit()

        return jsonify({'message': 'Estimate request submitted successfully!', 'estimate_id': new_estimate.id}), 201

    except Exception as e:
        # Log the exception (in production, consider using a logging library)
        print(f'Error occurred: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
