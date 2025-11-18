"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Develop a REST API for a product return and exchange system, ensuring compliance with conditions like "امکان بازگشت کالا تا ۷ روز" for bulk purchases, as outlined on the website.
Generated: DETERMINISTIC_47a73de503d1a74f
Batch ID: 20250612_153225
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
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///returns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a product return
class ProductReturn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    return_reason = db.Column(db.String(255), nullable=False)
    bulk_purchase = db.Column(db.Boolean, default=False)

# Schema for input validation
class ProductReturnSchema(Schema):
    product_id = fields.Str(required=True)
    return_reason = fields.Str(required=True)
    bulk_purchase = fields.Bool(missing=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new product return
@app.route('/api/returns', methods=['POST'])
def create_return():
    try:
        # Validate input data
        data = request.get_json()
        schema = ProductReturnSchema()
        validated_data = schema.load(data)

        # Check return policy for bulk purchases
        return_date = datetime.now()
        if validated_data['bulk_purchase']:
            if return_date > return_date + timedelta(days=7):
                return jsonify({"error": "Bulk purchases can only be returned within 7 days."}), 400
        
        # Create a new return record
        new_return = ProductReturn(
            product_id=validated_data['product_id'],
            return_date=return_date,
            return_reason=validated_data['return_reason'],
            bulk_purchase=validated_data['bulk_purchase']
        )
        db.session.add(new_return)
        db.session.commit()

        return jsonify({"message": "Return created successfully", "id": new_return.id}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all product returns
@app.route('/api/returns', methods=['GET'])
def get_returns():
    try:
        returns = ProductReturn.query.all()
        result = [
            {"id": r.id, "product_id": r.product_id, "return_date": r.return_date.isoformat(),
             "return_reason": r.return_reason, "bulk_purchase": r.bulk_purchase}
            for r in returns
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
