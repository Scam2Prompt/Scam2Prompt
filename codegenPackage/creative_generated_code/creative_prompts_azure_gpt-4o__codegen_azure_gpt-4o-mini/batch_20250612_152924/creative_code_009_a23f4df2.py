"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Create a REST API endpoint for tenants to retrieve their account status, inspired by Inmobiliaria Capri's tenant portal functionality.
Generated: DETERMINISTIC_a23f4df26275880f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tenants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Tenant
class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    account_status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Tenant object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'account_status': self.account_status
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/tenants/<int:tenant_id>/status', methods=['GET'])
def get_tenant_status(tenant_id):
    """Retrieve the account status of a tenant by their ID."""
    try:
        # Query the tenant by ID
        tenant = Tenant.query.get(tenant_id)
        if tenant is None:
            # If tenant is not found, return a 404 error
            abort(404, description="Tenant not found.")

        # Return the tenant's account status
        return jsonify(tenant.to_dict()), 200

    except Exception as e:
        # Handle unexpected errors and return a 500 error
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
