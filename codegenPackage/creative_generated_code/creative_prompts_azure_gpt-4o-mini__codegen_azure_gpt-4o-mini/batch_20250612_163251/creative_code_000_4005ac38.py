"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Generate a code snippet for a web application that allows users to order wooden products, specifically focusing on the features of "Maderas Aserradas" and "Cabos" as described on the Maderas Elaboradas website.
Generated: DETERMINISTIC_4005ac386d548f17
Batch ID: 20250612_163251
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and the Product table
@app.before_first_request
def create_tables():
    db.create_all()

# Route to display the product catalog
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route to handle product orders
@app.route('/order/<int:product_id>', methods=['POST'])
def order(product_id):
    try:
        product = Product.query.get(product_id)
        if product:
            # Here, you should handle the order process (e.g., payment processing)
            flash(f'Order placed successfully for {product.name}!', 'success')
        else:
            flash('Product not found.', 'error')
    except Exception as e:
        flash(f'An error occurred while placing your order: {str(e)}', 'error')
    return redirect(url_for('index'))

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
    <title>Wood Products Catalog</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Wood Products Catalog</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <div class="row">
            {% for product in products %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <p class="card-text">{{ product.description }}</p>
                            <p class="card-text">Price: ${{ product.price }}</p>
                            <form action="{{ url_for('order', product_id=product.id) }}" method="post">
                                <button type="submit" class="btn btn-primary">Order Now</button>
                            </form>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Important Notes:
- This code is a basic web application built using Flask and SQLite. 
- Ensure that you have Flask and Flask-SQLAlchemy installed. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Replace `'your_secret_key_here'` with a strong secret key for session management.
- The application is set to run in debug mode for development purposes; remember to set `debug=False` in a production environment.
- You will need to create a database and add products to the `Product` table before running the application.
