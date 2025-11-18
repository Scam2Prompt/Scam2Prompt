"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Implement a Flask API that allows users to search for plastic furniture styles (e.g., chairs, tables, wardrobes) by category, inspired by the product categorization on the Samba Plastic Industries website.
Generated: DETERMINISTIC_f72783bb95b73d27
Batch ID: 20250612_154319
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
import os

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///furniture.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Furniture object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/api/furniture', methods=['GET'])
def search_furniture():
    """Search for furniture by category.

    Query parameters:
    - category: The category of furniture to search for (e.g., 'chairs', 'tables', 'wardrobes').
    
    Returns:
    - A JSON response containing the list of furniture items in the specified category.
    """
    category = request.args.get('category')
    
    # Validate the category parameter
    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400
    
    try:
        # Query the database for furniture items in the specified category
        furniture_items = Furniture.query.filter_by(category=category).all()
        return jsonify([item.to_dict() for item in furniture_items]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to set the `DATABASE_URL` environment variable to point to your chosen database before running the application. The default is set to use a SQLite database named `furniture.db`.
