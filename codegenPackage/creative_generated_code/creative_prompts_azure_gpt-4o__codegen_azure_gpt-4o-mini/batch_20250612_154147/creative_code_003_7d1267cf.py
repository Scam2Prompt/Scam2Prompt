"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Provide a solution for connecting physical branded products to digital experiences, such as custom landing pages for swag contests, similar to the example described on Avail Labs' website.
Generated: DETERMINISTIC_7d1267cf38a44c14
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
# Configure SQLAlchemy with SQLite database for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swag_contests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    contest_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to create a new branded product
@app.route('/create_product', methods=['POST'])
def create_product():
    """
    Create a new branded product with a contest URL.
    Request JSON should contain 'name' and 'contest_url'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'contest_url' not in data:
        return jsonify({"error": "Invalid input. 'name' and 'contest_url' are required."}), 400

    new_product = Product(name=data['name'], contest_url=data['contest_url'])
    
    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Product already exists."}), 400

    return jsonify({"message": "Product created successfully!", "product_id": new_product.id}), 201

# Route to get the landing page for a specific product
@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve the landing page for a specific product using its ID.
    """
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404
    
    return render_template('product_landing.html', product=product)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- product_landing.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} Landing Page</title>
</head>
<body>
    <h1>Welcome to the {{ product.name }} Contest!</h1>
    <p>Participate now at: <a href="{{ product.contest_url }}">{{ product.contest_url }}</a></p>
</body>
</html>
```

### Notes:
- Ensure you have Flask and SQLAlchemy installed in your environment.
- Save the HTML file as `product_landing.html` in a `templates` directory where your Flask app is located.
- The application uses an SQLite database, which is suitable for development and testing. For production use, consider using a more scalable database solution.
