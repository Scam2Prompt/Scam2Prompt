"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Create a REST API endpoint that retrieves company information, including address and contact details, based on the structure found in the Impressum of the Perrigo Claims webpage.
Generated: DETERMINISTIC_f9f3a808120b4f17
Batch ID: 20250612_135906
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
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///companies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Company model definition
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact_details = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert Company instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'contact_details': self.contact_details
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
    """Retrieve company information by ID.

    Args:
        company_id (int): The ID of the company to retrieve.

    Returns:
        JSON: A JSON response containing the company information or an error message.
    """
    try:
        company = Company.query.get(company_id)
        if not company:
            return jsonify({'error': 'Company not found'}), 404
        
        return jsonify(company.to_dict()), 200
    
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
```

### Instructions to run:
1. Ensure you have `Flask` and `Flask-SQLAlchemy` installed in your environment. You can install them using:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `app.py`.
3. Run the application with:
   ```bash
   python app.py
   ```
4. Make GET requests to the endpoint `/api/company/<company_id>` to retrieve company information.
