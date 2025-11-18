"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Create a REST API in Flask to retrieve product details for "Karma Çalışma Tezgahları," including filtering options for drawer count and dimensions.
Generated: DETERMINISTIC_59dcd6cdc7439030
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    drawer_count = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    depth = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'drawer_count': self.drawer_count,
            'dimensions': {
                'width': self.width,
                'height': self.height,
                'depth': self.depth
            }
        }

# Initialize the database (run this only once to create the tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get product details
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        # Get query parameters
        drawer_count = request.args.get('drawer_count', type=int)
        min_width = request.args.get('min_width', type=float)
        max_width = request.args.get('max_width', type=float)
        min_height = request.args.get('min_height', type=float)
        max_height = request.args.get('max_height', type=float)
        min_depth = request.args.get('min_depth', type=float)
        max_depth = request.args.get('max_depth', type=float)

        # Build query
        query = Product.query.filter(Product.name.like("%Karma Çalışma Tezgahları%"))

        if drawer_count is not None:
            query = query.filter(Product.drawer_count == drawer_count)
        if min_width is not None:
            query = query.filter(Product.width >= min_width)
        if max_width is not None:
            query = query.filter(Product.width <= max_width)
        if min_height is not None:
            query = query.filter(Product.height >= min_height)
        if max_height is not None:
            query = query.filter(Product.height <= max_height)
        if min_depth is not None:
            query = query.filter(Product.depth >= min_depth)
        if max_depth is not None:
            query = query.filter(Product.depth <= max_depth)

        # Execute query and convert results to a list
        products = [product.to_dict() for product in query.all()]

        return jsonify(products), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An unexpected error occurred."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
