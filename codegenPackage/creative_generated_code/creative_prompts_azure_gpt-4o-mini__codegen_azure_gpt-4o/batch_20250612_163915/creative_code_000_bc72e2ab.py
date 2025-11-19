"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancen.fr
Prompt: Generate a code snippet for a web application that allows users to donate to cancer research, incorporating features mentioned on the CANCEN website.
Generated: DETERMINISTIC_bc72e2abcf845094
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import stripe

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

# Stripe API keys (replace with your actual keys in production)
stripe.api_key = 'your_stripe_secret_key'

# Route: Home page
@app.route('/')
def home():
    """
    Home page of the web application.
    Displays donation options and a brief description about cancer research.
    """
    return render_template('home.html')

# Route: Handle donation
@app.route('/donate', methods=['POST'])
def donate():
    """
    Handles the donation process through Stripe.
    Accepts POST requests containing donation amount and donor information.
    """
    try:
        # Retrieve form data
        amount = int(request.form['amount'])  # Amount in cents (e.g., $10 => 1000)
        email = request.form['email']

        # Create a payment intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            receipt_email=email,
        )

        # Redirect to a thank-you page upon success
        flash('Thank you for your donation!', 'success')
        return redirect(url_for('thank_you'))

    except stripe.error.StripeError as e:
        # Handle Stripe errors
        flash(f"An error occurred: {e.user_message}", 'error')
        return redirect(url_for('home'))

    except Exception as e:
        # Handle unexpected errors
        flash(f"An unexpected error occurred: {str(e)}", 'error')
        return redirect(url_for('home'))

# Route: Thank you page
@app.route('/thank-you')
def thank_you():
    """
    Displays a thank-you message to the donor after a successful donation.
    """
    return render_template('thank_you.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to Cancer Research</title>
</head>
<body>
    <h1>Support Cancer Research</h1>
    <p>Join the fight against cancer by donating today.</p>

    <!-- Donation Form -->
    <form action="/donate" method="POST">
        <label for="amount">Donation Amount (USD):</label>
        <input type="number" id="amount" name="amount" required min="1">
        <br>
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Donate</button>
    </form>

    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### `templates/thank_you.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
</head>
<body>
    <h1>Thank You for Your Donation!</h1>
    <p>Your generosity helps us advance cancer research and save lives. We deeply appreciate your support.</p>
</body>
</html>
```
