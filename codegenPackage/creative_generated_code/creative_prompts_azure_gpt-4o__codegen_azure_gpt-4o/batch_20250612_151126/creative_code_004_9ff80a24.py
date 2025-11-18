"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Write code to create a donation page for a nonprofit organization, ensuring secure payment processing and user confidentiality, similar to the ALPS Foundation's donation page.
Generated: DETERMINISTIC_9ff80a24fb77d2ca
Batch ID: 20250612_151126
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# donation_page.py

from flask import Flask, render_template, request, redirect, url_for, flash
import stripe

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this is a strong, secure secret key

# Stripe API keys (Use environment variables in production for security)
stripe.api_key = 'your_stripe_secret_key'

# Routes

@app.route('/')
def home():
    """
    Render the donation page.
    """
    return render_template('donation_page.html')

@app.route('/donate', methods=['POST'])
def donate():
    """
    Handle the donation form submission.
    Securely process payments using Stripe's API.
    """
    try:
        # Extract form data
        amount = int(request.form['amount'])  # Amount in dollars
        email = request.form['email']

        # Validate form data
        if amount <= 0:
            flash("Donation amount must be greater than zero.", "error")
            return redirect(url_for('home'))
        
        if not email:
            flash("Email is required.", "error")
            return redirect(url_for('home'))

        # Convert amount to cents for Stripe (Stripe processes amounts in cents)
        amount_cents = amount * 100

        # Create the payment intent with Stripe
        stripe.PaymentIntent.create(
            amount=amount_cents,
            currency='usd',
            receipt_email=email,
            description='Donation to Nonprofit Organization',
        )

        # Payment successful
        flash("Thank you for your generous donation!", "success")
        return redirect(url_for('home'))

    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        flash(f"Payment failed: {e.user_message}", "error")
        return redirect(url_for('home'))

    except Exception as e:
        # Handle other exceptions
        flash("An error occurred while processing your donation. Please try again.", "error")
        return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- donation_page.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donation Page</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Simple CSS styling for the donation page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            margin-top: 20px;
        }
        label {
            display: block;
            margin-bottom: 10px;
            color: #555;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
        .message {
            margin: 20px 0;
            text-align: center;
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Donate to Support Our Cause</h1>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="message">
                    {% for message in messages %}
                        <p>{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        <form action="/donate" method="POST">
            <label for="amount">Donation Amount ($):</label>
            <input type="number" id="amount" name="amount" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <button type="submit">Donate</button>
        </form>
    </div>
</body>
</html>
```

**Notes for Deployment:**
- Replace `your_secret_key` and `your_stripe_secret_key` with actual secure keys. Use environment variables for sensitive information in production.
- Set the Flask `debug` mode to `False` in production.
- Use HTTPS for secure communication (especially when handling sensitive payment details).
