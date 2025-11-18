"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Suggest tools or frameworks to build a web-based attendance system with features like "Absen Masuk" and "Absen Pulang," similar to formulir.site.
Generated: DETERMINISTIC_32fd3edf5b971ddb
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web framework and database handling
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///attendance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Attendance model
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), nullable=False)
    check_in_time = db.Column(db.DateTime, nullable=True)
    check_out_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Attendance {self.employee_id}>'

# Create database tables
with app.app_context():
    db.create_all()

# API endpoint to check in (Absen Masuk)
@app.route('/checkin', methods=['POST'])
def check_in():
    data = request.get_json()
    
    # Validate input data
    if not data or 'employee_id' not in data:
        return jsonify({"error": "Employee ID is required."}), 400

    # Create a new attendance record
    attendance = Attendance(employee_id=data['employee_id'], check_in_time=datetime.now())
    db.session.add(attendance)
    
    try:
        db.session.commit()
        return jsonify({"message": "Checked in successfully.", "id": attendance.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to check out (Absen Pulang)
@app.route('/checkout/<int:attendance_id>', methods=['POST'])
def check_out(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    
    if attendance is None:
        return jsonify({"error": "Attendance record not found."}), 404
    
    # Update check-out time
    attendance.check_out_time = datetime.now()
    
    try:
        db.session.commit()
        return jsonify({"message": "Checked out successfully."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get attendance records
@app.route('/attendance/<string:employee_id>', methods=['GET'])
def get_attendance(employee_id):
    records = Attendance.query.filter_by(employee_id=employee_id).all()
    return jsonify([{
        "id": record.id,
        "check_in_time": record.check_in_time,
        "check_out_time": record.check_out_time
    } for record in records]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### Note:
- This code is a simple Flask web application that allows employees to check in and check out.
- It uses SQLAlchemy for database interactions and assumes a PostgreSQL database if the `DATABASE_URL` environment variable is set.
- Proper error handling and data validation are included to ensure the robustness of the application.
