"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://11tesorosibericos.com
Prompt: Create an API endpoint that allows users to filter and search for Iberian ham products based on criteria such as type (e.g., Bellota, Cebo) and weight, reflecting the product structure of 11 Tesoros Ibéricos.
Generated: DETERMINISTIC_0e6cce1e96862936
Batch ID: 20250612_163952
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

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iberian_ham.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Iberian Ham model
class IberianHam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<IberianHam {self.type} - {self.weight}g>'


@app.route('/api/ham', methods=['GET'])
def get_ham():
    """
    Endpoint to filter Iberian ham products based on query parameters.
    Query parameters:
    - type: Filter by type (e.g., Bellota, Cebo)
    - weight: Filter by weight (e.g., 5.0)
    
    Returns:
    - A JSON list of Iberian ham products matching the criteria.
    """
    try:
        # Get query parameters
        ham_type = request.args.get('type')
        weight = request.args.get('weight', type=float)

        # Build the query
        query = IberianHam.query

        # Adding filters based on provided criteria
        if ham_type:
            query = query.filter(IberianHam.type.ilike(f'%{ham_type}%'))
        if weight:
            query = query.filter(IberianHam.weight == weight)

        # Execute the query and convert results to JSON
        results = query.all()
        hams = [{'id': ham.id, 'type': ham.type, 'weight': ham.weight} for ham in results]

        return jsonify(hams), 200

    except SQLAlchemyError as e:
        # Log error (for production, consider using a logging framework)
        print(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while querying the database."}), 500

    except Exception as e:
        # Catch-all for any other exceptions
        print(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Start the Flask application
    app.run(debug=True)
```
