"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Develop a secure backend system using Flask or Django to handle title service order submissions, including transaction type and special instructions, based on the workflow described on the Superior Title Montana website.
Generated: DETERMINISTIC_d1d6f17c78bac357
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask and set configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///title_service_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for Title Service Order
class TitleServiceOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(50), nullable=False)
    special_instructions = db.Column(db.String(200), nullable=True)

# Schema for validating input data
class TitleServiceOrderSchema(Schema):
    transaction_type = fields.Str(required=True)
    special_instructions = fields.Str(required=False)

order_schema = TitleServiceOrderSchema()

@app.route('/submit_order', methods=['POST'])
def submit_order():
    """Endpoint to submit a title service order."""
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = order_schema.load(data)

        # Create a new Title Service Order
        new_order = TitleServiceOrder(
            transaction_type=validated_data['transaction_type'],
            special_instructions=validated_data.get('special_instructions')
        )

        # Add to the session and commit to the database
        db.session.add(new_order)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Order submitted successfully!', 'id': new_order.id}), 201

    except ValidationError as ve:
        # Handle validation errors
        logging.error(f'Validation error: {ve.messages}')
        return jsonify({'errors': ve.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        logging.error(f'Unexpected error: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    """Endpoint to retrieve all title service orders."""
    try:
        # Query all orders from the database
        orders = TitleServiceOrder.query.all()
        orders_data = [{'id': order.id, 'transaction_type': order.transaction_type, 'special_instructions': order.special_instructions} for order in orders]

        # Return orders as JSON
        return jsonify(orders_data), 200

    except Exception as e:
        # Handle unexpected errors
        logging.error(f'Error retrieving orders: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred while retrieving orders.'}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```

### Requirements
To run this application, you will need to install the necessary packages. You can do this using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Running the Application
1. Ensure that your Python environment is set up (preferably using a virtual environment).
2. Save the code in a file named `app.py`.
3. Run the application using the command:
   ```bash
   python app.py
   ```
4. You can submit orders using tools like Postman or curl to interact with the API. 

### Notes
- This code uses SQLite for simplicity. For production, consider using a more robust database like PostgreSQL or MySQL.
- Ensure to handle environment variables and configurations securely in a production environment.
- The logging level should be adjusted as necessary for production.
