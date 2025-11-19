"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Create a REST API endpoint that allows users to submit feedback about their experiences with Harinder Farms' products and services, including corn silage and potato seeds.
Generated: DETERMINISTIC_453310ec2c929af8
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}, Product: {self.product_type}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Define the API route for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate the input data
        if not data or 'product_type' not in data or 'experience' not in data:
            return jsonify({'error': 'Invalid input. Please provide product_type and experience.'}), 400

        # Create a new Feedback instance
        feedback = Feedback(product_type=data['product_type'], experience=data['experience'])

        # Add and commit the new feedback to the database
        db.session.add(feedback)
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Feedback submitted successfully!', 'feedback_id': feedback.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error. Please try again later.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
