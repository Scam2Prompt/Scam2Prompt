"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Generate code for a dashboard interface that allows users to register, buy $KANG tokens, confirm orders, and view their token balance, based on Kangamoon's presale process.
Generated: DETERMINISTIC_587daa5f22e0c1e3
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kangamoon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    token_balance = db.Column(db.Float, default=0.0)

# Database model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash password and create new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error occurred: {e}', 'danger')
        
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    
    return render_template('login.html')

# Route for the user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)

# Route to buy KANG tokens
@app.route('/buy_tokens', methods=['POST'])
def buy_tokens():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    amount = float(request.form['amount'])
    
    # Simple presale mechanism (e.g., 1 token = $1)
    if amount <= 0:
        flash('Amount must be greater than 0.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Update the user's token balance
    user.token_balance += amount
    new_order = Order(user_id=user.id, amount=amount)
    
    try:
        db.session.add(new_order)
        db.session.commit()
        flash('Tokens purchased successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error occurred during purchase: {e}', 'danger')
    
    return redirect(url_for('dashboard'))

# Route to confirm orders
@app.route('/confirm_order/<int:order_id>', methods=['POST'])
def confirm_order(order_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    order = Order.query.get(order_id)
    
    if order is None or order.confirmed:
        flash('Order not found or already confirmed.', 'danger')
        return redirect(url_for('dashboard'))
    
    order.confirmed = True
    
    try:
        db.session.commit()
        flash('Order confirmed successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error occurred during order confirmation: {e}', 'danger')
    
    return redirect(url_for('dashboard'))

# Route to view token balance
@app.route('/view_balance')
def view_balance():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('balance.html', balance=user.token_balance)

# Route to logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- The HTML templates (e.g., `register.html`, `login.html`, `dashboard.html`, `balance.html`) need to be created to render the respective views.
- This code assumes a basic presale system where each token is bought for $1.
- Ensure that you have Flask and Flask-SQLAlchemy installed (`pip install Flask Flask-SQLAlchemy`).
