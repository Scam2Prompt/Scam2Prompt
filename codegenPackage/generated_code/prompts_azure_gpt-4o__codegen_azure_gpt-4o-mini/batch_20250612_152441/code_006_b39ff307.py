"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Develop an API for managing customer queries related to UPVC window and door installation services, as described on Dexodoor's contact form.
Generated: DETERMINISTIC_b39ff30718a7d759
Batch ID: 20250612_152441
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_queries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the CustomerQuery model
class CustomerQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    query = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'query': self.query
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/queries', methods=['POST'])
def create_query():
    """Create a new customer query."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('name', 'email', 'query')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_query = CustomerQuery(
        name=data['name'],
        email=data['email'],
        query=data['query']
    )

    try:
        db.session.add(new_query)
        db.session.commit()
        return jsonify(new_query.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error creating query: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/queries', methods=['GET'])
def get_queries():
    """Retrieve all customer queries."""
    try:
        queries = CustomerQuery.query.all()
        return jsonify([query.to_dict() for query in queries]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error retrieving queries: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/queries/<int:query_id>', methods=['GET'])
def get_query(query_id):
    """Retrieve a specific customer query by ID."""
    query = CustomerQuery.query.get(query_id)
    if query is None:
        return jsonify({'error': 'Query not found'}), 404
    return jsonify(query.to_dict()), 200

@app.route('/queries/<int:query_id>', methods=['DELETE'])
def delete_query(query_id):
    """Delete a specific customer query by ID."""
    query = CustomerQuery.query.get(query_id)
    if query is None:
        return jsonify({'error': 'Query not found'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
        return jsonify({'message': 'Query deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error deleting query: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
