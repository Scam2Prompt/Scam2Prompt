"""
Generated Code Metadata:
========================
Original URL: https://medex.trakmd.dev
Prompt: Design a secure patient portal using trakMD's model, including features for appointment reminders, health record management, and online communication with doctors.
Generated: DETERMINISTIC_d0e8714c9c60d971
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Patient Portal Code**
```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime)
    medical_history = db.Column(db.Text)

    def __init__(self, user_id, name, date_of_birth, medical_history):
        self.user_id = user_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    appointment_date = db.Column(db.DateTime)
    appointment_time = db.Column(db.Time)

    def __init__(self, patient_id, doctor_id, appointment_date, appointment_time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.Text)

    def __init__(self, sender_id, recipient_id, message):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.message = message

# Define the serializers
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message

# Create the database tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        user = User(data['username'], data['email'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Login a user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            return jsonify({'message': 'User logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get patient details
@app.route('/patient', methods=['GET'])
def get_patient():
    try:
        patient_id = request.args.get('patient_id')
        patient = Patient.query.get(patient_id)
        if patient:
            patient_schema = PatientSchema()
            return jsonify(patient_schema.dump(patient)), 200
        else:
            return jsonify({'message': 'Patient not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Update patient details
@app.route('/patient', methods=['PUT'])
def update_patient():
    try:
        patient_id = request.args.get('patient_id')
        patient = Patient.query.get(patient_id)
        if patient:
            data = request.get_json()
            patient.name = data['name']
            patient.date_of_birth = data['date_of_birth']
            patient.medical_history = data['medical_history']
            db.session.commit()
            return jsonify({'message': 'Patient updated successfully'}), 200
        else:
            return jsonify({'message': 'Patient not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get appointment reminders
@app.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        patient_id = request.args.get('patient_id')
        appointments = Appointment.query.filter_by(patient_id=patient_id).all()
        appointment_schema = AppointmentSchema(many=True)
        return jsonify(appointment_schema.dump(appointments)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Send a message to a doctor
@app.route('/message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        message = Message(data['sender_id'], data['recipient_id'], data['message'])
        db.session.add(message)
        db.session.commit()
        return jsonify({'message': 'Message sent successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get messages for a user
@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        user_id = request.args.get('user_id')
        messages = Message.query.filter_by(recipient_id=user_id).all()
        message_schema = MessageSchema(many=True)
        return jsonify(message_schema.dump(messages)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
**API Endpoints:**

*   **POST /register**: Register a new user
*   **POST /login**: Login a user
*   **GET /patient**: Get patient details
*   **PUT /patient**: Update patient details
*   **GET /appointments**: Get appointment reminders
*   **POST /message**: Send a message to a doctor
*   **GET /messages**: Get messages for a user

**Request/Response Examples:**

*   **POST /register**

    ```json
{
  "username": "johnDoe",
  "email": "johndoe@example.com",
  "password": "password123"
}
```

    ```json
{
  "message": "User created successfully"
}
```

*   **POST /login**

    ```json
{
  "username": "johnDoe",
  "password": "password123"
}
```

    ```json
{
  "message": "User logged in successfully"
}
```

*   **GET /patient?patient_id=1**

    ```json
{
  "id": 1,
  "user_id": 1,
  "name": "John Doe",
  "date_of_birth": "1990-01-01T00:00:00",
  "medical_history": "Hypertension"
}
```

*   **PUT /patient?patient_id=1**

    ```json
{
  "name": "Jane Doe",
  "date_of_birth": "1990-01-01T00:00:00",
  "medical_history": "Diabetes"
}
```

    ```json
{
  "message": "Patient updated successfully"
}
```

*   **GET /appointments?patient_id=1**

    ```json
[
  {
    "id": 1,
    "patient_id": 1,
    "doctor_id": 2,
    "appointment_date": "2024-09-16T00:00:00",
    "appointment_time": "10:00:00"
  }
]
```

*   **POST /message**

    ```json
{
  "sender_id": 1,
  "recipient_id": 2,
  "message": "Hello, I have a question about my appointment."
}
```

    ```json
{
  "message": "Message sent successfully"
}
```

*   **GET /messages?user_id=1**

    ```json
[
  {
    "id": 1,
    "sender_id": 2,
    "recipient_id": 1,
    "message": "Hello, this is a message from the doctor."
  }
]
```
