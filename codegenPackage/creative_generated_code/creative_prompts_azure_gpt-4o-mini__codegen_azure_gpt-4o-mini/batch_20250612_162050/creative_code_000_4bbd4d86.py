"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://obsidiajeans.com.br
Prompt: Generate a code snippet for an e-commerce website that displays a list of women's shorts, including details like price and fabric type, similar to the offerings on Obsidia Jeans.
Generated: DETERMINISTIC_4bbd4d8606779591
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    fabric_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}, Price: {self.price}, Fabric: {self.fabric_type}>'

# Route to display women's shorts
@app.route('/womens-shorts')
def display_shorts():
    try:
        # Query the database for women's shorts
        shorts = Product.query.all()
        return render_template('womens_shorts.html', shorts=shorts)
    except Exception as e:
        # Log the error and return an error message
        app.logger.error(f'Error fetching women\'s shorts: {e}')
        return "An error occurred while fetching data.", 500

# Create the database and add sample data if needed
@app.before_first_request
def create_tables():
    db.create_all()
    # Sample data for demonstration purposes
    if not Product.query.first():
        sample_products = [
            Product(name='Casual Denim Shorts', price=29.99, fabric_type='Denim'),
            Product(name='Cotton Summer Shorts', price=19.99, fabric_type='Cotton'),
            Product(name='Chino Shorts', price=24.99, fabric_type='Chino'),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- womens_shorts.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Women's Shorts</title>
</head>
<body>
    <h1>Women's Shorts</h1>
    <ul>
        {% for short in shorts %}
            <li>
                <strong>{{ short.name }}</strong> - 
                Price: ${{ short.price }} - 
                Fabric: {{ short.fabric_type }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
