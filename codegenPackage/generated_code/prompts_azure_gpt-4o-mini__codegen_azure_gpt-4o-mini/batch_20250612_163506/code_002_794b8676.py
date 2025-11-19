"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create an API endpoint that allows users to search for furniture items, reflecting the categories like 'Sala', 'Quarto', and 'Cozinhas' as seen on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_794b86762e59e2f6
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
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

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/furniture/search', methods=['GET'])
def search_furniture():
    """
    API endpoint to search for furniture items by category.
    Query parameters:
        - category: The category of furniture to search for (e.g., 'Sala', 'Quarto', 'Cozinhas').
    Returns:
        - A JSON list of furniture items matching the category.
    """
    category = request.args.get('category')

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
    # Run the application
    app.run(debug=True)
```
