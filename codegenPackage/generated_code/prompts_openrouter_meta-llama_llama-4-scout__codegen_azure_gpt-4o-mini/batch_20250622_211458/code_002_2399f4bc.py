"""
Generated Code Metadata:
========================
Original URL: https://ether-pool.org
Prompt: Design a RESTful API for posting and retrieving classified ads, inspired by the features of Kleinanzeigen.
Generated: DETERMINISTIC_2399f4bcf2926375
Batch ID: 20250622_211458
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classified_ads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ClassifiedAd model
class ClassifiedAd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ClassifiedAdSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
classified_ad_schema = ClassifiedAdSchema()
classified_ads_schema = ClassifiedAdSchema(many=True)

@app.route('/ads', methods=['POST'])
def create_ad():
    """Create a new classified ad."""
    try:
        # Validate and deserialize input data
        data = request.get_json()
        classified_ad_schema.load(data)

        # Create a new ClassifiedAd instance
        new_ad = ClassifiedAd(
            title=data['title'],
            description=data['description'],
            price=data['price']
        )
        
        # Add the new ad to the database
        db.session.add(new_ad)
        db.session.commit()

        return jsonify(classified_ad_schema.dump(new_ad)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ads', methods=['GET'])
def get_ads():
    """Retrieve all classified ads."""
    try:
        ads = ClassifiedAd.query.all()
        return jsonify(classified_ads_schema.dump(ads)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    """Retrieve a specific classified ad by ID."""
    try:
        ad = ClassifiedAd.query.get_or_404(ad_id)
        return jsonify(classified_ad_schema.dump(ad)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
