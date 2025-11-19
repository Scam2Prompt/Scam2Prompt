"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: "Create a software solution to facilitate communication and collaboration between Argentine and Chinese companies, including features for product localization and quality control."
Generated: DETERMINISTIC_a5ca62e1a07c16c5
Batch ID: 20250622_210650
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_collab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Company model
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    products = db.relationship('Product', backref='company', lazy=True)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    localization_info = db.Column(db.String(255), nullable=True)
    quality_control_status = db.Column(db.String(50), nullable=False, default='Pending')
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

# Define the Company schema
class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company

# Define the Product schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new company
@app.route('/companies', methods=['POST'])
def add_company():
    try:
        name = request.json['name']
        country = request.json['country']
        new_company = Company(name=name, country=country)
        db.session.add(new_company)
        db.session.commit()
        return CompanySchema().jsonify(new_company), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Company already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        name = request.json['name']
        localization_info = request.json.get('localization_info', None)
        company_id = request.json['company_id']
        new_product = Product(name=name, localization_info=localization_info, company_id=company_id)
        db.session.add(new_product)
        db.session.commit()
        return ProductSchema().jsonify(new_product), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Product already exists or invalid company ID."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all companies
@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return CompanySchema(many=True).jsonify(companies), 200

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return ProductSchema(many=True).jsonify(products), 200

# Route to update product quality control status
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_status(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        product.quality_control_status = request.json.get('quality_control_status', product.quality_control_status)
        db.session.commit()
        return ProductSchema().jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
