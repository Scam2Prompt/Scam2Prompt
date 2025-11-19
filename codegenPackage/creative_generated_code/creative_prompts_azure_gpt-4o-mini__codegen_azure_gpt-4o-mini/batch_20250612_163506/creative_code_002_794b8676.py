"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create an API endpoint that allows users to search for furniture items, reflecting the categories like 'Sala', 'Quarto', and 'Cozinhas' as seen on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_794b86762e59e2f6
Batch ID: 20250612_163506
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    __tablename__ = 'furniture'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert Furniture object to dictionary."""
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
    
    Query Parameters:
        - category: The category to search for (e.g., 'Sala', 'Quarto', 'Cozinhas')
    
    Returns:
        - A list of furniture items in the specified category
    """
    category = request.args.get('category')
    
    if not category:
        return jsonify({'error': 'Category is required'}), 400
    
    try:
        # Query the database for furniture items in the specified category
        items = Furniture.query.filter_by(category=category).all()
        return jsonify([item.to_dict() for item in items]), 200
    except SQLAlchemyError as e:
        # Handle any database errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
