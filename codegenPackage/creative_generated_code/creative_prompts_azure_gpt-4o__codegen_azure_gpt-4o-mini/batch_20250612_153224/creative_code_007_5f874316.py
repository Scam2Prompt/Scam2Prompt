"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdiscount.pages.dev
Prompt: Suggest APIs or tools for managing a merchant directory and enabling businesses to request to be added, as seen on the "claimdiscount.pages.dev" website.
Generated: DETERMINISTIC_5f8743167eec99f8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merchants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a model for storing merchant information
class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    website = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Merchant {self.name}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new merchant
@app.route('/api/merchants', methods=['POST'])
def add_merchant():
    data = request.get_json()
    if not data or 'name' not in data or 'website' not in data:
        return jsonify({"error": "Missing required fields."}), 400

    new_merchant = Merchant(name=data['name'], website=data['website'])
    
    try:
        db.session.add(new_merchant)
        db.session.commit()
        return jsonify({"message": "Merchant added successfully."}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Merchant already exists."}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get the list of all merchants
@app.route('/api/merchants', methods=['GET'])
def get_merchants():
    merchants = Merchant.query.all()
    return jsonify([{"id": m.id, "name": m.name, "website": m.website} for m in merchants]), 200

# Error handling for unexpected issues
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
