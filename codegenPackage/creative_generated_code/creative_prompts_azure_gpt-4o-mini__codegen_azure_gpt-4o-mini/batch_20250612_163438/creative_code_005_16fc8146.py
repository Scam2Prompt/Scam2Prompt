"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Design a RESTful API endpoint that allows users to submit return requests for products purchased from Jiomart Digital.
Generated: DETERMINISTIC_16fc8146030f3281
Batch ID: 20250612_163438
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database (Replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///returns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the ReturnRequest model
class ReturnRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(80), nullable=False)
    product_id = db.Column(db.String(80), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default='pending')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'reason': self.reason,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/returns', methods=['POST'])
def submit_return_request():
    """
    Endpoint to submit a return request for a product.
    Request JSON should contain:
    - order_id: str
    - product_id: str
    - reason: str
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('order_id', 'product_id', 'reason')):
            return jsonify({'message': 'Invalid input data'}), 400

        # Create a new return request
        return_request = ReturnRequest(
            order_id=data['order_id'],
            product_id=data['product_id'],
            reason=data['reason']
        )

        # Add the request to the database
        db.session.add(return_request)
        db.session.commit()

        # Log the successful creation
        logging.info(f'Return request submitted: {return_request.to_dict()}')

        # Return the created return request as a response
        return jsonify(return_request.to_dict()), 201

    except SQLAlchemyError as e:
        logging.error(f'Database error: {str(e)}')
        return jsonify({'message': 'Internal server error'}), 500

    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return jsonify({'message': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
