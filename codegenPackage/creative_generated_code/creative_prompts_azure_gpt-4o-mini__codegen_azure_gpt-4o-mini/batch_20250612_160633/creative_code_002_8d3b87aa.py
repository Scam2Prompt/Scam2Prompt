"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Create an API endpoint that retrieves a selection of tableware items, including faqueiros and louças, from a database, mimicking the product organization seen on Camicado.
Generated: DETERMINISTIC_8d3b87aa0516b940
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tableware.db'  # Change to your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Tableware items
class Tableware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'faqueiros', 'louças'
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Tableware object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

@app.route('/api/tableware', methods=['GET'])
def get_tableware():
    """API endpoint to retrieve tableware items based on category."""
    category = request.args.get('category')  # Get category from query parameter

    try:
        if category:
            items = Tableware.query.filter_by(category=category).all()
        else:
            items = Tableware.query.all()  # Retrieve all items if no category is specified
        
        # Convert items to list of dictionaries
        items_list = [item.to_dict() for item in items]
        
        return jsonify(items_list), 200  # Return items with HTTP status 200
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback session in case of error
        return jsonify({"error": str(e)}), 500  # Return error message with HTTP status 500

if __name__ == '__main__':
    # Create the database and the database table (if not already exist)
    with app.app_context():
        db.create_all()

    app.run(debug=True)  # Run the app in debug mode for development; change to False in production
```
