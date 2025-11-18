"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Create a web application using Flask that allows users to book online health sessions, pay for services, and receive follow-up advice via email or LINE.
Generated: DETERMINISTIC_71257e6c4bce2688
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///health_sessions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)

class HealthSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    service = db.Column(db.String(150), nullable=False)
    paid = db.Column(db.Boolean, default=False)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        email = request.form['email']
        
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
        
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
            flash('Login failed. Check your credentials.', 'danger')
    
    return render_template('login.html')

# Route for user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))
    
    sessions = HealthSession.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', sessions=sessions)

# Route for booking a health session
@app.route('/book_session', methods=['POST'])
def book_session():
    if 'user_id' not in session:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))
    
    service = request.form['service']
    date_time = datetime.strptime(request.form['date_time'], '%Y-%m-%d %H:%M')
    
    new_session = HealthSession(user_id=session['user_id'], date_time=date_time, service=service)
    db.session.add(new_session)
    db.session.commit()
    
    flash('Session booked successfully!', 'success')
    
    # Send confirmation email
    send_confirmation_email(session['user_id'], new_session)
    
    return redirect(url_for('dashboard'))

# Function to send confirmation email
def send_confirmation_email(user_id, session):
    user = User.query.get(user_id)
    msg = Message('Session Confirmation',
                  sender='noreply@example.com',
                  recipients=[user.email])
    
    msg.body = f'''
    Dear {user.username},

    Your health session has been successfully booked!

    Service: {session.service}
    Date & Time: {session.date_time.strftime('%Y-%m-%d %H:%M')}

    Thank you!
    '''
    
    with app.app_context():
        mail.send(msg)

# Run the application
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

**Note:** This code assumes that you have set up a suitable database and configured the mail server settings. Adjust the SMTP settings and the database URI according to your environment. Additionally, the HTML templates (`index.html`, `register.html`, `login.html`, and `dashboard.html`) are required for this application to run properly.
