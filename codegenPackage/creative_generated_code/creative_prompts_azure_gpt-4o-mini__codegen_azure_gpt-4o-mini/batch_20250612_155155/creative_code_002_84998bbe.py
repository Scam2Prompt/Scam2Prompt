"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://letz.dev
Prompt: Generate a code snippet for a web application that displays available domain names for sale, including features like making offers and checking bid statuses, inspired by letz.dev's listing.
Generated: DETERMINISTIC_84998bbed8c2ad24
Batch ID: 20250612_155155
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database connection (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Domain model to represent domain listings
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    offers = db.relationship('Offer', backref='domain', lazy=True)

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Route to display available domain names
@app.route('/', methods=['GET'])
def index():
    try:
        domains = Domain.query.all()  # Fetch all domain listings
        return render_template('index.html', domains=domains)
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Route to make an offer on a domain
@app.route('/offer', methods=['POST'])
def make_offer():
    # Validate incoming data
    data = request.get_json()
    if not data or 'domain_id' not in data or 'amount' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        # Create and save the offer
        new_offer = Offer(domain_id=data['domain_id'], amount=data['amount'])
        db.session.add(new_offer)
        db.session.commit()
        return jsonify({"message": "Offer submitted successfully"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Route to check the status of bids on a domain
@app.route('/bids/<int:domain_id>', methods=['GET'])
def check_bids(domain_id):
    try:
        offers = Offer.query.filter_by(domain_id=domain_id).all()  # Fetch offers for a specific domain
        return jsonify([{"id": offer.id, "amount": offer.amount} for offer in offers]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Listings</title>
</head>
<body>
    <h1>Available Domain Names for Sale</h1>
    <ul>
        {% for domain in domains %}
            <li>
                <strong>{{ domain.name }}</strong> - ${{ domain.price }}
                <button onclick="makeOffer({{ domain.id }})">Make an Offer</button>
            </li>
        {% endfor %}
    </ul>

    <script>
        function makeOffer(domainId) {
            const amount = prompt("Enter your offer amount:");
            if (amount) {
                fetch('/offer', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ domain_id: domainId, amount: parseFloat(amount) })
                })
                .then(response => response.json())
                .then(data => alert(data.message || data.error))
                .catch(error => alert('Error: ' + error));
            }
        }
    </script>
</body>
</html>
```
