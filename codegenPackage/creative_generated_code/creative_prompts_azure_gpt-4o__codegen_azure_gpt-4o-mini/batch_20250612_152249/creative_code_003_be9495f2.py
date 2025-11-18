"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Suggest tools or frameworks to create an event calendar for SKI Foundation's "Serial Webinar AgroSociopreneurship" program, ensuring integration with email notifications for participants.
Generated: DETERMINISTIC_be9495f2f376f073
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

# Initialize Flask Application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webinars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Initialize Extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Database Model for Webinar Event
class Webinar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    participants = db.relationship('Participant', backref='webinar', lazy=True)

# Database Model for Participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    webinar_id = db.Column(db.Integer, db.ForeignKey('webinar.id'), nullable=False)

# Route to View Webinars
@app.route('/')
def index():
    webinars = Webinar.query.all()
    return render_template('index.html', webinars=webinars)

# Route to Register for a Webinar
@app.route('/register/<int:webinar_id>', methods=['GET', 'POST'])
def register(webinar_id):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        try:
            new_participant = Participant(name=name, email=email, webinar_id=webinar_id)
            db.session.add(new_participant)
            db.session.commit()
            send_notification(email)
            flash('Registration successful! A confirmation email has been sent.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed: ' + str(e), 'danger')
    
    return render_template('register.html', webinar_id=webinar_id)

# Function to Send Email Notification
def send_notification(email):
    msg = Message("Webinar Registration Confirmation",
                  recipients=[email])
    msg.body = "Thank you for registering for the Serial Webinar AgroSociopreneurship program!"
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# Error Handling
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template("500.html"), 500

# Initialize Database and Create Tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Application
if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  # Replace with a secure key
    app.run(debug=True)
```

### HTML Templates (index.html and register.html)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webinar List</title>
</head>
<body>
    <h1>Upcoming Webinars</h1>
    <ul>
        {% for webinar in webinars %}
            <li>
                <strong>{{ webinar.title }}</strong> - {{ webinar.date.strftime('%Y-%m-%d %H:%M') }}
                <a href="{{ url_for('register', webinar_id=webinar.id) }}">Register</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### register.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for Webinar</title>
</head>
<body>
    <h1>Register for Webinar</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Notes
- Ensure to install the required packages via `pip install Flask Flask-SQLAlchemy Flask-Mail`.
- Replace SMTP server settings and `secret_key` with production-ready credentials.
- Create appropriate error template files `404.html` and `500.html` for better user experience.
