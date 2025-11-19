"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siprosa.org
Prompt: Write a code snippet for a web application that allows users to donate to educational initiatives like Siprosa School, focusing on user-friendly design and secure payment processing.
Generated: DETERMINISTIC_312ea70d0c7836db
Batch ID: 20250612_155803
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://js.stripe.com/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's a Python code snippet using Flask for the web application server and Stripe for secure payment processing. Ensure you have Flask and Stripe Python libraries installed (`pip install flask stripe`) before running this code.

```python
from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Stripe API keys (replace with your actual keys)
stripe.api_key = "sk_test_your_secret_key"
STRIPE_PUBLIC_KEY = "pk_test_your_public_key"

# Route for the homepage (donation form)
@app.route("/")
def home():
    return render_template("donation.html", public_key=STRIPE_PUBLIC_KEY)

# Route for processing the payment
@app.route("/donate", methods=["POST"])
def donate():
    try:
        # Retrieve donation amount and token from the request
        amount = int(request.form['amount'])  # Amount in cents (e.g., $10 = 1000 cents)
        token = request.form['stripeToken']

        # Create a charge using Stripe API
        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=token,
            description="Donation to Siprosa School Educational Initiative"
        )

        # Return a success message
        return jsonify({"message": "Donation successful! Thank you for your support."})
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An error occurred. Please try again later."}), 500

# Basic error handling for 404 not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
```

In addition to the Python code, you'll need a corresponding HTML template (`templates/donation.html`) for the donation form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to Siprosa School</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <h1>Donate to Siprosa School Educational Initiative</h1>
    <form action="/donate" method="POST" id="donation-form">
        <label for="amount">Donation Amount (USD):</label>
        <input type="number" name="amount" id="amount" required>
        <button type="button" id="pay-button">Donate</button>
    </form>
    <script>
        const stripe = Stripe("{{ public_key }}");
        const form = document.getElementById("donation-form");
        const payButton = document.getElementById("pay-button");

        payButton.addEventListener("click", async () => {
            const { token, error } = await stripe.createToken();
            if (error) {
                alert(error.message);
            } else {
                const hiddenInput = document.createElement("input");
                hiddenInput.type = "hidden";
                hiddenInput.name = "stripeToken";
                hiddenInput.value = token.id;
                form.appendChild(hiddenInput);
                form.submit();
            }
        });
    </script>
</body>
</html>
```
