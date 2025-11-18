"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdiscount.pages.dev
Prompt: Develop a dashboard for businesses to track their profits and manage discount offers, inspired by the features described on the "claimdiscount.pages.dev" website.
Generated: DETERMINISTIC_44fb6dbe69687e2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dashboard.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profit = db.Column(db.Float, default=0.0)
    discount_offers = db.relationship('DiscountOffer', backref='business', lazy=True)

# Define the DiscountOffer model
class DiscountOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the dashboard
@app.route('/')
def index():
    businesses = Business.query.all()
    return render_template('dashboard.html', businesses=businesses)

# Route to add a new business
@app.route('/add_business', methods=['POST'])
def add_business():
    try:
        data = request.json
        new_business = Business(name=data['name'])
        db.session.add(new_business)
        db.session.commit()
        return jsonify({'message': 'Business added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to update profit for a business
@app.route('/update_profit/<int:business_id>', methods=['PUT'])
def update_profit(business_id):
    try:
        data = request.json
        business = Business.query.get_or_404(business_id)
        business.profit += data['amount']
        db.session.commit()
        return jsonify({'message': 'Profit updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to add a discount offer
@app.route('/add_discount', methods=['POST'])
def add_discount():
    try:
        data = request.json
        new_discount = DiscountOffer(
            description=data['description'],
            percentage=data['percentage'],
            business_id=data['business_id']
        )
        db.session.add(new_discount)
        db.session.commit()
        return jsonify({'message': 'Discount offer added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to view all discount offers for a business
@app.route('/discounts/<int:business_id>', methods=['GET'])
def get_discounts(business_id):
    try:
        discounts = DiscountOffer.query.filter_by(business_id=business_id).all()
        return jsonify([{'id': d.id, 'description': d.description, 'percentage': d.percentage} for d in discounts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Dashboard</title>
</head>
<body>
    <h1>Business Dashboard</h1>
    <h2>Businesses</h2>
    <ul>
        {% for business in businesses %}
            <li>{{ business.name }} - Profit: ${{ business.profit }}</li>
        {% endfor %}
    </ul>
    <h2>Add Business</h2>
    <form id="addBusinessForm">
        <input type="text" id="businessName" placeholder="Business Name" required>
        <button type="submit">Add Business</button>
    </form>

    <script>
        document.getElementById('addBusinessForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const businessName = document.getElementById('businessName').value;

            fetch('/add_business', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: businessName })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                location.reload();
            });
        });
    </script>
</body>
</html>
```
