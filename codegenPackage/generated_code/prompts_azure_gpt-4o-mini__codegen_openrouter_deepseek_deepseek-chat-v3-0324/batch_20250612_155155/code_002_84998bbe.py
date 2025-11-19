"""
Generated Code Metadata:
========================
Original URL: https://letz.dev
Prompt: Generate a code snippet for a web application that displays available domain names for sale, including features like making offers and checking bid statuses, inspired by letz.dev's listing.
Generated: DETERMINISTIC_84998bbed8c2ad24
Batch ID: 20250612_155155
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    bids = db.relationship('Bid', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    listed_at = db.Column(db.DateTime, default=datetime.utcnow)
    bids = db.relationship('Bid', backref='domain', lazy=True)

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    domains = Domain.query.order_by(Domain.listed_at.desc()).all()
    return render_template('index.html', domains=domains)

@app.route('/domain/<int:domain_id>')
def domain_detail(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    bids = Bid.query.filter_by(domain_id=domain_id).order_by(Bid.amount.desc()).all()
    return render_template('domain_detail.html', domain=domain, bids=bids)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/make_offer/<int:domain_id>', methods=['POST'])
@login_required
def make_offer(domain_id):
    domain = Domain.query.get_or_404(domain_id)
    try:
        amount = float(request.form['amount'])
        if amount <= 0:
            flash('Offer amount must be positive.', 'danger')
            return redirect(url_for('domain_detail', domain_id=domain_id))
        
        bid = Bid(
            amount=amount,
            user_id=current_user.id,
            domain_id=domain_id
        )
        db.session.add(bid)
        db.session.commit()
        flash('Your offer has been submitted.', 'success')
    except ValueError:
        flash('Invalid offer amount.', 'danger')
    return redirect(url_for('domain_detail', domain_id=domain_id))

@app.route('/api/bids/<int:domain_id>')
def get_bids(domain_id):
    bids = Bid.query.filter_by(domain_id=domain_id).order_by(Bid.amount.desc()).all()
    bids_data = [{
        'id': bid.id,
        'amount': bid.amount,
        'status': bid.status,
        'created_at': bid.created_at.isoformat(),
        'username': bid.user.username
    } for bid in bids]
    return jsonify(bids_data)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Marketplace - {% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">Domain Marketplace</a>
            <div class="navbar-nav">
                {% if current_user.is_authenticated %}
                    <a class="nav-link" href="{{ url_for('logout') }}">Logout</a>
                {% else %}
                    <a class="nav-link" href="{{ url_for('login') }}">Login</a>
                    <a class="nav-link" href="{{ url_for('register') }}">Register</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Available Domains{% endblock %}

{% block content %}
<h1 class="mb-4">Available Domains</h1>
<div class="row">
    {% for domain in domains %}
    <div class="col-md-4 mb-4">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ domain.name }}</h5>
                <p class="card-text">${{ "%.2f"|format(domain.price) }}</p>
                <p class="card-text text-muted">{{ domain.description|default('No description available') }}</p>
                <a href="{{ url_for('domain_detail', domain_id=domain.id) }}" class="btn btn-primary">View Details</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

```html
<!-- templates/domain_detail.html -->
{% extends "base.html" %}

{% block title %}{{ domain.name }}{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <h1>{{ domain.name }}</h1>
        <p class="lead">Listed for ${{ "%.2f"|format(domain.price) }}</p>
        <p>{{ domain.description|default('No description available') }}</
