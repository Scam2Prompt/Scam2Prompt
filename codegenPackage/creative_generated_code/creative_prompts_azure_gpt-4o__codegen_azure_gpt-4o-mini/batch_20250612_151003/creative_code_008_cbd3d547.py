"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Write code to implement a booking system for in-person consultations about historical building restoration projects, including calendar integration and email confirmation features.
Generated: DETERMINISTIC_cbd3d54721c07aea
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Booking {self.name} at {self.date_time}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

def send_confirmation_email(name, email, date_time):
    """Send a confirmation email to the user."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg['Subject'] = 'Booking Confirmation'

    body = f'Dear {name},\n\nYour booking for {date_time} has been confirmed.\nThank you!'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f'An error occurred while sending email: {e}')

@app.route('/book', methods=['POST'])
def book_consultation():
    """API endpoint to book a consultation."""
    data = request.get_json()

    try:
        name = data['name']
        email = data['email']
        date_time = datetime.datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M:%S')

        # Validate booking time
        if date_time < datetime.datetime.now():
            return jsonify({'error': 'Cannot book in the past.'}), 400

        # Create a new booking
        new_booking = Booking(name=name, email=email, date_time=date_time)
        db.session.add(new_booking)
        db.session.commit()

        # Send confirmation email
        send_confirmation_email(name, email, date_time)

        return jsonify({'message': 'Booking confirmed!', 'booking_id': new_booking.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS.'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """API endpoint to retrieve all bookings."""
    try:
        bookings = Booking.query.all()
        return jsonify([{'id': b.id, 'name': b.name, 'email': b.email, 'date_time': b.date_time.strftime('%Y-%m-%d %H:%M:%S')} for b in bookings]), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Important Notes:
- Replace `your_email@example.com` and `your_email_password` with actual credentials.
- The SMTP server configuration must be set according to your email service provider.
- To run this code, ensure you have Flask and Flask-SQLAlchemy installed, and set up a virtual environment to manage dependencies.
