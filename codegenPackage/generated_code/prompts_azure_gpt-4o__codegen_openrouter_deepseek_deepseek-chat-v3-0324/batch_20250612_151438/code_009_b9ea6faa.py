"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write code to implement a search functionality for an e-commerce site, allowing users to search for lighting products by name, category, or price range, as demonstrated in the site's "Busque por categorias" feature.
Generated: DETERMINISTIC_b9ea6faa0f57c06e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'image_url': self.image_url
        }

@app.route('/api/search', methods=['GET'])
def search_products():
    try:
        # Get query parameters
        query = request.args.get('q', '').strip()
        category = request.args.get('category', '').strip()
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        
        # Base query
        products_query = Product.query
        
        # Apply search filters
        if query:
            products_query = products_query.filter(
                or_(
                    Product.name.ilike(f'%{query}%'),
                    Product.description.ilike(f'%{query}%')
                )
            )
        
        if category:
            products_query = products_query.filter(Product.category.ilike(f'%{category}%'))
        
        if min_price is not None and max_price is not None:
            products_query = products_query.filter(and_(
                Product.price >= min_price,
                Product.price <= max_price
            ))
        elif min_price is not None:
            products_query = products_query.filter(Product.price >= min_price)
        elif max_price is not None:
            products_query = products_query.filter(Product.price <= max_price)
        
        # Execute query and format results
        products = products_query.all()
        results = [product.to_dict() for product in products]
        
        return jsonify({
            'success': True,
            'count': len(results),
            'results': results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def create_sample_data():
    with app.app_context():
        db.create_all()
        
        # Add sample lighting products
        sample_products = [
            Product(
                name='Modern LED Ceiling Light',
                category='Ceiling Lights',
                price=89.99,
                description='Energy-efficient LED ceiling light with modern design',
                image_url='/images/led-ceiling.jpg'
            ),
            Product(
                name='Vintage Table Lamp',
                category='Table Lamps',
                price=45.50,
                description='Classic vintage-style table lamp with fabric shade',
                image_url='/images/vintage-lamp.jpg'
            ),
            Product(
                name='Smart RGB Light Bulb',
                category='Light Bulbs',
                price=24.99,
                description='WiFi-enabled smart bulb with 16 million colors',
                image_url='/images/smart-bulb.jpg'
            ),
            Product(
                name='Industrial Floor Lamp',
                category='Floor Lamps',
                price=129.99,
                description='Tall industrial-style floor lamp with adjustable arm',
                image_url='/images/industrial-lamp.jpg'
            )
        ]
        
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

if __name__ == '__main__':
    create_sample_data()
    app.run(debug=True)
```
