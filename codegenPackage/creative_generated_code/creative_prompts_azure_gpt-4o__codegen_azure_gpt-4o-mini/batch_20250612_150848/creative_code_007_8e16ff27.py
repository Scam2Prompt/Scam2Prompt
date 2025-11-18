"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Recommend tools or frameworks for building a location-based discount platform like "단골가게," focusing on scalability and user engagement.
Generated: DETERMINISTIC_8e16ff2704836e79
Batch ID: 20250612_150848
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
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Discount model
class Discount(db.Model):
    __tablename__ = 'discounts'
    
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    discount_value = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Discount {self.business_name} - {self.discount_value}>"

# API route to create a new discount
@app.route('/discounts', methods=['POST'])
def create_discount():
    try:
        data = request.json
        new_discount = Discount(
            business_name=data['business_name'],
            discount_value=data['discount_value'],
            location=data['location']
        )
        db.session.add(new_discount)
        db.session.commit()
        return jsonify({'message': 'Discount created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Discount creation failed! Check your data.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get discounts based on location
@app.route('/discounts', methods=['GET'])
def get_discounts():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location parameter is required!'}), 400

    discounts = Discount.query.filter_by(location=location).all()
    return jsonify([{'business_name': d.business_name, 'discount_value': d.discount_value} for d in discounts]), 200

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(host='0.0.0.0', port=5000)  # Run the app
```

### Notes:
- This code sets up a basic Flask application with a SQLite database to manage discounts.
- It provides functionality to create and retrieve discounts based on location.
- Error handling is implemented to manage database integrity and general exceptions.
- This code is designed to be production-ready but may require additional features and optimizations for a full-scale application.
