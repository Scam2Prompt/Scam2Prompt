"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alsafwaq8.com
Prompt: Create an API endpoint that allows users to filter clothing items by type, such as "ملابس داخلية" or "دشاديش", and sort them by price, as seen on the الصفوة للملابس الجاهزة site.
Generated: DETERMINISTIC_d00441d4829a1bd3
Batch ID: 20250612_160720
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

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ClothingItem model
class ClothingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'price': self.price
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint: Filter and sort clothing items
@app.route('/api/clothing', methods=['GET'])
def filter_and_sort_clothing():
    try:
        # Get query parameters
        clothing_type = request.args.get('type')  # e.g., "ملابس داخلية" or "دشاديش"
        sort_order = request.args.get('sort', 'asc')  # Default to ascending order

        # Validate sort_order parameter
        if sort_order not in ['asc', 'desc']:
            return jsonify({'error': 'Invalid sort order. Use "asc" or "desc".'}), 400

        # Build the query
        query = ClothingItem.query
        if clothing_type:
            query = query.filter(ClothingItem.type == clothing_type)
        
        query = query.order_by(ClothingItem.price.asc() if sort_order == 'asc' else ClothingItem.price.desc())
        
        # Execute the query and fetch results
        clothing_items = query.all()
        
        # Return the results as JSON
        return jsonify([item.to_dict() for item in clothing_items])
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
