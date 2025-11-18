"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradise-app.com
Prompt: Generate code to create a secure domain registration system for a travel or relaxation app, inspired by the domain promotion on paradise-app.com.
Generated: DETERMINISTIC_1027f30a0eebb314
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Domain model
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    user_email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Domain {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

def is_valid_domain(domain):
    """
    Validate the domain name using regex.
    A valid domain must be alphanumeric and can include hyphens or dots.
    """
    regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.(?!-)[A-Za-z0-9-]{1,63}(?<!-)$'
    return re.match(regex, domain) is not None

@app.route('/register', methods=['POST'])
def register_domain():
    """
    Endpoint to register a new domain.
    Expects a JSON payload with 'domain' and 'email'.
    Returns success or error message.
    """
    data = request.get_json()

    # Validate input
    if not data or 'domain' not in data or 'email' not in data:
        return jsonify({'error': 'Domain and email are required.'}), 400

    domain_name = data['domain']
    user_email = data['email']

    # Check domain validity
    if not is_valid_domain(domain_name):
        return jsonify({'error': 'Invalid domain name.'}), 400

    new_domain = Domain(name=domain_name, user_email=user_email)

    # Attempt to save the new domain to the database
    try:
        db.session.add(new_domain)
        db.session.commit()
        return jsonify({'message': 'Domain registered successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Domain already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/domains', methods=['GET'])
def list_domains():
    """
    Endpoint to list all registered domains.
    Returns a list of domains in JSON format.
    """
    domains = Domain.query.all()
    domain_list = [{'id': domain.id, 'domain': domain.name, 'email': domain.user_email} for domain in domains]
    return jsonify(domain_list), 200

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
```

Ensure you have the necessary packages installed before running the code:

```bash
pip install Flask Flask-SQLAlchemy
```
