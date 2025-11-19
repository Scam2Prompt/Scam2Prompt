"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzostudio.com
Prompt: Create an API integration that allows users to submit inquiries about architectural services, reflecting the contact features of RENZO Studio de Arquitetura.
Generated: DETERMINISTIC_625d614624797008
Batch ID: 20250612_162404
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

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true') == 'true'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

db = SQLAlchemy(app)
mail = Mail(app)

class Inquiry(db.Model):
    """Model for storing inquiries."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.id} from {self.name}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    """Endpoint to submit inquiries about architectural services."""
    data = request.get_json()

    # Validate the incoming JSON data
    if not data or not all(key in data for key in ['name', 'email', 'message']):
        return jsonify({"error": "Missing required fields."}), 400

    new_inquiry = Inquiry(name=data['name'], email=data['email'], message=data['message'])

    try:
        db.session.add(new_inquiry)
        db.session.commit()

        # Send confirmation email (can be customized)
        send_confirmation_email(new_inquiry)

        return jsonify({"message": "Inquiry submitted successfully!"}), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

def send_confirmation_email(inquiry):
    """Send a confirmation email to the user."""
    msg = Message('Inquiry Confirmation', recipients=[inquiry.email])
    msg.body = f"Thank you {inquiry.name} for reaching out to us. We have received your message:\n\n{inquiry.message}"
    try:
        mail.send(msg)
    except Exception as e:
        app.logger.error(f'Failed to send email: {e}')

if __name__ == '__main__':
    app.run(debug=True)
```
