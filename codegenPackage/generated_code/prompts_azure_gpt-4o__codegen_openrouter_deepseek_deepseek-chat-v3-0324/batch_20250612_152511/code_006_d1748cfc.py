"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Write code to implement a comparison feature for an e-commerce site, allowing users to compare digital products like "2500 جم زپتو" and "2800 جم براول استارز," as seen on "ای ار گیفت."
Generated: DETERMINISTIC_d1748cfc9d554158
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    """
    Product model representing digital products in the e-commerce site.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default='جم')
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    features = db.Column(db.JSON)  # Stores product features as JSON

    def to_dict(self):
        """Convert product object to dictionary for easy JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'currency': self.currency,
            'category': self.category,
            'description': self.description,
            'features': self.features
        }

@app.route('/compare', methods=['GET'])
def compare_products():
    """
    Compare multiple products based on their IDs.
    Expects 'product_ids' as a comma-separated string in the query parameters.
    """
    try:
        product_ids = request.args.get('product_ids', '')
        if not product_ids:
            raise BadRequest('Product IDs are required for comparison.')
        
        ids = [int(id.strip()) for id in product_ids.split(',')]
        if len(ids) < 2:
            raise BadRequest('At least two products are required for comparison.')
        
        products = Product.query.filter(Product.id.in_(ids)).all()
        if len(products) != len(ids):
            found_ids = {p.id for p in products}
            not_found = [str(id) for id in ids if id not in found_ids]
            raise NotFound(f'Products with IDs {", ".join(not_found)} not found.')
        
        return jsonify({
            'products': [p.to_dict() for p in products],
            'common_features': _get_common_features(products)
        })
    except ValueError:
        raise BadRequest('Invalid product ID format. Please provide numeric IDs separated by commas.')
    except Exception as e:
        raise e

def _get_common_features(products):
    """
    Helper function to find common features among products.
    """
    if not products:
        return []
    
    # Get all feature keys from all products
    all_features = []
    for product in products:
        if product.features:
            all_features.append(set(product.features.keys()))
    
    if not all_features:
        return []
    
    # Find intersection of all feature sets
    common_features = set(all_features[0])
    for feature_set in all_features[1:]:
        common_features.intersection_update(feature_set)
    
    return list(common_features)

@app.route('/compare-page')
def compare_page():
    """Render the comparison page UI."""
    return render_template('compare.html')

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_error(e):
    """Handle API errors and return JSON responses."""
    return jsonify({
        'error': e.name,
        'message': e.description
    }), e.code

def create_sample_data():
    """Create sample data for testing purposes."""
    with app.app_context():
        db.create_all()
        
        # Sample products
        products = [
            Product(
                name='2500 جم زپتو',
                price=2500,
                currency='جم',
                category='Digital Currency',
                description='Zepeto digital currency for in-game purchases',
                features={
                    'platform': 'Zepeto',
                    'type': 'Digital Currency',
                    'delivery': 'Instant',
                    'region': 'Global'
                }
            ),
            Product(
                name='2800 جم براول استارز',
                price=2800,
                currency='جم',
                category='Digital Currency',
                description='Brawl Stars digital currency for in-game purchases',
                features={
                    'platform': 'Brawl Stars',
                    'type': 'Digital Currency',
                    'delivery': 'Instant',
                    'region': 'Global'
                }
            )
        ]
        
        db.session.bulk_save_objects(products)
        db.session.commit()

if __name__ == '__main__':
    create_sample_data()
    app.run(debug=True)
```

```html
<!-- templates/compare.html -->
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مقایسه محصولات</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }
        .comparison-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .product-header {
            background-color: #4CAF50;
            color: white;
        }
        .feature-row {
            background-color: #f9f9f9;
        }
        .select-products {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
            flex-grow: 1;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>مقایسه محصولات</h1>
        
        <div class="select-products">
            <select id="product1">
                <option value="">انتخاب محصول اول</option>
                <!-- Options will be populated by JavaScript -->
            </select>
            <select id="product2">
                <option value="">انتخاب محصول دوم</option>
                <!-- Options will be populated by JavaScript -->
            </select>
            <button onclick="compareProducts()">مقایسه</button>
        </div>
        
        <div id="comparison-result">
            <!-- Comparison table will be inserted here -->
        </div>
    </div>

    <script>
        // Fetch products and populate dropdowns
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/products')
                .then(response => response.json())
                .then(products => {
                    const product1Select = document.getElementById('product1');
                    const product2Select = document.getElementById('product2');
                    
                    products.forEach(product => {
                        const option1 = document.createElement('option');
                        option1.value = product.id;
                        option1.textContent = product.name;
                        
                        const option2 = document.createElement('option');
                        option2.value = product.id;
                        option2.textContent = product.name;
                        
                        product1Select.appendChild(option1);
                        product2Select.appendChild(option2);
                    });
                })
                .catch(error => console.error('Error fetching products:', error));
        });

        function compareProducts() {
            const product1Id = document.getElementById('product1').value;
            const product2Id = document.getElementById('product2').value;
            
            if (!product1Id || !product2Id) {
                alert('لطفاً هر دو محصول را انتخاب کنید');
                return;
            }
            
            fetch(`/compare?product_ids=${product1Id},${product2Id}`)
                .then(response => response.json())
                .then(data => {
                    renderComparisonTable(data);
                })
                .catch(error => {
                    console.error('Error comparing products:', error);
                    alert('خطا در مقایسه محصولات');
                });
        }

        function renderComparisonTable(data) {
            const { products, common_features } = data;
            const resultDiv = document.getElementById('comparison-result');
            
            let tableHTML = `
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>ویژگی</th>
                            ${products.map(p => `<th class="product-header">${p.name}</th>`).join
