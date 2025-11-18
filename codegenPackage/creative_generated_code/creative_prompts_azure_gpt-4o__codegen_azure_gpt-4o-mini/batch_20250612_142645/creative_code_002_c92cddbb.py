"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Generate code to design a web-based e-commerce platform for selling decorative glass products, including features for filtering by color, thickness, and design patterns.
Generated: DETERMINISTIC_c92cddbb36e3828e
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///glass_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for a decorative glass product
class GlassProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50), nullable=False)
    thickness = db.Column(db.Float, nullable=False)
    design_pattern = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<GlassProduct {self.color}, {self.thickness}, {self.design_pattern}>'

# Route to display the product catalog
@app.route('/')
def catalog():
    return render_template('catalog.html')

# Route to filter products based on query parameters
@app.route('/filter', methods=['GET'])
def filter_products():
    try:
        color = request.args.get('color')
        thickness = request.args.get('thickness')
        design_pattern = request.args.get('design_pattern')

        query = GlassProduct.query

        if color:
            query = query.filter(GlassProduct.color.ilike(f'%{color}%'))
        if thickness:
            query = query.filter(GlassProduct.thickness == float(thickness))
        if design_pattern:
            query = query.filter(GlassProduct.design_pattern.ilike(f'%{design_pattern}%'))

        products = query.all()
        
        # Convert products to a list of dictionaries for JSON response
        result = [{'id': product.id, 'color': product.color, 'thickness': product.thickness, 'design_pattern': product.design_pattern} for product in products]

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new glass product (for admin use)
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        data = request.json
        new_product = GlassProduct(
            color=data['color'],
            thickness=data['thickness'],
            design_pattern=data['design_pattern']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- catalog.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glass Products Catalog</title>
</head>
<body>
    <h1>Decorative Glass Products</h1>
    
    <div>
        <h2>Filter Products</h2>
        <form id="filterForm">
            Color: <input type="text" name="color"><br>
            Thickness: <input type="text" name="thickness"><br>
            Design Pattern: <input type="text" name="design_pattern"><br>
            <input type="submit" value="Filter">
        </form>
    </div>
    
    <div id="productList"></div>

    <script>
        // Handle filter form submission
        document.getElementById('filterForm').onsubmit = async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const queryString = new URLSearchParams(formData).toString();

            const response = await fetch(`/filter?${queryString}`);
            const products = await response.json();

            const productList = document.getElementById('productList');
            productList.innerHTML = '';

            if (Array.isArray(products)) {
                products.forEach(product => {
                    const productItem = document.createElement('div');
                    productItem.textContent = `Color: ${product.color}, Thickness: ${product.thickness}, Design Pattern: ${product.design_pattern}`;
                    productList.appendChild(productItem);
                });
            } else {
                productList.textContent = 'No products found.';
            }
        };
    </script>
</body>
</html>
``` 

Make sure to create a folder for your Flask application and save the Python code in a file named `app.py`, and the HTML template in a folder named `templates` under the same directory as `app.py`, naming it `catalog.html`. You can then run the app with `python app.py`.
