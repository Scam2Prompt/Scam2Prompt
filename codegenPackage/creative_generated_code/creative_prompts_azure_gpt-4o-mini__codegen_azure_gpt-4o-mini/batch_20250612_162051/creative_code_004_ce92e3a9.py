"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Suggest a set of tools and libraries for implementing a website that enhances visibility and communication for a business, reflecting the web creation services of Global Service Consulting.
Generated: DETERMINISTIC_ce92e3a903b63b7d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure application for database and mail services
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_communication.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for storing messages
class MessageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Message {self.id} from {self.name}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        # Save the message to the database
        new_message = MessageModel(name=name, email=email, message=message)
        db.session.add(new_message)
        try:
            db.session.commit()
            flash('Message sent successfully!', 'success')
            send_email(name, email, message)
        except Exception as e:
            db.session.rollback()
            logging.error(f'Error saving message: {e}')
            flash('Failed to send message. Please try again later.', 'error')

        return redirect(url_for('home'))

    return render_template('contact.html')

# Function to send email notifications
def send_email(name, email, message):
    try:
        msg = Message('New Contact Form Submission',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['recipient@example.com'])
        msg.body = f'You have received a new message from {name} ({email}):\n\n{message}'
        mail.send(msg)
        logging.info('Email sent successfully.')
    except Exception as e:
        logging.error(f'Error sending email: {e}')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Make sure to replace placeholders such as `'your_email@example.com'`, `'your_password'`, and `'smtp.example.com'` with actual values. Also, create the corresponding HTML templates (`index.html` and `contact.html`) to render the web pages accordingly.
