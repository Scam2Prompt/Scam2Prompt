"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Write code for a web portal that includes membership registration, encrypted attendee management, and a built-in payment gateway supporting Visa, Mastercard, and American Express, as detailed by Virtual Media Events.
Generated: DETERMINISTIC_ede8b9d51ff72835
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['STRIPE_PUBLIC_KEY'] = os.getenv('STRIPE_PUBLIC_KEY')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, nullable=False)
    encrypted_data = db.Column(db.Text, nullable=False)
    payment_status = db.Column(db.String(50), default='pending')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)  # in cents
    date = db.Column(db.DateTime, nullable=False)

# Helper functions
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-confirm')

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt='email-confirm',
            max_age=expiration
        )
    except:
        return False
    return email

def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    msg = Message('Confirm Your Email', sender=app.config['MAIL_USERNAME'], recipients=[user_email])
    msg.body = f'Please click the link to confirm your email: {confirm_url}'
    mail.send(msg)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        send_confirmation_email(user.email)
        flash('Registration successful! Please check your email to confirm your account.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            if user.confirmed:
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
            else:
                flash('Please confirm your account before logging in.', 'error')
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    attendees = Attendee.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', attendees=attendees)

@app.route('/event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    
    if request.method == 'POST':
        # Encrypt attendee data (simplified for example)
        encrypted_data = f"ENCRYPTED:{current_user.name}:{current_user.email}"
        
        attendee = Attendee(
            user_id=current_user.id,
            event_id=event.id,
            encrypted_data=encrypted_data
        )
        db.session.add(attendee)
        db.session.commit()
        
        return redirect(url_for('payment', event_id=event.id))
    
    return render_template('event_detail.html', event=event)

@app.route('/payment/<int:event_id>', methods=['GET', 'POST'])
@login_required
def payment(event_id):
    event = Event.query.get_or_404(event_id)
    attendee = Attendee.query.filter_by(user_id=current_user.id, event_id=event_id).first_or_404()
    
    if request.method == 'POST':
        try:
            # Create Stripe charge
            charge = stripe.Charge.create(
                amount=event.price,
                currency='usd',
                source=request.form['stripeToken'],
                description=f'Payment for {event.name}'
            )
            
            attendee.payment_status = 'paid'
            db.session.commit()
            
            flash('Payment successful!', 'success')
            return redirect(url_for('dashboard'))
        
        except stripe.error.CardError as e:
            flash(f'Card error: {e.error.message}', 'error')
        except stripe.error.StripeError as e:
            flash('Payment failed. Please try again.', 'error')
            app.logger.error(f'Stripe error: {str(e)}')
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            app.logger.error(f'Payment error: {str(e)}')
    
    return render_template('payment.html', 
                         event=event,
                         stripe_public_key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    
    attendees = Attendee.query.all()
    return render_template('admin.html', attendees=attendees)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialize database
def create_tables():
    with app.app_context():
        db.create_all()

if __
