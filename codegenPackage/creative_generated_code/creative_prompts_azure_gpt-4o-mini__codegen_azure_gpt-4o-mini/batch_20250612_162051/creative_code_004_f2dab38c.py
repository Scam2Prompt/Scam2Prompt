"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Illustrate how to implement a customer feedback system in a computer repair service application, taking cues from the customer satisfaction guarantees of Geeks on Repair.
Generated: DETERMINISTIC_f2dab38cab6366d4
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)

    def __init__(self, customer_name, service_rating, comments=None):
        self.customer_name = customer_name
        self.service_rating = service_rating
        self.comments = comments

# Feedback schema for serialization
class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Extract data from the request
        data = request.json
        customer_name = data.get('customer_name')
        service_rating = data.get('service_rating')
        comments = data.get('comments')

        # Validate input data
        if not customer_name or not service_rating:
            return jsonify({"error": "Customer name and service rating are required."}), 400
        
        # Create feedback instance
        new_feedback = Feedback(customer_name=customer_name, service_rating=service_rating, comments=comments)
        
        # Add to the session and commit
        db.session.add(new_feedback)
        db.session.commit()

        return FeedbackSchema().jsonify(new_feedback), 201

    except Exception as e:
        # Handle exceptions and return error message
        return jsonify({"error": str(e)}), 500

# Route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedback_list = Feedback.query.all()
        return FeedbackSchema(many=True).jsonify(feedback_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Ensure you have Flask, Flask-SQLAlchemy, and Flask-Marshmallow installed in your Python environment.
2. Run the application; it will create a SQLite database called `feedback.db`.
3. Use a tool like Postman or Curl to submit feedback via the `/feedback` endpoint with a POST request, and retrieve feedback using a GET request.
