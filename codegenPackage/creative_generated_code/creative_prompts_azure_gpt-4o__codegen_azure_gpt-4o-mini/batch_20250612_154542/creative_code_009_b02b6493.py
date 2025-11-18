"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generalearnings.com
Prompt: Develop a dashboard interface for investors to view their deposits, withdrawals, referral bonuses, and portfolio performance, inspired by the features on generalearnings.com.
Generated: DETERMINISTIC_b02b6493625f394c
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investors.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database model for users and their investments
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    deposits = db.relationship('Deposit', backref='owner', lazy=True)
    withdrawals = db.relationship('Withdrawal', backref='owner', lazy=True)
    referral_bonuses = db.relationship('ReferralBonus', backref='owner', lazy=True)

class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class ReferralBonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash password for security
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'danger')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    deposits = Deposit.query.filter_by(user_id=current_user.id).all()
    withdrawals = Withdrawal.query.filter_by(user_id=current_user.id).all()
    referral_bonuses = ReferralBonus.query.filter_by(user_id=current_user.id).all()
    
    # Calculate total deposits, withdrawals, and bonuses
    total_deposits = sum(deposit.amount for deposit in deposits)
    total_withdrawals = sum(withdrawal.amount for withdrawal in withdrawals)
    total_referrals = sum(bonus.amount for bonus in referral_bonuses)
    
    return render_template('dashboard.html', deposits=deposits, withdrawals=withdrawals,
                           referral_bonuses=referral_bonuses,
                           total_deposits=total_deposits,
                           total_withdrawals=total_withdrawals,
                           total_referrals=total_referrals)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

**Note**: This code is a simplified version and assumes you have HTML templates (`register.html`, `login.html`, and `dashboard.html`) set up to provide a user interface. Ensure to replace `'your_secret_key'` with a secure key in production.
