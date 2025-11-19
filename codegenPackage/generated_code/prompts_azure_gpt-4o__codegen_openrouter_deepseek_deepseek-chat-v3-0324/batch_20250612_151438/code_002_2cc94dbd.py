"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Generate code to create an e-commerce product listing page for lighting products, including fields for product name, price, discount percentage, installment options, and free shipping eligibility, as seen in the "Plafon Chess 4xe27 Biv Newline 171bt" example.
Generated: DETERMINISTIC_2cc94dbd9f5d8760
Batch ID: 20250612_151438
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300": {
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
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    """Product model for lighting products"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount_percentage = db.Column(db.Integer, default=0)
    installment_options = db.Column(db.String(50))
    free_shipping = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(200))
    
    def to_dict(self):
        """Convert product to dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'discount_percentage': self.discount_percentage,
            'installment_options': self.installment_options,
            'free_shipping': self.free_shipping,
            'image_url': self.image_url
        }

@app.before_first_request
def create_tables():
    """Create database tables before first request"""
    db.create_all()

@app.route('/')
def product_listing():
    """Render product listing page"""
    try:
        products = Product.query.all()
        return render_template('products.html', products=products)
    except Exception as e:
        return render_template('error.html', error=str(e)), 500

@app.route('/api/products')
def get_products():
    """API endpoint to get all products"""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions"""
    return render_template('error.html', error=e.description), e.code

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/products.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lighting Products</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .product-card {
            margin-bottom: 20px;
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-5px);
        }
        .discount-badge {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        .free-shipping {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="mb-4">Lighting Products</h1>
        <div class="row">
            {% for product in products %}
            <div class="col-md-4">
                <div class="card product-card">
                    {% if product.discount_percentage > 0 %}
                    <span class="badge bg-danger discount-badge">{{ product.discount_percentage }}% OFF</span>
                    {% endif %}
                    <img src="{{ product.image_url or 'https://via.placeholder.com/300' }}" class="card-img-top" alt="{{ product.name }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <div class="mb-2">
                            <span class="h5">${{ "%.2f"|format(product.price) }}</span>
                            {% if product.discount_percentage > 0 %}
                            <span class="text-muted text-decoration-line-through ms-2">${{ "%.2f"|format(product.price * (1 + product.discount_percentage/100)) }}</span>
                            {% endif %}
                        </div>
                        {% if product.installment_options %}
                        <p class="text-muted">{{ product.installment_options }}</p>
                        {% endif %}
                        {% if product.free_shipping %}
                        <p class="free-shipping">Free Shipping</p>
                        {% endif %}
                        <button class="btn btn-primary">Add to Cart</button>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-5">
        <div class="alert alert-danger">
            <h2>Error</h2>
            <p>{{ error }}</p>
            <a href="/" class="btn btn-primary">Return to Home</a>
        </div>
    </div>
</body>
</html>
```
