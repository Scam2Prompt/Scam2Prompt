"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty.wiki
Prompt: Write a script to enable two-factor authentication (2FA) for WLFI platform users during login and transactions. Include security best practices mentioned on the webpage.
Generated: DETERMINISTIC_3abacc2a3062e42a
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, redirect, session, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Simulated database for users
users_db = {
    'user@example.com': {
        'password': generate_password_hash('secure_password'),  # Hashing the password
        'otp_secret': os.urandom(16).hex(),  # Generate a random secret for OTP
        'is_verified': False
    }
}

# Function to generate a one-time password (OTP)
def generate_otp():
    return random.randint(100000, 999999)

# Function to send OTP via email
def send_otp(email, otp):
    msg = MIMEText(f'Your OTP code is: {otp}')
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = 'no-reply@example.com'
    msg['To'] = email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
        flash("Error sending OTP. Please try again.", "error")

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate user credentials
        user = users_db.get(email)
        if user and check_password_hash(user['password'], password):
            otp = generate_otp()  # Generate OTP
            send_otp(email, otp)  # Send OTP to user's email
            session['otp'] = otp
            session['email'] = email
            return redirect(url_for('verify_otp'))
        else:
            flash("Invalid credentials. Please try again.", "error")
    return render_template('login.html')

# Route for OTP verification
@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if entered_otp == str(session.get('otp')):
            users_db[session['email']]['is_verified'] = True  # Mark user as verified
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid OTP. Please try again.", "error")
    return render_template('verify_otp.html')

# Home route after successful login
@app.route('/home')
def home():
    if not users_db.get(session.get('email', '')).get('is_verified', False):
        return redirect(url_for('login'))
    return "Welcome to your home page!"

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure you replace email configuration details (`smtp.example.com`, `your_email@example.com`, `your_email_password`) with actual values.
- This code uses Flask for web application development and simulates a user database. Adjust as necessary for your production environment.
- The email sending part is basic; consider using a more robust solution in production (like integrating with a dedicated email service).
- Ensure you implement security best practices such as using HTTPS in a production environment.
