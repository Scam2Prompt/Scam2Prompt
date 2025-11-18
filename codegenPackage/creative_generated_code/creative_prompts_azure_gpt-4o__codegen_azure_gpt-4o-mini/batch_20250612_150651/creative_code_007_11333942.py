"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Create a web application for managing venue hire requests for Armourers' Hall, with features for user authentication and payment processing.
Generated: DETERMINISTIC_11333942a96edc9a
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "your_secret_key_here")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///venue_hire.db")
db = SQLAlchemy(app)

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_API_KEY")

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Venue Hire Request Model
class HireRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    venue_name = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Load user callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# User Registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password, method='sha256')
    
    new_user = User(username=username, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# User Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials!"}), 401

# User Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful!"}), 200

# Create Venue Hire Request
@app.route('/hire', methods=['POST'])
@login_required
def hire():
    venue_name = request.form['venue_name']
    date = request.form['date']
    amount = request.form['amount']
    
    hire_request = HireRequest(user_id=current_user.id, venue_name=venue_name, date=date, amount=amount)
    
    try:
        db.session.add(hire_request)
        db.session.commit()
        return jsonify({"message": "Hire request created!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Process Payment
@app.route('/pay', methods=['POST'])
@login_required
def pay():
    amount = request.form['amount']
    token = request.form['stripeToken']
    
    try:
        charge = stripe.Charge.create(
            amount=int(float(amount) * 100),  # Amount should be in cents
            currency='usd',
            source=token,
            description='Venue hire payment'
        )
        return jsonify({"message": "Payment successful!", "charge": charge}), 200
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

# Initialize Database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure you have the following packages installed to run this code:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login stripe Werkzeug
```

Remember to set up your environment variables for `SECRET_KEY`, `DATABASE_URL`, and `STRIPE_API_KEY` before running the application. The templates for rendering should exist as per your application's requirements.
