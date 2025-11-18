"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Suggest an API design for a laboratory management system that handles test categories such as "perfil hepático," "perfil lipídico," and "paquete gastro," and allows users to query available tests and submit medical orders.
Generated: DETERMINISTIC_c674f39c17051c9f
Batch ID: 20250612_152827
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TestCategory model
class TestCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    tests = db.relationship('Test', backref='category', lazy=True)

# Define the Test model
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('test_category.id'), nullable=False)

# Define the MedicalOrder model
class MedicalOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)

    test = db.relationship('Test', backref='orders', lazy=True)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/categories', methods=['GET'])
def get_categories():
    """Retrieve all test categories."""
    try:
        categories = TestCategory.query.all()
        return jsonify([{'id': c.id, 'name': c.name} for c in categories]), 200
    except SQLAlchemyError:
        return jsonify({'error': 'Database query error'}), 500

@app.route('/tests', methods=['GET'])
def get_tests():
    """Retrieve all tests with their categories."""
    try:
        tests = Test.query.all()
        return jsonify([{'id': t.id, 'name': t.name, 'category': t.category.name} for t in tests]), 200
    except SQLAlchemyError:
        return jsonify({'error': 'Database query error'}), 500

@app.route('/order', methods=['POST'])
def submit_order():
    """Submit a medical order for a test."""
    data = request.json
    try:
        # Validate input data
        if 'patient_name' not in data or 'test_id' not in data:
            return jsonify({'error': 'Missing data: patient_name and test_id are required'}), 400
        
        # Create a new MedicalOrder
        order = MedicalOrder(patient_name=data['patient_name'], test_id=data['test_id'])
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order submitted successfully', 'order_id': order.id}), 201

    except SQLAlchemyError:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Database error while submitting order'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
