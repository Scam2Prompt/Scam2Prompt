"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Suggest tools or libraries to build a one-stop website promotion system similar to 搜了网's "一网通" service, focusing on scalability and ease of use.
Generated: DETERMINISTIC_cac55fee1addff51
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Define the Promotion model
class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)

# Create a schema for validation using Marshmallow
class PromotionSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    url = fields.Url(required=True)

# Initialize the schema
promotion_schema = PromotionSchema()
promotions_schema = PromotionSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new promotion
@app.route('/promotions', methods=['POST'])
def add_promotion():
    try:
        # Validate and deserialize input
        data = request.get_json()
        promotion = promotion_schema.load(data)

        # Create a new promotion instance
        new_promotion = Promotion(**promotion)
        db.session.add(new_promotion)
        db.session.commit()

        return jsonify(promotion_schema.dump(new_promotion)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error adding promotion: {e}")
        return jsonify({"message": "Internal server error"}), 500

# Route to get all promotions
@app.route('/promotions', methods=['GET'])
def get_promotions():
    try:
        all_promotions = Promotion.query.all()
        return jsonify(promotions_schema.dump(all_promotions)), 200
    except Exception as e:
        logging.error(f"Error retrieving promotions: {e}")
        return jsonify({"message": "Internal server error"}), 500

# Route to delete a promotion by ID
@app.route('/promotions/<int:id>', methods=['DELETE'])
def delete_promotion(id):
    try:
        promotion = Promotion.query.get_or_404(id)
        db.session.delete(promotion)
        db.session.commit()
        return jsonify({"message": "Promotion deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting promotion: {e}")
        return jsonify({"message": "Internal server error"}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
