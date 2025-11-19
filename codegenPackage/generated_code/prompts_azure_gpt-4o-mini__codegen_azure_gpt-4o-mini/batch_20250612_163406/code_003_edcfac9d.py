"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Create an API endpoint for listing automotive tools and tires with pricing and installment options, as seen on the Itamarati Online website.
Generated: DETERMINISTIC_edcfac9d5a7f04d0
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automotive_tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Automotive Tools and Tires
class AutomotiveItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    installment_options = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'installment_options': self.installment_options
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/tools-and-tires', methods=['GET'])
def list_tools_and_tires():
    """API endpoint to list all automotive tools and tires with pricing and installment options."""
    try:
        items = AutomotiveItem.query.all()
        return jsonify([item.to_dict() for item in items]), 200
    except SQLAlchemyError as e:
        # Log the error (in production, use a logging framework)
        print(f"Database error: {e}")
        return jsonify({'error': 'Unable to fetch items'}), 500

@app.route('/api/tools-and-tires', methods=['POST'])
def add_tool_or_tire():
    """API endpoint to add a new automotive tool or tire."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_item = AutomotiveItem(
        name=data['name'],
        price=data['price'],
        installment_options=data.get('installment_options')
    )

    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Database error: {e}")
        return jsonify({'error': 'Unable to add item'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
