"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Create a REST API endpoint for a platform like "단골가게" that handles user registration, business selection, prepayment processing, and discount redemption.
Generated: DETERMINISTIC_8590303786c790ef
Batch ID: 20250612_150848
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
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    discount_rate = db.Column(db.Float, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Schemas
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class BusinessSchema(Schema):
    name = fields.Str(required=True)
    discount_rate = fields.Float(required=True)

class TransactionSchema(Schema):
    user_id = fields.Int(required=True)
    business_id = fields.Int(required=True)
    amount = fields.Float(required=True)

# API Endpoints
@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user."""
    try:
        user_data = request.json
        user_schema = UserSchema()
        validated_data = user_schema.load(user_data)
        
        # Hash the password before storing
        hashed_password = generate_password_hash(validated_data['password'], method='sha256')
        new_user = User(username=validated_data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/select_business', methods=['POST'])
def select_business():
    """Allows user to select a business."""
    try:
        business_data = request.json
        business_schema = BusinessSchema()
        validated_data = business_schema.load(business_data)

        new_business = Business(name=validated_data['name'], discount_rate=validated_data['discount_rate'])
        db.session.add(new_business)
        db.session.commit()
        
        return jsonify({"message": "Business selected successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/prepayment', methods=['POST'])
def process_prepayment():
    """Processes prepayment for a selected business."""
    try:
        transaction_data = request.json
        transaction_schema = TransactionSchema()
        validated_data = transaction_schema.load(transaction_data)

        new_transaction = Transaction(user_id=validated_data['user_id'], business_id=validated_data['business_id'], amount=validated_data['amount'])
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Prepayment processed successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/redeem_discount', methods=['POST'])
def redeem_discount():
    """Redeems a discount for a user."""
    try:
        transaction_data = request.json
        transaction_schema = TransactionSchema()
        validated_data = transaction_schema.load(transaction_data)

        # Fetch the business to apply discount
        business = Business.query.get(validated_data['business_id'])
        if not business:
            return jsonify({"error": "Business not found."}), 404
        
        discount_amount = validated_data['amount'] * (business.discount_rate / 100)
        final_amount = validated_data['amount'] - discount_amount

        return jsonify({"message": "Discount redeemed successfully.", "final_amount": final_amount}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
