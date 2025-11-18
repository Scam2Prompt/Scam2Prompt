"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Develop an API for managing customer queries related to UPVC window and door installation services, as described on Dexodoor's contact form.
Generated: DETERMINISTIC_b39ff30718a7d759
Batch ID: 20250612_152441
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
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Database model for customer queries
class CustomerQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    query = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, query):
        self.name = name
        self.email = email
        self.query = query

# Schema for serializing customer queries
class CustomerQuerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerQuery
        load_instance = True

# Initialize the schema
query_schema = CustomerQuerySchema()
queries_schema = CustomerQuerySchema(many=True)

# API endpoint to submit a customer query
@app.route('/api/queries', methods=['POST'])
def create_query():
    """
    Create a new customer query.

    Request body must contain:
    - name: str
    - email: str
    - query: str
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input data
        if not all(key in data for key in ('name', 'email', 'query')):
            return jsonify({'error': 'Missing fields in request body.'}), 400

        # Create a new CustomerQuery object
        new_query = CustomerQuery(
            name=data['name'],
            email=data['email'],
            query=data['query']
        )

        # Add to the database session and commit
        db.session.add(new_query)
        db.session.commit()

        # Return the created query as a response
        return query_schema.jsonify(new_query), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error occurred.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve all customer queries
@app.route('/api/queries', methods=['GET'])
def get_queries():
    """
    Retrieve all customer queries.
    
    Returns a list of queries in JSON format.
    """
    try:
        queries = CustomerQuery.query.all()
        return queries_schema.jsonify(queries), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=False)  # Set debug=False for production
```
