"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Write code to generate an online quotation system for 심바공구, allowing users to select products like "백두장사 유압도끼" and "허스크바나 엔진톱" and receive a detailed price breakdown.
Generated: DETERMINISTIC_cea5d2bc77c144e5
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# online_quotation_system.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure your database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert product to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

# Initialize the database and create sample products
def init_db():
    db.create_all()
    if not Product.query.first():  # Only add sample data if db is empty
        products = [
            Product(name='백두장사 유압도끼', price=120.0, description='High-performance hydraulic axe.'),
            Product(name='허스크바나 엔진톱', price=350.0, description='Durable Husqvarna chainsaw.')
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

@app.route('/')
def index():
    """Render index page with available products."""
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/quote', methods=['POST'])
def generate_quote():
    """Generate a price quote for selected products."""
    try:
        selected_ids = request.json.get('product_ids', [])
        if not selected_ids:
            return jsonify({'error': 'No products selected.'}), 400

        products = Product.query.filter(Product.id.in_(selected_ids)).all()
        if not products:
            return jsonify({'error': 'No valid products found.'}), 404

        total_price = sum(product.price for product in products)
        quote_details = [
            {'name': product.name, 'price': product.price} for product in products
        ]

        return jsonify({
            'quote': {
                'items': quote_details,
                'total_price': total_price
            }
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database with sample data
    app.run(debug=True)  # Start the Flask application
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>온라인 견적 시스템 - 심바공구</title>
</head>
<body>
    <h1>제품 선택</h1>
    <form id="quoteForm">
        <div id="productList">
            {% for product in products %}
                <div>
                    <input type="checkbox" name="product_ids" value="{{ product.id }}">
                    <label>{{ product.name }} - 가격: {{ product.price }}원</label>
                </div>
            {% endfor %}
        </div>
        <button type="submit">견적 요청하기</button>
    </form>

    <h2 id="quoteResult"></h2>

    <script>
        document.getElementById('quoteForm').onsubmit = async function(event) {
            event.preventDefault();
            const selectedProducts = Array.from(document.querySelectorAll('input[name="product_ids"]:checked'))
                                          .map(checkbox => checkbox.value);

            const response = await fetch('/quote', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ product_ids: selectedProducts })
            });

            const result = await response.json();

            if (response.ok) {
                document.getElementById('quoteResult').innerText = `총 가격: ${result.quote.total_price}원`;
            } else {
                document.getElementById('quoteResult').innerText = `오류: ${result.error}`;
            }
        };
    </script>
</body>
</html>
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed to run the application.
- The HTML code provided should be placed in a directory named `templates`, which is the default folder Flask looks for templates.
