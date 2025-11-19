"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: How can I design a user-friendly interface for booking appointments online for a counseling service, based on the features of That Counseling Place?
Generated: DETERMINISTIC_e87e65f05a1413ca
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Counselor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    specialization = db.Column(db.String(100))
    bio = db.Column(db.Text)
    available_slots = db.relationship('AvailableSlot', backref='counselor', lazy=True)

class AvailableSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counselor_id = db.Column(db.Integer, db.ForeignKey('counselor.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    is_booked = db.Column(db.Boolean, default=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('available_slot.id'), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    client = db.relationship('Client', backref='appointments')
    slot = db.relationship('AvailableSlot', backref='appointment')

# Helper Functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not all([name, email, phone, password, confirm_password]):
            flash('All fields are required', 'error')
            return redirect(url_for('register'))

        if not validate_email(email):
            flash('Invalid email address', 'error')
            return redirect(url_for('register'))

        if not validate_phone(phone):
            flash('Invalid phone number', 'error')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))

        if Client.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))

        client = Client(name=name, email=email, phone=phone)
        client.set_password(password)
        db.session.add(client)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not all([email, password]):
            flash('All fields are required', 'error')
            return redirect(url_for('login'))

        client = Client.query.filter_by(email=email).first()
        if not client or not client.check_password(password):
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))

        session['client_id'] = client.id
        session['client_name'] = client.name
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'client_id' not in session:
        flash('Please login to access this page', 'error')
        return redirect(url_for('login'))

    client = Client.query.get(session['client_id'])
    appointments = client.appointments
    return render_template('dashboard.html', client=client, appointments=appointments)

@app.route('/counselors')
def counselors():
    counselors_list = Counselor.query.all()
    return render_template('counselors.html', counselors=counselors_list)

@app.route('/book/<int:counselor_id>', methods=['GET', 'POST'])
def book_appointment(counselor_id):
    if 'client_id' not in session:
        flash('Please login to book an appointment', 'error')
        return redirect(url_for('login'))

    counselor = Counselor.query.get_or_404(counselor_id)
    
    if request.method == 'POST':
        slot_id = request.form.get('slot_id')
        notes = request.form.get('notes', '')

        if not slot_id:
            flash('Please select a time slot', 'error')
            return redirect(url_for('book_appointment', counselor_id=counselor_id))

        slot = AvailableSlot.query.get(slot_id)
        if not slot or slot.is_booked:
            flash('This slot is no longer available', 'error')
            return redirect(url_for('book_appointment', counselor_id=counselor_id))

        appointment = Appointment(
            client_id=session['client_id'],
            slot_id=slot_id,
            notes=notes
        )
        slot.is_booked = True
        db.session.add(appointment)
        db.session.commit()

        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('dashboard'))

    # Get available slots for the next 2 weeks
    now = datetime.now(pytz.utc)
    two_weeks_later = now + timedelta(days=14)
    available_slots = AvailableSlot.query.filter(
        AvailableSlot.counselor_id == counselor_id,
        AvailableSlot.start_time >= now,
        AvailableSlot.start_time <= two_weeks_later,
        AvailableSlot.is_booked == False
    ).order_by(AvailableSlot.start_time).all()

    return render_template('book.html', counselor=counselor, slots=available_slots)

@app.route('/cancel/<int:appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    if 'client_id' not in session:
        flash('Please login to cancel an appointment', 'error')
        return redirect(url_for('login'))

    appointment = Appointment.query.get_or_404(appointment_id)
    if appointment.client_id != session['client_id']:
        flash('You can only cancel your own appointments', 'error')
        return redirect(url_for('dashboard'))

    appointment.slot.is_booked = False
    db.session.delete(appointment)
    db.session.commit()

    flash('Appointment cancelled successfully', 'success')
    return redirect(url_for('dashboard'))

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    # Implementation would be similar to client login but with admin credentials
    pass

@app.route('/admin/dashboard')
def admin_dashboard():
    # Implementation would show all appointments and allow managing counselors
    pass

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Note: This is a Flask application that would require corresponding HTML templates in a `templates` folder. The templates are not included here but would be needed for a complete implementation. The code includes all the backend logic for user registration, login, appointment booking, and cancellation.
