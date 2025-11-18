"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Write code to optimize a sales funnel for pre-selling services and booking appointments, based on the "Click, Capture, Close" model described on the Client Fuel website.
Generated: DETERMINISTIC_82608a1c62770f37
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python implementation of a basic sales funnel using the "Click, Capture, Close" model. This code is designed for a Flask-based web application with database integration for managing leads and booking appointments.

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a lead
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for an appointment
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Route: Landing page (Click phase)
@app.route('/')
def landing_page():
    # Render a landing page where potential clients can learn more and be encouraged to sign up
    return render_template('landing_page.html')

# Route: Capture lead information (Capture phase)
@app.route('/capture', methods=['POST'])
def capture_lead():
    try:
        # Capture lead details from form submission
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Validate required fields
        if not name or not email:
            return jsonify({'error': 'Name and email are required fields'}), 400

        # Check for duplicate email
        if Lead.query.filter_by(email=email).first():
            return jsonify({'error': 'This email has already been registered'}), 400

        # Save lead to database
        lead = Lead(name=name, email=email, phone=phone)
        db.session.add(lead)
        db.session.commit()

        return jsonify({'message': 'Lead captured successfully'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'An error occurred while capturing the lead', 'details': str(e)}), 500

# Route: Booking appointments (Close phase)
@app.route('/book', methods=['POST'])
def book_appointment():
    try:
        # Capture appointment details from form submission
        lead_id = request.form.get('lead_id')
        date = request.form.get('date')
        notes = request.form.get('notes')

        # Validate required fields
        if not lead_id or not date:
            return jsonify({'error': 'Lead ID and appointment date are required'}), 400

        lead = Lead.query.get(lead_id)
        if not lead:
            return jsonify({'error': 'Lead not found'}), 404

        # Convert date string to datetime object
        appointment_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        # Save appointment to database
        appointment = Appointment(lead_id=lead_id, date=appointment_date, notes=notes)
        db.session.add(appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment booked successfully'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'An error occurred while booking the appointment', 'details': str(e)}), 500

# Route: View all leads (Admin dashboard)
@app.route('/leads', methods=['GET'])
def view_leads():
    try:
        leads = Lead.query.all()
        return render_template('leads.html', leads=leads)
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching leads', 'details': str(e)}), 500

# Route: View all appointments (Admin dashboard)
@app.route('/appointments', methods=['GET'])
def view_appointments():
    try:
        appointments = Appointment.query.all()
        return render_template('appointments.html', appointments=appointments)
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching appointments', 'details': str(e)}), 500

# Initialize the database
@app.before_first_request
def setup_database():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes:
1. This code uses Flask for setting up the web server and SQLAlchemy for database operations.
2. The `landing_page.html`, `leads.html`, and `appointments.html` templates need to be created to support the UI.
3. Error handling is implemented to ensure production stability.
4. Date format for appointments is expected to be `YYYY-MM-DD HH:MM:SS`.
5. This implementation is designed for demonstration purposes and can be extended with additional features such as authentication or integration with external tools.
