"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goltaa.com
Prompt: Generate a code snippet for an e-commerce website that displays flower arrangement products with pricing and discount information similar to گلتا's product listings.
Generated: DETERMINISTIC_d5d44d9374b49c91
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flowers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=True)  # Discount percentage

    def final_price(self):
        """Calculate the final price after applying discount."""
        if self.discount:
            return self.price * (1 - self.discount / 100)
        return self.price

# Route to display flower arrangements
@app.route('/products')
def products():
    """Fetch product listings and render them in a template."""
    try:
        # Query all products from the database
        all_products = Product.query.all()
        return render_template('products.html', products=all_products)
    except Exception as e:
        # Log the error (logging implementation can be added)
        return jsonify({"error": "Unable to fetch products", "message": str(e)}), 500

# Create a sample database if it doesn't exist
@app.before_first_request
def create_tables():
    """Create database tables if they do not exist."""
    db.create_all()
    # Populate with example data if empty
    if Product.query.count() == 0:
        sample_products = [
            Product(name='Rose Bouquet', price=50, discount=10),
            Product(name='Tulip Arrangement', price=30, discount=0),
            Product(name='Lily Set', price=40, discount=5),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Template (products.html)
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flower Arrangements</title>
</head>
<body>
    <h1>Flower Arrangements</h1>
    <ul>
        {% for product in products %}
            <li>
                <strong>{{ product.name }}</strong><br>
                Original Price: ${{ product.price }}<br>
                {% if product.discount %}
                    Discount: {{ product.discount }}%<br>
                    Final Price: ${{ product.final_price() }}<br>
                {% else %}
                    No Discount Available<br>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
