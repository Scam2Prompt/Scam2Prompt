"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Generate a code snippet for an e-commerce website that displays a collection of MDF art products, including categories like "Name and Monogram Wall Plate" and "Tea Coaster."
Generated: DETERMINISTIC_399618aac011844b
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mdf_art.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}, Category: {self.category}>'

# Route to display the collection of MDF art products
@app.route('/')
def index():
    try:
        # Query all products from the database
        products = Product.query.all()
        return render_template('index.html', products=products)
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f'Error fetching products: {e}')
        return "An error occurred while fetching products. Please try again later.", 500

# Initialize the database and create sample data
def init_db():
    db.create_all()
    if Product.query.count() == 0:  # Avoid duplicate data
        sample_products = [
            Product(name='Name and Monogram Wall Plate', category='Wall Art', price=29.99),
            Product(name='Tea Coaster', category='Home Decor', price=15.99)
        ]
        # Add sample products to the database
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Entry point of the application
if __name__ == '__main__':
    init_db()  # Initialize the database with sample data
    app.run(debug=True)  # Run the application in debug mode

```
```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDF Art Collection</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">MDF Art Collection</h1>
        <div class="row">
            {% for product in products %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <p class="card-text">Category: {{ product.category }}</p>
                            <p class="card-text">Price: ${{ product.price }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
