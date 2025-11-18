"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Develop a prototype for an online portal that allows patients to access their health data and medical staff to monitor patient conditions in real-time, inspired by the features of Hooshmand Teb's smart medical system.
Generated: DETERMINISTIC_ee4301f0c7c1e915
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_data.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# User Model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'patient' or 'staff'


# Patient Data Model
class PatientData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    health_data = db.Column(db.JSON, nullable=False)  # Store health data as JSON
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password'], method='sha256'),
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'error': 'Invalid username or password.'}), 401


# Route for logging out
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful.'}), 200


# Route for patients to access their health data
@app.route('/patient/data', methods=['GET'])
@login_required
def get_patient_data():
    if current_user.role != 'patient':
        return jsonify({'error': 'Unauthorized access.'}), 403
    data = PatientData.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'id': d.id, 'health_data': d.health_data, 'timestamp': d.timestamp} for d in data]), 200


# Route for staff to monitor patient conditions
@app.route('/staff/patients', methods=['GET'])
@login_required
def get_all_patients_data():
    if current_user.role != 'staff':
        return jsonify({'error': 'Unauthorized access.'}), 403
    patient_data = PatientData.query.all()
    return jsonify([{'patient_id': pd.user_id, 'health_data': pd.health_data, 'timestamp': pd.timestamp} for pd in patient_data]), 200


# Exception handling for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


# Main entry point to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
