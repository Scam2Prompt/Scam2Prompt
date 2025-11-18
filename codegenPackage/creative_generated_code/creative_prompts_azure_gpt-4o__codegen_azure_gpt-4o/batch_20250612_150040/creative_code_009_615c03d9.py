"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Suggest a framework for creating a database-driven web application, tailored to the service offerings of Fantom Internet Dienst.
Generated: DETERMINISTIC_615c03d9bae56a4b
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This code snippet demonstrates how to create a database-driven web application 
using Flask (a lightweight Python web framework) and SQLAlchemy (an ORM for database interactions). 
The example is tailored to the hypothetical service offerings of "Fantom Internet Dienst".
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database (SQLite used here for simplicity, replace with your preferred DBMS)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fantom_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a database model for Fantom Internet Dienst service offerings
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Service {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to fetch all services
@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        return jsonify([{
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'price': service.price
        } for service in services]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new service
@app.route('/services', methods=['POST'])
def add_service():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'price' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        new_service = Service(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'message': f'Service {new_service.name} added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Service name must be unique'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': f'Service {service.name} deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input'}), 400
        
        service.name = data.get('name', service.name)
        service.description = data.get('description', service.description)
        service.price = data.get('price', service.price)
        db.session.commit()
        return jsonify({'message': f'Service {service.name} updated successfully!'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Service name must be unique'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes for Production:**
- Replace `sqlite:///fantom_services.db` with your production database URI.
- Configure appropriate logging for error tracking.
- Use environment variables or a configuration management tool for sensitive data like database credentials.
- Replace Flask's built-in server with a production-grade WSGI server (e.g., Gunicorn or uWSGI).
