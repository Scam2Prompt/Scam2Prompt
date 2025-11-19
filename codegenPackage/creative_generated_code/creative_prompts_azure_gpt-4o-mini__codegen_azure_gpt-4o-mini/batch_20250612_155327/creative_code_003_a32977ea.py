"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Generate a code snippet that demonstrates how to implement two-factor authentication for a login system, similar to the security measures in the Socrates GM employee portal.
Generated: DETERMINISTIC_a32977eadc8c119b
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
import time
from flask import Flask, request, redirect, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

# Function to send email for 2FA
def send_2fa_email(email, code):
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')
            message = f'Subject: Your 2FA Code\n\nYour code is: {code}'
            server.sendmail('your_email@example.com', email, message)
    except Exception as e:
        print(f"Error sending email: {e}")

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
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
            # Generate 2FA code
            two_factor_code = random.randint(100000, 999999)
            session['two_factor_code'] = two_factor_code
            session['user_id'] = user.id
            # Send 2FA code to user's email
            send_2fa_email(user.email, two_factor_code)
            return redirect(url_for('verify_2fa'))
        else:
            return "Invalid username or password", 401
    return render_template('login.html')

# Route to verify 2FA code
@app.route('/verify_2fa', methods=['GET', 'POST'])
def verify_2fa():
    if request.method == 'POST':
        input_code = request.form['code']
        if int(input_code) == session.get('two_factor_code'):
            session.pop('two_factor_code', None)  # Clear the code
            return "Login successful!", 200  # Proceed to the user's dashboard
        else:
            return "Invalid 2FA code", 401
    return render_template('verify_2fa.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
