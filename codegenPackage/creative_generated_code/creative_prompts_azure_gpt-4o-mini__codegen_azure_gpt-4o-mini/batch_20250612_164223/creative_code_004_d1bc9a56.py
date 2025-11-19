"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Develop a REST API endpoint that returns detailed information about Rheinmetall suppliers based on their geographical location.
Generated: DETERMINISTIC_d1bc9a568d112b9d
Batch ID: 20250612_164223
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

app = Flask(__name__)

# Configure the database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///suppliers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Supplier(db.Model):
    """Model representing a supplier."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Supplier object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'details': self.details
        }

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    """Endpoint to get suppliers based on geographical location."""
    try:
        # Get the location query parameter
        location = request.args.get('location')
        
        if not location:
            return jsonify({'error': 'Location parameter is required.'}), 400
        
        # Query suppliers based on location
        suppliers = Supplier.query.filter_by(location=location).all()
        
        # Convert suppliers to a list of dictionaries
        suppliers_list = [supplier.to_dict() for supplier in suppliers]
        
        return jsonify(suppliers_list), 200

    except SQLAlchemyError as e:
        # Log the error (in a real-world application, use proper logging)
        print(f"Database error: {str(e)}")
        return jsonify({'error': 'Database query failed.'}), 500

    except Exception as e:
        # Log unexpected errors
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
