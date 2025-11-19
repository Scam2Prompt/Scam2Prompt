"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Generate a code snippet to create an e-commerce product page for herbal supplements similar to those offered by Habbasyi Niaga Utama, focusing on Habbatussauda and its health benefits.
Generated: DETERMINISTIC_42368111f533e57f
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/habbatussauda.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habbasyi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.price}')"

# Define the Habbatussauda product
class Habbatussauda(Product):
    def __init__(self, name, description, price, image_url):
        super().__init__(name, description, price, image_url)
        self.health_benefits = [
            "Boosts immune system",
            "Rich in antioxidants",
            "May help reduce inflammation",
            "Supports heart health"
        ]

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the product page
@app.route('/product', methods=['GET'])
def product_page():
    try:
        # Query the database for Habbatussauda product
        habbatussauda = Product.query.filter_by(name='Habbatussauda').first()
        if habbatussauda is None:
            # Create a new Habbatussauda product if it doesn't exist
            habbatussauda = Habbatussauda(
                name='Habbatussauda',
                description='A herbal supplement made from black seed oil',
                price=19.99,
                image_url='https://example.com/habbatussauda.jpg'
            )
            db.session.add(habbatussauda)
            db.session.commit()
        
        # Render the product page template
        return render_template('product.html', product=habbatussauda)
    except Exception as e:
        # Handle any exceptions
        return str(e), 500

# Route for adding new products
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        # Get the product details from the form data
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        image_url = request.form['image_url']

        # Create a new product instance
        product = Product(name, description, price, image_url)

        # Add the product to the database
        db.session.add(product)
        db.session.commit()

        # Redirect to the product page
        return redirect(url_for('product_page'))
    except Exception as e:
        # Handle any exceptions
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- product.html template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habbatussauda Product Page</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <img src="{{ product.image_url }}" alt="Product Image">
    <h2>Health Benefits:</h2>
    <ul>
    {% for benefit in product.health_benefits %}
        <li>{{ benefit }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```
