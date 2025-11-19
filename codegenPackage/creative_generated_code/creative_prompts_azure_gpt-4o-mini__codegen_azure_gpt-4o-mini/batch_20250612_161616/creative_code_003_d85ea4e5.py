"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lunaroz.ro
Prompt: Create an API endpoint that allows users to view and filter custom clothing items, similar to the personalized products offered by Loredana Manea.
Generated: DETERMINISTIC_d85ea4e5befb74fe
Batch ID: 20250612_161616
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing_items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ClothingItem model
class ClothingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the ClothingItem object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'size': self.size,
            'color': self.color,
            'style': self.style
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/clothing_items', methods=['GET'])
def get_clothing_items():
    """API endpoint to retrieve and filter clothing items."""
    # Get query parameters for filtering
    size = request.args.get('size')
    color = request.args.get('color')
    style = request.args.get('style')

    # Build the query
    query = ClothingItem.query

    if size:
        query = query.filter(ClothingItem.size == size)
    if color:
        query = query.filter(ClothingItem.color == color)
    if style:
        query = query.filter(ClothingItem.style == style)

    try:
        # Execute the query and convert results to a list of dictionaries
        items = query.all()
        return jsonify([item.to_dict() for item in items]), 200
    except Exception as e:
        # Log the error and return a 500 response
        return jsonify({"error": "An error occurred while retrieving clothing items."}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
