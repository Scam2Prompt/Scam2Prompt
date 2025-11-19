"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Suggest tools or frameworks to design a booking system for The Second City's private events and team-building workshops, ensuring seamless integration with their existing website.
Generated: DETERMINISTIC_751885075511162b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, IntegerField, validators
from datetime import datetime
import stripe
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Stripe
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Configure logging
handler = RotatingFileHandler('booking_system.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Database Models
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)  # in cents
    is_private = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='event', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    company_name = db.Column(db.String(100))
    special_requests = db.Column(db.Text)
    payment_intent_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Forms
class BookingForm(FlaskForm):
    customer_name = StringField('Full Name', [validators.InputRequired()])
    customer_email = StringField('Email', [validators.InputRequired(), validators.Email()])
    customer_phone = StringField('Phone', [validators.InputRequired()])
    participants = IntegerField('Number of Participants', [validators.InputRequired(), validators.NumberRange(min=1)])
    company_name = StringField('Company Name')
    special_requests = StringField('Special Requests')

# Routes
@app.route('/')
def index():
    events = Event.query.filter_by(is_private=True).all()
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>', methods=['GET', 'POST'])
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    form = BookingForm()
    
    if form.validate_on_submit():
        try:
            # Create payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=event.price * form.participants.data,
                currency='usd',
                metadata={
                    'event_id': event.id,
                    'customer_name': form.customer_name.data,
                    'customer_email': form.customer_email.data
                }
            )
            
            # Create booking
            booking = Booking(
                event_id=event.id,
                customer_name=form.customer_name.data,
                customer_email=form.customer_email.data,
                customer_phone=form.customer_phone.data,
                participants=form.participants.data,
                company_name=form.company_name.data,
                special_requests=form.special_requests.data,
                payment_intent_id=payment_intent.id
            )
            
            db.session.add(booking)
            db.session.commit()
            
            return render_template('checkout.html', 
                                client_secret=payment_intent.client_secret,
                                stripe_public_key=app.config['STRIPE_PUBLIC_KEY'])
        
        except Exception as e:
            app.logger.error(f"Error processing booking: {str(e)}")
            db.session.rollback()
            return render_template('error.html', message="An error occurred while processing your booking.")
    
    return render_template('event_detail.html', event=event, form=form)

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET')
        )
    except ValueError as e:
        app.logger.error(f"Invalid payload: {str(e)}")
        return jsonify({'status': 'error'}), 400
    except stripe.error.SignatureVerificationError as e:
        app.logger.error(f"Invalid signature: {str(e)}")
        return jsonify({'status': 'error'}), 400
    
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        booking = Booking.query.filter_by(payment_intent_id=payment_intent['id']).first()
        if booking:
            booking.payment_status = 'completed'
            db.session.commit()
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', False))
```
