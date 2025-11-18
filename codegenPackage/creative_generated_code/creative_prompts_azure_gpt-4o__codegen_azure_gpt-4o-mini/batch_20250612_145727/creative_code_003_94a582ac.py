"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Generate code for a web application that allows users to input their desired loan amount and repayment period, then matches them with suitable MFO offers, as seen on nocreditcheck.online.
Generated: DETERMINISTIC_94a582ace9272d6c
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define LoanOffer model
class LoanOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    repayment_period = db.Column(db.Integer, nullable=False)  # in months
    interest_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<LoanOffer {self.id}: Amount={self.amount}, Period={self.repayment_period}, Rate={self.interest_rate}>'

# Create the database and LoanOffer table
with app.app_context():
    db.create_all()

# Home route to render the input form
@app.route('/')
def index():
    return render_template('index.html')

# API route to get loan offers based on user input
@app.route('/api/match_offers', methods=['POST'])
def match_offers():
    try:
        # Get user inputs from the request
        loan_amount = float(request.json.get('amount'))
        repayment_period = int(request.json.get('period'))

        # Validate user inputs
        if loan_amount <= 0 or repayment_period <= 0:
            return jsonify({'error': 'Invalid input values. Amount and period must be greater than zero.'}), 400

        # Query for matching loan offers
        offers = LoanOffer.query.filter(
            LoanOffer.amount <= loan_amount,
            LoanOffer.repayment_period <= repayment_period
        ).all()

        # Format offers for response
        offers_list = [{'id': offer.id, 'amount': offer.amount, 
                        'repayment_period': offer.repayment_period, 
                        'interest_rate': offer.interest_rate} for offer in offers]

        return jsonify({'offers': offers_list}), 200

    except ValueError:
        return jsonify({'error': 'Invalid input types. Amount must be a number and period must be an integer.'}), 400
    except Exception as e:
        # Log or print the exception for debugging
        app.logger.error(f'Error occurred: {e}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Matcher</title>
    <script>
        async function matchOffers() {
            const amount = document.getElementById('amount').value;
            const period = document.getElementById('period').value;

            const response = await fetch('/api/match_offers', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ amount: amount, period: period })
            });

            const data = await response.json();

            if (response.ok) {
                const offersDiv = document.getElementById('offers');
                offersDiv.innerHTML = '';
                data.offers.forEach(offer => {
                    offersDiv.innerHTML += `<p>Offer ID: ${offer.id}, Amount: ${offer.amount}, Period: ${offer.repayment_period}, Rate: ${offer.interest_rate}</p>`;
                });
            } else {
                alert(data.error);
            }
        }
    </script>
</head>
<body>
    <h1>Find Your Loan Offers</h1>
    <label for="amount">Desired Loan Amount:</label>
    <input type="number" id="amount" required>
    <br>
    <label for="period">Repayment Period (months):</label>
    <input type="number" id="period" required>
    <br>
    <button onclick="matchOffers()">Find Offers</button>
    <div id="offers"></div>
</body>
</html>
```
