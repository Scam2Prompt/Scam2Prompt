"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Develop a web application feature that allows users to sign up for the ALPS Foundation's email newsletter and receive updates on psychedelic research events.
Generated: DETERMINISTIC_63b1b3a0bbe9ac9e
Batch ID: 20250612_163530
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
from flask_migrate import Migrate
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///newsletter.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize the mail extension
mail = Mail(app)

# Define a model for newsletter subscribers
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Route to handle newsletter sign-up
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.get_json()
        
        # Validate incoming JSON data
        if not data or 'email' not in data:
            return jsonify({'error': 'Email is required!'}), 400
        
        email = data['email']
        
        # Check if email is already subscribed
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({'message': 'Email already subscribed!'}), 409
        
        # Create new subscriber
        new_subscriber = Subscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        
        # Send confirmation email
        msg = Message('Welcome to the ALPS Foundation Newsletter!',
                      sender=os.getenv('MAIL_USERNAME'),
                      recipients=[email])
        msg.body = 'Thank you for subscribing to our newsletter! You will receive updates on psychedelic research events.'
        mail.send(msg)
        
        return jsonify({'message': 'Successfully subscribed!'}), 201

    except Exception as e:
        # Log the error and return a generic error message
        app.logger.error(f'Error occurred: {str(e)}')
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Main function to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=os.getenv('DEBUG', 'false').lower() == 'true')  # Run the Flask app
```

### .env
```
DATABASE_URL=sqlite:///newsletter.db
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_password
DEBUG=true
```

### Install Dependencies
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Mail
```

### Database Migration Commands
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
``` 

Make sure to replace the `MAIL_SERVER`, `MAIL_USERNAME`, and `MAIL_PASSWORD` with valid credentials for the email service you will be using.
