"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calltpd.com
Prompt: How can I implement a payroll processing API to manage employee payments effectively?
Generated: DETERMINISTIC_90332e5cabdd258b
Batch ID: 20250612_162508
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
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payroll.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    last_payment_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Employee {self.name}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add an employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    
    # Validate incoming data
    if not data or 'name' not in data or 'salary' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        new_employee = Employee(name=data['name'], salary=data['salary'])
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee added', 'employee_id': new_employee.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to process payroll for an employee
@app.route('/payroll/<int:employee_id>', methods=['POST'])
def process_payroll(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    try:
        # Simulate payment processing here
        employee.last_payment_date = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': f'Payroll processed for {employee.name}'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get employee details
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    return jsonify({
        'id': employee.id,
        'name': employee.name,
        'salary': employee.salary,
        'last_payment_date': employee.last_payment_date.strftime('%Y-%m-%d %H:%M:%S') if employee.last_payment_date else None
    }), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
