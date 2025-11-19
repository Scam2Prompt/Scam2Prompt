"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Suggest a framework for building a client management system for law firms, based on the values of integrity and excellence outlined on the CAAG website.
Generated: DETERMINISTIC_dded2828bbe3ea61
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code suggestion for building a client management system for law firms using Python and Flask. This framework adheres to core values of integrity and excellence by focusing on security, maintainability, and scalability.

```python
"""
Client Management System for Law Firms
Framework: Flask (Python)
Values: Integrity and Excellence
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity, replace with PostgreSQL/MySQL for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key for production

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String(100), nullable=False)  # Client's name
    email = db.Column(db.String(100), unique=True, nullable=False)  # Client's email
    phone = db.Column(db.String(20), nullable=False)  # Client's phone number
    hashed_password = db.Column(db.String(256), nullable=False)  # Password hash

    def __repr__(self):
        return f"<Client {self.name}>"

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for 404 (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal server error occurred"}), 500

# Endpoint to add a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        # Parse the request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        # Validate required fields
        if not name or not email or not phone or not password:
            return jsonify({"error": "All fields are required"}), 400

        # Check if the email already exists
        if Client.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new client record
        client = Client(name=name, email=email, phone=phone, hashed_password=hashed_password)
        db.session.add(client)
        db.session.commit()

        return jsonify({"message": "Client added successfully", "client": {"id": client.id, "name": client.name, "email": client.email, "phone": client.phone}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        clients = Client.query.all()
        client_list = [{"id": client.id, "name": client.name, "email": client.email, "phone": client.phone} for client in clients]
        return jsonify({"clients": client_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific client by ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404
        return jsonify({"client": {"id": client.id, "name": client.name, "email": client.email, "phone": client.phone}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update client details
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404

        # Parse the request data
        data = request.get_json()
        client.name = data.get('name', client.name)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)

        db.session.commit()
        return jsonify({"message": "Client updated successfully", "client": {"id": client.id, "name": client.name, "email": client.email, "phone": client.phone}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"error": "Client not found"}), 404
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Set debug mode to False for production
```

### Notes:
- Replace `your_secret_key` with a strong, random secret key for production use.
- For production settings, consider using a more robust database such as PostgreSQL or MySQL.
- Set `debug=False` in the `app.run()` method for production to avoid exposing sensitive information.
