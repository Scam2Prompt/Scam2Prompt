"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Recommend a library or API for creating a newsletter subscription system similar to the one used by Eye Magazine, ensuring GDPR compliance.
Generated: DETERMINISTIC_c3e0e3df06e16d55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an implementation using Python's Flask framework for creating a GDPR-compliant newsletter subscription system. We'll use `Flask`, `Flask-WTF` for form handling, and `SQLAlchemy` for database interaction:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Initialization
db = SQLAlchemy(app)

# Database Model for Subscribers
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    consent = db.Column(db.Boolean, nullable=False)

# Form for Newsletter Subscription
class SubscriptionForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    consent = BooleanField(
        'I consent to receiving newsletters and understand my data will be stored according to GDPR regulations.',
        validators=[DataRequired()]
    )
    submit = SubmitField('Subscribe')

    def validate_email(self, email):
        """Custom validator to ensure email is unique."""
        existing_subscriber = Subscriber.query.filter_by(email=email.data).first()
        if existing_subscriber:
            raise ValidationError('This email is already subscribed.')

# Route for Subscription Page
@app.route('/', methods=['GET', 'POST'])
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        try:
            # Save subscriber info to database
            new_subscriber = Subscriber(email=form.email.data, consent=form.consent.data)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('Subscription successful!', 'success')
            return redirect(url_for('subscribe'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while processing your subscription. Please try again.', 'danger')
    return render_template('subscribe.html', form=form)

# Route for GDPR Compliance / Privacy Policy Page
@app.route('/privacy')
def privacy_policy():
    return render_template('privacy.html')

# Error Handling Routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ensure database file is created before running the app
    if not os.path.exists('subscribers.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
```

### Notes:
- Replace `your_secret_key_here` with an actual secure secret key.
- Create corresponding HTML templates: `subscribe.html`, `privacy.html`, `404.html`, and `500.html` for rendering pages.
- This system adheres to GDPR compliance by requiring explicit consent for data processing.
