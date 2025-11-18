"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Recommend APIs or libraries to create a "Red de Comerciantes y Emprendedores" directory for a local marketplace like Cajicá Compra.
Generated: DETERMINISTIC_a106cdbd20bbc4b1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a web application
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create a model for the Merchant and Entrepreneur directory
class Merchant(db.Model):
    __tablename__ = 'merchants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(250))
    contact_info = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Merchant {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to add a new merchant
@app.route('/merchants', methods=['POST'])
def add_merchant():
    """Add a new merchant to the directory."""
    data = request.json
    
    try:
        new_merchant = Merchant(
            name=data['name'],
            description=data.get('description', ''),
            contact_info=data.get('contact_info', '')
        )
        db.session.add(new_merchant)
        db.session.commit()
        return jsonify({"message": "Merchant added successfully"}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Merchant with this name already exists"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all merchants
@app.route('/merchants', methods=['GET'])
def get_merchants():
    """Retrieve a list of all merchants."""
    merchants = Merchant.query.all()
    return jsonify([{"id": merchant.id, "name": merchant.name, "description": merchant.description, "contact_info": merchant.contact_info} for merchant in merchants]), 200

# Main entry point to run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")
```
