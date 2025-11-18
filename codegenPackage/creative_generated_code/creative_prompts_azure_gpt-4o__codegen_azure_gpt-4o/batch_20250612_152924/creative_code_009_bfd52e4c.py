"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Generate code for a donation portal tailored for a crowdfunded university initiative, including features for secure payment processing and donor recognition.
Generated: DETERMINISTIC_bfd52e4c9a144ef7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# donation_portal.py
from flask import Flask, request, render_template, redirect, url_for, flash
import stripe

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for production

# Stripe API credentials
stripe.api_key = 'your_stripe_secret_key'  # Replace with your secret Stripe API key

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')  # Render the homepage

# Route for donation form
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        try:
            # Collect form data
            donor_name = request.form['name']
            donor_email = request.form['email']
            amount = int(request.form['amount']) * 100  # Convert dollars to cents
            
            # Create a Stripe PaymentIntent
            stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method_types=['card'],
                receipt_email=donor_email
            )
            
            # Flash a success message and redirect
            flash('Thank you for your donation, {}!'.format(donor_name), 'success')
            return redirect(url_for('index'))
        
        except stripe.error.StripeError as e:
            # Handle Stripe errors
            flash('Payment processing error: {}'.format(e), 'danger')
            return redirect(url_for('donate'))
        
        except ValueError:
            # Handle invalid input errors
            flash('Invalid donation amount. Please enter a valid number.', 'danger')
            return redirect(url_for('donate'))
    return render_template('donate.html')  # Render the donation form

# Route for donor recognition
@app.route('/donors')
def donors():
    # In a production system, donor data would be fetched from a database
    donor_list = [
        {'name': 'Alice', 'amount': 100},
        {'name': 'Bob', 'amount': 50},
        {'name': 'Charlie', 'amount': 200},
    ]
    return render_template('donors.html', donors=donor_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University Donation Portal</title>
</head>
<body>
    <h1>Welcome to the University Donation Portal</h1>
    <a href="/donate">Make a Donation</a><br>
    <a href="/donors">View Donors</a>
</body>
</html>
```

```html
<!-- donate.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Make a Donation</title>
</head>
<body>
    <h1>Make a Donation</h1>
    <form method="POST" action="/donate">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="amount">Donation Amount (USD):</label>
        <input type="number" id="amount" name="amount" required><br>
        <button type="submit">Donate</button>
    </form>
</body>
</html>
```

```html
<!-- donors.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donor Recognition</title>
</head>
<body>
    <h1>Donor Recognition</h1>
    <ul>
        {% for donor in donors %}
        <li>{{ donor.name }} - ${{ donor.amount }}</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```
