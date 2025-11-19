"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: "Create a CRM software for a small business, incorporating features such as contact management, sales tracking, and marketing automation, using a suitable programming language and database, inspired by MDA Tech Sys's CRM software services."
Generated: DETERMINISTIC_cf7f245804bbeabd
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return f'<Contact {self.name}>'

# Define the Sale model
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    contact = db.relationship('Contact', backref='sales')

    def __repr__(self):
        return f'<Sale {self.id} - Amount: {self.amount}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_contact = Contact(name=data['name'], email=data['email'], phone=data.get('phone'))

    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Contact with this email already exists.'}), 400

# Route to get all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in contacts]), 200

# Route to add a new sale
@app.route('/sales', methods=['POST'])
def add_sale():
    data = request.json
    new_sale = Sale(contact_id=data['contact_id'], amount=data['amount'], date=data['date'])

    try:
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'Sale added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all sales
@app.route('/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    return jsonify([{'id': s.id, 'contact_id': s.contact_id, 'amount': s.amount, 'date': s.date} for s in sales]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask and Flask-SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

### Usage
- Start the application:
```bash
python crm.py
```
- Use a tool like Postman or curl to interact with the API.
