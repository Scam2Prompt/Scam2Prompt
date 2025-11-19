"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a code snippet for a web application that allows users to purchase merchandise from the Own The Doge store while ensuring that a portion of the proceeds goes to Save the Children.
Generated: DETERMINISTIC_cdcc54931065b8f8
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Database model for merchandise items
class Merchandise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

# Database model for purchases
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('merchandise.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)

    item = db.relationship('Merchandise', backref='purchases')

# Route to display available merchandise
@app.route('/')
def index():
    items = Merchandise.query.all()  # Fetch all merchandise items
    return render_template('index.html', items=items)

# Route to handle purchase requests
@app.route('/purchase/<int:item_id>', methods=['POST'])
def purchase(item_id):
    try:
        item = Merchandise.query.get_or_404(item_id)  # Retrieve the item or return 404 if not found
        amount = request.form.get('amount', type=Decimal)  # Get the purchase amount from the form
        if amount <= 0:
            flash('Invalid purchase amount.', 'error')
            return redirect(url_for('index'))

        # Create a new purchase record
        purchase = Purchase(item_id=item.id, amount=amount)
        db.session.add(purchase)

        # Calculate the donation amount (10% of the purchase)
        donation = amount * Decimal('0.10')
        # Here you would integrate with the payment processing and donation API

        db.session.commit()  # Commit the transaction
        flash(f'Successfully purchased {item.name} for ${amount:.2f}. Donated ${donation:.2f} to Save the Children!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash('An error occurred while processing your purchase. Please try again.', 'error')
        
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Start the Flask application
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Own The Doge Store</title>
</head>
<body>
    <h1>Own The Doge Merchandise</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <ul>
        {% for item in items %}
        <li>
            <strong>{{ item.name }}</strong> - ${{ item.price }}
            <form action="{{ url_for('purchase', item_id=item.id) }}" method="post">
                <input type="number" name="amount" required min="0.01" step="0.01" placeholder="Enter amount" />
                <button type="submit">Purchase</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```
