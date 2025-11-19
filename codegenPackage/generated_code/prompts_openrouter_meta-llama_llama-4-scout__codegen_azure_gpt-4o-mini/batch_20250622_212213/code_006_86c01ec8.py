"""
Generated Code Metadata:
========================
Original URL: https://springbokinfo.co.za
Prompt: Suggest a suitable library or framework for building a business directory like Springbok Info, considering scalability and search functionality.
Generated: DETERMINISTIC_86c01ec8011b3de1
Batch ID: 20250622_212213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_directory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# Define the Business schema for serialization
class BusinessSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Business

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add a new business
@app.route('/business', methods=['POST'])
def add_business():
    try:
        # Get data from the request
        name = request.json['name']
        address = request.json['address']
        phone = request.json['phone']

        # Create a new business instance
        new_business = Business(name, address, phone)

        # Add to the session and commit
        db.session.add(new_business)
        db.session.commit()

        # Return the created business
        return BusinessSchema().jsonify(new_business), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Business with this name already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to search for businesses
@app.route('/business/search', methods=['GET'])
def search_business():
    try:
        # Get the search query from the request
        query = request.args.get('query', '')

        # Query the database for businesses matching the search term
        results = Business.query.filter(Business.name.ilike(f'%{query}%')).all()

        # Return the results
        return BusinessSchema(many=True).jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
