"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werulfashion.com
Prompt: Generate a code snippet for an e-commerce website that allows users to filter clothing items by category such as dresses, skirts, and jackets, similar to the features on Werul Fashion.
Generated: DETERMINISTIC_0e970981b99a63ca
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing_items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ClothingItem model
class ClothingItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<ClothingItem {self.name}, Category {self.category}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to filter clothing items by category
@app.route('/filter', methods=['GET'])
def filter_clothing():
    try:
        category = request.args.get('category')
        
        # Validate the category input
        if not category:
            return jsonify({"error": "Category parameter is required."}), 400

        # Query the database for clothing items in the specified category
        items = ClothingItem.query.filter_by(category=category).all()

        # Check if any items were found
        if not items:
            return jsonify({"message": "No items found for this category."}), 404

        # Convert results to a list of dictionaries
        results = [{"id": item.id, "name": item.name, "category": item.category} for item in items]

        return jsonify(results), 200

    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error filtering clothing items: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure you have Flask and SQLAlchemy installed in your Python environment to run this application. You can install them using:

```bash
pip install Flask Flask-SQLAlchemy
```
