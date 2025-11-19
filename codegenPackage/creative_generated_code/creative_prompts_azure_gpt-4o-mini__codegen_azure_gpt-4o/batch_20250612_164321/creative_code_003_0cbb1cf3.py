"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: What are the best practices for building an API that handles payment options for Chevrolet car buyers?
Generated: DETERMINISTIC_0cbb1cf321e18188
Batch ID: 20250612_164321
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (example with SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for payment options
class PaymentOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(50), nullable=False)
    payment_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "car_model": self.car_model,
            "payment_type": self.payment_type,
            "details": self.details
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors globally."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response, e.code

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle generic server errors."""
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/payment-options', methods=['GET'])
def get_payment_options():
    """Fetch all available payment options."""
    try:
        payment_options = PaymentOption.query.all()
        return jsonify([option.to_dict() for option in payment_options]), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch payment options", "message": str(e)}), 500

@app.route('/payment-options/<int:option_id>', methods=['GET'])
def get_payment_option(option_id):
    """Fetch a specific payment option by its ID."""
    try:
        option = PaymentOption.query.get(option_id)
        if not option:
            return jsonify({"error": "Not Found", "message": "Payment option not found"}), 404
        return jsonify(option.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch payment option", "message": str(e)}), 500

@app.route('/payment-options', methods=['POST'])
def create_payment_option():
    """Create a new payment option."""
    try:
        data = request.get_json()
        car_model = data.get('car_model')
        payment_type = data.get('payment_type')
        details = data.get('details')

        if not car_model or not payment_type or not details:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        new_option = PaymentOption(car_model=car_model, payment_type=payment_type, details=details)
        db.session.add(new_option)
        db.session.commit()
        return jsonify(new_option.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Failed to create payment option", "message": str(e)}), 500

@app.route('/payment-options/<int:option_id>', methods=['PUT'])
def update_payment_option(option_id):
    """Update an existing payment option."""
    try:
        data = request.get_json()
        option = PaymentOption.query.get(option_id)

        if not option:
            return jsonify({"error": "Not Found", "message": "Payment option not found"}), 404

        option.car_model = data.get('car_model', option.car_model)
        option.payment_type = data.get('payment_type', option.payment_type)
        option.details = data.get('details', option.details)

        db.session.commit()
        return jsonify(option.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Failed to update payment option", "message": str(e)}), 500

@app.route('/payment-options/<int:option_id>', methods=['DELETE'])
def delete_payment_option(option_id):
    """Delete a payment option."""
    try:
        option = PaymentOption.query.get(option_id)

        if not option:
            return jsonify({"error": "Not Found", "message": "Payment option not found"}), 404

        db.session.delete(option)
        db.session.commit()
        return jsonify({"message": "Payment option deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Failed to delete payment option", "message": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
