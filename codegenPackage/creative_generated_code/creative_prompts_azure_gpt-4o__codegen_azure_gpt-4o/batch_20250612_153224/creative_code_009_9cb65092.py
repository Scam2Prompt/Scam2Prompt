"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Recommend a library for managing multilingual product descriptions and pricing for Bollé's Colombian distributor website.
Generated: DETERMINISTIC_9cb65092359c36e3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code using the `Flask` web framework and `Babel` for managing multilingual product descriptions and `SQLAlchemy` for storing product pricing.

```python
from flask import Flask, request, jsonify
from flask_babel import Babel, _
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for Babel and SQLAlchemy
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

babel = Babel(app)
db = SQLAlchemy(app)

# Error handling for invalid locales
@babel.localeselector
def get_locale():
    locale = request.args.get('lang')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    return app.config['BABEL_DEFAULT_LOCALE']


# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_es = db.Column(db.String(100), nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    description_es = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self, lang):
        """
        Converts product data to a dictionary based on the requested language.
        """
        return {
            "id": self.id,
            "name": self.name_en if lang == 'en' else self.name_es,
            "description": self.description_en if lang == 'en' else self.description_es,
            "price": self.price,
        }


# Error handler for database query issues
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": _("Resource not found")}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": _("An internal error occurred")}), 500


# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        lang = get_locale()
        products = Product.query.all()
        return jsonify([product.to_dict(lang) for product in products])
    except Exception as e:
        app.logger.error(f"Error fetching products: {e}")
        return jsonify({"error": _("Failed to fetch products")}), 500


# Route to get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        lang = get_locale()
        product = Product.query.get(product_id)
        if not product:
            return not_found_error(404)
        return jsonify(product.to_dict(lang))
    except Exception as e:
        app.logger.error(f"Error fetching product {product_id}: {e}")
        return jsonify({"error": _("Failed to fetch product")}), 500


# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        # Validate request data
        if not all(key in data for key in ('name_en', 'name_es', 'description_en', 'description_es', 'price')):
            return jsonify({"error": _("Invalid input data")}), 400

        new_product = Product(
            name_en=data['name_en'],
            name_es=data['name_es'],
            description_en=data['description_en'],
            description_es=data['description_es'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": _("Product added successfully"), "product": new_product.to_dict('en')}), 201
    except Exception as e:
        app.logger.error(f"Error adding product: {e}")
        return jsonify({"error": _("Failed to add product")}), 500


if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Ensure you install the necessary dependencies before running this code:

```bash
pip install flask flask-babel flask-sqlalchemy
```
