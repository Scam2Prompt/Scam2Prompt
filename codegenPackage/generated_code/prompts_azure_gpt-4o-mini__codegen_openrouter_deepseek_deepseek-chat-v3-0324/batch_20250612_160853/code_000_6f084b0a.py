"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Generate a code snippet for a web application that allows patients to book appointments with a cardiologist, incorporating features like email confirmation and contact details as mentioned on the Ask a Cardiologist website.
Generated: DETERMINISTIC_6f084b0a7a154fe8
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import datetime
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import re

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

mail = Mail(app)

# Database setup
def init_db():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            reason TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (patient_id) REFERENCES patients (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper functions
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

def send_confirmation_email(patient_email, appointment_date, appointment_time):
    try:
        msg = Message('Appointment Confirmation',
                      recipients=[patient_email])
        msg.body = f'''
        Thank you for booking an appointment with our cardiology department.
        
        Appointment Details:
        Date: {appointment_date}
        Time: {appointment_time}
        
        If you need to reschedule or cancel, please contact us at:
        Phone: +1 (555) 123-4567
        Email: cardiology@hospital.com
        
        Address:
        123 Medical Center Drive
        Cardiology Department
        City, State 12345
        '''
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        if not all([name, email, phone, password]):
            flash('All fields are required', 'error')
            return redirect(url_for('register'))
        
        if not is_valid_email(email):
            flash('Invalid email address', 'error')
            return redirect(url_for('register'))
        
        if not is_valid_phone(phone):
            flash('Invalid phone number', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        
        try:
            conn = sqlite3.connect('appointments.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO patients (name, email, phone, password) VALUES (?, ?, ?, ?)',
                          (name, email, phone, hashed_password))
            conn.commit()
            flash('Registration successful! Please login to book an appointment.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        except Exception as e:
            flash('An error occurred during registration', 'error')
            print(f"Registration error: {e}")
            return redirect(url_for('register'))
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('appointments.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, password FROM patients WHERE email = ?', (email,))
        patient = cursor.fetchone()
        conn.close()
        
        if patient and check_password_hash(patient[2], password):
            session['patient_id'] = patient[0]
            session['patient_name'] = patient[1]
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'patient_id' not in session:
        return redirect(url_for('login'))
    
    patient_id = session['patient_id']
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, date, time, reason, status FROM appointments WHERE patient_id = ? ORDER BY date, time', (patient_id,))
    appointments = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    if 'patient_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        reason = request.form.get('reason', '')
        
        try:
            appointment_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if appointment_date < datetime.date.today():
                flash('Cannot book appointments in the past', 'error')
                return redirect(url_for('book_appointment'))
        except ValueError:
            flash('Invalid date format', 'error')
            return redirect(url_for('book_appointment'))
        
        try:
            conn = sqlite3.connect('appointments.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO appointments (patient_id, date, time, reason) VALUES (?, ?, ?, ?)',
                          (session['patient_id'], date, time, reason))
            conn.commit()
            
            # Get patient email for confirmation
            cursor.execute('SELECT email FROM patients WHERE id = ?', (session['patient_id'],))
            patient_email = cursor.fetchone()[0]
            
            if send_confirmation_email(patient_email, date, time):
                flash('Appointment booked successfully! Confirmation sent to your email.', 'success')
            else:
                flash('Appointment booked successfully, but confirmation email failed to send.', 'warning')
            
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash('An error occurred while booking the appointment', 'error')
            print(f"Booking error: {e}")
            return redirect(url_for('book_appointment'))
        finally:
            conn.close()
    
    return render_template('book.html')

@app.route('/cancel/<int:appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    if 'patient_id' not in session:
        return redirect(url_for('login'))
    
    try:
        conn = sqlite3.connect('appointments.db')
        cursor = conn.cursor()
        
        # Verify the appointment belongs to the logged-in patient
        cursor.execute('SELECT patient_id FROM appointments WHERE id = ?', (appointment_id,))
        result = cursor.fetchone()
        
        if not result or result[0] != session['patient_id']:
            flash('Invalid appointment', 'error')
            return redirect(url_for('dashboard'))
        
        cursor.execute('UPDATE appointments SET status = "cancelled" WHERE id = ?', (appointment_id,))
        conn.commit()
        flash('Appointment cancelled successfully', 'success')
    except Exception as e:
        flash('An error occurred while cancelling the appointment', 'error')
        print(f"Cancellation error: {e}")
    finally:
        conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```
