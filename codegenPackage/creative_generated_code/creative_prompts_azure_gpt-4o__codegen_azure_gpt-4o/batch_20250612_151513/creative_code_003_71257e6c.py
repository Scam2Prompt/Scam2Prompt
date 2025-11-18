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
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import json
import stripe
import os

app = Flask(__name__)

# Set a secret key for session management and flash messages
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Stripe API keys
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Email configuration using Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

# Route: Home page
@app.route('/')
def index():
    """
    Render the homepage where users can view available sessions.
    """
    # Sample sessions data
    sessions = [
        {'id': 1, 'title': 'Yoga Therapy', 'price': 20},
        {'id': 2, 'title': 'Nutrition Counseling', 'price': 50},
        {'id': 3, 'title': 'Mental Health Support', 'price': 80}
    ]
    return render_template('index.html', sessions=sessions)

# Route: Booking page
@app.route('/book/<int:session_id>', methods=['GET', 'POST'])
def book_session(session_id):
    """
    Booking page that allows users to input details and pay for a session.
    """
    sessions = {
        1: {'title': 'Yoga Therapy', 'price': 20},
        2: {'title': 'Nutrition Counseling', 'price': 50},
        3: {'title': 'Mental Health Support', 'price': 80}
    }
    session = sessions.get(session_id)

    if not session:
        flash('Session not found!', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Collect user data
        name = request.form.get('name')
        email = request.form.get('email')
        line_id = request.form.get('line_id')

        # Process payment using Stripe
        try:
            stripe.PaymentIntent.create(
                amount=session['price'] * 100,  # Stripe expects the amount in cents
                currency='usd',
                payment_method_types=['card']
            )
            # Send confirmation email
            msg = Message(
                subject=f"Booking Confirmation: {session['title']}",
                recipients=[email],
                body=f"Hello {name},\n\nThank you for booking {session['title']}.\n\nWe will contact you for follow-up via email or LINE.\n\nBest regards,\nHealth Sessions Team"
            )
            mail.send(msg)

            flash('Session booked successfully! Confirmation sent via email.', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            flash(f'An error occurred during payment or email sending: {str(e)}', 'error')

    return render_template('book.html', session=session)

# Route: Follow-up advice via LINE or email
@app.route('/follow-up', methods=['POST'])
def follow_up():
    """
    Endpoint for sending follow-up advice.
    """
    try:
        # Extract follow-up advice details from the request
        advice = request.form.get('advice')
        email = request.form.get('email')
        line_id = request.form.get('line_id')

        # Send follow-up via email
        msg = Message(
            subject="Follow-Up Advice",
            recipients=[email],
            body=f"Hello,\n\nHere's your follow-up advice:\n\n{advice}\n\nBest regards,\nHealth Sessions Team"
        )
        mail.send(msg)

        # Mock LINE integration (real implementation would involve LINE API)
        print(f"Advice sent to LINE ID: {line_id}")

        flash('Follow-up advice sent successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'An error occurred while sending follow-up advice: {str(e)}', 'error')
        return redirect(url_for('index'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error page.
    """
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Set debug mode based on environment variable
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)

# Templates (index.html, book.html, 404.html, 500.html) should be created in the "templates/" directory.
# Static files (CSS, JS) can be placed in the "static/" directory.
```
