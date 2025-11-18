"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Create a web application that integrates real-time account access for personal loan management, similar to the online banking features described by Ambro Contables.
Generated: DETERMINISTIC_478a548e98529ddc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    """Model representing a user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    loans = db.relationship('Loan', backref='owner')


class Loan(db.Model):
    """Model representing a personal loan."""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    """Load user from the user ID."""
    return User.query.get(int(user_id))


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user."""
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    return render_template('register.html')


@app.route('/loans', methods=['GET', 'POST'])
@login_required
def loans():
    """Manage loans: view existing loans or create a new one."""
    if request.method == 'POST':
        amount = request.json.get('amount')
        interest_rate = request.json.get('interest_rate')
        duration_months = request.json.get('duration_months')
        new_loan = Loan(amount=amount, interest_rate=interest_rate, duration_months=duration_months, owner=current_user)
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({'message': 'Loan created successfully'}), 201
    
    loans = Loan.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': loan.id, 'amount': loan.amount, 'interest_rate': loan.interest_rate, 'duration_months': loan.duration_months} for loan in loans]), 200


if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the application with debugging turned off for production
```
