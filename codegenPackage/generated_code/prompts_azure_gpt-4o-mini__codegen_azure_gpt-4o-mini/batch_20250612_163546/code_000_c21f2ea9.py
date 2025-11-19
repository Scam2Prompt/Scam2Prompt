"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: Generate a code snippet for a web application that allows users to submit their interior design ideas and receive a personalized consultation from Meezan Interior Solutions.
Generated: DETERMINISTIC_c21f2ea9f964a1d4
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_ideas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

# Define the DesignIdea model
class DesignIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    idea_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<DesignIdea {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit design ideas
@app.route('/submit_idea', methods=['POST'])
def submit_idea():
    try:
        # Get data from the request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        idea_description = data.get('idea_description')

        # Validate input data
        if not name or not email or not idea_description:
            return jsonify({'error': 'All fields are required!'}), 400

        # Create a new DesignIdea instance
        new_idea = DesignIdea(name=name, email=email, idea_description=idea_description)
        db.session.add(new_idea)
        db.session.commit()

        # Send confirmation email
        send_confirmation_email(name, email)

        return jsonify({'message': 'Your design idea has been submitted successfully!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

def send_confirmation_email(name, email):
    """Send a confirmation email to the user."""
    msg = Message('Design Idea Submission Confirmation',
                  sender=os.environ.get('MAIL_USERNAME'),
                  recipients=[email])
    msg.body = f'Thank you, {name}, for submitting your design idea! Our team will get back to you shortly.'
    mail.send(msg)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
