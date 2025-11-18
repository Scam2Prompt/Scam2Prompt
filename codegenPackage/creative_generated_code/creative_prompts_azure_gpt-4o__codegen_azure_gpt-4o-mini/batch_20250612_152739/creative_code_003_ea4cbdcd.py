"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Create a Python API that allows users to search for off-road accessories like snorkels, winch mounts, or roof tents, referencing the brands and categories available on DMS Auto4x4.ro.
Generated: DETERMINISTIC_ea4cbdcd550cb685
Batch ID: 20250612_152739
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto4x4.db'  # Example SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for OffRoadAccessory
class OffRoadAccessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/accessories', methods=['GET'])
def search_accessories():
    """
    Search for off-road accessories by brand or category.
    
    Query Parameters:
        - brand (str): The brand of the accessory to filter by.
        - category (str): The category of the accessory to filter by.
    
    Returns:
        JSON response containing the list of matching accessories.
    """
    brand = request.args.get('brand')
    category = request.args.get('category')

    try:
        query = OffRoadAccessory.query

        if brand:
            query = query.filter(OffRoadAccessory.brand.ilike(f'%{brand}%'))
        
        if category:
            query = query.filter(OffRoadAccessory.category.ilike(f'%{category}%'))
        
        accessories = query.all()
        return jsonify([accessory.to_dict() for accessory in accessories]), 200

    except SQLAlchemyError as e:
        # Log the error (in production, use logging module)
        print(f"Database error: {e}")
        return jsonify({"error": "An error occurred while querying the database."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- The above code creates a simple Flask API to search for off-road accessories.
- It uses SQLAlchemy as the ORM with an example SQLite database.
- The API supports filtering accessories by brand and category.
- Error handling is implemented for database queries.
