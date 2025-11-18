"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Generate code to implement a search functionality for a directory website where users can search for businesses like "Ταπετσαρίες Αυτοκινήτων" by name, category, or city.
Generated: DETERMINISTIC_d9596589c4475b3b
Batch ID: 20250612_151044
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_directory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Business {self.name}>'

# Endpoint to search for businesses
@app.route('/search', methods=['GET'])
def search_businesses():
    # Get search parameters from query string
    name = request.args.get('name')
    category = request.args.get('category')
    city = request.args.get('city')

    # Start query on the Business model
    query = Business.query

    # Filter by name if provided
    if name:
        query = query.filter(Business.name.ilike(f'%{name}%'))

    # Filter by category if provided
    if category:
        query = query.filter(Business.category.ilike(f'%{category}%'))

    # Filter by city if provided
    if city:
        query = query.filter(Business.city.ilike(f'%{city}%'))

    try:
        # Execute the query and return results
        results = query.all()
        # Format results into a list of dictionaries
        businesses = [{'id': biz.id, 'name': biz.name, 'category': biz.category, 'city': biz.city} for biz in results]
        return jsonify(businesses), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

### Notes:
- You need to have Flask and Flask-SQLAlchemy installed in your Python environment.
- You can run migrations and populate your database with sample data for testing.
- The search functionality supports flexible queries using partial matches for name, category, and city.
