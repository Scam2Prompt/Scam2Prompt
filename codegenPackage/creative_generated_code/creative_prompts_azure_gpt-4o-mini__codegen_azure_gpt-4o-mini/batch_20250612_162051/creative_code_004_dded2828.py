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

```python
# Client Management System for Law Firms

# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications

# Initialize the database
db = SQLAlchemy(app)

# Model for storing client information
class Client(db.Model):
    """Model representing a client in the system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Client {self.name}>'

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Route to add a new client
@app.route('/clients', methods=['POST'])
def add_client():
    """Add a new client to the system."""
    try:
        data = request.json
        new_client = Client(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(new_client)
        db.session.commit()
        return jsonify({"message": "Client added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Client with this name or email already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a list of all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve a list of all clients."""
    clients = Client.query.all()
    return jsonify([{'id': client.id, 'name': client.name, 'email': client.email, 'phone': client.phone} for client in clients]), 200

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug to False in production
    except Exception as e:
        print(f"An error occurred while running the app: {str(e)}")
```
