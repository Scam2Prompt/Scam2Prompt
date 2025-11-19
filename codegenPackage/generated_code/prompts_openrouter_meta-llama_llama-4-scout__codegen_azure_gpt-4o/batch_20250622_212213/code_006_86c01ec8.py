"""
Generated Code Metadata:
========================
Original URL: https://springbokinfo.co.za
Prompt: Suggest a suitable library or framework for building a business directory like Springbok Info, considering scalability and search functionality.
Generated: DETERMINISTIC_86c01ec8011b3de1
Batch ID: 20250622_212213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based implementation for a scalable business directory with search functionality
# Using SQLAlchemy for database management and Elasticsearch for search capabilities

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch, exceptions as es_exceptions

# Initialize Flask app
app = Flask(__name__)

# Configure database (PostgreSQL in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/business_directory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Define the Business model
class Business(db.Model):
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Business object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'category': self.category
        }

# Error handling for Elasticsearch connection
try:
    if not es.ping():
        raise es_exceptions.ConnectionError("Elasticsearch server is not reachable.")
except es_exceptions.ConnectionError as e:
    print(f"Error: {e}")
    exit(1)

# Route to add a new business
@app.route('/business', methods=['POST'])
def add_business():
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ('name', 'address', 'phone', 'category')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new business entry
        business = Business(
            name=data['name'],
            address=data['address'],
            phone=data['phone'],
            category=data['category']
        )
        db.session.add(business)
        db.session.commit()

        # Index the business in Elasticsearch for search functionality
        es.index(index='businesses', id=business.id, body=business.to_dict())

        return jsonify({'message': 'Business added successfully', 'business': business.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to search businesses
@app.route('/search', methods=['GET'])
def search_businesses():
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({'error': 'Search query is required'}), 400

        # Perform search in Elasticsearch
        search_results = es.search(index='businesses', body={
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['name', 'address', 'category']
                }
            }
        })

        # Extract and return results
        businesses = [hit['_source'] for hit in search_results['hits']['hits']]
        return jsonify({'results': businesses}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to list all businesses
@app.route('/businesses', methods=['GET'])
def list_businesses():
    try:
        businesses = Business.query.all()
        return jsonify({'businesses': [business.to_dict() for business in businesses]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Ensure database tables are created
    db.create_all()
    # Run the Flask app
    app.run(debug=True)
```
