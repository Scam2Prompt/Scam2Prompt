"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write code to implement a client management system for consulting firms using Django or Flask.
Generated: DETERMINISTIC_c56447411687c2da
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is production-ready code using Flask for a client management system:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI (replace with your own database settings)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each client
    name = db.Column(db.String(100), nullable=False)  # Client name
    email = db.Column(db.String(100), unique=True, nullable=False)  # Client email
    phone = db.Column(db.String(15), nullable=True)  # Client phone number
    company = db.Column(db.String(100), nullable=True)  # Client company name

    def to_dict(self):
        """Convert the Client object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'company': self.company
        }

# Route to create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    try:
        data = request.json
        # Validate required fields
        if 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required fields.'}), 400

        # Create and add a new client
        new_client = Client(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            company=data.get('company')
        )
        db.session.add(new_client)
        db.session.commit()

        return jsonify(new_client.to_dict()), 201  # Return the created client with 201 status
    except IntegrityError:
        db.session.rollback()  # Rollback changes in case of error
        return jsonify({'error': 'Email already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        clients = Client.query.all()
        return jsonify([client.to_dict() for client in clients]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific client by ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({'error': 'Client not found.'}), 404

        return jsonify(client.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an existing client
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({'error': 'Client not found.'}), 404

        data = request.json
        client.name = data.get('name', client.name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        client.company = data.get('company', client.company)

        db.session.commit()
        return jsonify(client.to_dict()), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({'error': 'Client not found.'}), 404

        db.session.delete(client)
        db.session.commit()

        return jsonify({'message': 'Client deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database (run once to create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Update the `SQLALCHEMY_DATABASE_URI` to match your database settings.
- You can disable debug mode in production by setting `debug=False` when running the app.
- This code uses Flask's built-in development server, which is not suitable for production. Use a production-grade WSGI server like Gunicorn or uWSGI.
