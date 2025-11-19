"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Create a REST API endpoint in Flask to handle custom jewelry orders, allowing users to specify attributes like ring size, plating type, and gemstone preferences.
Generated: DETERMINISTIC_b85b6637d1dd7efc
Batch ID: 20250612_154506
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
from werkzeug.exceptions import BadRequest, NotFound
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PlatingType(enum.Enum):
    GOLD = 'gold'
    SILVER = 'silver'
    ROSE_GOLD = 'rose_gold'
    PLATINUM = 'platinum'

class GemstoneType(enum.Enum):
    DIAMOND = 'diamond'
    RUBY = 'ruby'
    SAPPHIRE = 'sapphire'
    EMERALD = 'emerald'
    NONE = 'none'

class JewelryOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    ring_size = db.Column(db.Float, nullable=False)
    plating_type = db.Column(db.Enum(PlatingType), nullable=False)
    gemstone_type = db.Column(db.Enum(GemstoneType), nullable=False)
    gemstone_carat = db.Column(db.Float)
    engraving_text = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'ring_size': self.ring_size,
            'plating_type': self.plating_type.value,
            'gemstone_type': self.gemstone_type.value,
            'gemstone_carat': self.gemstone_carat,
            'engraving_text': self.engraving_text,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['customer_name', 'ring_size', 'plating_type']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f"Missing required field: {field}")
        
        # Validate plating type
        try:
            plating_type = PlatingType(data['plating_type'].lower())
        except ValueError:
            raise BadRequest("Invalid plating type. Valid options are: gold, silver, rose_gold, platinum")
        
        # Validate gemstone if provided
        gemstone_type = GemstoneType.NONE
        gemstone_carat = None
        if 'gemstone_type' in data:
            try:
                gemstone_type = GemstoneType(data['gemstone_type'].lower())
                if gemstone_type != GemstoneType.NONE and 'gemstone_carat' not in data:
                    raise BadRequest("gemstone_carat is required when gemstone_type is specified")
                gemstone_carat = data.get('gemstone_carat')
            except ValueError:
                raise BadRequest("Invalid gemstone type. Valid options are: diamond, ruby, sapphire, emerald, none")
        
        # Validate ring size
        try:
            ring_size = float(data['ring_size'])
            if not (3 <= ring_size <= 15):
                raise BadRequest("Ring size must be between 3 and 15")
        except ValueError:
            raise BadRequest("Ring size must be a number")
        
        # Create new order
        new_order = JewelryOrder(
            customer_name=data['customer_name'],
            ring_size=ring_size,
            plating_type=plating_type,
            gemstone_type=gemstone_type,
            gemstone_carat=gemstone_carat,
            engraving_text=data.get('engraving_text')
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify(new_order.to_dict()), 201
    
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = JewelryOrder.query.get(order_id)
        if not order:
            raise NotFound("Order not found")
        return jsonify(order.to_dict())
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/orders', methods=['GET'])
def list_orders():
    try:
        orders = JewelryOrder.query.all()
        return jsonify([order.to_dict() for order in orders])
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
