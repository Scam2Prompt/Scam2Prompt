"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Create a script to send updates to users who sign up for the HAGGIS Hunt campaign, integrating the "Sign up for updates" feature mentioned on the site.
Generated: DETERMINISTIC_0a9389c7b19c930a
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    try:
        # Set up the SMTP server
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = "your_email@example.com"
        smtp_password = "your_email_password"

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
            
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

@app.route('/signup', methods=['POST'])
def signup():
    """Route for users to sign up for updates."""
    try:
        # Parse JSON data from request
        data = request.get_json()
        email = data.get('email')

        # Validate email presence
        if not email:
            raise BadRequest("Email is required")

        # Check for existing user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "Already signed up for updates."}), 400

        # Create a new user
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()

        # Send confirmation email
        send_email(email, "Welcome to HAGGIS Hunt!", "Thank you for signing up for updates!")

        return jsonify({"message": "Successfully signed up for updates!"}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
