"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: Create a subscription-based application using Mary AI's advanced features. Include monetization options such as consulting, customization, and marketplace integrations.
Generated: DETERMINISTIC_6c5f57281e1c2248
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stripe
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Stripe
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    stripe_customer_id = db.Column(db.String(120))
    subscription_id = db.Column(db.String(120))
    subscription_status = db.Column(db.String(20))
    subscription_end = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    amount = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

class MarketplaceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        user = User(username=username, email=email)
        user.set_password(password)

        try:
            # Create Stripe customer
            customer = stripe.Customer.create(
                email=email,
                name=username
            )
            user.stripe_customer_id = customer.id
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return jsonify({'message': 'User created successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401

        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/profile')
@login_required
def profile():
    return jsonify({
        'username': current_user.username,
        'email': current_user.email,
        'subscription_status': current_user.subscription_status,
        'subscription_end': current_user.subscription_end.isoformat() if current_user.subscription_end else None
    })

@app.route('/subscribe', methods=['POST'])
@login_required
def subscribe():
    data = request.json
    plan_id = data.get('plan_id')

    try:
        # Create subscription
        subscription = stripe.Subscription.create(
            customer=current_user.stripe_customer_id,
            items=[{'price': plan_id}],
            payment_behavior='default_incomplete',
            expand=['latest_invoice.payment_intent']
        )

        current_user.subscription_id = subscription.id
        current_user.subscription_status = 'incomplete'
        db.session.commit()

        return jsonify({
            'subscriptionId': subscription.id,
            'clientSecret': subscription.latest_invoice.payment_intent.client_secret
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/subscription/webhook', methods=['POST'])
def subscription_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.environ.get('STRIPE_WEBHOOK_SECRET')
        )
    except ValueError as e:
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle subscription events
    if event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']
        customer_id = invoice['customer']
        subscription_id = invoice['subscription']

        user = User.query.filter_by(stripe_customer_id=customer_id).first()
        if user:
            user.subscription_status = 'active'
            user.subscription_end = datetime.utcnow() + timedelta(days=30)
            db.session.commit()

    return jsonify({'success': True}), 200

@app.route('/services')
def list_services():
    services = Service.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'description': s.description,
        'price': s.price
    } for s in services])

@app.route('/services/order', methods=['POST'])
@login_required
def order_service():
    data = request.json
    service_id = data.get('service_id')

    service = Service.query.get(service_id)
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    try:
        # Create payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(service.price * 100),
            currency='usd',
            customer=current_user.stripe_customer_id,
            description=f'Service: {service.name}'
        )

        order = Order(
            user_id=current_user.id,
            service_id=service.id,
            amount=service.price,
            status='pending'
        )
        db.session.add(order)
        db.session.commit()

        return jsonify({
            'clientSecret': payment_intent.client_secret,
            'orderId': order.id
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/marketplace')
def list_marketplace_items():
    items = MarketplaceItem.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'price': i.price,
        'created_by': i.created_by
    } for i in items])

@app.route('/marketplace/purchase', methods=['POST'])
@login_required
def purchase_marketplace_item():
    data = request.json
    item_id = data.get('item_id')

    item = MarketplaceItem.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    try:
        # Create payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(item.price * 100
