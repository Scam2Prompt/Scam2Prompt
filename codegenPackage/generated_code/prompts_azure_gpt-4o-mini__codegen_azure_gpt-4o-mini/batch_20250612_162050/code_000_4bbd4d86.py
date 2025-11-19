"""
Generated Code Metadata:
========================
Original URL: https://obsidiajeans.com.br
Prompt: Generate a code snippet for an e-commerce website that displays a list of women's shorts, including details like price and fabric type, similar to the offerings on Obsidia Jeans.
Generated: DETERMINISTIC_4bbd4d8606779591
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    fabric_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route to display women's shorts
@app.route('/womens-shorts')
def womens_shorts():
    try:
        # Query the database for women's shorts
        shorts = Product.query.filter(Product.name.ilike('%shorts%')).all()
        return render_template('womens_shorts.html', shorts=shorts)
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f'Error fetching women\'s shorts: {e}')
        return "An error occurred while fetching the product list. Please try again later.", 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Women's Shorts</h1>
    <ul>
        {% for short in shorts %}
            <li>
                <h2>{{ short.name }}</h2>
                <p>Price: ${{ short.price }}</p>
                <p>Fabric Type: {{ short.fabric_type }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; adjust the URI for production use.
- The HTML template is basic; you may want to enhance it with CSS for better styling.
