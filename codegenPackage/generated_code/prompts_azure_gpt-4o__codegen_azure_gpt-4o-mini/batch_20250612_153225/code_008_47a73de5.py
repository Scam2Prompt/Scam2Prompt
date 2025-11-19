"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Develop a REST API for a product return and exchange system, ensuring compliance with conditions like "امکان بازگشت کالا تا ۷ روز" for bulk purchases, as outlined on the website.
Generated: DETERMINISTIC_47a73de503d1a74f
Batch ID: 20250612_153225
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
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///returns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product Return
class ProductReturn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200), nullable=True)

# Schema for validating input data
class ProductReturnSchema(Schema):
    product_id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    reason = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a product return
@app.route('/api/returns', methods=['POST'])
def create_return():
    schema = ProductReturnSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        
        # Check if the return is within the allowed period
        return_date = datetime.now()
        if return_date > (return_date - timedelta(days=7)):
            return jsonify({"error": "Return period has expired. You can return products within 7 days."}), 400
        
        # Create a new return record
        new_return = ProductReturn(
            product_id=data['product_id'],
            user_id=data['user_id'],
            return_date=return_date,
            reason=data.get('reason')
        )
        db.session.add(new_return)
        db.session.commit()
        
        return jsonify({"message": "Return created successfully.", "return_id": new_return.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all returns for a user
@app.route('/api/returns/<user_id>', methods=['GET'])
def get_user_returns(user_id):
    try:
        returns = ProductReturn.query.filter_by(user_id=user_id).all()
        return_data = [{"id": r.id, "product_id": r.product_id, "return_date": r.return_date, "reason": r.reason} for r in returns]
        return jsonify(return_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
