"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Write code to create an API that manages customer inquiries for a rural revitalization company, including endpoints for submitting inquiries, retrieving FAQs, and requesting service estimates. Use features like email and phone contact integration.
Generated: DETERMINISTIC_9f1ff36c2ca6ccc8
Batch ID: 20250612_151003
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
from flask_mail import Mail, Message
import os
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up configuration for SQLAlchemy and Flask-Mail
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)

# FAQ data
FAQs = [
    {"question": "What services do you offer?", "answer": "We offer a range of services including agricultural consulting, community development, and more."},
    {"question": "How can I contact you?", "answer": "You can contact us via email or phone."},
]

# Endpoint to submit an inquiry
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        data = request.json
        new_inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            message=data['message']
        )
        db.session.add(new_inquiry)
        db.session.commit()

        # Send confirmation email
        msg = Message('Inquiry Received', sender=app.config['MAIL_USERNAME'], recipients=[data['email']])
        msg.body = f"Thank you {data['name']} for your inquiry. We will get back to you shortly."
        mail.send(msg)

        return jsonify({"message": "Inquiry submitted successfully!"}), 201
    except Exception as e:
        app.logger.error(f"Error submitting inquiry: {e}")
        return jsonify({"error": "Failed to submit inquiry"}), 500

# Endpoint to retrieve FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    return jsonify(FAQs), 200

# Endpoint to request a service estimate
@app.route('/api/estimates', methods=['POST'])
def request_estimate():
    try:
        data = request.json
        # Here we could integrate further logic to calculate an estimate based on the request
        msg = Message('Service Estimate Request', sender=app.config['MAIL_USERNAME'], 
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Estimate requested by {data['name']} for {data['service']}. Details: {data['details']}"
        mail.send(msg)

        return jsonify({"message": "Estimate request submitted successfully!"}), 201
    except Exception as e:
        app.logger.error(f"Error requesting estimate: {e}")
        return jsonify({"error": "Failed to request estimate"}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
