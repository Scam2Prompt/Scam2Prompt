"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about diving gear, similar to the customer service features offered on acula.com.ua.
Generated: DETERMINISTIC_4192ac9e4072a5cd
Batch ID: 20250612_163243
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.id}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry about diving gear.
    
    Request Body:
    - name (str): The name of the user.
    - email (str): The email of the user.
    - message (str): The inquiry message.

    Returns:
    - JSON response with success or failure message and HTTP status code.
    """
    try:
        data = request.get_json()

        # Validate request body
        if not data or not all(key in data for key in ('name', 'email', 'message')):
            logging.warning('Invalid input data')
            return jsonify({'message': 'Invalid input data'}), 400

        # Create a new inquiry instance
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )

        # Add inquiry to the session and commit
        db.session.add(new_inquiry)
        db.session.commit()

        logging.info(f'Inquiry submitted successfully: {new_inquiry}')
        return jsonify({'message': 'Inquiry submitted successfully!'}), 201

    except Exception as e:
        logging.error(f'Error submitting inquiry: {e}')
        return jsonify({'message': 'An error occurred while submitting your inquiry.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
