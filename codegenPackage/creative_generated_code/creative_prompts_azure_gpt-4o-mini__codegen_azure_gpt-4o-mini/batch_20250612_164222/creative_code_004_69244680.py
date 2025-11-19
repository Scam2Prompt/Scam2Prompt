"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts.sparklingz.nl
Prompt: What are the best practices for integrating a customer service support system in a webshop like Sparklingz?
Generated: DETERMINISTIC_69244680fae2e5d0
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.exceptions import BadRequest, InternalServerError

# Initialize the Flask application
app = Flask(__name__)

# Configure database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the SupportRequest model
class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<SupportRequest {self.customer_email}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/support', methods=['POST'])
def submit_support_request():
    """
    Endpoint to submit a support request.
    Expects JSON with 'email' and 'message'.
    """
    try:
        data = request.get_json()
        if not data or 'email' not in data or 'message' not in data:
            raise BadRequest("Invalid input: 'email' and 'message' are required.")

        # Create a new support request
        support_request = SupportRequest(customer_email=data['email'], message=data['message'])
        db.session.add(support_request)
        db.session.commit()

        # Send a confirmation email to the customer
        send_confirmation_email(data['email'])

        return jsonify({"message": "Support request submitted successfully."}), 201

    except BadRequest as e:
        logging.error(f'Error: {e}')
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

def send_confirmation_email(customer_email):
    """
    Send a confirmation email to the customer after submitting a support request.
    
    :param customer_email: Email address of the customer
    """
    try:
        msg = Message('Support Request Received',
                      sender='your_email@example.com',
                      recipients=[customer_email])
        msg.body = 'Thank you for contacting us. We will get back to you shortly.'
        mail.send(msg)
    except Exception as e:
        logging.error(f'Failed to send email: {e}')
        raise InternalServerError("Failed to send confirmation email.")

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
