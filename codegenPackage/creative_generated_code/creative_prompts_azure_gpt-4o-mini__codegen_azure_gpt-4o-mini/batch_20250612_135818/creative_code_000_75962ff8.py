"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csh-gamesapp.weebly.com
Prompt: How can I implement a promotional email signup feature similar to the one on the Piuka website?
Generated: DETERMINISTIC_75962ff85283bbda
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
import re

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'
mail = Mail(app)

# Database model for email signups
class EmailSignup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<EmailSignup {self.email}>'

# Route to handle email signups
@app.route('/signup', methods=['POST'])
def signup():
    """Handle promotional email signups."""
    # Get the email from the request body
    data = request.get_json()
    email = data.get('email')

    # Validate email format
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email address."}), 400

    # Check if the email already exists
    existing_signup = EmailSignup.query.filter_by(email=email).first()
    if existing_signup:
        return jsonify({"message": "Email already signed up."}), 200

    # Create a new signup entry
    new_signup = EmailSignup(email=email)
    db.session.add(new_signup)

    try:
        db.session.commit()
        # Send confirmation email
        send_confirmation_email(email)
        return jsonify({"message": "Successfully signed up for promotions!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error signing up. Please try again."}), 500

def send_confirmation_email(email):
    """Send a confirmation email to the user."""
    msg = Message("Thank you for signing up for our promotions!", recipients=[email])
    msg.body = "You have successfully signed up for our promotional emails. Stay tuned for exciting offers!"
    
    try:
        mail.send(msg)
    except Exception as e:
        # Log the error or take appropriate action
        print(f"Failed to send email: {str(e)}")

# Error handler
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all exceptions and return a JSON response."""
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```
