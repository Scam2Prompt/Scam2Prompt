"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Develop a mobile app for parents and students that includes online fee payment, homework updates, and exam result downloads, as described in Him Saral's mobile app features.
Generated: DETERMINISTIC_1585a1893f03ad21
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///school_app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the database models
class User(db.Model):
    """Model for users (parents and students)"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'parent' or 'student'

class FeePayment(db.Model):
    """Model for fee payments"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default='pending')  # 'pending', 'completed', 'failed'

class HomeworkUpdate(db.Model):
    """Model for homework updates"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    homework_details = db.Column(db.Text, nullable=False)

class ExamResult(db.Model):
    """Model for exam results"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    result_details = db.Column(db.Text, nullable=False)

# Route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user (parent or student)"""
    data = request.json
    try:
        new_user = User(username=data['username'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for fee payment
@app.route('/pay_fee', methods=['POST'])
def pay_fee():
    """Process fee payment"""
    data = request.json
    try:
        payment = FeePayment(user_id=data['user_id'], amount=data['amount'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message": "Payment processed successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for homework updates
@app.route('/homework_update', methods=['POST'])
def update_homework():
    """Submit homework updates"""
    data = request.json
    try:
        homework = HomeworkUpdate(user_id=data['user_id'], homework_details=data['homework_details'])
        db.session.add(homework)
        db.session.commit()
        return jsonify({"message": "Homework update submitted successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for downloading exam results
@app.route('/exam_results/<int:user_id>', methods=['GET'])
def get_exam_results(user_id):
    """Retrieve exam results for a user"""
    try:
        results = ExamResult.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": result.id, "result_details": result.result_details} for result in results]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

### Note:
- Ensure to set the `DATABASE_URL` environment variable for production use.
- This code uses Flask for the backend and assumes a SQLite database for simplicity. Adjust the database configuration as needed for production.
- The app is designed to be run in a development environment with `debug=True`. Change this to `False` for production.
